---
title: Atomic Swaps
type: Desired Project
priority: 2
flywheel: Liquidity
category: DeFi Core
---

Enables trust-minimized peer-to-peer swaps of shielded assets without revealing details to a third party or the public, bootstrapping early, decentralized private liquidity.

## FURPS+ (v0.1)

[v0.1 milestone](https://github.com/logos-co/ecosystem/milestone/7)

Phase 1: HTLC PoC — Maker sells λ (LEZ) for ETH (Ethereum)

- **Maker**: the party that creates and publishes the swap offer
- **Taker**: the party that accepts and initiates the swap

### Functionality

1. Maker sells λ for ETH (Ethereum)
2. Original owners can reclaim funds after timeout if swap did not complete
3. Native tokens only (ETH on Ethereum, λ on LEZ)

### Usability

1. Daemon monitors both chains for swap events and preimage hash reveals
2. Clear error messages on failure, timeout, or invalid state transitions
3. Default timeouts for demo purposes (5-10 min)
4. User may need to run specific CLI commands to progress swap; Or a daemon will be available (TBC)

### Reliability

1. Refund path for incomplete swaps is available for both parties

### Performance

### Supportability

1. New CLI

### + (Privacy, Anonymity, Censorship-Resistance)

1. On-chain traces of atomic swaps on Ethereum chain
2. Cross-chain linkability via shared hash lock: the two sides of a swap are correlatable on-chain regardless of account privacy on LEZ. Private LEZ accounts hide participant identity but not the swap linkage itself
3. Amounts visible on ETH side

## ADR

### Decisions

1. **Target chain**: Ethereum  - familiarity, simpler see HTLC, potential usage of eth wallet module, top 3 desired from strategy
2. **Swap direction**: Maker sells λ (LEZ) for ETH — prioritises bootstrapping inbound liquidity to LEZ
3. **Swap mechanism**: HTLC — simplest trust-minimised primitive; adaptor signatures deferred to a later phase
4. **Interface**: New standalone CLI — will try using Logos Core, but not make it a blocking dependency

5. **Counterparty negotiation**: Hardcoded swap params for PoC; discovery via Logos Messaging deferred to a later phase

## Dependencies

### LEE / LEZ Wallet Module

- Validity Windows (LEE block context) LEZ programs need a way to enforce timeouts. Validity windows (`valid_from` / `valid_until`) let the swap contract distinguish "before deadline" from "after deadline" without leaking timing metadata
- Watching events/equivalent

### Ethereum Wallet Module

- Deploying smart contract
- Getting events

### Chat Module

For v0.2:

- We will aim to have some negotiation - ideally chat module enable boostrapping a conversation based on information maker broadcasts.

## Demand Validation

**Potential Users:** Early adopters, OTC traders, cross-chain users, arbitrageurs

**Use Cases:**

- Cross-chain swaps: Exchange assets between privacy L1 and other chains
- OTC trading: Large trades without market impact or public visibility
- P2P exchange: Direct user-to-user trading without [[engineering/desired_projects/private_dex|DEX]]
- Private arbitrage: Exploit price differences across venues privately
- Trustless escrow: Buy/sell with strangers without intermediaries

## Technical Validation

**Risks & Challenges:**

- Counterparty discovery: Finding trading partners without revealing intent
- Price negotiation: Agreeing on rates privately
- Cross-chain verification: Validating external chain state privately
- Timeout handling: Managing refunds if swap fails
- Fee coordination: Determining who pays gas on each chain

**Integration Points:**

- Private communication channels for off-chain trade negotiation
- Decentralized order books for publishing trade offers without revealing identity
- Reputation systems via ZK reputation proofs
- [[engineering/desired_projects/bridges|Bridge]] integration for cross-chain atomic swaps
- [[engineering/desired_projects/private_dex|DEX]] fallback if atomic swap fails
