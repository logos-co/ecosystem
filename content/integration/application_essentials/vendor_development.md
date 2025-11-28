---
title: Standalone App Development (vendor)
type: Developer Journey
priority:
category: Developer Tools
---

Development path for building standalone applications that embed Logos core modules (messaging, storage, blockchain or others) using LogosLib SDKs with frameworks like Electron, Tauri, or Flutter; CLI and TUI may also be a target.

## FURPS+

### Functionality
- Enable developers to add LogosLib as a dependency to their projects
- Support building standalone applications with embedded Logos core modules
- Enable applications to access [[integration/infrastructure_essentials/logos_messaging|Logos Messaging]], [[integration/infrastructure_essentials/logos_storage|Logos Storage]], and blockchain functionality
- Enable applications to access custom made modules; loaded from [[Logos Storage]] at build time

### Usability
- Provide clear SDK documentation to use [[logos lib]] as a vendor/dependency in given languages (eg Rust, NodeJS)
- Include build tooling and packaging commands
- Offer example applications and starter templates
- Provide debugging capabilities for embedded modules

### Supportability
- Frameworks: Electron, Tauri, Flutter, CLI, TUI
- Desktop platforms: Windows, macOS, Linux
- Mobile platforms: Android, iOS

### + (Privacy, Anonymity, Censorship-Resistance)

- Applications inherit privacy features of embedded Logos core modules
- Modules can be loaded from [[Logos Storage]] and can avoid dependency on centralized infra (e.g. GitHub) 
- Modules integrity can be verify at build time

## Demand Validation

**Potential Users:**
- Application developers building desktop or mobile apps on Logos.
- [[Waku (Logos Messaging)]] already has captured leads interested in Waku Rust SDK -> this would bne the new Rust SDK.

Note this method bypasses the installation of the [[Logos Launcher]]:

### Pros
1. Potentially less "clicks" for users:
    ```
    Install Logos Launcher -> Start launcher -> find mini app -> start mini app
    ```
    vs
    ```
    Install standalone app -> start standalone app
    ```
2. Friendly integration for existing apps, with an existing userbase: Devs add [[logoslib]] as a vendor, and don't need to ask users to isntall new app ([[Logos Launcher]])
3. Still onboard developers to the Logos stack (not users, see cons-1)

### Cons

1. Does not onboard users on [[Logos Launcher]], [[Activity Hub]], etc
2. Another journey to maintain
3. Potentially a faster path to production (need to review [[Logos Launcher]]) readiness

**To validate**:
- Does the **pros** outweigh the **cons**?
- Is there appetite to fund this?

## Possible Implementation

- **[[integration/application_essentials/logos_js_sdk|Logos JS SDK]]**: JavaScript/TypeScript SDK with FFI bindings to core modules
- **[[Logos Rust SDK]]**: A Rust wrapper to logos lib to load and use Logos modules (eg for Tauri or other Rust based app).
- **Framework Integration**: Build tooling for Electron, Tauri, and Flutter
- **Packaging**: Commands to ensure required modules can be bundled in standalone application.
- **Distribution**: Left to the developer.

## Technical Validation

**Risks & Challenges:**
- FFI module loading complexity and platform-specific issues
- Application bundle size with embedded modules
- Cross-platform build and distribution complexity
- Developer learning curve for LogosLib integration
- Added commands to include in standalone application CI/CD.

**Dependencies:**
- [[integration/application_essentials/logos_js_sdk|Logos JS SDK]]

**Integration Points:**
- [[integration/application_essentials/liblogos|liblogos]] for core module access
- [[integration/infrastructure_essentials/logos_core|Logos Core]] module system
- UI framework build systems (Electron, Tauri, Flutter)
