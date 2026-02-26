---
title: LEZ Developer Framework
type: Core Primitive
priority: 0
flywheel: Developer Experience
category: Infrastructure & Tooling
---

A developer framework for building applications on the Logos Execution Zone (LEZ) — the Logos smart contract layer powered by Nescience's zkVM. Inspired by [Anchor](https://www.anchor-lang.com/) for Solana: write your program logic with proc macros and get IDL generation, a CLI, and project scaffolding for free.

PoC: https://github.com/jimmy-claw/lez-framework  
Example: https://github.com/jimmy-claw/lez-multisig-framework  
Scaffold tool: https://github.com/logos-co/logos-scaffold

## Demand Validation

**Potential Users:** Developers building dApps, tooling, and services on the Logos stack

**Use Cases:**

- **dApp developers**: Build privacy-preserving applications (multisig, DAOs, DeFi) on LEZ without deep zkVM expertise
- **Ecosystem growth**: Lower the barrier to entry for third-party developers contributing to the Logos ecosystem
- **Rapid prototyping**: Scaffold, build, and deploy a LEZ program in minutes rather than days
- **Logos Core integration**: Generate typed FFI clients automatically for Qt/QML Logos Core modules

## Possible Implementation

The framework consists of four components:

- **`lez-framework` crate** — proc macro (`#[lez_program]`) that annotates Rust program code with account constraints, PDA derivation, and instruction metadata
- **`lez-cli`** — generates a full CLI from the program's IDL; developers get a working command-line client with zero boilerplate
- **`lez-client-gen`** — reads the IDL and generates typed Rust client code + C FFI headers for Logos Core Qt module integration
- **`logos-scaffold`** — scaffolding tool (`logos-scaffold new`) that bootstraps a new LEZ project with correct workspace layout, Nix build configs, and Makefile

**Developer workflow:**
```
logos-scaffold new my-program   # Scaffold project
make build                       # Compile RISC Zero guest
make idl                         # Generate IDL from annotations
make deploy                      # Deploy to LEZ sequencer
make cli ARGS="..."              # Submit transactions via auto-generated CLI
```

## Technical Validation

**Risks & Challenges:**

- RISC Zero zkVM compilation requires a dedicated toolchain (risc0-toolchain); build times are long
- IDL generation relies on proc macros — complex account relationships require careful annotation
- C FFI headers for Logos Core integration are generated automatically by `lez-client-gen` from the IDL; manual updates are only needed for types not yet expressible in the IDL schema
- Nix build reproducibility across Linux/macOS requires careful flake configuration

**Integration Points:**

- [[engineering/desired_projects/multisig|Multisig Treasury]]: Reference implementation of LEZ Framework — `lez-multisig-framework`
- [[engineering/application_essentials/scaffold|Logos Scaffold]]: `logos-scaffold new` bootstraps LEZ framework projects
- [[engineering/desired_projects/private_daos|Private DAOs]]: LEZ programs as governance backends
- Logos Core modules: `lez-client-gen` generates Qt-compatible FFI for any LEZ program

---

## FURPS Specification

### v0.1 — Current Implementation

#### F — Functionality

**Program Authoring**
- **`#[lez_program]` proc macro** — annotate a Rust module to define a LEZ program. Eliminates all boilerplate: no manual dispatch loop, no manual serialization.
- **`#[instruction]` marker** — marks individual functions inside `#[lez_program]` as on-chain instructions.
- **Account constraints via attributes** — declarative account requirements expressed inline:
  - `#[account(signer)]` — account must authorize the transaction
  - `#[account(init)]` — account is being created (must be in default/empty state)
  - `#[account(mut)]` — account is writable
  - `#[account(pda = literal("seed"))]` — PDA derived from a constant string seed
  - `#[account(pda = account("other"))]` — PDA derived from another account's ID
  - `#[account(pda = arg("name"))]` — PDA derived from an instruction argument
  - `members: Vec<AccountWithMetadata>` — variable-length trailing account list (`rest: true` in IDL)
- **External instruction enum** — programs using a shared `Instruction` enum can reference it via `#[lez_program(instruction = "my_crate::Instruction")]` to avoid duplicate type generation.
- **Runtime validation** — generated code automatically validates `signer` and `init` constraints before invoking the handler; returns structured `LezError` on failure.

