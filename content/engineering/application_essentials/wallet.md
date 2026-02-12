---
title: Wallet
type: Core Primitive
priority:
flywheel: Network Effects
category: Developer Tooling
---

## FURPS

### Functionality

- Cross-layer bridge between L1 and LEZ for token movement; support gas-related flows.
- Support token sources from L1 (consensus, bridge) and external (atomic swap into LEZ).
- Deterministic key management.

### Usability

- Single-command bootstrap for all wallets at the same time.
- Clear separation between L1 and LEZ contexts in generated/config layouts.
- Discoverable commands for bridge and gas flows.
- Defaults that reduce cross-layer confusion (e.g. network-aware config).

### Reliability

- Vertical slices (L1-only, LEZ-only, bridge flow) reproducible on a clean machine.
- Local/DevNet workflows isolatable from production state.

### Performance

- Key operations within demo-tolerable time.

### Supportability

- Versioning and toolchain versions explicit in output.
- Env-based config for networks and endpoints.

### + (Privacy, Anonymity, Censorship-Resistance)

- No upload of keys or source to third parties for core flows.
- Explicit network targeting to avoid cross-network key reuse.

## ADR (Architectural Decision Records)

### Unified Wallet

One wallet module instead of two.
Combine L1 and LEZ capabilities in a single module because users need both contexts;
separate modules would force consumers to import and orchestrate both.
Unified module simplifies distribution and onboarding.

### Cross-Layer Design: Observe First

Cross-layer flows (bridging, gas, "where are my tokens") are hard to explain and non-obvious.
Avoid premature abstraction.
Document and categorize real usage before committing to a higher-order API.

### Distribution via Logos Core

Ship both wallet capabilities together in Logos Core so users get both contexts in one product.
UI/UX should make the L1/LEZ relationship and flows discoverable.

### Expose Underlying Wallets; Higher-Order Commands Later

One wallet for both execution environments that exposes underlying L1 and LEZ wallets clearly.
Once user operations at the intersection are known,
implement them as higher-order wallet commands rather than requiring manual composition.

## Dependencies

### Internal Dependencies

- [[engineering/infrastructure_essentials/logos_core|Logos Core]] for distribution and module hosting
- Logos Blockchain for L1 wallet
- Logos Execution Environment (LEZ) for LEZ wallet

### Runtime Dependencies

- RPC endpoints for L1 and LEZ
- Bridge infrastructure for token movement between L1 and LEZ
- Network configuration (env-based or equivalent) for both layers
