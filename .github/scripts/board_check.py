#!/usr/bin/env python3
"""Flag misplaced items on the RFP & LPrize Tracking board (project 18).

Evaluates every board item against the rules in content/rfp_lifecycle.md and writes the
result into two project fields:

  * "Board check"        single-select: "✅ OK" / "🔴 Misplaced" / "🟠 Warning"
  * "Board check reason" text: which rule(s) the item breaks, empty when OK

It only ever writes those two fields. It never edits, labels, relinks or closes issues/PRs
(see "Scope boundary" in rfp_lifecycle.md).

Environment:
  GH_TOKEN       token with Projects read/write and read access to logos-co/{ecosystem,rfp,lambda-prize}
  DRY_RUN        "true" = print what would change, write nothing
  GRACE_MINUTES  don't newly flag an item that was edited on the board within this window (default 60),
                 because parents and children are usually moved one at a time. Clearing a flag is never delayed.
"""
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

PROJECT_NUMBER = 18
FIELD_CHECK = "Board check"
FIELD_REASON = "Board check reason"
OK, RED, AMBER = "✅ OK", "🔴 Misplaced", "🟠 Warning"
DRY_RUN = os.environ.get("DRY_RUN", "false").lower() == "true"
GRACE = timedelta(minutes=int(os.environ.get("GRACE_MINUTES", "60")))
IGNORE_FILE = Path(__file__).resolve().parent.parent / "board-check-ignore.json"

ORDER = [
    "Backlog", "Priority list", "Writing", "Legal & EcoDev review", "Ready to publish",
    "Published (accepting proposals/submissions)",
    "RFPs Closed for proposals (reviewing proposals)", "Proposals & Submissions to review",
    "RFPs Contracting", "RFPs In delivery", "Pending RFP milestone", "RFP milestone in review",
    "RFP Milestone & λ-Prize accepted", "Complete",
]
IDX = {s: i for i, s in enumerate(ORDER)}
PUBLISHED = IDX["Published (accepting proposals/submissions)"]
CLOSED_FOR_PROPOSALS = "RFPs Closed for proposals (reviewing proposals)"
IN_REVIEW = "Proposals & Submissions to review"
CONTRACTING = "RFPs Contracting"
IN_DELIVERY = "RFPs In delivery"

# Which Status columns each kind of item may sit in (rfp_lifecycle.md: "Status × kind reference table").
ALLOWED = {
    "main_rfp": set(ORDER[: PUBLISHED + 1]) | {CLOSED_FOR_PROPOSALS, CONTRACTING, IN_DELIVERY, "Complete"},
    "main_lp": set(ORDER[: PUBLISHED + 1]) | {"Complete"},
    "proposal": {IN_REVIEW, CONTRACTING},
    "milestone": {"Pending RFP milestone", "RFP milestone in review", "RFP Milestone & λ-Prize accepted", "Complete"},
    "lp_submission": {IN_REVIEW, "RFP Milestone & λ-Prize accepted", "Complete"},
}

ITEMS_QUERY = """
query($cursor: String) {
  organization(login: "logos-co") {
    projectV2(number: %d) {
      items(first: 100, after: $cursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          updatedAt
          fieldValues(first: 30) {
            nodes {
              ... on ProjectV2ItemFieldSingleSelectValue { name field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldTextValue { text field { ... on ProjectV2FieldCommon { name } } }
              ... on ProjectV2ItemFieldDateValue { date field { ... on ProjectV2FieldCommon { name } } }
            }
          }
          content {
            __typename
            ... on Issue {
              number title state
              repository { nameWithOwner }
              labels(first: 20) { nodes { name } }
              parent { number repository { nameWithOwner } }
              subIssues(first: 50) { nodes { number title repository { nameWithOwner } } }
            }
            ... on PullRequest {
              number title state merged
              repository { nameWithOwner }
              labels(first: 20) { nodes { name } }
            }
          }
        }
      }
    }
  }
}
""" % PROJECT_NUMBER

META_QUERY = """
query {
  organization(login: "logos-co") {
    projectV2(number: %d) {
      id
      fields(first: 60) {
        nodes {
          ... on ProjectV2FieldCommon { id name }
          ... on ProjectV2SingleSelectField { options { id name } }
        }
      }
    }
  }
}
""" % PROJECT_NUMBER

