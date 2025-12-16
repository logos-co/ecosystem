---
title: Logos Core DevEx
type: Developer Guide
priority:
category: Developer Tools
---

# Logos Core Developer Experience

Overview of the different development paths for building applications on the Logos technology stack.

## Development Paths

The Logos ecosystem supports multiple development journeys, each suited to different use cases, developer skills, and distribution strategies.

### Mini Apps (Logos App)

Applications distributed via the [[integration/infrastructure_essentials/package_manager|Package Manager]] and loaded within the [[Logos App]]. This provides a "dApp browser" experience with seamless access to Logos infrastructure.

**Two implementation options:** Web Mini App and QML Mini App

| Aspect             | Web Mini App                  | QML Mini App                   |
| ------------------ | ----------------------------- | ------------------------------ |
| **Languages**      | HTML/CSS/JavaScript[^1]       | QML/C++                        |
| **Developer Pool** | All web developers            | Qt developers                  |
| **Tooling**        | Web DevTools, npm, bundlers   | Qt Creator, qmlscene           |
| **Performance**    | Good (native WebView)         | Excellent (native Qt)          |
| **Access to Core** | Via Logos JS SDK              | Via Qt Remote Objects          |
| **Learning Curve** | Low for web devs              | Medium (requires Qt knowledge) |
| **Best For**       | Rapid prototyping, simple UIs | Complex native-feeling UIs     |

[^1]: JavaScript support to be confirmed

#### Web Mini App Distribution Strategies

There are two possible strategies for distributing web-based mini apps:

**1. QML Module Template**

Developers receive a template to create and distribute a **QML Plugin with embedded QtWebView** that includes their web app.

- Developer packages their web app (HTML/CSS/JS) inside a QML module
- The QML module includes QtWebView configured to load the bundled web app
- Distributed as a complete QML plugin via [[integration/infrastructure_essentials/package_manager|Package Manager]]
- More control over the QtWebView configuration and lifecycle

**2. Web App Distribution**

Developers distribute only the **web app files (HTML, JS, CSS)** which are loaded in a generic Logos Core QML Module with QtWebView.

- Developer only ships web assets (no Qt/QML knowledge required)
- A standard Logos Core QML module handles loading and rendering
- Simpler distribution format - just web files
- Less control but lower barrier to entry

**Shared characteristics:**

- Distributed via [[integration/infrastructure_essentials/package_manager|Package Manager]]
- Run within Logos App environment
- Access to Logos Core modules (messaging, storage, blockchain)
- Decentralized, anonymous, censorship-resistant distribution

### Standalone App

Applications that **embed Logos modules directly** using [[integration/infrastructure_essentials/liblogos|liblogos]] SDKs, distributed independently of the Logos App.

**Frameworks:** Electron, Tauri, Flutter, CLI, TUI, or even Qt

**Characteristics:**

- Full control over UI and distribution
- Logos modules bundled within the application
- Modules retrieved from [[integration/infrastructure_essentials/package_manager|Package Manager]] at build time
- No dependency on Logos App being installed

**Use cases:**

- Existing apps with established user bases adding Logos features
- New apps wanting full control over distribution and branding
- CLI/TUI tools for developers and power users

**Trade-offs:**

- Does not onboard users to [[Logos App]] ecosystem
- Larger application bundle size
- Developer responsible for module updates
- Logos Core security model (sandboxing, module permissions) not carried over

### External App (Kernel Runtime)

External applications that **connect to the Logos App Kernel** running as a separate process, enabling apps to leverage Logos infrastructure without embedding modules.

**Characteristics:**

- Application connects to running Logos App via IPC/RPC
- Shared Logos runtime across multiple applications
- Lighter application bundle (no embedded modules)
- More UI flexibility - own window and design
- Potentially distributable via [[integration/infrastructure_essentials/package_manager|Package Manager]]

**Use cases:**

- Browser extensions connecting to local Logos App
- Lightweight tools that leverage user's existing Logos setup
- Applications in languages not natively supported by liblogos
- Development and debugging tools

**Trade-offs:**

- Requires user to have Logos App running
- Split user experience (two apps)
- IPC overhead compared to embedded modules

## Module Security & Privacy

A key concern is ensuring user confidence that modules retrieved from the [[integration/infrastructure_essentials/package_manager|Package Manager]] will not breach user privacy. Third-party modules must be prevented from:

- **Calling home**: Unauthorised network requests that could leak user activity or data
- **Writing forensic traces**: Disk writes that a secondary program (malware) could forensically access to extract user behaviour

### Sandboxing Strategy

For **QML/Qt modules**, sandboxing is required to restrict:

- Network access (no external connections)
- Disk access (limited to module-specific storage)

### Trust Model

The trust model is based on users trusting the code emerging from Logos R&D at a given point in time. **Logos Core** and core infrastructure modules (Blockchain, Messaging, Storage) fall under the same security model - they are **trusted modules** granted special permissions for network and disk access.

Integrity checks may be performed to ensure trusted modules have not been compromised (e.g., signature verification, hash validation against known releases).

**Third-party modules** introduce a new set of developers into the trust chain. Since users have not explicitly trusted these developers, additional safeguards are required:

- Sandboxing to restrict network and disk access
- User authorisation prompts when accessing trusted modules
- Token-based authentication and permissions

## Journey Comparison

| Journey                           | UI Flexibility                      | Ecosystem Integration          | Security Model                                        | Trade-offs                  |
| --------------------------------- | ----------------------------------- | ------------------------------ | ----------------------------------------------------- | --------------------------- |
| **QML Mini App**                  | Limited - within Logos App frame    | Deep - fully embedded          | Full - sandboxing, permissions                        | Constrained UI; requires Qt |
| **Web Mini App**                  | Limited - within Logos App frame    | Deep - fully embedded          | Full - sandboxing, permissions                        | Web tech but constrained    |
| **External App (Kernel Runtime)** | More flexibility - own window       | Medium - connects to Logos App | Limited - Auth of Logos core module but no sandboxing | Split user experience       |
| **Standalone App**                | Full flexibility - complete control | Lower - not embedded           | None - security model not carried over                | Less connected to ecosystem |

## Current Proposed Priorities

### Mini App Concept - Qt

- Generally more appetite from leadership
- Provides cohesive user experience within Logos App
- Enables ecosystem network effects through discovery and curation
- Focus on Qt as more certainty in terms of strategy

### Standalone App Development - Rust

- Existing integration leads via [[integration/infrastructure_essentials/logos_messaging|Logos Messaging]] (Rust SDK demand)
- Important for onboarding existing applications with established user bases
- Faster path to production for some use cases
