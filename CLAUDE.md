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

## Sandbox-First Protocol

**CRITICAL:** When modifying dashboard files, Canvas files, `.base` files, or core system files, ALWAYS use sandbox/TEST versions first.

1. Create `-TEST` or `- TEST` suffixed copies before making changes
2. Explicitly tell David: "I've updated the TEST version. Please verify it works before I migrate to production."
3. Wait for confirmation before touching production files

**Files requiring sandbox-first:** `Weekly Dashboard.canvas`, `Projects List.base`, all `.base` files in `E - The Foundry/Dashboard/`, templates in `A - The Observatory/Documentation/Templates/`.

## Index Files

Key folders contain `_index.md` files listing their contents with one-line summaries. **When creating or deleting vault files, update the nearest `_index.md`.** These are the first place to look when navigating — scan the index before doing a full Glob/Grep.
