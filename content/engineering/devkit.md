---
title: Devkit
type:
priority:
category: Developer Tools
---

# Approach

Provide a coherent single developer environment for the community to build,
run, debug, and ship Logos apps end-to-end.

This exists to shorten the feedback loop between:
- Logos R&D teams (core codebases + modules)
- Community builders (external developers building on Logos tech)

The primary mechanism is **standardization + streamlining**:
- One coherent scaffold that works across developer OS / environments
- A predictable workflow for build/run/deploy/debug
- A consistent project structure that makes support and contributions frictionless

## Why it is needed

We need a foundation that supports multiple development targets:
- Narrow: Logos Execution Zone (LEZ) / Logos blockchain program development
- Broader: apps that may later integrate [[engineering/infrastructure_essentials/logos_storage|Logos Storage]], [[engineering/infrastructure_essentials/logos_messaging|Logos Messaging]], and other modules

Without a scaffold, each builder:
- Reinvents project wiring and environment setup
- Has longer time-to-first-success
- Produces inconsistent layouts and workflows that are hard to support
- Has higher friction to contribute back upstream

And with increasing complexity of Logos stack it managing such environment will be harder and harder.

## Community contribution loop

A coherent scaffold makes contribution "stupidly easy" by:
- Enforcing consistent formats and structure
- Making it easy to reproduce issues (environment parity)
- Enabling standardized "reporting / diagnostics" flows for support
- Encouraging upstream improvements not only to the scaffold repo, but to:
  - specific modules (e.g., blockchain module)
  - underlying software codebases beneath those modules

# Versions

## v0.1

[[engineering/application_essentials/scaffold|FURPS]]

This step is well defined and primarily focuses on:
- LEZ (Logos Execution Zone) / Logos blockchain program development
- Bootstrapping a project and development environment quickly
- Localnet-only interactions (initial vertical slice)
- Early templates and meaningful developer shortcuts

Key characteristics:
- Provides the first coherent developer entrypoint
- Proves the basic workflow: scaffold, build, deploy, interact
- Establishes baseline structure and conventions to build on

Main limitation:
- Only LEZ and too environment-limited (localnet focus)
- Not yet a general developer kit for broader Logos modules

## v0.2

Extends the LEZ / blockchain developer experience with multi-network targeting
and begins extracting reusable modules from scaffold patterns.

Primary goals:
- Extend and harden the LEZ / blockchain developer experience
- Add network targets beyond localnet:
  - localnet
  - testnet (target)
  - mainnet (uncertain)
- Improve security and usability around:
  - deployment workflows
  - secrets handling
  - environment configuration that is easy *and* secure

### Derive "experience - modules"

In v0.2 we should continue extracting reusable building blocks discovered in v0.1 into tangible modules.

Example already identified:
- A framework for writing LEZ / blockchain programs
  - macros
  - boilerplate reduction
  - common shortcuts / patterns
  - packaged as a separate module (not just scaffold code)

In v0.2, continue searching for:
- additional reusable patterns
- developer shortcuts that belong in modules (not in scaffold glue)
- clearer separation between:
  - scaffold tooling (DevEx glue, project wiring, workflows)
  - Logos libraries/framework modules (developer-facing primitives)

### Support and feedback loop improvements

v0.2 should expand DevEx features that help:
- collecting feedback
- providing support
- observing community patterns and bringing them back upstream

## v0.3+

Broadens the scaffold from LEZ-only tooling to full Logos application development,
starting with [[engineering/infrastructure_essentials/wallet|Wallet]] integration and templates built on [[engineering/application_essentials/logos_core_devex|Logos Core]].

Primary goals:
- Support for Logos Core and Logos Modules
- Make Logos modules + Logos Core the primary scaffolding path for apps
- Provide a diverse set of templates and sample apps
- Enable bootstrapping of a full-fledged Logos application that is sufficient for real project

Outcome expectation:
- A developer can scaffold a "real Logos app" end-to-end.
- The scaffold becomes the standard entrypoint for app creation and delivery.

Open uncertainty acknowledged:
- Exact mechanics of "Logos Core + modules" integration are not fully clear yet
- The resulting app should be runnable in the intended Logos viewer environment
- Scaffold roadmap is directly coupled to module maturity and availability

# Design Principles

- Devkit foundation must be **lean**.
- It should provide what cannot (or should not) live inside the Logos stack itself:
  - tooling
  - useful shortcuts
  - development routines / runtime glue
  - organizing structure and conventions
- Logos Scaffold must also enable community contributions and standard DevEx support flows.
