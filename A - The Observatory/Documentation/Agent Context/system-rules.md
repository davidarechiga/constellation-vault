---
title: System Rules
description: Vault conventions and tool constraints that all agents must follow
type: reference
tags:
  - agent-context
created: 2026-03-30
---

# System Rules

> Canonical rules for how the Constellation vault works. Skills and agents should load this when they need to create or modify vault content.

## Vault Conventions

- **Wikilinks only** for internal notes: `[[Note Title]]` — never `[text](path.md)`
- **No Dataview queries** — the vault uses `.base` files (TaskNotes plugin) for aggregated views
- **Folder notes** — each major folder has a `.md` file with the same name as the folder
- **Task system** — TaskNotes in `E - The Foundry/Tasks/[Project]/` with `.base` dashboards → see `.claude/rules/task-notes.md`
- **Index files** — `_index.md` in key folders; update when creating or deleting files

## File & Path Rules

- Vault root: `$HOME/Constellation/`
- Always quote paths in bash commands (spaces in folder names)
- Daily notes: `C - Signal Relay/Daily/YYYY-MM-DD.md`
- Weekly notes: `C - Signal Relay/Weekly/YYYY-WNN.md`
- Task files: `E - The Foundry/Tasks/[Project]/[Task Name].md`

## What Agents Can Edit

- Daily notes, task files, project hubs, `_index.md` files
- `.base` files, Canvas files, any vault content

## Read-Only

- Templates in `A - The Observatory/Documentation/Templates/` — copy, don't edit originals

## Safety

- The vault is git-tracked. If a file is corrupted: `git checkout -- <file>`

## ACE Structure

| Folder | Role |
|--------|------|
| `A - The Observatory/` | Atlas — knowledge, reference, ideas |
| `C - Signal Relay/` | Calendar — daily notes, weekly reviews, inbox |
| `E - The Foundry/` | Efforts — projects, tasks, life areas, dashboards |
