---
description: Obsidian plugin list, daily/weekly note format, linking and tag conventions for Constellation vault
paths:
  - "Constellation/C - Signal Relay/**"
  - "Constellation/A - The Observatory/**"
---

# Vault Conventions

## Active Plugins

- **tasknotes** — Primary task system. Frontmatter-driven task files with `.base` aggregated views.
- **omnisearch** — Full-text search across the vault.
- **folder-notes** — Notes that represent folders (share the folder name).
- **homepage / home-tab** — Custom homepage on vault open.
- **obsidian-icon-folder** — Custom folder icons (cosmetic).
- **smart-connections** — Semantic search and note linking via AI embeddings.
- **smart-templates** — AI-assisted note templates (Templater syntax: `<% %>`).
- **mcp-tools** — Model Context Protocol integration for external tool access.
- **obsidian-local-rest-api** — Local REST API for programmatic vault access.
- **dataview** — Installed but NOT used for queries. Vault uses `.base` files instead.
- **obsidian-tasks-plugin** — Legacy task plugin. Superseded by tasknotes.

## Daily Note Format

Location: `C - Signal Relay/Daily/YYYY-MM-DD.md`

Standard sections:
```
## Top 3
## Schedule
## Notes / Journal
## Prep For Tomorrow
```

## Weekly Note Format

Location: `C - Signal Relay/Weekly/YYYY-WNN.md`

Standard sections:
```
## Wins
## Improvements
## Habit Health
## Project Health
## Next Week Focus
```

## Linking Conventions

- Internal links: `[[Note Title]]` — resolved by title, not path
- Tags: `#tagname` (no spaces, lowercase preferred)
- MOCs in `A - The Observatory/MOCs/` are topic index notes — use them to discover related notes
- Folder notes (same name as parent folder) serve as the hub for that folder

## Folder Note Pattern

Each major folder has a `.md` file with the same name as the folder (e.g., `Active.md` inside `Active/`). These are rendered when clicking the folder in Obsidian. They should contain: purpose statement, quick links to key sub-notes, and an embedded `.base` view where relevant.
