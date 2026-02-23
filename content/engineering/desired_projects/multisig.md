---
title: Multisig Treasury / Vault
type: Core Primitive
priority: 0
flywheel: Security
category: Custody & Security
---

Multi-signature governance program for LEZ, enabling M-of-N threshold approval for on-chain actions. Protects shared treasuries, DAOs, and team-controlled assets by requiring multiple authorised signers before any funds move.

**Repository:** [jimmy-claw/lez-multisig](https://github.com/jimmy-claw/lez-multisig)

## FURPS+ (v0.1)

### Functionality

- [x] Multi-sig smart contract can be set up with M-of-N threshold at deployment; where M is configured and N is the total number of currently authorised signers
- [x] Authorised signers can be set up at deployment
- [ ] Authorised signers can be added *(v0.2)*
- [ ] Authorised signers can be removed *(v0.2)*
- [x] Signing workflow enables first signer to propose, and others to add their signature; once threshold is met any member can execute
- [x] Members identified by LEZ public keys (AccountIds, 32 bytes)
- [x] Multisig owns a treasury vault (PDA, derived from `create_key`)
- [x] Multiple independent multisigs supported per program via unique `create_key`
- [x] Support native token (λ) transfers via ChainedCall to token program
- [x] Members can reject proposals

### Usability

- [ ] Authorised signers cannot be removed if N would become strictly less than M *(v0.2, guarded in spec)*
- [x] Signature proposal displays relevant information (proposal index, status, approvals, target action)
- [ ] Signatures are exchanged over Logos Messaging, enabling in-band signing requests *(v0.2)*
- [x] CLI for all operations: create, propose, approve, reject, execute, info

```
# Create 2-of-3 multisig
lez-wallet multisig create --threshold 2 --member <pk1> --member <pk2> --member <pk3>

# View multisig info
lez-wallet multisig info --account <multisig_id>

# Propose transfer
lez-wallet multisig propose --multisig <id> --to <recipient> --amount 100

# Approve / Reject / Execute
lez-wallet multisig approve --multisig <id> --proposal <index>
lez-wallet multisig reject  --multisig <id> --proposal <index>
lez-wallet multisig execute --multisig <id> --proposal <index>
```

### Reliability

- [x] No funds move without M valid approvals from distinct members
- [x] Nonce-based replay protection (handled by LEZ runtime)
- [x] Clear error messages for insufficient approvals, invalid members, wrong proposal state
- [x] Proposals are immutable once executed or rejected — status cannot be reversed

### Performance

- [x] Each approve/reject is a single on-chain transaction
- [x] Execute is a single on-chain transaction emitting one ChainedCall
- [x] O(M) approval checks per execute

### Supportability

- [x] Unit tests for all instruction handlers
- [x] Integration test: create → fund → propose → approve → execute → verify balances
- [x] [Technical specification](https://github.com/jimmy-claw/lez-multisig/blob/main/SPEC.md) documents full account model, PDA derivation, instruction set, validation rules
- [x] [Gap analysis](https://github.com/jimmy-claw/lez-multisig/blob/main/docs/gap-analysis.md) for runtime dependencies

### + (Privacy, Anonymity, Censorship-Resistance)

- Proposal and approval actions are on-chain transactions — visible to validators
- Member lists are stored in plaintext in the multisig state account
- Future: private multisig would require shielded voting and ZK threshold proofs

## ADR

### Decisions

1. **Execution model**: Squads-style on-chain proposals — members approve asynchronously without offline coordination. No signature aggregation required.
2. **Delegation pattern**: ChainedCall — the multisig never directly modifies external state. On execute, it emits a `ChainedCall` to the target program (e.g., token program). Minimal surface area.
3. **Account model**: PDA-based — Multisig State, Proposal, and Vault are all Program Derived Accounts. Deterministic addressing, no key management.
4. **Member accounts**: Must be fresh keypairs claimed by the multisig program during `CreateMultisig` (LEZ runtime constraint — see [LSSA #339](https://github.com/logos-blockchain/lssa/issues/339)).
5. **Interface**: CLI integrated into `lez-wallet` — no standalone binary needed.
6. **Signer management**: Deferred to v0.2 — keeps v0.1 scope minimal while spec covers the design.

## Dependencies

### LEZ Runtime (LSSA)

- ChainedCall support for delegated execution
- PDA derivation for deterministic account addressing
- Account ownership and claiming semantics
- Nonce-based replay protection

### Token Program

- Native token (λ) transfer instruction — target of ChainedCall on execute

### Logos Messaging *(v0.2)*

- In-band notification when a proposal is created or needs signing
- Could integrate with Status messenger or Waku for decentralised delivery

## Demand Validation

**Potential Users:** DAOs, teams, treasuries, protocol governance

**Use Cases:**

- Treasury management: Shared team funds requiring multi-party approval
- Protocol governance: Parameter changes or upgrades gated by multisig
- Escrow: Third-party mediated transactions with threshold release
- Grant programs: Committee-approved fund disbursement

## Technical Validation

**Risks & Challenges:**

- Member account claiming constraint requires dedicated keypairs per multisig (runtime limitation)
- No `CloseProposal` instruction yet — executed/rejected proposals consume storage indefinitely
- No time-lock between threshold reached and execution — instant execute once M approvals collected
- Cross-program interaction limited to single ChainedCall per execute

**Integration Points:**

- Token program for native transfers
- Future: DEX, atomic swaps, or bridge programs as ChainedCall targets
- Future: Logos Messaging for signing notifications
- Future: Logos Core Qt module for GUI-based multisig management