**IDL Generation**
- **`generate_idl!` macro** — one-liner IDL generator that reads a guest program's source file at compile time and emits a `fn main()` printing complete IDL JSON.
- **IDL covers:** instruction names, account lists (with writable/signer/init/pda/rest flags), argument names and types, PDA seed definitions (const/account/arg), lssa-lang-compatible discriminators (SHA-256 of `global:{name}`), execution mode, and variant names.
- **`rest: true` propagation** — `Vec<AccountWithMetadata>` parameters correctly emit `"rest": true` in IDL JSON, ensuring client-side transaction builders append variable-length accounts correctly.
- **`instruction_type` field** — IDL includes the external instruction enum path when `#[lez_program(instruction = ...)]` is used, enabling downstream codegen to use the native type.
- **lssa-lang superset** — generated IDL is backward-compatible with lssa-lang tooling; additional fields are optional and safely ignored by older consumers.

**CLI (`lez-cli`)**
- **Auto-generated subcommands** — reads an IDL JSON file and builds a complete CLI with one subcommand per instruction.
- **Type-aware argument parsing** — supports `u8/u32/u64/u128` (decimal), `[u8; N]` (hex or UTF-8 padded), `[u32; 8]`/`program_id` (comma-separated u32s), `Vec<[u8;32]>` (comma-separated hex/base58), `Option<T>`.
- **Automatic PDA computation** — PDA accounts with known seeds are computed automatically from IDL definitions; users do not supply them manually.
- **Multi-binary program ID resolution** — `--bin-<name> <path>` flags auto-fill program ID args from binary files.
- **Dry-run mode** — `--dry-run` prints parsed arguments and serialized TX data without submitting.
- **Transaction building and submission** — reads wallet from environment (`NSSA_WALLET_HOME_DIR`), fetches nonces, signs, and submits via sequencer client.
- **TX confirmation polling** — polls sequencer until transaction is included in a block (or times out with error).
- **`inspect` subcommand** — extracts and displays ProgramId from ELF binaries (decimal, hex, and raw byte formats).

**Project Scaffolding (`lez-cli init`)**
- **`lez-cli init <name>`** — bootstraps a complete LEZ project with correct workspace layout: `_core/`, `methods/`, `methods/guest/`, `examples/`.
- **Generated files:** workspace `Cargo.toml`, `.gitignore`, `Makefile` with `build/idl/cli/deploy/setup/inspect/status/clean` targets, `README.md`, guest program skeleton, `generate_idl.rs` (one-liner), `<name>_cli.rs` (three-line CLI wrapper).
- **State management** — Makefile stores deployed program IDs and account IDs in a local `.state` file.

**Client Code Generation (`lez-client-gen`)**
- **Typed Rust client** — generates a `<Program>Client` struct with one async method per instruction, `<Instruction>Accounts` structs with correct ordering, and PDA computation helpers.
- **C FFI wrappers** — generates `extern "C"` functions (one per instruction) with JSON-in/JSON-out pattern matching the LEZ Qt plugin pattern.
- **C header file** — generates a `.h` file with declarations for all FFI functions and an include guard.
- **`rest` account support** — accounts with `rest: true` become `Vec<AccountId>` and are appended after fixed accounts.
- **`instruction_type` support** — when IDL specifies an external instruction enum, codegen imports the native type instead of generating a local one.

**PDA Derivation**
- **SHA-256 multi-seed hashing** — `SHA-256(seed1 || seed2 || ...)` for multi-seed PDAs. Non-commutative, no self-cancellation. Matches upstream `nssa` derivation.
- **Single-seed pass-through** — single seed used directly without hashing.

**Error Types**
- **Structured `LezError` enum** — `AccountCountMismatch`, `InvalidAccountOwner`, `AccountAlreadyInitialized`, `AccountNotInitialized`, `InsufficientBalance`, `DeserializationError`, `SerializationError`, `Overflow`, `Unauthorized`, `PdaMismatch`, `Custom` (code + message).
- **Numeric error codes** — each variant maps to a deterministic numeric code for client-side handling.
- **Borsh serializable** — errors can be transmitted over the wire.

**Testing**
- **Unit tests** — account constraint validation, PDA derivation correctness (commutativity, self-cancellation, multi-seed vs single-seed).
- **E2E test pipeline** — validates the full pipeline against a fixture program: build → IDL generation → IDL validation → client/FFI codegen → fixture unit tests.
- **CI** — separate jobs for unit tests (no heavy deps) and E2E tests (installs `logos-blockchain-circuits`).

#### P — Performance

- IDL generation is a compile-time macro step — no runtime overhead for on-chain programs.
- TX submission latency is network-bound (sequencer round-trip); CLI overhead is not the bottleneck.
- `lez-client-gen` codegen is I/O-bound on reading the IDL file; no benchmarks have been run.
- No formal performance benchmarks exist for v0.1. This section will be updated as measurement data becomes available.

#### R — Reliability

- E2E tests validate the full scaffold → build → IDL → client/FFI pipeline on every CI run.
- Dry-run mode allows TX validation without network round-trips.
- Structured error types prevent silent failures; all errors carry context.
- Missing arguments are detected before any network calls; clear error messages with the missing flag names.

