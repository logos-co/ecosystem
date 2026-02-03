---
title: Activity Hub
type: Desired Project
priority:
flywheel: Network Effects
category: Movement Tools
---

The activity hub serves two main purposes, which are related to the life cycle of Logos movement participants (better word?).

When a new person is interested in the Logos Movement, they can open the activity hub and proceed to a tutorial-like experience to learn more about Logos and get onboarded.

The result of this activity should give them enough context to understand what they can do (calls to actions). This could be done via a series of onboarding _quests_, that involves setting up the contributor _career path_.

Once someone is onboarded in the Logos movement, then the activity hub acts as the homepage, or _base_ from most further activities. It must enable a contributor to navigate through the Logos movement and technology content.

It is also from there that one can find further quests (call to action), such as:

- developers: ideas to build, projects to contribute too, libraries to use and dogfood, documentation to use
- writers: subjects to write about, books to read and amplify
- end-users: projects and app to try, and open bugs and feature requests for
- Circle leaders: push latest circle reports, organise task for the circle, etc.
- etc

These are some potential examples of sub-portal within the activity hub. The activity hub should act as a one-stop-shop for all Logos related activities.

Because of this, the browser stack needs to be considered. The strategy is:

- Only static content is available in the Web, with a CTA to onboard contributors in Logos App
- Interactive content is delivered in the Activity Hub, a *default* mini app in the Logos App
## Gamification

Gamification is a critical part of the Logos movement. As we live, join circle, discuss with fellow exiters, we play the game of life.
The activity hub is at the core of the gamification of participation in Logos.

Every potential contributions can take the form of a quest. Depending of the profile of the users (associated circles, career path, etc), then the activity hub must be able to push the relevant to the user. Whether it is an event to join near their (selected) location, a new library release for them to integrate in their app, a new app released by another contributor to dogfood and provide feedback.

Finally, the completion of quests may lead to onchain attestation or reward (e.g. NFT). Gaming mechanics must be studied and most relevant ones applied without restrain.
## Demand Validation

**Potential Users:** Newcomers to Logos, active contributors (developers, writers, organizers), circle leaders, community members

**Use Cases:**

- Onboarding new movement participants with minimal friction
- Discovering contribution opportunities aligned with skills and interests
- Coordinating circle activities and tracking deliverables
- Gamifying participation through quests and attestations
- Navigating the Logos ecosystem and technology stack

## Possible Implementation

- **Progressive Web App (PWA)**: Web-first implementation deployable to traditional hosting and IPFS
- **Logos Core Integration**: Native application using Logos Storage and private networking for censorship-resistant access
- **Quest Engine**: Pluggable system for defining, tracking, and completing contribution quests
- **Profile System**: User profiles with career paths, completed quests, and earned attestations (optionally private)
- **Sub-Portal Framework**: Modular architecture allowing independent development of role-specific portals (developer, writer, etc.)

## Technical Validation

**Risks & Challenges:**

- Balancing newcomer accessibility (web-first) with privacy guarantees (Logos Core)
- Maintaining content synchronization across dual deployment
- Designing quest system that incentivizes genuine contribution without gaming
- Building network effects from cold start (empty hub problem)
- Privacy-preserving analytics for quest completion and engagement metrics

**Integration Points:**

- [[engineering/desired_projects/circle_cms|Circle Content Management System]] for documentation and knowledge management
- [[engineering/desired_projects/private_daos|Private DAOs]] for governance and decision-making
- Logos Storage for censorship-resistant content hosting
- Private attestation systems for quest completion verification

## Sub-portals

TODO: a tree map of sub-portals necessary in the activity hub.

- [[engineering/desired_projects/circle_cms|Circle Content Management System]]
