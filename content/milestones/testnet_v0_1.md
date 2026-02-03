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

**Assumption**: Only messaging module integrates Logos Core module. Delivery is disjoint from stack.

### Eco Dev Activity

[Red team the capability discovery module.](https://github.com/logos-co/ecosystem/issues/27)

- Use messaging demo app to test module as users.
- No specific PoC Apps for this, as module is not an API exposed to developer (aka no Logos Core module).

### Questions

- How to consume the module?
- C-bindings provided in discovery module?
- Discovery module delivered as Logos Core module?
  - Or, test discovery via messaging module?
  - I assume the former
- Should we even do anything on this? dogfooding can be driven by messaging/storage/blockchain to integrate it.

## Blockchain - Consensus / DA

**R&D Delivery**:
- Running validators
  - taking note on resource consumption - help determine if it can run on Raspberry Pi 
- Staking
- Setting up and using wallet
- Receiving tokens from faucet
- No DA

### Eco Dev activity

1. [Dogfood steps above](https://github.com/logos-co/ecosystem/issues/28)
2. Build PoC GUI to help users do steps (in Logos Core)
3. Initiate block explorer discovery work

### Questions

- CLI Wallet only?
- Wallet module available via Logos Core? Can we build a quick GUI?
- is blockchain team already planning to build a GUI?

## Blockchain - LSSA

**R&D Delivery**:
- Centralized sequencer, settles on Logos Blockchain (via inscriptions, no DA)
- CLI wallet
- Native token transfers (public and private)
- Creation and transfer of custom tokens (public and private)
- Can interact with AMM sample app (public and private)
- Develop, deploy and execute custom smart contracts (public and private)
- Track public transactions through explorer, some info for private state (eg number of transactions)
- Transaction generator 

### Eco Dev Activity

1. [Setup and use wallet](https://github.com/logos-co/ecosystem/issues/28):
   - get native tokens, transfer
   - create custom token, transfer
   - pool, exchange tokens in AMM
   - use explorer when doing above
1. Start building scaffold - focus on smart contract development
	1. https://github.com/logos-co/ecosystem/issues/30
2. Create 2 new smart contracts, deploy, doc for users to test - using scaffold
3. [Multi-sig CLI PoC](https://github.com/logos-co/ecosystem/issues/31)
4. Initiate scaffold work
5. Initiate block explorer discovery work

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

1. Dogfood demo app
2. Build alternative PoC apps using chat module

### Questions

- Extent of the API?

## Storage

**R&D Delivery:**
- Demo App that shows storage module
- storage module

### Eco Dev Activity

1. PoC Apps using storage module

### Questions

- This is for straight storage, correct?
  - Aka, not embedded in Logos Package manager
  - no expectation of retrieving a module from storage and executing it 