#### U — Usability

- **Three-line CLI wrapper** — program authors wrap `lez_cli::run().await` in `main()`; no CLI boilerplate required.
- **One-liner IDL generator** — `generate_idl!("path/to/program.rs")` is the complete generate_idl binary.
- **`make` workflow** — all common operations available via `make <target>`.
- **Contextual help** — `lez-cli --help` lists all instructions; `lez-cli <instruction> --help` shows detailed account and argument descriptions with type format hints.
- **Auto-computed PDAs** — PDA accounts are resolved without user input and noted as `(PDA — auto-computed)` in help output.

#### S — Supportability

- MIT licensed. Cargo workspace with clear crate separation: `lez-framework-core` (types/errors/IDL), `lez-framework-macros` (proc macros), `lez-framework` (umbrella), `lez-cli` (CLI + scaffolding), `lez-client-gen` (codegen).
- E2E fixture program in `tests/e2e/fixture_program/` serves as canonical example and regression baseline.
- `docs/` directory for design documentation.

---

### v0.2 — Next: Significantly Improved Usability & Correctness

#### F — Functionality

**Guest-Side PDA Verification (Security Gap Fix)**
- **Issue:** `#[account(pda = ...)]` annotations are currently purely cosmetic in generated guest code — they document intent in the IDL but the generated validation does not verify that the supplied account ID matches the expected PDA. A buggy or malicious client can pass any account ID for a PDA-annotated parameter.
- **Blocker:** Requires [lssa#347](https://github.com/logos-blockchain/lssa/issues/347) — programs currently have no access to their own program ID at runtime, which is a required input to PDA derivation.
- **v0.2:** Once lssa#347 is resolved, `generate_validation` emits PDA derivation + comparison code for each `pda = ...` account. Returns `LezError::PdaMismatch` on mismatch. Covers all seed types (`literal`, `account`, `arg`).

**IDL-Embedded CLI (Eliminate `--idl` Flag)**
- **Issue:** Users must pass `--idl <file>` to every CLI invocation — significant friction for end users of program-specific CLIs.
- **v0.2:** `lez_cli::run_with_idl(idl_str: Option<&str>)` — callers embed IDL via `include_str!()` or provide a default path. Result: `multisig create-multisig ...` works without `--idl` prefix.

**On-the-Fly IDL Generation During FFI Build**
- **Issue:** IDL files committed to source drift from actual program source, causing client/FFI bugs (wrong account layouts, missing flags).
- **v0.2:** `lez-client-gen` runs IDL extraction as the mandatory first step. IDL JSON becomes a build artifact (`.gitignore`), not a source file. Stale IDL is physically eliminated.

**`lez-client-gen` as Logos Scaffold Build Step**
- `logos-scaffold build client` and `logos-scaffold build ffi` run `lez-client-gen` automatically as part of the standard build pipeline. No manual codegen step required.

**Nix Build Support**
- Nix flake templates in `lez-cli init` output for reproducible builds compatible with Logos Core module packaging.

#### P — Performance

- IDL generation on-the-fly during FFI build adds incremental build time (not yet measured).
- Guest-side PDA verification adds SHA-256 operations per instruction invocation; zkVM proving cost impact is not yet measured.

#### R — Reliability

- Guest-side PDA verification closes the security gap where `pda = ...` annotations were documentation-only.
- Eliminating committed IDL files removes a class of drift-induced bugs.

#### U — Usability

- **No `--idl` flag** — the single biggest UX friction point for end users of program-specific CLIs.
- **`logos-scaffold build`** becomes a single command for the full pipeline: guest binary → IDL → client/FFI → ready to deploy.
- **Nix templates in scaffold** — correct build configs from day one for Logos Core / Nix users.

#### S — Supportability

- IDL-as-build-artifact aligns with standard practice (Anchor, Solidity ABIs) — easier to explain and onboard.
- Guest-side PDA verification makes `#[account(pda = ...)]` annotations self-documenting AND enforced — the code is the spec.

---

## Known Limitations (Not Scoped for v0.2)

- **Private/UTXO instructions** — current framework only handles public account-based transactions.
- **Cross-program invocation (CPI)** — no support for one LEZ program calling another on-chain.
- **Account ownership constraints** — `#[account(owner = PROGRAM_ID)]` is parsed but validation is a stub.
- **Custom error propagation to client** — `LezError` round-trip from guest error → client-readable response is not yet complete end-to-end.
- **Multi-sequencer support** — CLI targets a single sequencer endpoint; decentralized sequencer support requires v0.2+ of the underlying LEZ infrastructure.