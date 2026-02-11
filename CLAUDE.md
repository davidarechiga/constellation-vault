# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is an Obsidian vault named "Constellation" - a personal knowledge management system organized using the **ACE method** (Atlas, Calendar, Efforts) with **Zettelkasten** principles. Notes are found through links and Maps of Content (MOCs) rather than folder hierarchies.

## Vault Structure

The vault uses the ACE organizational framework with Constellation-themed folder names:

- **A - The Observatory/** (Atlas) — Knowledge space. Notes organized by connections, not categories.
  - `MOCs/` — Maps of Content (topic index notes: Music, Health, Creative Work, Cooking, Career, Family)
  - `Sources/` — Book notes, articles, literature notes (includes Book Notes, ChatGPT sources)
  - `Documentation/` — System docs, Constellation Guide, and Templates
  - `Archive/` — Completed or inactive items
  - `Attachments/` — Media files and embedded resources
  - `TaskNotes/` — Plugin folder for TaskNotes system config and default views
  - All other subfolders — Topic-based knowledge (Design, Music, Hobbies, Writing, etc.)
- **C - Signal Relay/** (Calendar) — Time-based entries and daily workflow.
  - `Daily/` — Daily notes
  - `Weekly/` — Weekly reviews
  - Folder note serves as the main navigation hub and dashboard
- **E - The Foundry/** (Efforts) — All active work: projects, life areas, tasks, and dashboards.
  - `Active/` — Current projects with deadlines (Baby Prep, Music, Pixel Glitch, Frameloop, Career, Constellation Mobile)
  - `Ongoing/` — Life areas requiring continuous attention (Personal Growth, Camille, River, Cyrus, Household)
  - `Someday/` — Future/paused projects
  - `Dashboard/` — Canvas dashboards, .base views, hub files (Weekly Dashboard, Signal Relay Dashboard, Projects List)
  - `Tasks/` — TaskNotes system organized by project subfolder

The vault root contains **only** the three ACE folders plus `CLAUDE.md`.

## Obsidian Plugins

The vault uses these community plugins:
- **dataview** — Query and display data from notes
- **obsidian-tasks-plugin** — Task management with advanced querying
- **omnisearch** — Enhanced full-text search
- **homepage** / **home-tab** — Custom homepage functionality
- **obsidian-icon-folder** — Custom icons for folders
- **folder-notes** — Create notes that represent folders
- **smart-connections** — AI-powered semantic search and note linking
- **smart-templates** — AI-assisted note templates
- **mcp-tools** — Model Context Protocol integration
- **obsidian-local-rest-api** — Local REST API for external tool access
- **tasknotes** — Task management system with granular frontmatter metadata and aggregated views

## Task Organization System: TaskNotes + Bases

The vault uses a dual system for task organization:

### TaskNotes (Primary Task Files)
Individual task files stored in `E - The Foundry/Tasks/[Project Name]/` with the following structure:

**Frontmatter metadata:**
```yaml
tags:
  - task
  - [project-tag]  # e.g., baby, music, career
title: Task Name
status: open | in-progress | done
priority: high | normal | low
due: YYYY-MM-DD
owner: David | Camille | Shared
projects:
  - "[[Project Name]]"
```

**File structure pattern:**
1. **Context Section** (at top for scannability)
   - Why critical
   - Done when (acceptance criteria)
   - Related links
   - Pro tips

2. **Strategy/Overview**
   - High-level approach or methodology
   - Key resources or constraints

3. **Task Breakdown** (action items with subtasks)
   - Grouped by category or phase
   - Nested checkboxes for sub-items
   - Clear, specific actions

4. **Source/References** (at bottom)

### Bases (Query Dashboards)
`.base` files provide aggregated views of TaskNotes:

**Types of views:**
- **Task List** — All non-completed tasks sorted by urgency
- **Kanban boards** — Group by status, timeline, owner, or priority
- **Completed view** — Archive of finished tasks with modification date

**Key .base files:**
- `Signal Relay Dashboard.base` — All tasks across projects (in `E - The Foundry/Dashboard/`)
- `baby-prep-tasks.base` — Baby prep tasks (in `E - The Foundry/Active/1 Baby Prep - Cyrus/`)
- `career-tasks.base` — Career tasks (in `E - The Foundry/Active/6 Career Transition 2026/`)
- `relationship-tasks.base` — Relationship tasks (in `E - The Foundry/Ongoing/2 🥰 Camille/`)
- `Projects List.base` — All projects tagged with `#project` (in `E - The Foundry/Dashboard/`)

### How They Work Together

- **TaskNotes** = detailed action plans and checklists (individual task files)
- **Bases** = aggregated views and progress tracking across multiple tasks
- **Project hubs** (like `1 Baby Prep - Cyrus.md`) embed the base and link to related TaskNotes
- **Weekly Dashboard** (Canvas) embeds per-project .base files for at-a-glance priority view

## Linking Conventions

- Obsidian uses wikilinks: `[[Note Title]]` to create bidirectional links between notes
- Links are resolved by note title, not file path
- The vault emphasizes connected thinking through liberal use of links between related concepts
- **MOCs** (Maps of Content) in `A - The Observatory/MOCs/` serve as topic indexes — use these to discover notes by topic

## Working with Notes

When creating or modifying notes in this vault:
- Use wikilink syntax `[[Note Title]]` for internal links, not markdown links
- Match the organizational structure:
  - **Signal Relay** for daily/weekly time-based notes
  - **E - The Foundry/Active** for project-specific content
  - **E - The Foundry/Ongoing** for life area content
  - **The Observatory** for reference/knowledge notes
- Notes may contain Dataview queries or task syntax from the tasks plugin
- Task syntax uses checkbox format: `- [ ]` (incomplete), `- [x]` (complete)
- Tags use hashtag syntax: `#tagname` (e.g., `#outdoor`, `#project`)

## Task Planning Preferences

**IMPORTANT:** David needs help staying on top of tasks. Be proactive in helping organize and structure tasks.

### Task Structure Standard (Established Feb 2026)

**Use collapsible nested subtasks** for any task with multiple steps or checklist items:

```markdown
  - **Context**: Why this matters or background information
  - **Done when**: Clear acceptance criteria
  - **Related**: [[Wikilink to related note]]
```

### When to Use Nested Subtasks

1. **Multi-step workflows** — Tasks with 3+ sequential actions
2. **Checklists** — Shopping lists, packing lists, inventory items
3. **Category groupings** — Related items that can be checked off individually

### Subtask Benefits

- **Collapsible sections** — Click arrows to expand/collapse, reducing visual clutter
- **Progress tracking** — Parent tasks show `[ ]` (none), `[/]` (partial), `[x]` (complete)
- **Focused execution** — Expand only the section you're working on
- **Clear next actions** — Each subtask is a specific, checkable action

### Task Description Components

Every enriched task should include:
1. **Action subtasks** — Specific checkable steps
2. **Context bullets** — "Why critical" or "Why matters" (non-checkable)
3. **Acceptance criteria** — "Done when..." statement (non-checkable)
4. **Related links** — Wikilinks to related notes or dependencies (non-checkable)

### Proactive Task Management

When David shares new tasks or projects:
1. **Ask clarifying questions** if the task scope is unclear
2. **Suggest breaking down** tasks with 3+ steps into subtasks
3. **Add context bullets** for why the task matters and when it's complete
4. **Organize by deadline** and recommend priority levels
5. **Connect to existing projects** by adding wikilinks to related notes
6. **Offer to create project hubs** for multi-task initiatives

David has expressed: "I really need assistance staying on top of things" - be proactive, helpful, and organizational.

## Sandbox-First Protocol

**CRITICAL:** When modifying dashboard files, Canvas files, .base files, or core system files, ALWAYS use sandbox/TEST versions first.

### Protocol Steps

1. **Always work in sandbox/TEST versions first**
   - Create `-TEST` or `- TEST` suffixed copies before making changes
   - Never modify production files directly during development

2. **Ask user to verify** the sandbox version works correctly
   - Explicitly state: "I've updated the TEST version. Please verify it works before I migrate to production."
   - Wait for user confirmation before proceeding

3. **Only migrate to production** after explicit user approval

4. **Never update production files** until sandbox is verified

### Files That Require Sandbox-First

- `Weekly Dashboard.canvas` → Test in `Weekly Dashboard - TEST.canvas`
- `Projects List.base` → Test in `Projects List - TEST.base`
- Main dashboard files in `E - The Foundry/Dashboard/`
- Template files in `A - The Observatory/Documentation/Templates/`
- Any `.base` files used in production

## File Paths

Due to iCloud sync, the working directory path is:
```
/Users/davidarechiga/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)
```

Note: The vault is named "Constellation" but the folder on disk is still "Second Brain (iCloud)".

Always use quotes around paths containing spaces when using command-line tools.
