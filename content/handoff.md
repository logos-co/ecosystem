---
title: R&D ↔ Eco Dev Handoff Protocol
---

**R&D builds it. Eco Dev breaks it, then evangelizes it. Both succeed together.**

---

## Philosophy

### Red Team Role

Eco Dev acts as **guaranteed co-developers** - the first external developers to stress-test technology:

- **Permission to break**: Misuse, stress test, find edge cases
- **Permission to be confused**: If experienced Eco Dev doesn't understand it, community won't either
- **Permission to say "no"**: Can flag software as not ready
- **No blame culture**: Finding issues is success, not failure

### Bazaar Model Alignment

Following Eric Raymond's "The Cathedral and the Bazaar":

**"Given enough eyeballs, all bugs are shallow"** (Linus's Law)

**Red team = Guaranteed eyeballs without gating public access**:

- Public release happens when R&D handoff complete
- Red team tests in parallel with community access
- Red team seeds the bazaar (initial feedback, shallow bugs, use it in examples and PoCs)
- **Goal**: Red team becomes obsolete as community co-developers emerge

---

## Team Ownership

### R&D Delivers

| Deliverable                        | Why?                                                        |
|------------------------------------|-------------------------------------------------------------|
| **Code**                           | Functioning software is the core of the delivery            |
| **Logos Core Module** (if library) | Usable in Logos Core, pre-wrapped                           |
| **Protocol, API Specs, FURPS**     | Clear expectation of behaviour and functionality delivered   |
| **Documentation**                  | To quickly jump into activities, and bypass discovery phase |
| **Dogfooding Proof**               | Help ensure the above is done and bases are covered         |

### Eco Dev Delivers

**Prerequisite**: Red Team/Solution, DevKit, and Contributor Journey streams must familiarise themselves with Logos R&D features and deliverables before engaging in handoff activities. This ensures effective testing, accurate communication, and quality output.

Eco Dev outputs are organised by **strategic impact** below. For detailed stream responsibilities and outputs, see [[integration/index#Streams|Eco Dev Engineering Streams]].

### Eco Dev Does NOT Own

Eco Dev is not responsible for:

- **R&D Process**: Setting priorities, defining roadmap, milestones (including testnet), or generally being involved in the Logos R&D process
- **Initial Documentation**: Producing initial docs, writing specs, FURPS, or APIs (see [R&D Delivers](#rd-delivers))
- **End-User Facing or Protocol Production Software**: Only developer tools are to be produced by the Eco Dev team
- **Wrapping C-Bindings**: Libraries produced by Logos R&D should be demonstrated usable in Logos Core before handoff.

### Delivery Strategy

For ecosystem essentials identified through handoff activities, the Integration stream determines the delivery approach. See the [[integration/index#Build internally, with Partner or via XPrize?|Build/Partner/XPrize decision flow]] in Eco Dev Engineering.

#### 1. Improve the Software

| Output                | Impact                                                                                                        |
|-----------------------|---------------------------------------------------------------------------------------------------------------|
| **GitHub Issues**     | Document bugs, edge cases, and confusion points discovered during testing (label: `from-eco-dev`)             |
| **Documentation PRs** | Fix unclear language, improve structure, ensure LLM-readability                                               |
| **PoC applications**  | Test the code by building PoCs of applications, ensure appropriate developer and user experience is delivered |

#### 2. Get Builder Attention

| Output                        | Impact                                                       |
|-------------------------------|--------------------------------------------------------------|
| **Vibe Coding Sessions**      | Live, honest exploration showing real developer experience   |
| **Long-form Posts**           | Deep dives on features, use cases, architectural decisions   |
| **Short-form Announcements**  | Discord posts, Twitter threads, release summaries            |
| **Presentations & Workshops** | Conference talks, meetups, hands-on sessions                 |
| **Office Hours**              | Regular Q&A sessions for direct builder support and feedback |

#### 3. Enable Distribution

| Output                 | Impact                                                                                                                                                                |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Examples**           | Application code others can fork/reference (could emerge from live vibe coding sessions).                                                                             |
| **PoC applications**   | Demonstrate feasibility and design of specific use cases, enabling more integration opportunities                                                                     |
| **Integration Guides** | Tutorials, videos and other complementary material to documentation and examples to show how Logos integrates with other tools/protocols or enable specific use cases |

#### 4. Enable Partnerships

| Output                        | Impact                                                                                  |
|-------------------------------|-----------------------------------------------------------------------------------------|
| **Value Proposition Mapping** | Map Logos features to partner/lead use cases and pain points for targeted outreach      |
| **Partnership Decks**         | Create tailored presentations for ecosystem partnerships (VCs, protocols, enterprises)  |
| **Integration Requirements**  | Document partner technical requirements and feed to Integration team for prioritization |
| **Case Studies**              | Document successful integrations/partnerships for sales pipeline and credibility        |
| **Partnership Pipeline**      | Track and nurture potential ecosystem integrations (e.g., protocols using Logos stack)  |

**Stream Ownership Mapping** (see [[integration/index|Eco Dev Engineering]] for stream details):

- **Improve Software**: Red Team/Solution (dogfooding, PoCs, bug reports) + DevKit (tooling feedback)
- **Get Builder Attention**: Contributor Journey (DevRel assets, workshops) + Marketing & Growth (social media, announcements)
- **Enable Distribution**: DevKit (sample apps, tooling) + Contributor Journey (examples, guides)
- **Enable Partnerships**: Business Development (value prop, partner connections, pipeline) + Integration (requirements, delivery strategy)

---

## Workflow

```mermaid
sequenceDiagram
    participant RD as R&D
    participant ED as Eco Dev
    participant GH as GitHub
    participant PUB as Public/Builders

    RD->>RD: Build + Document + Dogfood
    RD->>ED: Release
    RD->>PUB: Release

    Note over ED,PUB: Public gets access immediately

    par Improve Software
        ED->>ED: Test & break it (red team)
        ED->>ED: Build PoC applications
        ED->>GH: File issues (bugs, edge cases, UX)
        ED->>GH: Open docs PRs
    and Community Testing
        PUB->>PUB: Try software
        PUB->>GH: File issues
    end

    GH->>RD: Issues & PRs
    RD->>RD: Fix critical issues
    RD->>GH: Push fixes

    par Get Builder Attention
        ED->>PUB: Vibe coding sessions
        ED->>PUB: Long-form posts
        ED->>PUB: Short announcements (Discord/Twitter)
        ED->>PUB: Workshops & talks
        ED->>PUB: Office hours
    and Enable Distribution
        ED->>GH: Examples (from vibe sessions)
        ED->>GH: PoC applications
        ED->>PUB: Integration guides (tutorials, videos)
    and Enable Partnerships
        ED->>ED: Value prop mapping
        ED->>PUB: Partnership decks & case studies
        ED->>ED: Track partnership pipeline
    and Growing Bazaar
        PUB->>PUB: Build applications
        PUB->>GH: Contributions & feedback
    end

    Note over ED,PUB: Success = Community engagement > Eco Dev contributions
```

---

## Success Metrics

Metrics organized by **strategic impact**: software quality, builder attention, and distribution reach.

### 1. Improve the Software

| Metric                | Target                       | Why It Matters                           |
| --------------------- | ---------------------------- | ---------------------------------------- |
| **Issues Filed**      | >3 GitHub issues per release | Validate red team testing rigor          |
| **Documentation PRs** | >=1 PR per handoff           | Improve docs quality and LLM-readability |

### 2. Get Builder Attention

| Metric                        | Target                              | Why It Matters              |
| ----------------------------- | ----------------------------------- | --------------------------- |
| **Vibe Session Views**        | >500 views per session              | Measure DevRel reach        |
| **Long-form Post Engagement** | >1000 reads per post                | Measure deep content impact |
| **Short-form Reach**          | >100 interactions (Discord/Twitter) | Measure awareness spread    |
| **Workshop Attendance**       | >20 attendees per session           | Measure hands-on engagement |

### 3. Enable Distribution

| Metric                       | Target                                        | Why It Matters                |
| ---------------------------- | --------------------------------------------- | ----------------------------- |
| **Example Forks/References** | >10 forks or mentions in 90 days              | Measure code reuse            |
| **External Integrations**    | >1 external project using feature in 6 months | Measure protocol distribution |
| **Community Builds**         | First community application within 60 days    | Validate builder success      |

### 4. Bazaar Health (Overall)

| Metric                          | Target                                        | Why It Matters                        |
| ------------------------------- | --------------------------------------------- | ------------------------------------- |
| **Community Engagement Growth** | Community contributions > Eco Dev (over time) | Success = Eco Dev becomes unnecessary |
| **Self-Service Rate**           | >80% questions answered by docs/Known Issues  | Measure documentation quality         |

---

## Communication

The R&D teams need to have a clear process or roadmap to easily find the artefact for each deliverable (code, docs, etc).

**Handoff initiation**: R&D prompts Eco Dev team in `#ecodev` that a deliverable is done. Pointing to a single artefact (GitHub Issue or roadmap.logos.co page) that contains all information.

**Communication**: Lightweight communication can be done in the R&D's team general Discord channel (e.g. `#messaging-lobby`).

**Eco Dev Artefacts**: As per [Eco Dev Delivers](#eco-dev-delivers), the nature of artefact will dictate the channel (X live stream, blog post, etc).

**Escalation**: Once open in GitHub, critical issues are brought to the attention of the R&D lead of the software and R&D head. This may include issues from the community.

---

## Applies To

✅ Infrastructure components, developer tools, protocols, major features

❌ Internal tooling, research prototypes, emergency hotfixes

---
