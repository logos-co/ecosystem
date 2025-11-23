# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is the **Logos Ecosystem Wiki** - a static site built with Quartz 4 to document Logos ecosystem-related information. The repository may be made public in the future, so never commit sensitive information.

The content focuses on the Integration effort which enables bi-directional feedback between the Logos technical stack and community by identifying technological needs, translating them into requirements, and propagating information about deliveries to encourage ecosystem building.

## Technology Stack

- **Quartz 4**: Static site generator for publishing digital gardens from Markdown
- **TypeScript**: Strict mode enabled, targeting ESNext
- **Preact**: UI framework (JSX runtime configured via tsconfig.json)
- **Content Source**: Markdown files in `content/` directory (designed for Obsidian vault workflow)

## Key Commands

### Development
```bash
# Build and serve with live reload (primary dev command)
npx quartz build --serve

# Build documentation with live reload
npm run docs
```

### Code Quality
```bash
# Type checking and formatting check
npm run check

# Auto-format code with Prettier
npm run format

# Run tests
npm test
```

## Architecture

### Plugin System
Quartz uses a three-phase plugin architecture defined in `quartz/plugins/types.ts`:

1. **Transformers** (`quartz/plugins/transformers/`): Process markdown content (parse, syntax highlighting, link crawling, etc.)
2. **Filters** (`quartz/plugins/filters/`): Determine which content to publish (e.g., RemoveDrafts)
3. **Emitters** (`quartz/plugins/emitters/`): Generate output files (HTML pages, assets, sitemap, RSS, etc.)

Plugins are configured in `quartz.config.ts` and execute in the order: Transformers → Filters → Emitters.

### Build Pipeline
The build process (`quartz/build.ts`) follows this flow:
1. Parse markdown files using transformers
2. Filter content based on filter plugins
3. Emit static assets and pages using emitter plugins
4. Support incremental builds via change detection

### Component System
UI components (`quartz/components/*.tsx`) are Preact-based with three optional lifecycle hooks:
- `css`: Static stylesheet resource
- `beforeDOMLoaded`: Scripts that run before DOM ready
- `afterDOMLoaded`: Scripts that run after DOM ready

Layout structure is defined in `cfg.ts` as `FullPageLayout` with regions: head, header, beforeBody, pageBody, afterBody, left, right, footer.

### Content Management
- **Content Directory**: `content/` - Root for all markdown files
- **Obsidian Integration**: Open the `content/` folder (not repo root) as Obsidian vault
  - Enable "Automatically update internal links"
  - Set link format to "Absolute path in vault"
  - Enable Wikilinks
  - Use Templater plugin with `templates/` folder for auto-populated files
- **Ignore Patterns**: Configured in `quartz.config.ts` - currently ignores `private`, `templates`, `.obsidian`
- **Link Resolution**: Uses `shortest` markdown link resolution strategy

## Important Configuration

### quartz.config.ts
Central configuration file containing:
- Site metadata (pageTitle, baseUrl, locale)
- Theme settings (typography, colors for light/dark mode)
- Analytics provider (currently set to Plausible)
- Plugin configuration for all three phases
- Ignore patterns for content filtering

### Content Structure
- `content/index.md`: Site homepage
- `content/integration/`: Integration effort documentation
  - `concerns/`: Priority drivers (sustainability, movement, tech de-risking)
  - `desired_projects/`: Ecosystem project categories (DeFi, NFTs, DAOs, etc.)

## Logos Integration Framework

### Mission
The Integration effort establishes bi-directional feedback between the Logos technical stack and ecosystem by:
- Identifying and evaluating technological needs of the community
- Translating needs into requirements for the technology stack
- Propagating information about deliveries to encourage building and contribution

### Prioritization Framework
Three primary concerns drive requirement prioritization (defined in `content/integration/index.md`):
1. **Sustainability**: Enable onchain activity and value accrual to sustain technology stack development
2. **Movement**: Provide technological solutions for the movement to organize and solve winnable issues
3. **Technology De-Risking**: Enable early delivery and validation of technology with highest unknowns and risks

### Desired Projects Taxonomy
Projects in `content/integration/desired_projects/` follow a standardized frontmatter structure:
- `type`: Project category (e.g., "Desired Project", "Core Primitive")
- `priority`: Numeric priority (0 = highest)
- `flywheel`: Economic flywheel (Liquidity, Security, Network Effects)
- `category`: Technical category (DeFi Core, Infrastructure, Governance, etc.)

**Priority Tiers** (from `sustainability.md`):
- **Priority 0**: Core Primitives (Multisig)
- **Priority 1**: Infrastructure Essentials (Bridges)
- **Priority 2**: DeFi Core & Liquidity (Private DEX, Atomic Swaps)
- **Priority 3**: Stable Medium of Exchange (Private Stablecoin)
- **Priority 4**: Capital Efficiency (Private Lending)
- **Priority 5**: Network Security (Liquid Staking)
- **Priority 6**: NFTs & Digital Identity
- **Priority 7**: Advanced DeFi (Derivatives)
- **Priority 8**: Ecosystem Growth (Launchpads)
- **Priority 9**: Network Effects (Social Apps, Private DAOs)

### Privacy-First Context
All desired projects emphasize privacy-preserving implementations for the Logos L1:
- Shielded transactions and balances
- ZK proofs for eligibility/verification without revealing identity
- MEV resistance through encrypted mempools
- Anonymous participation in governance and DeFi

## Development Notes

- The site uses CustomOgImages plugin which is commented out in the default config to speed up build times
- File paths use `FilePath` type and utility functions from `quartz/util/path.ts`
- Build context (`BuildCtx`) flows through all plugins and components
- Date handling supports multiple sources with priority: frontmatter → git → filesystem
- When adding new desired projects, follow the established frontmatter schema and priority framework

## Content Authorship Indicators

To clearly distinguish LLM-generated content from human-curated content, use the following markdown blockquote indicator:

### LLM-Generated Content Marker
Wrap LLM-generated sections that have not yet been reviewed by humans with:

```markdown
> [!ai-generated]
> This section was generated by an LLM and has not yet been human-reviewed.
```

**Usage Guidelines:**
- **IMPORTANT**: The indicator belongs to a whole section and must ALWAYS be placed immediately after the section header (before any content)
- The indicator applies to the entire section, including all subsections, until the next same-level or higher-level header
- Add this indicator to any section generated by Claude or other LLMs
- Remove the indicator once a human has reviewed, edited, and approved the content
- Human reviewers should delete the entire blockquote when content is verified

**Example:**
```markdown
## FURPS

> [!ai-generated]
> This section was generated by an LLM and has not yet been human-reviewed.

### Functionality
- Statement 1
- Statement 2
```

After human review and approval, simply remove the `> [!ai-generated]` block, leaving only the content.

## Content Quality Commands

### "check" Command
When the user says "check", perform the following quality assurance tasks across the repository:

1. **Ensure document structure consistency**: Verify that files within the same folders follow consistent structure patterns (e.g., all files in `content/integration/desired_projects/` have similar headings, sections, and frontmatter format)

2. **Add internal links**: Identify mentions of concepts and artifacts that are defined elsewhere in the repository and add wikilinks to connect them (e.g., if a file mentions "Multisig" and there's a `Multisig.md` file, link to it)

3. **Validate internal links**: Check that all existing internal links in the repository point to valid files that exist
