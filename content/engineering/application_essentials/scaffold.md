---
title: Scaffold
type: Core Primitive
priority:
flywheel: Network Effects
category: Developer Tooling
---

Scaffolding tooling that lets developers bootstrap a project,
write and build Rust smart contracts,
deploy to a local or devnet environment,
and interact with contracts via a wallet.

## FURPS

### Functionality

- Create a project from one command and produce a runnable folder with contract and CLI client skeletons.
- Compile and deploy contract source into deployable chain artifacts from the generated project.
- Provide a CLI client flow that triggers wallet-based calls against the example contract on local or dev networks.
- Deploy compiled contracts to devnet using explicit network configuration in the generated project.

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
- Network configuration for local and devnet deployment is centralized and editable in one documented location.
- The scaffolded project includes command references for build, deploy, and interaction steps.

### + (Privacy, Anonymity, Censorship-Resistance)

- Local workflow does not require uploading source code, artifacts, or private keys to third-party services.
- CLI interaction flow works with locally controlled wallet keys and does not require custodial key management.
- Local development and testing can run fully offline from public networks.
- Devnet interaction uses explicit wallet and RPC configuration so developers can avoid accidental cross-network key reuse.

## ADR (Architectural Decision Records)

### Project Structure (Single-Repo Template)

Developers need one bootstrap target that is immediately runnable and easy to modify.
Use a single generated project containing contract, CLI client, configuration, and deployment scripts.
Single-template onboarding is very simple.

### CLI

The workflow should be discoverable for new developers.
Expose one CLI surface with subcommands for init, build, deploy, and interact.
One CLI improves onboarding but makes it hard to maintain backward-compatibility.

### Local Runtime

Local development should work without requiring manually managed external node setup.
Provide embedded localnet lifecycle commands as part of scaffold workflow.
The scaffolded toolchain can start, stop, and reset a localnet environment
that supports deploy and wallet-based interaction for the generated example contract.

### Build Pipeline

Contract compilation should align with Rust ecosystem standards
and avoid unnecessary abstraction.
Use native Cargo-based build flow as the primary compilation path.

### Network Configuration

Developers need explicit, editable environment targeting for local and devnet workflows.
Use environment-file based network configuration as the default model.
Generated projects include env files for local and devnet RPC,
wallet interaction settings used by deploy and interact commands.
Env files are familiar and automation-friendly,
but require strict handling to avoid credential leakage.

## Dependencies

### Internal Dependencies

- Logos Core DevEx for overall developer journey alignment and terminology.
- Logos Blockchain and Logos Execution Environment for functionality. 
- Wallet Module for interactions with Logos Execution Environment.

### Runtime Dependencies

- Local network runtime availability for local deploy and interaction workflows.
- Devnet RPC endpoint availability and stable chain configuration.
- Deterministic local/devnet account and chain configuration via environment files.

### Wallet Dependencies

- Wallet available for signing transactions initiated by CLI interaction commands.
- Network-aware wallet configuration to prevent cross-network key misuse.
