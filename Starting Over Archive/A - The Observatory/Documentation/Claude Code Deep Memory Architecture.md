---
cssclasses: []
title: Claude Code Deep Memory Architecture
tags:
  - documentation
  - claude-code
  - system
description: How the Constellation vault is wired for token-efficient Claude Code sessions
created: 2026-03-25
---

# Claude Code Deep Memory Architecture

> This documents the memory system implemented on 2026-03-25, based on the research note [[Deep Memory For Claude Code Through Obsidian Vault]].

---

## Why This Exists

Naive Claude Code setups dump everything into CLAUDE.md — a single file that loads every session, consuming tokens even when 90% of the content is irrelevant to the current task. This system instead routes context across five tiers, so only the minimum necessary tokens load by default, with deep knowledge accessible on demand.

**Before:** CLAUDE.md = 216 lines, always loaded, warehouse-style.
**After:** CLAUDE.md = ~51 lines, pure router. Deep content in path-scoped rules, memory files, and skills.

---

## The Five Tiers

### Tier 0 — CLAUDE.md (Always Loaded)

**File:** `/Users/davidarechiga/Constellation/CLAUDE.md`
**Target:** Under 150 lines. Survives `/compact`.

Contains only:
- Vault root path + one-line ACE folder descriptions
- Core rules (wikilinks, no Dataview, sandbox protocol)
- Pointers to rules/ and skills for deeper detail
- `_index.md` maintenance instruction

**Rule:** Never add deep content here. Anything longer than 3 lines belongs in a rules/ file or skill.

---

### Tier 1 — `.claude/rules/` (Path-Scoped, Always Loaded When Matching)

**Location:** `/Users/davidarechiga/Constellation/.claude/rules/`

Rules files use YAML `paths:` frontmatter — they only consume tokens when Claude is working in matching folder patterns.

| File | Loads When | Content |
|------|-----------|---------|
| `task-notes.md` | Working in `E - The Foundry/**` | Full TaskNotes frontmatter spec, nested subtask format, 4-component structure, .base file locations |
| `vault-conventions.md` | Working in `C - Signal Relay/**` or `A - The Observatory/**` | Plugin list, daily/weekly note format, linking conventions, folder note pattern |

---

### Tier 2 — Auto-Memory (Project Context, Persists Across Sessions)

**Location:** `~/.claude/projects/-Users-davidarechiga-Constellation/memory/`

| File | Purpose |
|------|---------|
| `MEMORY.md` | Index — first 200 lines always load |
| `vault-overview.md` | ACE structure, task system rules, David's context |
| `vault-path.md` | Path migration record (iCloud → Obsidian Sync, Mar 2026) |
| `current-work.md` | Active projects, life areas, blockers — **update after each `/weekly` review** |
| `decisions.md` | Why key system choices were made (no Dataview, sandbox protocol, ACE structure) |

**Update cadence:** `current-work.md` should be refreshed weekly. `decisions.md` grows over time as new architectural choices are made.

---

### Tier 3 — Skills (Zero Cost at Rest)

Skills load only name + description (~100 tokens each) at startup. Full skill body loads only when triggered.

| Skill | Trigger | What It Does |
|-------|---------|-------------|
| `/morning` | Morning check-in | Briefing + time-blocked schedule into daily note |
| `/evening` | End of day | Prep for tomorrow + seeds next day's note |
| `/weekly` | Weekly review | Scans 7 days, writes weekly summary + next-week focus |
| `/organize-inbox` | Inbox sorting | Classifies and moves notes from `C - Signal Relay/Inbox/` |
| `/session-persist` | Save session learnings | Writes session log to daily note, promotes durable insights to memory |
| `/vault-navigator` | Find notes | Checks `_index.md` files before doing expensive Glob/Grep |

---

### Tier 4 — Per-Folder `_index.md` Files (Navigation Layer)

Each frequently-navigated folder has an `_index.md` — a ~200-token manifest of what's inside. Claude checks these before doing a full Glob/Grep (10–50× more expensive).

| Index File | Folder |
|-----------|--------|
| `A - The Observatory/🎵 Music & Audio Production/_index.md` | Music notes |
| `A - The Observatory/💼 Career Development/_index.md` | Career notes |
| `E - The Foundry/Active/_index.md` | Active projects (status + next action) |
| `E - The Foundry/Ongoing/_index.md` | Life areas (key notes per area) |
| `E - The Foundry/Tasks/_index.md` | Task subfolders by project |
| `C - Signal Relay/_index.md` | Today's daily note + this week's weekly note |

**Maintenance rule (in CLAUDE.md):** When creating or deleting vault files, update the nearest `_index.md`.

---

### Tier 5 — Stop Hook (Passive Session Capture)

**Script:** `/Users/davidarechiga/Constellation/.claude/hooks/on-stop.sh`
**Trigger:** Automatically runs when Claude Code session ends.

What it does (shell only — no AI):
1. Finds vault `.md` files modified in the last 2 hours
2. Appends a compact breadcrumb to today's daily note under `## 🤖 Session Log`:

```
- 14:32 — Claude session ended. Modified: Mix Maintenance, _index, Career Transition 2026
```

For **full AI-generated session summaries** with durable insight extraction → run `/session-persist` manually.

---

## Token Budget Impact

| Context type | Before | After |
|-------------|--------|-------|
| CLAUDE.md | ~4,200 tokens (216 lines) | ~1,050 tokens (51 lines) |
| Rules (task context) | 0 (baked into CLAUDE.md) | ~1,200 tokens (only when in Foundry) |
| Skills (6 installed) | N/A | ~600 tokens at rest total |
| Memory files | ~1,000 tokens | ~2,500 tokens (richer, 5 files) |
| Navigation | Glob/Grep per lookup | `_index.md` scan (~200 tokens each) |

---

## Maintenance Checklist

- [ ] After `/weekly`: update `memory/current-work.md` with project status
- [ ] When new architectural choice is made: add to `memory/decisions.md`
- [ ] When adding/deleting vault files: update nearest `_index.md`
- [ ] Keep CLAUDE.md under 150 lines — move anything longer to rules/ or a skill

---

## Related

- [[Deep Memory For Claude Code Through Obsidian Vault]] — source research note
- [[Constellation Guide]] — overall vault system documentation
