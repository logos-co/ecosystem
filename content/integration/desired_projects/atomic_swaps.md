---
title: Atomic Swaps
type: Desired Project
priority: 2
flywheel: Liquidity
category: DeFi Core
---

Enables trust-minimized peer-to-peer swaps of shielded assets without revealing details to a third party or the public, bootstrapping early, decentralized private liquidity.

## Functionality

- Enable trust-minimized P2P swaps of shielded assets
- Ensure atomicity (either both sides complete or neither does)
- Support cross-chain swap capability
- Provide trustless escrow without intermediary knowledge
- Enable OTC trading for large deals

## Design Constraints (Privacy)

- Hide counterparties (neither party's identity or address revealed)
- Conceal amounts (trade sizes not publicly visible)
- Protect asset types being swapped
- Prevent timing analysis (swap negotiations and execution not linkable)

## Demand Validation

**Potential Users:** Early adopters, OTC traders, cross-chain users, arbitrageurs

**Use Cases:**
- Cross-chain swaps: Exchange assets between privacy L1 and other chains
- OTC trading: Large trades without market impact or public visibility
- P2P exchange: Direct user-to-user trading without DEX
- Private arbitrage: Exploit price differences across venues privately
- Trustless escrow: Buy/sell with strangers without intermediaries

## Possible Implementation

- **Hash Time-Locked Contracts (HTLCs) with privacy**: Traditional atomic swap mechanism enhanced with ZK proofs, shielded lock and unlock conditions
- **Adaptor signatures**: Cryptographic technique for atomic swaps with no on-chain hash revelation required
- **ZK atomic swaps**: Zero-knowledge proofs for swap conditions with fully encrypted swap parameters
- **Blind escrow**: Third-party facilitator who cannot see trade details, trustless via cryptographic commitments

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
- Bridge integration for cross-chain atomic swaps
- DEX fallback if atomic swap fails