SET_SELECT = """
mutation($project: ID!, $item: ID!, $field: ID!, $option: String!) {
  updateProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field,
    value: {singleSelectOptionId: $option}}) { projectV2Item { id } }
}
"""
SET_TEXT = """
mutation($project: ID!, $item: ID!, $field: ID!, $text: String!) {
  updateProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field,
    value: {text: $text}}) { projectV2Item { id } }
}
"""
CLEAR = """
mutation($project: ID!, $item: ID!, $field: ID!) {
  clearProjectV2ItemFieldValue(input: {projectId: $project, itemId: $item, fieldId: $field}) {
    projectV2Item { id }
  }
}
"""


def graphql(query, **variables):
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    for key, value in variables.items():
        if value is not None:
            cmd += ["-f", f"{key}={value}"]
    last = ""
    for attempt in range(3):
        run = subprocess.run(cmd, capture_output=True, text=True)
        if run.returncode == 0:
            return json.loads(run.stdout)["data"]
        last = run.stderr.strip() or run.stdout.strip()
        time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"GraphQL call failed: {last}")


def load_meta():
    project = graphql(META_QUERY)["organization"]["projectV2"]
    fields = {n["name"]: n for n in project["fields"]["nodes"] if n and n.get("name")}
    for name in (FIELD_CHECK, FIELD_REASON):
        if name not in fields:
            sys.exit(f'Project field "{name}" does not exist on project {PROJECT_NUMBER}. Create it first.')
    options = {o["name"]: o["id"] for o in fields[FIELD_CHECK].get("options", [])}
    for name in (OK, RED, AMBER):
        if name not in options:
            sys.exit(f'Option "{name}" is missing from the "{FIELD_CHECK}" field.')
    return project["id"], fields[FIELD_CHECK]["id"], fields[FIELD_REASON]["id"], options


def load_items():
    items, cursor = [], None
    while True:
        page = graphql(ITEMS_QUERY, cursor=cursor)["organization"]["projectV2"]["items"]
        for node in page["nodes"]:
            content = node["content"]
            if not content:  # draft issue
                continue
            values, text, dates = {}, {}, {}
            for v in node["fieldValues"]["nodes"]:
                if not v or not v.get("field"):
                    continue
                if "date" in v:
                    dates[v["field"]["name"]] = v["date"]
                elif "text" in v:
                    text[v["field"]["name"]] = v["text"]
                elif "name" in v:
                    values[v["field"]["name"]] = v["name"]
            repo = content["repository"]["nameWithOwner"]
            is_issue = content["__typename"] == "Issue"
            parent = content.get("parent")
            items.append({
                "item_id": node["id"],
                "updated": datetime.fromisoformat(node["updatedAt"].replace("Z", "+00:00")),
                "repo": repo,
                "num": content["number"],
                "key": (repo, content["number"]),
                "title": content["title"],
                "is_pr": not is_issue,
                "state": content["state"],  # OPEN / CLOSED / MERGED
                "labels": [l["name"].lower() for l in content["labels"]["nodes"]],
                "status": values.get("Status"),
                "category": values.get("Category"),
                "rfp_value": values.get("RFP"),
                "lp_value": values.get("λ-Prize"),
                "closing_date": dates.get("Closing date"),
                "current_check": values.get(FIELD_CHECK),
                "current_reason": text.get(FIELD_REASON, ""),
                "parent": (parent["repository"]["nameWithOwner"], parent["number"]) if parent else None,
                "subs": [(s["repository"]["nameWithOwner"], s["number"], s["title"])
                         for s in content["subIssues"]["nodes"]] if is_issue else [],
            })
        if not page["pageInfo"]["hasNextPage"]:
            return items
        cursor = page["pageInfo"]["endCursor"]


def classify(items):
    """Kind comes from repo + labels first, title second. Titles alone are unreliable: some
    proposals have no [PROPOSAL] prefix (e.g. rfp#197)."""
    by_key = {i["key"]: i for i in items}
    for i in items:
        i["kind"], i["unlabeled_proposal"] = None, False
        repo, title = i["repo"], i["title"]
        if i["is_pr"] and repo.endswith("/lambda-prize"):
            i["kind"] = "lp_submission"
        elif repo.endswith("/rfp") and not i["is_pr"]:
            if "milestone" in i["labels"] or title.startswith("[MILESTONE]"):
                i["kind"] = "milestone"
            elif "proposal" in i["labels"] or title.startswith("[PROPOSAL]"):
                i["kind"] = "proposal"
        elif repo.endswith("/ecosystem") and not i["is_pr"]:
            if re.match(r"\[(Internal )?RFP\]", title):
                i["kind"] = "main_rfp"
            elif title.startswith("[LP]"):
                i["kind"] = "main_lp"
    for i in items:  # an unlabelled sub-issue of a main RFP issue is a proposal
        parent = by_key.get(i["parent"]) if i["parent"] else None
        if i["kind"] is None and i["repo"].endswith("/rfp") and parent and parent["kind"] == "main_rfp":
            i["kind"], i["unlabeled_proposal"] = "proposal", True
    return by_key


