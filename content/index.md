---
title: Ecosystem Development Engineering
---

# Logos Ecosystem Development Engineering

Home of the Logos **Ecosystem Development Engineering** ("Eco Dev Eng") team. We sit between Logos R&D and the wider community/ecosystem: we dogfood and stress-test what R&D ships, build proof-of-concept apps, maintain developer tooling, shape RFPs and Lambda Prizes, and feed real builder and business needs back into the stack.

## Team

| Name          | GitHub                                               |
| ------------- | ---------------------------------------------------- |
| Franck (lead) | [@fryorcraken](https://github.com/fryorcraken)       |
| James Zaki    | [@jzaki](https://github.com/jzaki)                   |
| Vaclav Pavlin | [@vpavlin](https://github.com/vpavlin)               |
| Danish Arora  | [@danisharora099](https://github.com/danisharora099) |
| Sasha         | [@weboko](https://github.com/weboko)                 |
| Alisher       | [@xAlisher](https://github.com/xAlisher)             |

# Mandate

Enable bi-directional feedback between the Logos technical stack and the Logos community/ecosystem. By:

- Identifying and evaluating the technological needs of the community and ecosystem
- Translating those needs into requirements for the technology stack and value of said requirements
- Propagating information about latest delivery, to encourage the community to use, build, remix and contribute back to the Logos Technology stack
- Providing (solution) engineering capabilities for ecosystem development activities.

# What We Do

The team's work is organised into five streams, **numbered in priority order**. Team members shift between streams as priorities demand, as long as their role at a given time is clear to ensure software delivery. For how these streams collaborate during R&D handoffs, see the [[handoff|R&D ↔ Eco Dev Handoff Protocol]].

Two of these streams relate as layers: **Journeys** validate and orient people around what Logos R&D delivers, and **RFPs & Lambda Prizes** finance the work built _on top of_ that delivered stack.

## 1. RFPs & Lambda Prizes

RFPs and Lambda Prizes are our **instrument to finance work built on top of the journeys and what Logos R&D delivers**. They fund two types of demand:

1. **Readiness of the stack** — what we want built so the stack is "batteries included"
2. **Demand from users** — what end-users and partners want built (including partner integrations)

**Mandate:** Identify what to finance (readiness + user/partner demand), choose the delivery vehicle (build internally, partner, RFP, or Lambda Prize — see decision flow below), and own the technical side of RFPs and Lambda Prizes.

**Competency:** Solution Engineers, technical product specification, requirements engineering, and architecture review.

**Outputs:**

- Identification and validation of components the community should build, from both readiness and user/partner demand
- Delivery strategy: re-use, partnership, RFP, or build internally
- λPrize and RFP technical requirements, scoping and estimation (as [PRs](https://github.com/logos-co/rfp/pulls))
- Input on λPrize and RFP dependencies, feasibility and priorities
- Technical and architectural sign-off of proposals (applications) and of deliverables
- Business and application needs expressed back to Logos R&D
- Support for candidates on their delivery; pulling in SME (Logos R&D) when necessary

**Feedback to:** Logos R&D on priorities for desired components and related essentials.

## 2. Journeys

A **journey** is a high-level user story of what Logos R&D (our internal team) is delivering — "here is what someone can do with the stack." Journeys are the spine the team works along to validate and orient people around each R&D delivery.

**Mandate:** For each R&D delivery, identify the journey, refine the documentation for it, and dogfood the docs and journey end-to-end.

**Competency:** Solution / Architect — deep understanding of how to use the full Logos stack; technical writing.

**Outputs:**

- Journeys mapping what people can build and do with the Logos stack (see [journeys.logos.co](https://journeys.logos.co))
- Review and refinement of documentation for each journey
- Dogfooding / red-teaming of the docs and journey (permission to break — see [[handoff|the Handoff Protocol]])
- GitHub Issues documenting bugs, edge cases, confusion points (label: `from-eco-dev`)
- DevEx evaluation (reports/issues) and feature requests

**Feedback to:** Logos R&D on bugs and desired features; Doc team on docs.

## 3. DevKit / DappFoundry

**Mandate:** Build and maintain tooling and SDKs for Logos development.

**Competency:** Tooling, scripting, blockchain development, full software cycle.

**Outputs:**

- [Logos Scaffold](https://github.com/logos-co/scaffold): local dev environment for Logos Blockchain and Core, with template apps
- [spel](https://github.com/logos-co/spel): DevKit tooling
- SDK wrappers in other languages for Logos Core
- Template apps and examples (polished reference implementations, can be adapted from sample apps)

**Feedback to:** Logos R&D on bugs and desired features emerging from usage and developer experience.

**Note:** The tooling produced by DevKit is **not** a workaround for API issues.

## 4. Builder Support & Workshops

**Mandate:** Provide hands-on engineering support to builders and run workshops at physical events.

**Competency:** Solution engineering, mentorship, community engagement.

**Outputs:**

- Builder support: mentorship, technical assistance, solution engineering (incl. λPrize candidates and partners)
- Workshops and hands-on sessions at physical events
- Examples and integration guides that emerge from supporting builders

## 5. Sample Apps

**Mandate:** Build [[sample_apps|Sample Apps]] as Proof-of-Concepts — a tool to document and verify more complex usage of the stack and show feasibility.

**Competency:** Blockchain development, full software cycle, solution engineering.

**Outputs:**

- Sample apps (PoCs) demonstrating feasibility and more complex stack usage
- Architecture Decision Records, functional and technical requirements (FURPS)
- Feasibility findings fed back into Journeys and RFP/Lambda Prize scoping

# Build internally, with a Partner, via RFP or via Lambda Prize?

When do we want to build internally, find a partner, or push an RFP or a Lambda Prize?

Lambda Prize is meant for complicated and ambitious projects — huge challenges where we do not dictate the solution. We're looking at a category of problem and put a price to solve it. We let someone else draft the product requirements and solution.

RFPs are here to outsource development effort while keeping tight control on the output.

The other ways are for specific projects or ideas that we, the community, want to see built.

```mermaid
flowchart TD
    START["Idea comes in<br/>(Logos circle, internal, or other)"]
    POC["PoC to prove feasibility"]
    PARTNER{"External partners<br/>provide same thing?"}
    CONVINCE{"Can convince<br/>to integrate?"}
    COST["Evaluate cost"]
    INTEGRATE["Partner Integration"]
    DEV_INTEREST{"Developers want<br/>to build it?"}
    RFP["RFP with price tag<br/>(support developers)"]
    INTERNAL["Build Internally"]

    START --> POC
    POC --> PARTNER
    PARTNER -->|Yes| CONVINCE
    PARTNER -->|No| DEV_INTEREST
    CONVINCE -->|Yes| COST
    CONVINCE -->|No| DEV_INTEREST
    COST --> INTEGRATE
    DEV_INTEREST -->|Yes| RFP
    DEV_INTEREST -->|No / Critical| INTERNAL
```

# Concerns / Priorities

> We are still building the house; once ready, we want to invite more people and then decide whether to build a pool or gym next.

> Current priorities mainly come from completing an MVP level product and doing the mainnet launch. Once done, it will be more realistic to be driven by community feedback.

> Ideally the R&D priorities should be set by eco dev findings. Continuous push and pull.

What drives the prioritisation of the requirements forwarded to the Logos contributors?

1. **Sustainability** — Enable and drive onchain activity and value accrual to sustain the development of the technology stack for the Movement. Ensure that the L1 comes with batteries included, i.e. essential apps are available at mainnet launch.
2. **Movement** — The end goal, why we are all here. Provide the technological solutions needed by the movement, contributors and participants, circles and people to organise, identify and solve winnable issues. Make the Internet a catalyst for prosperity and emancipation. No one is free until we are all free. See the [Logos Manifesto](https://logos.co/manifesto) for the vision, and [Farewell to Westphalia](https://logos.co/farewell-to-westphalia) to open the conversation on how we get there.
3. **Technology De-Risking** — Enable early delivery and validation of technology with the most unknowns and risks. Engineering teams flag the risks to get them prioritised accordingly.

# Monthly Priorities

## Feb 2026

- Progress on atomic swap sample app — set FURPS and start development
- Progress on multisig wallet — set FURPS and continue development
- Progress on scaffold — set FURPS and start development
- Review infra essentials (e.g. block explorer), understand R&D delivery scope and review need for partners (rolled over)
- Agree and set process for docs handover

## Dec-Jan 2025

- Set a scope of work for Eco Dev Engineering for [[milestones/testnet_v0_1|testnet_v0_1]]
  - Start smart contract dogfooding and scaffold — highest priority
  - Consider desired apps, review requirements, and plan PoCs for them
  - Review infra essentials (e.g. block explorer), understand R&D delivery scope and review need for partners
- Validation matrix work postponed (might touch on it)

# Goals

See the [Eco Dev Eng GitHub Project board](https://github.com/orgs/logos-co/projects/11/views/1).

1. Dogfood and software for [Testnet v0.1](https://roadmap.logos.co/testnets/v01). See [[milestones/testnet_v0_1|Testnet v0.1]].
   1. Priority on [LEE/LEZ user journeys](https://github.com/logos-co/ecosystem/milestone/4)
2. Build Multi-Sig sample app v0.1. [Milestone](https://github.com/logos-co/ecosystem/milestone/8).
3. Build Atomic Swaps sample app v0.1. [Milestone](https://github.com/logos-co/ecosystem/milestone/7).
4. Build [Scaffold Devkit](https://github.com/logos-co/scaffold) v0.1. [Milestone](https://github.com/logos-co/ecosystem/milestone/9).
5. Build Forum sample app v0.1 (based on opchan protocol) as a base for circle CMS and activity hub use cases.

Note: AMM sample app has been built by the LEE/LEZ team.

# Testnet Scope Flow

```mermaid
flowchart TB
    RD["<b>Logos R&D</b><br/>Sets testnet scope & objective"]
        subgraph ecodev["Eco Dev Team"]
        subgraph eng["Engineering Streams"]
            INT["<b>Integration</b><br/>Ecosystem map, delivery strategy,<br/>requirements"]
            XP["<b>λPrize & RFPs Advisory</b><br/>Technical sign-off, requirements,<br/>feasibility & candidate support"]
            RT["<b>Red Team / Solution</b><br/>Dogfooding, PoCs,<br/>builder support"]
            DK["<b>DevKit / DappFoundry</b><br/>Tooling, SDKs,<br/>sample apps"]
        end
        subgraph bd["BD Streams"]
            CJ["<b>Contributor Journey</b><br/>DevRel assets, metrics"]
            BDP["<b>Partnerships</b><br/>Partner connections"]
        end
        subgraph content["Content & Growth"]
            DOC["<b>Documentation</b>"]
            WEB["<b>Website Content</b>"]
            MG["<b>Marketing & Growth</b>"]
            CI["<b>Circles</b>"]
        end
    end

    RD <-->|"scope & feedback"| INT
    INT -->|"delivery strategy"| XP
    INT -->|"priorities"| RT
    INT -->|"priorities"| DK
    INT -->|"partner needs"| BDP
    XP <-->|"solution input"| RT
    XP -->|"campaign needs"| MG
    RT -->|"PoCs"| DK
    RT -->|"examples"| CJ
    DK -->|"tooling"| CJ
    CJ -->|"translates"| content
    BDP -.->|"connections"| INT
    RT -.->|"bugs & DevEx"| RD
    DK -.->|"bugs & DevEx"| RD
    XP -.->|"SME needs"| RD
    content -->|"CTAs"| USERS["Users & Personas"]
```

**Translation:** Testnet scope requires technical translation into priorities and execution order.

- **Integration** translates to: Engineering teams (Red Team, DevKit, Contributor Journey) + BD
- **Contributor Journey** translates to: Documentation, Website Content, Marketing & Growth

# Processes

- [[handoff|R&D ↔ Eco Dev Handoff Protocol]]
- [[sample_apps|Sample Apps]]

# Milestones

- [[milestones/testnet_v0_1|Testnet v0.1]]

# Resources

- [Logos website](https://logos.co)
- [Logos Docs](https://github.com/logos-co/logos-docs) (documentation website is WIP)
- [Journeys](https://journeys.logos.co)
- [Flywheels](https://friendly-carnival-n3z5zww.pages.github.io/) ([repo](https://github.com/logos-co/flywheels.logos.co))
- [Eco Dev Eng GitHub Project board](https://github.com/orgs/logos-co/projects/11/views/1)
- DevKit: [scaffold](https://github.com/logos-co/scaffold) · [spel](https://github.com/logos-co/spel)
- [RFPs](https://github.com/logos-co/rfp/pulls) · [Ecosystem milestones](https://github.com/logos-co/ecosystem/milestones)

# Content Authorship

This wiki uses AI assistance to draft and organise content. To maintain transparency, LLM-generated sections that haven't been human-reviewed are marked with an indicator placed immediately after the section header:

> [!ai-generated]
> This section was generated by an LLM and has not yet been human-reviewed.

The indicator applies to the entire section (from the header through all subsections until the next same-level or higher-level header). Once content is reviewed and approved by a human contributor, this indicator is removed. Unmarked content has been human-curated.
