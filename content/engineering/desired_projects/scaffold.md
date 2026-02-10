---
title: Scaffold
type: Core Primitive
priority:
flywheel: Network Effects
category: Developer Tooling
---

Scaffolding tooling that lets developers bootstrap a project,
write and build Rust smart contracts,
deploy to a local or testnet environment,
and interact with contracts via a wallet.

## FURPS

### Functionality

- Create a project from one command and produce a runnable folder with contract and CLI client skeletons.
- Compile and deploy contract source into deployable chain artifacts from the generated project.
- Provide a CLI client flow that triggers wallet-based calls against the example contract on local or test networks.
- Deploy compiled contracts to testnet using explicit network configuration in the generated project.

### Usability

- Single command bootstrap with no manual project wiring required.
- Generated layout clearly separates contract code, client code, config, and deploy scripts.
- Scaffolded example contract and CLI interaction commands are straightforward to modify for real application logic.

### Reliability

- Bootstrap output is deterministic for a fixed scaffold version and the same input options.
- Local network can be started and torn down in isolation without modifying host-global blockchain state.
- Core smoke flow (init, build, local deploy and interact) succeeds in CI runs on supported environments.

### Performance

- Project scaffold generation completes in under 30 seconds on a standard developer machine.
- Local network is ready for first deploy in under 60 seconds.
- First clean build of scaffolded example contract completes in under 180 seconds.
- Local deployment of scaffolded example contract completes in under 60 seconds.

### Supportability

- Scaffold version and toolchain versions are explicit in generated output so projects remain buildable over time.
- Network configuration for local and testnet deployment is centralized and editable in one documented location.
- The scaffolded project includes command references for build, deploy, and interaction steps.

### + (Privacy, Anonymity, Censorship-Resistance)

- Local workflow does not require uploading source code, artifacts, or private keys to third-party services.
- CLI interaction flow works with locally controlled wallet keys and does not require custodial key management.
- Local development and testing can run fully offline from public networks.
- Testnet interaction uses explicit wallet and RPC configuration so developers can avoid accidental cross-network key reuse.
