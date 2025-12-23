---
title: Activity Hub
type: Desired Project
priority:
flywheel: Network Effects
category: Movement Tools
---

The activity hub serves two main purposes, which are related to the life cycle of Logos external contributors.

When a new person is interested in the Logos Movement, they can open the activity hub and proceed to a tutorial-like experience to learn more about Logos and get onboarded.

The result of this activity should give them enough context to understand what they can do (calls to actions). This could be done via a series of onboarding _quests_, that involves setting up the contributor _career path_ (developer, node operator, user, etc).

Once someone is onboarded in the Logos movement, then the activity hub acts as the homepage, or _base_ for further activities. It must enable a contributor to navigate through the Logos movement and technology content.

It is also from there that one can find further quests (call to action), such as:

- developers: ideas to build, projects to contribute too, libraries to use and dogfood, documentation to use
- writers: subjects to write about, books to read and amplify
- end-users: projects and app to try, and open bugs and feature requests for
- Circle leaders: push latest circle reports, organise task for the circle, etc.
- etc

These are some potential examples of sub-portal within the activity hub. The activity hub should act as a one-stop-shop for all Logos related activities.

## Browser vs Logos App

As mentioned above, the Activity Hub is expected to be a mini app in the [[Logos App]] . It may even have a special place in it. Such as the _default_ mini app. This is to be confirmed as it has a number of implications.

In terms of contributor journey, we do expect some of it to start in the browser.
Every journey should end with the contributor installing Logos App.
However, there is some options in terms of how long they can stay in the browser, and how soon they should be expected to install the Logos App.

Of course, we want their journey in the browser to be as short as possible. Yet, long enough so that we do onboard them and convince them to install the Logos App.

Moreover, delivering the contributor journeys in the browser is likely to be faster, as existing solutions can be re-used. For example, using GitHub repo to list existing Project ("awesome Logos") or ideas ("ideas.logos.com") is straightforward.

Finally, it should also be possible to mirror some content from Logos App to the browser, or vice-versa, as readonly snapshots. For examples:
- Docs living in GitHub can be mirrored in Logos App using a QtWebView module.
- A forum-like mini app where people list their _made with Logos projects_, could have the content mirrored on a read-only static html web page.
## Proposed Solution

Assuming
- We want to deliver key component of the contributor journey with testnet v0.1
- We ultimately want the Activity Hub to live in Logos App
- We do not want to invest in Logos technology in the browser

Proposal
1. Deliver select key components of the contributor journey in the browser, using web2 technology such as MarkDown + GitHub + Quartz, Discourse, etc.
2. Identify select key component to build the activity hub as a mini app, mainly based on technical requirements and dependencies (simplest/easiest first)
3. When ready as mini apps, migrate portals from (1) into Logos App, and provide read-only web mirror for key select components.
## Demand Validation

**Users:** Newcomers to Logos, active contributors (developers, writers, organizers), circle leaders, community members

**Use Cases:**

- Onboarding new movement participants with minimal friction
- Discovering contribution opportunities aligned with skills and interests
- Coordinating circle activities and tracking deliverables
- Gamifying participation through quests and attestations
- Navigating the Logos ecosystem and technology stack
## Technical Validation

**Risks & Challenges:**

- Balancing newcomer accessibility (web-first) with privacy guarantees (Logos Core)
- Maintaining content synchronization across dual deployment (proposed read-only snapshot for select components)
- Designing quest system that incentivizes genuine contribution
- Building network effects from cold start (empty hub problem)

**Integration Points:**

- [[integration/desired_projects/circle_cms|Circle Content Management System]] for documentation and knowledge management
- [[integration/desired_projects/private_daos|Private DAOs]] for governance and decision-making
- Logos Storage for censorship-resistant content hosting
- Logos Messaging for real-time collaboration and private communication
- Private attestation systems for quest completion verification
