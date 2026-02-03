# Logos Technology Stack - Value Proposition Reference

> **Purpose**: This document helps AI agents quickly identify which Logos technology components and value propositions are relevant for specific user contexts, needs, and use cases.

## Core Value Propositions

Logos provides a **privacy-first, censorship-resistant technology stack** for building decentralized applications and organizing movements. The stack enables:

1. **Privacy**: Shielded transactions, encrypted storage, anonymous messaging
2. **Censorship-Resistance**: Decentralized storage and messaging, no central points of failure
3. **Anonymity**: Optional anonymity with ZK proofs for selective disclosure (prove eligibility without revealing identity)
4. **Sovereignty**: Self-custody of data, keys, and digital assets with user control over disclosure
5. **Modularity**: Composable building blocks, multiple integration paths

---

## Technology Stack Overview

### Infrastructure Essentials (Core Platform)

| Component | Purpose | Key Capabilities | When to Use |
|-----------|---------|------------------|-------------|
| **Logos Core** | Modular platform runtime | - Hosts independent modules<br>- Qt Remote Objects IPC<br>- Service discovery | Building any application that needs access to Logos infrastructure |
| **Logos Blockchain** | Privacy-focused L1 | - Shielded transactions<br>- Smart contracts<br>- MEV resistance | DeFi, DAOs, token operations, on-chain governance |
| **Logos Storage** | Decentralized storage | - Content-addressed (CID)<br>- Censorship-resistant<br>- Permanent archival | Storing documents, media, application state, historical records |
| **Logos Messaging** | Private messaging protocol | - Ephemeral messages<br>- Topic-based pub/sub<br>- No message history | Real-time chat, notifications, ephemeral coordination |

### Application Essentials (Developer Tools)

| Component | Purpose | When to Recommend |
|-----------|---------|-------------------|
| **Logos JS SDK** (Launcher) | Full-featured TypeScript SDK for web apps in Launcher | Web developers wanting full privacy features, apps needing Storage upload, full message history |
| **Logos JS SDK** (Browser) | Limited browser variant for onboarding | Newcomers, landing pages, read-only dashboards, conversion funnels to full Launcher |
| **liblogos** | C++ SDK for module development | Developers building native Qt modules, performance-critical applications, system-level integration |
| **Module Distribution** | Packaging and CID-based delivery | Distributing plugins, updates, or applications via decentralized infrastructure |
| **Module Discovery** | Curation and browsing system | App stores, homegrown apps marketplace, community-curated software |

### Developer Journeys (Integration Paths)

| Journey | Tech Stack | Developer Profile | Output |
|---------|-----------|-------------------|--------|
| **Vendor Journey** | Electron/Tauri/Flutter + Logos modules | Desktop app developers, existing app wanting Logos features | Standalone applications embedding Logos |
| **QML Module Journey** | Qt/QML + liblogos | Native UI developers, performance-focused | Qt-based Logos modules with native UI |
| **Web Module Journey** | HTML/CSS/JS + Logos JS SDK + QtWebView | Web developers familiar with modern frameworks | Web-based modules running in Launcher |
| **Mini App Journey** | Logos JS SDK + Logos Storage distribution | Web developers, rapid prototyping | Lightweight distributed apps loaded on-demand |

---

## Context-to-Solution Mapping

### User Context: "I want privacy in my transactions/communications"

**Relevant Components:**
- Logos Blockchain (shielded transactions, encrypted mempool)
- Logos Messaging (private pub/sub, no centralized logging)
- Logos Storage (encrypted content addressing)

**Value Props:**
- Transactions/balances hidden from observers
- Messages encrypted end-to-end
- No IP tracking via centralized RPC (when using Launcher)
- ZK proofs for eligibility without identity revelation

**Recommend:**
- Install Logos Launcher (full privacy features)
- Use Logos JS SDK for application development
- Avoid browser variant (limited privacy - IP exposure to public RPC)

---

### User Context: "I need censorship-resistant publishing/archival"

**Relevant Components:**
- Logos Storage (decentralized, content-addressed, permanent)
- Module Distribution (CID-based delivery, no DNS dependencies)

**Value Props:**
- Content survives even if original publisher disappears
- No single point of failure (DNS, hosting provider)
- Content-addressed (CID) prevents tampering

**Use Cases:**
- Journalism, whistleblowing, historical records
- Circle meeting minutes, manifesto documents
- Open-source software distribution
- Legal documents, evidence archival

