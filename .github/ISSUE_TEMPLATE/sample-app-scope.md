---
name: "Sample App Scoping"
about: "Discover and define scope for new sample app version"
title: "Discover and define scope for <sample app name>"
labels: sample-app
assignees: ''

---

Define the scope for the <NAME> sample app v<VERSION>.

## Definition of Done

All deliverables should be done as a PR on a new repo for the sample app.

- [ ] FURPS+ in a `FURPS.md`: to agree on the limited scope of the 
- [ ] ADRs (Architecture Decision Record) in a `ADR.md`
- [ ] Component and design patterns used in a `Dependencies` section of `README.md`

<!--

## Why?

Justifying the Definition of Done. Do note that all artefact should be light and nimble.

### FURPS+

Agree on the scope of the sample apps. Sample apps are here to:

- Explore and PoC specific boundaries, designs
- Demonstrate what is possible to users
- Provide to developers a canonical way to build on Logos
- Dogfood our documentation, stack and devkit: sample apps are meant to be built using the resources we give to developers; identifying and correcting any issue or gaps

Hence, a sample app needs to have a clear limited scope to fit the above.
By defining a scope, and reviewing it, we can help trim off any excess, and "stop" building when it is enough.

### Architectural Decision Records (ADRs)

ADRs are here to document why we made specific design decisions. FURPS only document behaviour.

As we build sample apps, we make decisions to use the Logos component (delivery, storage, etc) in some specific manners.
We document those decisions so that developers using sample apps as inspiration or examples, understand why we do so.

For example:
- In chat, we send message over delivery because it gives us better latency
- But we send images over storage, and then cid over delivery, because delivery has a small message size (150KiB), and is rate limited (RLN).

Or justifiying why using the Zone SDK (new zone) vs LEZ.
Etc.

### Dependencies

Provide clear information for potential users and developer what components and designs are used in this sample app.

This makes it easier for a developer to find example for a specific use case. For example:

- upload encrypted data to storage, exchanging data address (cid) in a e2ee chat
- upload clear data to starge, indexing it in a custom Logos zone
- Write an LEZ program that uses compose with TWAP oracle program

-->

## Notes

- <Questions and known gotchas regarding this sample app>