def load_ignored():
    if not IGNORE_FILE.exists():
        return set()
    return {(e["repo"], e["number"]) for e in json.loads(IGNORE_FILE.read_text())}


def evaluate(items, by_key, ignored):
    """Returns {item_key: [(severity, rule, message), ...]}."""
    result = defaultdict(list)

    def add(i, sev, rule, msg):
        result[i["key"]].append((sev, rule, msg))

    # Main issues in a column they may not be in; their children's parent-based flags are cascades.
    bad_parents = {i["key"] for i in items if i["kind"] in ("main_rfp", "main_lp")
                   and i["status"] and i["status"] not in ALLOWED[i["kind"]] and i["key"] not in ignored}

    contracting = defaultdict(list)
    for i in items:
        if i["kind"] == "proposal" and i["status"] == CONTRACTING and i["parent"]:
            contracting[i["parent"]].append(i)

    for i in items:
        if i["key"] in ignored:
            continue
        kind, status = i["kind"], i["status"]
        if kind is None:
            add(i, "AMBER", "unclassified", "could not tell what kind of item this is (repo/labels/title)")
            continue
        if i["unlabeled_proposal"]:
            add(i, "AMBER", "hygiene", "looks like a proposal but has no `proposal` label (the auto-add workflow filters on it)")
        if status is None:
            add(i, "RED", "status", "no Status set")
            continue

        # 1. Status vs kind
        if status not in ALLOWED[kind]:
            add(i, "RED", "status-vs-kind", f"a {kind.replace('_', ' ')} can't be in '{status}'")

        # 2. Closed / merged state vs Status
        if kind == "proposal" and i["state"] == "CLOSED":
            add(i, "RED", "closed", "closed proposal is still on the board (remove it)")
        if kind == "lp_submission" and i["state"] == "CLOSED":
            add(i, "RED", "closed", "PR closed without merging is still on the board (remove it)")
        if kind == "lp_submission" and i["state"] == "MERGED" and status == IN_REVIEW:
            add(i, "RED", "closed", "PR is merged but still in the review column")
        if kind in ("main_rfp", "main_lp") and i["state"] == "CLOSED" and status != "Complete":
            add(i, "RED", "closed", "main issue is closed but not Complete")
        if kind == "milestone" and i["state"] == "CLOSED" and status in ("Pending RFP milestone", "RFP milestone in review"):
            add(i, "RED", "closed", "milestone is closed but still pending/in review")

        # 3. Parent / child consistency
        parent = by_key.get(i["parent"]) if i["parent"] else None
        parent_status = parent["status"] if parent else None
        if kind == "milestone":
            if not i["parent"]:
                add(i, "RED", "parent", "milestone is not a sub-issue of any RFP issue")
            elif parent_status and i["parent"] not in bad_parents \
                    and parent_status not in (CONTRACTING, IN_DELIVERY, "Complete"):
                add(i, "RED", "parent", f"parent is in '{parent_status}', expected Contracting / In delivery / Complete")
        if kind == "proposal":
            if not i["parent"]:
                add(i, "RED", "parent", "proposal is not a sub-issue of its RFP's main issue")
            elif i["parent"] in bad_parents or i["parent"] in ignored or not parent_status:
                pass
            elif parent_status == IN_DELIVERY and status != CONTRACTING:
                add(i, "RED", "parent", "parent is In delivery; a non-accepted proposal should be unlinked from it")
            elif IDX[parent_status] < PUBLISHED:
                add(i, "RED", "parent", f"parent is in '{parent_status}' (left of Published) while proposals are in review")
        if kind == "main_rfp" and status == IN_DELIVERY:
            if not any(t.startswith("[MILESTONE]") for _, _, t in i["subs"]):
                add(i, "AMBER", "parent", "In delivery but has no [MILESTONE] sub-issues yet")
            stray = [f"#{n}" for r, n, t in i["subs"]
                     if not t.startswith("[MILESTONE]") and (by_key.get((r, n)) or {}).get("status") != CONTRACTING]
            if stray:
                add(i, "RED", "parent", f"In delivery but still has non-milestone sub-issues: {', '.join(stray)}")

        # 4. Category matches kind
        expected = "LPrize" if kind in ("main_lp", "lp_submission") else "RFP"
        if i["category"] is None:
            add(i, "RED", "category", f"Category is empty (expected {expected})")
        elif i["category"] != expected:
            add(i, "RED", "category", f"Category is {i['category']} but a {kind.replace('_', ' ')} should be {expected}")

        # 5. Published or further right => the RFP / λ-Prize value must be set
        if IDX[status] >= PUBLISHED:
            if kind in ("main_rfp", "proposal", "milestone") and not i["rfp_value"]:
                add(i, "RED", "field", "RFP field is empty (required from Published onwards; add the RFP-0NN option first if it doesn't exist)")
            if kind in ("main_lp", "lp_submission") and not i["lp_value"]:
                add(i, "RED", "field", "λ-Prize field is empty (required from Published onwards; add the LP-00NN option first if it doesn't exist)")

        # 6. An RFP open for proposals must say when it closes
        if kind == "main_rfp" and status == "Published (accepting proposals/submissions)" and not i["closing_date"]:
            add(i, "RED", "closing-date", "RFP is Published (open for proposals) but has no Closing date")

    for parent_key, group in contracting.items():
        if len(group) > 1 and parent_key not in ignored:
            for i in group:
                if i["key"] not in ignored:
                    add(i, "AMBER", "parent", f"{len(group)} proposals of the same RFP are in Contracting (only the accepted one belongs there)")
    return result


