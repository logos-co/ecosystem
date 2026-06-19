---
title: Sample Apps
---

# Sample Apps

Sample apps are PoC applications that are for testnet purposes only (aka, not mainnet). They are created to demonstrate the feasibility of a desired project.
They can become a template for developer to build said desired projects and push it to production/mainnet.
They can also serve as:

- Example on how to build on the Logos stack.
- Demo applications
- Dogfooding vector to test specific features of the Logos stack

A sample app moves through three phases: **Scope**, **Build**, and **Document**. Each has its own deliverables and team review expectations.

## Scope

The scope is agreed upon and reviewed before building starts. Scoping deliverables are produced as a PR on the sample app's repo so the team can review them. Keep all artefacts light and nimble — the goal is to agree on a clear, limited scope, trim off any excess, and know when building is "enough".

### 1. Functional scope

What this version will do, captured as [FURPS+](https://en.wikipedia.org/wiki/FURPS) or user stories. Lives in a `FURPS.md` alongside the sample app.

Sample apps need a clear, limited scope because they exist to:

- Explore and PoC specific boundaries and designs.
- Demonstrate what is possible to users.
- Provide developers a canonical way to build on Logos.
- Dogfood our documentation, stack and devkit: sample apps are meant to be built using the resources we give to developers, identifying and correcting any issue or gaps.

> The functional scope **must** be reviewed by the team (i.e. as a PR).

### 2. ADRs

Architecture Decision Records documenting **why** we built it this way, conveying how to use the Logos stack. Lives in an `ADR.md` alongside the sample app.

FURPS+ documents behaviour; ADRs document the reasoning behind design and protocol choices. As we build sample apps, we make decisions to use Logos components (delivery, storage, etc.) in specific ways. We document those decisions so that developers using sample apps as inspiration or examples understand why we did so. For example:

- In chat, we send messages over delivery because it gives us better latency.
- But we send images over storage, and then the CID over delivery, because delivery has a small message size (150KiB) and is rate limited (RLN).
- Justifying why we use the Zone SDK (new zone) vs LEZ.

> ADRs **must** be reviewed by the team (i.e. as a PR).

### 3. Dependencies

What the sample app uses: the specific components and design patterns of the Logos stack it depends on. Captured in a `Dependencies` section of the `README.md`.

This makes it easier for a developer to find an example for a specific use case. For example:

- Upload encrypted data to storage, exchanging the data address (CID) in an e2ee chat.
- Upload clear data to storage, indexing it in a custom Logos zone.
- Write an LEZ program that composes with a TWAP oracle program.

## Build

The sample app is built against the scope above, in a public repo with the right licensing.

- The built module is published to the Eco Dev Eng Logos module repo (repo: _TBD_).

## Document

Once built, a documentation packet ("doc-packet") is handed off to the doc team:

- **How to install** (via the Logos module repo) and use it.
- **What the code demonstrates** — drawing on the Dependencies above, so developers can find the example matching their use case.

A GUI doc-packet does not need screenshots and can be very light.

> The documentation **must** be reviewed by the team.

## Tracking

Each release of a sample app is tracked with a milestone on the [present repo](https://github.com/logos-co/ecosystem/milestones).

Scoping is kicked off with the **Sample App Scoping** issue template in this repo.
