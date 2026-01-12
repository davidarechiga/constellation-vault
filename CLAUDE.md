# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

[[0 📡 Signal Relay]]
## Repository Overview

This is an Obsidian vault named "Constellation" - a personal knowledge management system organized using the PARA method (Projects, Areas, Resources, Archives). It is not a traditional code repository, but rather a collection of markdown notes with bidirectional links, organized hierarchically.

## Vault Structure

The vault follows a modified PARA organizational framework:

- **0 📡 Signal Relay** - Dashboard and capture area for new notes and quick thoughts that haven't been categorized yet
- **1 🔨 The Foundry** - Active projects with specific outcomes and deadlines (e.g., baby prep, music releases, brand projects, app development)
- **2 📻 Wavelengths** - Ongoing areas of life requiring continuous attention:
  - `1 🛫 Personal Growth` - Self-improvement topics (cooking, health, music performance, career development)
  - `2 🥰 Camille` - Relationship notes and shared activities
  - `3 🐶 River` - Pet-related notes
  - `4 👶 Cyrus` - Baby prep and parenting
  - `5 🏡 Household` - Home management
- **3 📚 The Library** - Reference materials, ideas, writing, poetry, and topic-based knowledge (design, computer science, book notes, travel, hobbies)
- **4 📦 Archive** - Completed or inactive items from other categories
- **Attachments** - Media files and embedded resources
- **0 📡 Signal Relay/0 📡 Signal Relay.md** - Primary dashboard and entry point to the vault

## Obsidian Plugins

The vault uses these community plugins:
- **dataview** - Query and display data from notes
- **obsidian-tasks-plugin** - Task management with advanced querying
- **omnisearch** - Enhanced full-text search
- **homepage** / **home-tab** - Custom homepage functionality
- **obsidian-icon-folder** - Custom icons for folders
- **folder-notes** - Create notes that represent folders
- **smart-connections** - AI-powered semantic search and note linking
- **smart-templates** - AI-assisted note templates
- **mcp-tools** - Model Context Protocol integration
- **obsidian-local-rest-api** - Local REST API for external tool access

## Linking Conventions

- Obsidian uses wikilinks: `[[Note Title]]` to create bidirectional links between notes
- Links are resolved by note title, not file path
- The vault emphasizes connected thinking through liberal use of links between related concepts

## Working with Notes

When creating or modifying notes in this vault:
- Use wikilink syntax `[[Note Title]]` for internal links, not markdown links
- Preserve emoji prefixes in folder names (e.g., `📡`, `🔨`, `📻`, `📚`, `📦`)
- Match the organizational structure: Signal Relay for dashboard/captures, The Foundry for active projects, Wavelengths for ongoing life areas, The Library for reference
- The `0 📡 Signal Relay/0 📡 Signal Relay.md` folder note serves as the main navigation hub
- Notes may contain Dataview queries or task syntax from the tasks plugin
- Task syntax uses checkbox format: `- [ ]` (incomplete), `- [x]` (complete)
- Tags use hashtag syntax: `#tagname` (e.g., `#outdoor`, `#project`)

## File Paths

The vault is stored in Dropbox at:
```
/Users/davidarechiga/Dropbox/Constellation
```

Always use quotes around paths containing spaces when using command-line tools.

## External Files

Music production files are stored at the Dropbox root (not in the vault):
- `~/Dropbox/Ableton/` (169GB) - Ableton projects and samples
- `~/Dropbox/Splice/` (28GB) - Sample packs
- `~/Dropbox/sounds/` (20GB) - Audio assets
- `~/Dropbox/Sample Inbox/` - Sample library

Reference these from notes using relative paths: `../../Ableton/...`

Other organized files:
- `~/Dropbox/Files/Legacy/` - Old PARA folders and archived content
- `~/Dropbox/Files/Projects/` - Active project files
- `~/Dropbox/Files/Resources/` - Reference materials
- `~/Dropbox/Files/Screenshots/` - Screenshot library