def verdict(findings):
    if any(sev == "RED" for sev, _, _ in findings):
        return RED
    if findings:
        return AMBER
    return OK


def reason_text(findings):
    ordered = sorted(findings, key=lambda f: (f[0] != "RED", f[1]))
    return "; ".join(f"{rule}: {msg}" for _, rule, msg in ordered)[:900]


def main():
    project_id, check_field, reason_field, options = load_meta()
    items = load_items()
    by_key = classify(items)
    ignored = load_ignored()
    findings = evaluate(items, by_key, ignored)
    now = datetime.now(timezone.utc)

    changes, skipped, report = [], [], []
    for i in items:
        f = findings.get(i["key"], [])
        want, why = verdict(f), reason_text(f)
        if want != OK:
            report.append((want, i, why))
        same = i["current_check"] == want and (i["current_reason"] or "") == why
        if same:
            continue
        # Don't newly flag an item that was only just edited (parent/child moves happen one at a time).
        if want != OK and now - i["updated"] < GRACE and i["current_check"] in (None, OK):
            skipped.append(i)
            continue
        changes.append((i, want, why))

    ref = lambda i: f'{i["repo"].split("/")[1]}#{i["num"]}'
    print(f"{len(items)} items evaluated, {len(report)} flagged, {len(changes)} field updates, "
          f"{len(skipped)} left alone (edited < {int(GRACE.total_seconds() // 60)} min ago)"
          f"{'  [DRY RUN: nothing written]' if DRY_RUN else ''}")
    for want, i, why in sorted(report, key=lambda r: (r[0] != RED, ref(r[1]))):
        print(f"  {want}  {ref(i)}  [{i['status']}]  {i['title'][:60]}\n        {why}")

    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a") as fh:
            fh.write(f"### Board check{' (dry run)' if DRY_RUN else ''}\n\n")
            fh.write(f"{len(items)} items, {len(report)} flagged, {len(changes)} updates.\n\n")
            if report:
                fh.write("| | Item | Status | Why |\n|---|---|---|---|\n")
                for want, i, why in sorted(report, key=lambda r: (r[0] != RED, ref(r[1]))):
                    link = f'https://github.com/{i["repo"]}/{"pull" if i["is_pr"] else "issues"}/{i["num"]}'
                    fh.write(f"| {want} | [{ref(i)}]({link}) | {i['status']} | {why} |\n")

    if DRY_RUN:
        return
    for i, want, why in changes:
        if i["current_check"] != want:
            graphql(SET_SELECT, project=project_id, item=i["item_id"], field=check_field, option=options[want])
        if (i["current_reason"] or "") != why:
            if why:
                graphql(SET_TEXT, project=project_id, item=i["item_id"], field=reason_field, text=why)
            else:
                graphql(CLEAR, project=project_id, item=i["item_id"], field=reason_field)
    print(f"wrote {len(changes)} item(s)")


if __name__ == "__main__":
    main()
