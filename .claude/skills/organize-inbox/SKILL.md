---
name: organize-inbox
description: Organizes notes in the Obsidian vault using the ACE method (Atlas/Calendar/Efforts). Use when the user wants to organize inbox notes, categorize entries, move files between folders, consolidate similar notes, or restructure the vault. Handles batch organization, file classification, and wikilink creation.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, TodoWrite, AskUserQuestion
---

# Organize Inbox Skill

Helps organize loose notes in the "Constellation" Obsidian vault using the ACE framework.

## Vault Root
`/Users/davidarechiga/Constellation/Constellation/`

## ACE Structure

- **A - The Observatory/** (Atlas — knowledge & reference)
  - `✍️ Ideas, Thoughts & Poetry/` — creative writing, poetry, shower thoughts
  - `🌟 Lifestyle & Personal/` — health, wellness, habits, personal growth, recipes
  - `🎨 Design & Creative Work/` — design notes, creative projects, visual inspiration
  - `🎮 Entertainment & Media/` — movies, games, music to listen to, concerts, TV
  - `🎵 Music & Audio Production/` — music production notes, song ideas, gear, mixing
  - `💼 Career Development/` — career notes, job search, skills, networking
  - `Checklists/` — reusable checklists and reference lists
  - `MOCs/` — Maps of Content (topic index notes)
  - `Sources/` — book notes, articles, literature notes
  - `Documentation/` — system docs, templates, guides
  - `Archive/` — completed or inactive reference notes

- **C - Signal Relay/** (Calendar — time-based)
  - `Inbox/` — **primary inbox** where new notes land before being sorted
  - `Daily/` — daily notes (YYYY-MM-DD.md)
  - `Weekly/` — weekly review notes

- **E - The Foundry/** (Efforts — active work)
  - `Active/` — active projects with deadlines
  - `Ongoing/` — life areas (Personal Growth, Camille, River, Cyrus, Household)
  - `Someday/` — future/paused projects
  - `Tasks/` — TaskNotes organized by project subfolder
    - `Tasks/Inbox/` — loose unclassified task notes

## Core Workflow

When organizing loose notes:

1. **Ask user preferences first** using AskUserQuestion:
   - Show categorized list first vs. auto-move vs. interactive one-by-one
   - Whether to consolidate similar notes or keep separate

2. **Locate loose notes** — always start with:
   - `C - Signal Relay/Inbox/` — **primary inbox**, where all new notes are created
   - `E - The Foundry/Tasks/Inbox/` — unclassified task notes
   - Any `.md` files that don't belong in their current location
   - Notes the user explicitly points to

3. **Analyze content** — read each note to determine:
   - Is it a **task/action**? → TaskNote in `E - The Foundry/Tasks/[Project]/`
   - Is it **time-based**? → `C - Signal Relay/Daily/` or `Weekly/`
   - Is it **reference/knowledge**? → appropriate `A - The Observatory/` subfolder
   - Is it **active project work**? → `E - The Foundry/Active/[Project]/`
   - Is it **ongoing life area**? → `E - The Foundry/Ongoing/[Area]/`

4. **Use TodoWrite to track progress**:
   - Create todos per category batch
   - Mark in_progress then completed as you work

5. **Create consolidated notes** for similar content:
   - Multiple song ideas → consolidate into `🎵 Music & Audio Production/`
   - Multiple Camille-related notes → `E - The Foundry/Ongoing/2 🥰 Camille/`
   - Multiple recipes → `🌟 Lifestyle & Personal/`

6. **Move files systematically**:
   - Always quote paths in bash commands (spaces in path)
   - Use `mv` with full absolute paths
   - Verify moves were successful

7. **Clean up**:
   - Delete stub/empty notes
   - Remove originals that were fully consolidated
   - Verify inbox is empty after processing

8. **Provide summary**:
   - Before/after counts
   - What was consolidated
   - Where files were moved
   - Wikilinks to key notes

## Classification Guide

**Task Notes** → `E - The Foundry/Tasks/[Project]/`
- Anything with a clear action, due date, or checklist
- Use TaskNote frontmatter: `status`, `priority`, `due`, `owner`, `projects`, `tags`
- Unclassified tasks go to `Tasks/Inbox/` temporarily

**Active Projects** → `E - The Foundry/Active/[Project]/`
- Music Releases, Career Transition 2026, Pixel Glitch, Frameloop, Ancestry Research, frmwrk_

**Ongoing Life Areas** → `E - The Foundry/Ongoing/`
- `1 🛫 Personal Growth/` — self-improvement, goals, therapy notes
- `2 🥰 Camille/` — relationship notes, date ideas, check-in questions
- `3 🐶 River/` — pet care notes
- `4 👶 Cyrus/` — baby/parenting notes
- `5 🏡 Household/` — home maintenance, finance, admin

**Music & Audio** → `A - The Observatory/🎵 Music & Audio Production/`
- Song ideas, production notes, mixing notes, gear research
- Specific release work → `E - The Foundry/Active/Music Releases/`

**Design & Creative** → `A - The Observatory/🎨 Design & Creative Work/`
- Design inspiration, creative concepts, visual ideas

**Personal Growth / Health** → `A - The Observatory/🌟 Lifestyle & Personal/`
- Wellness notes, habit ideas, recipes, personal values

**Entertainment** → `A - The Observatory/🎮 Entertainment & Media/`
- Movies/TV to watch, games, concerts, books

**Career** → `A - The Observatory/💼 Career Development/`
- General career notes, skill development
- Active job search work → `E - The Foundry/Active/Career Transition 2026/`

**Creative Writing / Ideas** → `A - The Observatory/✍️ Ideas, Thoughts & Poetry/`
- Poetry, stream-of-consciousness, shower thoughts, philosophical notes

**Archive** → `A - The Observatory/Archive/`
- Completed, outdated, or inactive reference notes

## Technical Notes

- Always quote all paths in bash commands (path contains spaces)
- Use wikilink syntax: `[[Note Title]]` not markdown links
- Do NOT use Dataview queries — vault uses `.base` files for dynamic views
- Tags use `#tagname` syntax
- TaskNote frontmatter fields: `tags`, `title`, `status`, `priority`, `due`, `owner`, `projects`
