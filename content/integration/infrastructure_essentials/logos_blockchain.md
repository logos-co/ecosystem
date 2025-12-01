---
title: Logos Blockchain
type: Core Infrastructure
priority: 0
category: Infrastructure
---

Privacy-preserving Layer 1 blockchain combining Nomos for data availability and consensus with LSSA (Logos State Separation Architecture) for private execution.
## FURPS+

### Functionality
- Provide data availability and consensus via Nomos
- Execute private smart contracts via LSSA (formerly Nescience SSA)
- Support RISC Zero (risc0) as the execution environment
- Enable private state transitions with zero-knowledge proofs

### Reliability
- Ensure transaction finality through Nomos consensus
- Provide verifiable execution proofs via RISC Zero
- Maintain operational resilience through low barriers to node participation

### + (Privacy, Anonymity, Censorship-Resistance)

- **Privacy**: Private execution hides transaction details and contract state
- **Anonymity**: Nomos makes validator contributions indistinguishable, concealing block proposers and disassociating them from their stake; LSSA separates state to prevent identity correlation
- **Security**: Zero-knowledge proofs ensure correctness without revealing data
- **Censorship-Resistance**: Transaction neutrality processes transactions without discrimination; users can recover assets even when actively censored by applications

## Demand Validation

**Potential Users:** All applications requiring private on-chain execution, DeFi protocols, DAOs, identity systems, network states and sensitive social processes

**Use Cases:**
- Private DeFi transactions (swaps, lending, stablecoins)
- Anonymous governance and voting
- Private identity and credential verification
- Confidential smart contract execution
- Trust-minimised governing services

## Possible Implementation

- **Consensus & DA Layer**: Nomos provides data availability and transaction ordering
- **Execution Layer**: LSSA executes contracts in RISC Zero zkVM
- **Proof System**: RISC Zero generates validity proofs for state transitions

## Technical Validation

**Risks & Challenges:**
- Proof generation performance and costs
- Developer tooling maturity for risc0
- Complexity of private state management

**Open Questions:**
- **Consensus integration**: Whether LSSA provides its own consensus at launch or relies entirely on Nomos
- **EVM compatibility**: EVM-to-risc0 transpilation tooling is a pending decision
- **RPC compatibility**: Whether ETH JSON-RPC can be supported is under evaluation

**Integration Points:**
- Host marketplace contracts of [[integration/infrastructure_essentials/logos_storage|Logos Storage]] durability engine
- Host contracts of [[integration/infrastructure_essentials/logos_messaging|Logos Messaging]] DoS protection RLN
- [[integration/infrastructure_essentials/logos_core|Logos Core]] as the node runtime
