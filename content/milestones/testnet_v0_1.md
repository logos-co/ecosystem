---
title: Logos Testnet v0.1 - Eco Dev activities
---

TODO: Link to reference page

## AnnonComms

**R&D Delivery**: Demo app that demonstrates the capability discovery module and mixnet features.

**Assumption**: Only messaging module integrates Logos Core module.

### Eco Dev Activity

Red team the capability discovery module.

**Proposal**:
- Use messaging demo app to test module as users.
- No specific PoC Apps for this, as module is not an API exposed to dev

### Questions

- How to consume the module?
- C-bindings provided in discovery module?
- Discovery module delivered as Logos Core module?
- Or, test discovery via messaging module?

## Blockchain - Consensus / DA

**R&D Delivery**:
- Running validators
- Staking
- Setting up and using wallet
- Receiving tokens from faucet
- DA -> not confirmed

### Eco Dev activity

**Proposal**:
1. Dogfood steps above
2. Build PoC GUI to help users do steps (in Logos Core)

### Questions

- CLI Wallet only?
- Wallet module available via Logos Core? Can we build a quick GUI?

## Blockchain - LSSA

**R&D Delivery**:
- Centralized sequencer, settles on Logos Blockchain (consensus usage, maybe DA)
- CLI wallet
- Native token transfers (public and private)
- Creation and transfer of custom tokens (public and private)
- Can interact with AMM sample app (public and private)
- Deploy/execute custom smart contracts (public and private)
- Track public transactions through explorer, some info for private state (eg number of transactions)
- Transaction generator 

### Eco Dev Activity

**Proposal**:
1. Setup and use wallet:
  - get native tokens, transfer
  - create custom token, transfer
  - pool, exchange tokens in AMM
  - use explorer when doing above
2. Start building scaffold
3. Create 2 new smart contracts, deploy, doc for users to test - using scaffold

### Questions

- is the explorer a CLI or Browser?
- Is DST handling throughput test?
- What about native native token faucet?
- Is wallet available through Logos Core modules? can we build a PoC gui?