---
title: Logos Testnet v0.1 - Eco Dev activities
---

TODO: Link to reference page

## Priorities

Highest Priority: LSSA - to derisk and already available.
Then, will depend on delivery from other teams.

Regarding PoCs, we should prioritized based on desired apps priorities and readiness to build/time to effort.

## Logos Core

**R&D Delivery**: TBC

### Eco Dev Activity

TBC

### Questions

- Will it be ready to build PoC (Qt) GUIs? Web GUI? (assume not re Web)
- Or only TUI/CLI?

## AnonComms

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
- Should we even do anything on this? dogfooding can be driven by messaging/storage/blockchain to integrate it.

## Blockchain - Consensus / DA

**R&D Delivery**:
- Running validators
  - taking note on resource consumption - help determine if it can run on Raspberry Pi 
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
- is blockchain team already planning to build a GUI?

## Blockchain - LSSA

**R&D Delivery**:
- Centralized sequencer, settles on Logos Blockchain (consensus usage, maybe DA)
- CLI wallet
- Native token transfers (public and private)
- Creation and transfer of custom tokens (public and private)
- Can interact with AMM sample app (public and private)
- Develop, deploy and execute custom smart contracts (public and private)
- Track public transactions through explorer, some info for private state (eg number of transactions)
- Transaction generator 

### Eco Dev Activity

**Proposal**:
1. Setup and use wallet:
   - get native tokens, transfer
   - create custom token, transfer
   - pool, exchange tokens in AMM
   - use explorer when doing above
2. Start building scaffold - focus on smart contract development
3. Create 2 new smart contracts, deploy, doc for users to test - using scaffold

### Questions

- is the explorer a CLI or Browser?
- Is DST handling throughput test?
- What about native token faucet?
- Is wallet available through Logos Core modules? can we build a PoC gui?

## Messaging

**R&D Delivery**:
- demo app for Chat SDK (Logos Core)
- Logos Chat Module

### Eco Dev Activity

**Proposal**:
1. Dogfood demo app
2. Build alternative PoC apps

### Questions

- Extent of the API?

## Storage

**R&D Delivery:**
- Demo App that shows storage module
- storage module

### Eco Dev Activity

**Proposal**:
1. PoC Apps using storage module

### Questions

- This is for straight storage, correct?
  - Aka, not embedded in Logos Package manager
  - no expectation of retrieving a module from storage and executing it 