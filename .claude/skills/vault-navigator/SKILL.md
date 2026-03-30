---
name: vault-navigator
description: Find relevant notes in the Constellation vault efficiently. Use when the user asks "where is X", "find notes about Y", "what do I have on Z", or when Claude needs to locate context before starting a task. Checks _index.md files first before doing expensive Glob/Grep.
version: 1.0.0
---

# Vault Navigator Skill

## Purpose

Locate relevant vault notes with minimal token cost by scanning `_index.md` files before falling back to full search. A folder index costs ~200 tokens to scan; a full Glob of the same folder can cost 10–50×.

## Navigation Hierarchy (cheapest first)

1. **`_index.md` files** — check the relevant folder's index first
2. **Folder notes** (e.g., `Active.md`, `Ongoing.md`) — contain quick links to sub-notes
3. **`Constellation.md`** — vault hub, links to all major areas
4. **Glob/Grep** — only if above don't surface the answer

## Index File Locations

| Folder | Index file |
|--------|-----------|
| Music & Audio | `A - The Observatory/🎵 Music & Audio Production/_index.md` |
| Career | `A - The Observatory/💼 Career Development/_index.md` |
| Active projects | `E - The Foundry/Active/_index.md` |
| Ongoing life areas | `E - The Foundry/Ongoing/_index.md` |
| Tasks by project | `E - The Foundry/Tasks/_index.md` |
| Signal Relay (daily/weekly) | `C - Signal Relay/_index.md` |

## Workflow

### Step 1 — Classify the query
- Is it about a **project or task**? → Start at `E - The Foundry/Active/_index.md` or `Tasks/_index.md`
- Is it about a **knowledge topic** (music, career, health)? → Start at the relevant Observatory subfolder index
- Is it **time-based** (daily note, weekly)? → Start at `C - Signal Relay/_index.md`
- Is it **unclear**? → Read `Constellation.md` first for orientation

### Step 2 — Scan the index
Read the relevant `_index.md`. Each entry is one line: note title + summary. Identify the 1–3 most relevant notes.

### Step 3 — Fetch if needed
Read the most relevant note. Follow wikilinks for depth if the user needs more context.

### Step 4 — Return results
Respond with:
- Wikilinks to the top 1–3 relevant notes
- One-sentence summary of what each contains
- Offer to read the most relevant one in full

## Fallback: No index exists yet
If an `_index.md` doesn't exist for the folder you need, use Glob to list contents and Grep for keywords. Note to the user that the index is missing and offer to create it.
