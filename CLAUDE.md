# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

## Vault Overview

This is an Obsidian vault named **Constellation** — a personal knowledge management system using the **ACE method** (Atlas, Calendar, Efforts) with Zettelkasten principles. Notes are found through links and MOCs, not folder hierarchies.

**Vault root:** `$HOME/Constellation/`

Always quote paths in bash commands (spaces in folder names). Always use paths under `$HOME/Constellation/` when referencing vault files.

## Folder Structure

- **A - The Observatory/** (Atlas) — Knowledge & reference. Topic subfolders, MOCs, Sources, Documentation, Archive, Attachments.
- **C - Signal Relay/** (Calendar) — Time-based entries. `Daily/`, `Weekly/`, `Inbox/` (primary capture inbox).
- **E - The Foundry/** (Efforts) — All active work. `Active/`, `Ongoing/`, `Someday/`, `Tasks/`, `Dashboard/`.

Vault root contains only the three ACE folders plus `Constellation.md`.

## Core Rules

- **Wikilinks only:** Use `[[Note Title]]` — never markdown links for internal notes.
- **No Dataview:** The vault uses `.base` files (TaskNotes plugin) for all aggregated views. Never write Dataview queries.
- **Task system:** TaskNotes in `E - The Foundry/Tasks/[Project]/` + `.base` dashboards. → See `.claude/rules/task-notes.md` for full spec.
- **Organizing notes:** Use `/organize-inbox` to sort loose notes from `C - Signal Relay/Inbox/`.
- **Folder conventions:** → See `.claude/rules/vault-conventions.md` for plugin list and note format details.

## Proactive Task Help

David needs help staying on top of tasks. When new tasks or projects come up:
1. Ask clarifying questions if scope is unclear
2. Break 3+ step tasks into collapsible nested subtasks
3. Add context, acceptance criteria, and wikilinks
4. Organize by deadline and suggest priority levels
5. Offer to create project hubs for multi-task initiatives

## Safety Net

The vault is a git repository. All files — including `.base`, Canvas, and system docs — can be freely edited. If something breaks, run `git checkout -- <file>` to restore it. No sandbox copies needed.

## Agent Navigation

When navigating the vault, follow these pointers:

| Goal | Where to look |
|------|--------------|
| Find tasks | `E - The Foundry/Tasks/_index.md` → project subfolder |
| Today's daily note | `C - Signal Relay/Daily/YYYY-MM-DD.md` — construct from current date, don't rely on index links |
| Log a decision / note | Today's daily note `## 📝 Notes`, or the relevant project hub |
| Find knowledge / reference | `A - The Observatory/_index.md` → topic subfolder |
| Find active projects | `E - The Foundry/Active/_index.md` |
| Find life areas | `E - The Foundry/Ongoing/_index.md` |
| Check project dashboards | `E - The Foundry/Dashboard/Projects List.base` |
| Agent context for skills | `A - The Observatory/Documentation/Agent Context/` |

**What agents can freely edit:** daily notes, task files, project hubs, `_index.md` files, `.base` files, Canvas files — the vault is git-tracked, so everything is recoverable.

**Read-only:** Templates in `A - The Observatory/Documentation/Templates/` — copy them, don't edit the originals.

## Index Files

Key folders contain `_index.md` files listing their contents with one-line summaries. **When creating or deleting vault files, update the nearest `_index.md`.** These are the first place to look when navigating — scan the index before doing a full Glob/Grep.