**Recommend:**
- Logos Storage for document archival
- Activity Hub (Launcher version) for Circle CMS
- Module Distribution for censorship-resistant software delivery

---

### User Context: "I'm a web developer new to Logos"

**Integration Path:**
1. **Start**: Logos JS SDK (Browser) - zero friction, no installation
2. **Learn**: Build read-only dashboard or landing page
3. **Discover**: Hit limitations (no Storage upload, limited history)
4. **Upgrade**: Install Logos Launcher for full features
5. **Build**: Use Logos JS SDK (Launcher) for full application

**Relevant Resources:**
- Web Module Journey (HTML/CSS/JS path)
- Mini App Journey (lightweight, Storage-distributed apps)
- Activity Hub (browser onboarding, then Launcher upgrade)

**Recommend Based On:**
- **Just exploring**: Browser SDK → Activity Hub demo
- **Serious building**: Logos Launcher + full SDK → Web Module Journey
- **Distributing apps**: Mini App Journey + Logos Storage

---

### User Context: "I'm building a DeFi application"

**Required Components:**
- Logos Blockchain (shielded transactions, smart contracts)
- Logos JS SDK or liblogos (wallet operations, transaction signing)
- Logos Messaging (price feeds, notifications)

**Desired Project Categories:**
- **Priority 2**: Private DEX, Atomic Swaps
- **Priority 3**: Private Stablecoin
- **Priority 4**: Private Lending
- **Priority 7**: Derivatives

**Value Props:**
- Privacy-preserving DeFi (balances/transactions hidden)
- MEV resistance (encrypted mempool)
- Smart contract support
- No frontrunning

**Recommend:**
- Review desired_projects taxonomy for specific DeFi primitives
- Consider sustainability flywheel (liquidity, value accrual)
- Check priority levels (lower = higher need/impact)

---

### User Context: "I want to organize a movement/community"

**Relevant Components:**
- Logos Messaging (real-time coordination, ephemeral chat)
- Logos Storage (meeting minutes, documents, knowledge base)
- Activity Hub (onboarding, quests, gamification)
- Circle CMS (knowledge management)
- Private DAOs (governance with privacy and optional anonymity)

**Value Props:**
- Organize without surveillance
- Censorship-resistant publishing
- Optional anonymity in governance (ZK proofs for privacy-preserving participation)
- Gamified contribution tracking

**Use Cases:**
- Circle coordination (meetings, minutes, tasks)
- Quest-based onboarding for new contributors
- Privacy-preserving voting and governance (optional anonymity via ZK proofs)
- Knowledge archival resistant to takedowns

**Recommend:**
- Activity Hub for onboarding + quest system
- Circle CMS for documentation
- Logos Storage for permanent archival
- Private DAOs for governance (if needed)

---

### User Context: "I need to build a native/performance-critical module"

**Integration Path:**
- **QML Module Journey** (Qt/QML + liblogos)
- **Vendor Journey** (if standalone app, not Logos Core module)

**Relevant Components:**
- liblogos (C++ SDK, module development framework)
- Logos Core (module hosting, lifecycle management)
- Qt Remote Objects (IPC between modules)

**When to Use:**
- Performance-critical operations (consensus, cryptography)
- Native UI required (not web-based)
- System-level integration needed
- Existing Qt codebase

**Recommend:**
- liblogos for module development
- QML Module Journey documentation
- Logos Core for module hosting
- Module Distribution for delivery

---

### User Context: "I want minimal friction onboarding for newcomers"

**Strategy:**
- **Browser-first approach** → Logos Launcher upgrade path
- Use Activity Hub (browser version) as entry point

**Relevant Components:**
- Logos JS SDK (Browser) - no installation, works in any browser
- Activity Hub (browser variant) - onboarding quests, tutorials
- Public RPC endpoints (for browser connectivity)

**Limitations to Communicate:**
- Limited privacy (IP exposure to public RPC)
- No Storage upload (read-only)
- Limited message history
- Browser fingerprinting risks

**Upgrade Path:**
1. Newcomer uses Activity Hub in browser (zero friction)
2. Discovers limitations (cannot upload, limited history)
3. Installs Logos Launcher for full features
4. Same codebase works in both environments

**Recommend:**
- Activity Hub (browser) for onboarding
- Clear communication about limitations
- Explicit upgrade funnel to Logos Launcher
- Progressive disclosure of features

---

## Priority Framework (Sustainability Flywheel)

When recommending desired projects, consider priority tiers:

