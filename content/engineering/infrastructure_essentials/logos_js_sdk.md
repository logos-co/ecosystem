---
title: Logos JS SDK
type: Developer Tool
priority: 0
category: Developer Tools
---

JavaScript/TypeScript SDK for building web applications that run within the Logos App, with full access to Logos Core modules (blockchain, storage, messaging).

## FURPS+

### Functionality

- Full access to all Logos Core backend modules (wallet, chat, messaging, storage)
- Connect to Logos blockchain nodes for [[engineering/infrastructure_essentials/blockchain_wallet|Logos Wallet]] actions
- Upload and download data to/from [[engineering/infrastructure_essentials/logos_storage|Logos Storage]]
- Publish and subscribe to messages via [[engineering/infrastructure_essentials/logos_messaging|Logos Messaging]]
- Support account management and key handling
- Enable interaction with smart contracts

### Usability

- Provide intuitive API with comprehensive documentation
- Include TypeScript type definitions for IDE support
- Offer example code and starter templates
- Simple async/await API for calling backend modules
- Event-driven architecture with `EventEmitter` pattern

### Supportability

- Maintain backward compatibility across versions
- Provide clear migration guides for breaking changes
- Support modern bundlers (Webpack, Vite, Rollup)
- Cross-platform support (Windows, macOS, Linux, Android, iOS)

### + (Privacy, Anonymity, Censorship-Resistance)

- Anonymous retrieval of modules, including frontend, via [[engineering/infrastructure_essentials/package_manager|Package Manager]]
- Censorship-resistant retrieval of modules, including frontend, via [[engineering/infrastructure_essentials/package_manager|Package Manager]]

## Demand Validation

**Potential Users:** Web developers building [[engineering/application_essentials/logos_core_devex|mini apps]] for Logos App

**Use Cases:**

- [[engineering/desired_projects/activity_hub|Activity Hub]] with full Logos Storage integration
- Private chat applications with message persistence
- DeFi applications with full wallet integration
- Content management tools leveraging Logos Storage
- Developer dashboards accessing all Logos modules

## Possible Implementation

- **Core Library**: TypeScript wrapper around Logos Core FFI
- **Qt WebChannel Bridge**: Communication between WebView and Qt backend
- **Module Access**: Reflective API for all loaded Logos modules (`logos.wallet.*`, `logos.chat.*`)
- **Event System**: Subscribe to module events (`logos.chat.onChatMessage()`)
- **Storage Client**: Full read/write access to Logos Storage
- **Messaging Client**: Full pub/sub access to Logos Messaging

### Example API

```javascript
const logos = new LogosAPI()

// Full storage access
await logos.storage.upload(data)
const content = await logos.storage.download(cid)

// Full messaging access with history
await logos.chat.joinChannel("general")
const history = await logos.chat.retrieveHistory("general")

// Wallet operations
const balance = await logos.wallet.ethBalance("0x...")
```

## Technical Validation

**Risks & Challenges:**

- Maintaining API stability as backend modules evolve
- Qt WebChannel communication overhead
- TypeScript bindings generation from C++ modules
- Debugging WebView-embedded applications
- Documenting all available module methods

**Dependencies:**

- [[engineering/infrastructure_essentials/logos_core|Logos Core]] with module system
- QtWebView with Qt WebChannel support
- [[engineering/infrastructure_essentials/liblogos|liblogos]] for module APIs
- Logos App runtime environment

**Integration Points:**

- [[engineering/infrastructure_essentials/logos_core|Logos Core]] modules (wallet, chat, waku, storage)
- QtWebView for rendering web applications
- Qt WebChannel for JavaScript-to-C++ bridge
- [[engineering/application_essentials/logos_core_devex|Development Journey]] for developers
