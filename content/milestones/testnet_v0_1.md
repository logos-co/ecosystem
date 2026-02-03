---
title: Logos Testnet v0.1 - Eco Dev activities
---

[Logos Testnet Version 0.1](https://roadmap.logos.co/testnets/v01)

## Priorities

Highest Priority: LSSA - to derisk and already available.
Then, will depend on delivery from other teams.

Regarding PoCs, we should prioritized based on desired apps priorities and readiness to build/time to effort.

## Logos Core

**R&D Delivery**:
- package manager over GitHub
- Modules
	- Blockchain Wallet
	- LEZ Wallet
	- LEZ block explorer
	- Blockchain node
	- Storage node
	- Chat node
	- Messaging node
- Simple App UIs
	- Blockchain Wallet
	- LEZ Wallet
	- Chat App
	- Filesharing App
	- Mix Push Message App
- Headless server mode
	- Blockchain node
	- Storage node
	- Messaging node

### Eco Dev Activity

- Build with Logos Core modules
	- Multisig, Atomic swap PoCs to use LEZ wallet and messaging or Chat node modules
	- Go through docs/tutorials for other modules
- run nodes in headless server mode
- Try the App UIs
## AnonComms

**R&D Delivery**: Demo app that demonstrates the capability discovery module and mixnet features.
### Eco Dev Activity

[Red team the capability discovery demo app.](https://github.com/logos-co/ecosystem/issues/27)

- Use messaging demo app to test module as users.
- No specific PoC Apps for this, as module is not an API exposed to developer (aka no Logos Core module).

## Blockchain

### Bedrock

**R&D Delivery**:
- Running validators
  - taking note on resource consumption - help determine if it can run on Raspberry Pi 
- Staking
- Setting up and using wallet
- Receiving tokens from faucet
- Sending tokens

### Eco Dev activity

1. [Dogfood steps above](https://github.com/logos-co/ecosystem/issues/28)
2. Build PoC GUI to help users do steps (in Logos Core)
3. Initiate block explorer discovery work

## LEE / LEZ

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

## Messaging

**R&D Delivery**:
- demo app for Chat SDK (Logos Core)
- Logos Chat Module

### Eco Dev Activity

1. Dogfood demo app
2. Build alternative PoC apps using chat module

## Storage

**R&D Delivery:**
- Demo App that shows storage module
- storage module

### Eco Dev Activity

1. PoC Apps using storage module