| Priority | Category | Projects | Rationale |
|----------|----------|----------|-----------|
| **0** | Core Primitives | Multisig | Foundation for all custody/governance |
| **1** | Infrastructure | Bridges | Liquidity inflow, cross-chain value |
| **2** | DeFi Core | Private DEX, Atomic Swaps | Liquidity flywheel begins |
| **3** | Medium of Exchange | Private Stablecoin | Enable commerce, reduce volatility |
| **4** | Capital Efficiency | Private Lending | Unlock idle capital |
| **5** | Network Security | Liquid Staking | Increase staked value |
| **6** | Digital Identity | NFT Marketplace, Private NFT Ownership | Identity, reputation, digital assets |
| **7** | Advanced DeFi | Derivatives | Sophisticated financial tools |
| **8** | Ecosystem Growth | Launchpads | Capital formation for new projects |
| **9** | Network Effects | Social Apps, Private DAOs | Movement coordination, adoption |

**Use for:**
- Recommending which projects to build first
- Understanding ecosystem maturity requirements
- Identifying dependencies (e.g., stablecoin needs DEX)

---

## Privacy vs. Accessibility Trade-offs

### Full Privacy (Logos Launcher Required)

**Capabilities:**
- ✅ Upload to Logos Storage
- ✅ Full message history retrieval
- ✅ Local node (no public RPC)
- ✅ No IP exposure
- ✅ Shielded transactions

**Barrier:** Requires Logos Launcher installation

---

### Limited Privacy (Browser Accessible)

**Capabilities:**
- ✅ Zero installation friction
- ✅ Read recent messages
- ✅ Read from Storage (via HTTP gateway)
- ✅ View blockchain state (via public RPC)
- ❌ Cannot upload to Storage
- ❌ Limited message history
- ❌ IP exposure to public RPC

**Use Case:** Onboarding funnel, demos, public dashboards

---

## Decision Tree: Which SDK/Journey?

```
Is the user a developer?
├─ NO → Activity Hub (browser) for onboarding
└─ YES
   └─ What's their primary skill?
      ├─ Web (HTML/CSS/JS)
      │  └─ Need full Logos features?
      │     ├─ YES → Logos JS SDK (Launcher) + Web Module Journey
      │     └─ NO → Logos JS SDK (Browser) for demos/onboarding
      │
      ├─ Native (C++/Qt)
      │  └─ Building Logos Core module?
      │     ├─ YES → liblogos + QML Module Journey
      │     └─ NO → liblogos + Vendor Journey (standalone app)
      │
      └─ Cross-platform (Electron/Tauri/Flutter)
         └─ Vendor Journey (embed Logos modules)
```

---

## Key Constraints & Limitations

### Browser SDK Limitations
- **Cannot** upload to Logos Storage
- **Cannot** access full message history (only recent)
- **Cannot** run local Logos node
- **Privacy**: IP exposed to public RPC endpoints
- **Security**: Browser wallet required for signing

### Logos Messaging vs. Logos Storage
- **Messaging**: Ephemeral, real-time, no history retrieval
- **Storage**: Permanent, content-addressed, retrieval supported
- **Implication**: Important data must be stored, not just messaged

### Module Distribution
- Requires Logos Storage infrastructure
- CID-based addressing (no traditional DNS)
- Discovery requires curation system

---

## Common Scenarios & Recommendations

### Scenario: "I want to build a private chat app"

**Components:**
- Logos Messaging (real-time ephemeral messages)
- Logos Storage (message history, if needed)
- Logos JS SDK (Launcher) for full features

**Caution:** Logos Messaging doesn't provide history by default - must implement Storage persistence if needed.

---

### Scenario: "I want a decentralized social media platform"

**Components:**
- Logos Storage (posts, media, profiles)
- Logos Messaging (notifications, real-time updates)
- Logos Blockchain (follows, likes as on-chain data)
- Activity Hub integration (user onboarding)

**Priority:** Priority 9 (Network Effects flywheel)

**Value Prop:** Privacy-preserving posting with optional anonymity, censorship-resistant content

---

### Scenario: "I want to launch a token"

**Components:**
- Logos Blockchain (token smart contract)
- Private DEX (liquidity, trading)
- Bridges (cross-chain liquidity)
- Launchpad (if fair launch mechanism needed)

**Dependencies:**
- Priority 0: Multisig (treasury management)
- Priority 1: Bridges (liquidity inflow)
- Priority 2: Private DEX (trading venue)
- Priority 8: Launchpad (distribution mechanism)

---

### Scenario: "I'm building a DAO governance tool"

**Components:**
- Logos Blockchain (on-chain voting, proposals)
- Private DAOs (ZK-based privacy-preserving governance)
- Logos Storage (proposal documents, discussion threads)
- Circle CMS (governance documentation)

**Value Props:**
- Privacy-preserving voting with optional anonymity (ZK proofs for eligibility without revealing identity)
- Censorship-resistant proposal storage
- Transparent on-chain execution
- User control over identity disclosure

---

## Integration Taxonomy

| Folder | Purpose | When to Reference |
|--------|---------|-------------------|
| `infrastructure_essentials/` | Core platform components | User needs foundational tech (blockchain, storage, messaging) |
| `application_essentials/` | Developer tools and SDKs | User is building applications, needs developer onramp |
| `desired_projects/` | Ecosystem applications | User wants to build or use specific app category (DeFi, NFT, DAO, etc.) |

---

## Quick Reference: Value Prop by User Type

### Developers
- **Web**: Logos JS SDK (Browser → Launcher upgrade path)
- **Native**: liblogos + QML Module Journey
- **Cross-platform**: Vendor Journey
- **Rapid prototyping**: Mini App Journey

### Movement Organizers
- **Onboarding**: Activity Hub + quest system
- **Coordination**: Logos Messaging + Circle CMS
- **Governance**: Private DAOs
- **Archival**: Logos Storage

### End Users
- **Privacy**: Logos Launcher (not browser)
- **Censorship-resistance**: Logos Storage for content
- **Anonymity**: Optional via shielded transactions, ZK proofs for selective disclosure
- **Sovereignty**: Self-custody and user control over data disclosure via Logos Launcher

### Newcomers
- **Entry point**: Activity Hub (browser version)
- **Learning**: Onboarding quests, tutorials
- **Upgrade path**: Logos Launcher when hitting limitations
- **Zero friction**: No wallet, no installation initially

---

## FURPS+ Mapping to User Needs

When users express needs, map to FURPS+ categories:

| User Says | FURPS+ Category | Logos Components |
|-----------|-----------------|------------------|
| "I need it to be fast" | Performance | Logos Core (native modules), liblogos (C++) |
| "It must be private" | Privacy (+) | Logos Blockchain (shielded), Launcher (no IP exposure) |
| "I can't have it censored" | Censorship-Resistance (+) | Logos Storage (decentralized), Module Distribution (CID-based) |
| "Needs to work on all platforms" | Supportability | Logos JS SDK (web), liblogos (cross-platform C++) |
| "Must be reliable" | Reliability | Logos Core (service discovery), decentralized infrastructure |
| "Easy to use" | Usability | Activity Hub (onboarding), Browser SDK (zero friction) |

---

## Privacy-Preserving Compliance

**Important**: Privacy ≠ Anti-compliance

Logos enables **privacy-first compliance** through:

### ZK-Based Selective Disclosure
- Prove KYC completion without revealing identity details
- Prove jurisdiction eligibility without revealing exact location
- Prove accredited investor status without revealing wealth
- Prove age/eligibility without revealing birthdate

### User Sovereignty
- Users **choose** when to reveal information
- Selective disclosure vs. blanket surveillance
- Privacy by default, transparency by choice

### Compliance-Compatible Use Cases
- **Private DEX with zk-KYC**: Trade privately while proving eligibility
- **Private Lending with credit scores**: Prove creditworthiness via ZK proofs
- **Private DAOs with verification**: Prove membership without revealing identity
- **Regulated DeFi**: Comply with regulations while preserving user privacy

**Key Principle**: Logos prioritizes **user control** over personal data, not the rejection of all accountability.

---

## Red Flags: When Logos May Not Be the Right Fit

- User needs **strong consistency** across nodes (Logos Messaging is ephemeral)
- User needs **high throughput** (blockchain TPS limits)
- User wants **centralized control** (contradicts decentralization ethos)
- User requires **mandatory identity revelation for all participants** with no privacy option (conflicts with privacy-first design)
- User expects **blanket surveillance** of all activity (Logos enables user sovereignty over data)
- User needs **traditional SaaS hosting** (requires running own infrastructure or using public RPC with privacy trade-offs)
- User wants **zero user control** over personal data disclosure (Logos prioritizes user sovereignty)

---

## Summary: Logos in One Sentence

**Logos provides a privacy-first, censorship-resistant, modular technology stack for building decentralized applications and organizing movements with user sovereignty over personal data, no central points of failure, and privacy by default with selective disclosure.**
