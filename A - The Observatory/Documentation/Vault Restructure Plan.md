---
tags:
  - note
  - project
title: Vault Restructure — Running Todo
---

## Why This Matters
The ACE restructure (Atlas/Calendar/Efforts) is largely complete in the file system, but git has ~1,942 unstaged changes and several loose ends remain before the vault is fully clean and committed. A second phase of organization simplification follows — covering folder consolidation, naming cleanup, and tag/link strategy — to make the vault leaner and easier to navigate long-term.

## Done When
- [ ] Git repo is fully committed and clean
- [ ] All `_index.md` files reflect the current folder structure
- [ ] No orphaned wikilinks or broken references
- [ ] `Constellation.md` home note is accurate
- [ ] Folder structure passes the consolidation audit (no thin subfolders)
- [ ] Naming is consistent across active areas (no emoji clutter, no auto-generated titles)
- [ ] Tag taxonomy is defined, documented, and applied vault-wide

---

## Task Breakdown

### Git / Version Control
- [ ] Review and commit `.obsidian/` config changes (plugin updates, removed plugins)
  - Removed: `actions-uri`, `obsidian-full-calendar`, `obsidian-tasks-plugin`, `obsidian-tracker`, `smart-connections`
  - Updated: `folder-notes`, `homepage`, `quickadd`, `templater`, `omnisearch`, etc.
- [ ] Commit deletion of `.keep-the-rhythm/` backups
- [ ] Commit all Archive file deletions (moved into Observatory in Phase 8)
- [ ] Commit all Attachment file deletions
- [ ] Commit remaining vault note moves/renames
- [ ] Final `git status` should be clean

### Index Files (`_index.md`)
- [x] Verify `A - The Observatory/_index.md` reflects Archive, Attachments, Templates moved in
- [x] Verify `E - The Foundry/Tasks/_index.md` is up to date
- [x] Verify `C - Signal Relay/_index.md` exists and is current
- [ ] Add `_index.md` to any subfolders missing one

### Wikilinks & References
- [ ] Search for broken links to old folder paths (e.g. references to removed numbered prefixes)
- [ ] Update `Constellation.md` home note if any links are stale
- [ ] Check `Constellation Guide` for outdated folder references

### Plugin Cleanup
- [ ] Confirm removed plugins (`obsidian-full-calendar`, `obsidian-tasks-plugin`, `obsidian-tracker`, `smart-connections`) are fully uninstalled in Obsidian
- [ ] Confirm `.base` dashboards are still working after plugin changes
- [ ] Verify `keep-the-rhythm` plugin still works (backups deleted)

### Post-Restructure Polish
- [x] Update `Constellation.md` — change Last updated date from 2026-03-25
- [ ] Archive any notes in `C - Signal Relay/Inbox/` that piled up during restructure
- [ ] Confirm `E - The Foundry/Dashboard/` canvas and `.base` files still load correctly

---

## Organization Simplification

### Folder Consolidation
Goal: reduce folder depth and eliminate subfolders that exist only to hold a handful of notes. Fewer folders = faster navigation and less decision fatigue when filing.

- [ ] Audit `A - The Observatory/` subfolders
  - List every subfolder and count its direct note files
  - Any subfolder with fewer than 4 notes that is not expected to grow: merge its contents into the parent folder or a single `Misc` holding folder
  - **Done when**: No subfolder exists solely to hold 1-3 notes with no growth trajectory
- [ ] Audit `E - The Foundry/Tasks/` project subfolders
  - Identify subfolders with zero open tasks or whose parent project is complete/abandoned
  - Archive completed project task folders; delete empty ones
  - **Done when**: Every Tasks subfolder maps to a currently active project
- [ ] Evaluate `A - The Observatory/Lifestyle & Personal/` subfolder structure
  - If subcategory folders (e.g. Exercise, Finance, Health) each contain only 2-4 notes, collapse them into a flat `Lifestyle & Personal/` folder and use tags or note prefixes to distinguish topics
  - **Done when**: Folder depth in this section is no more than 2 levels (Observatory > Lifestyle & Personal > note)
- [ ] Review `E - The Foundry/Ongoing/` life area folders
  - Confirm all 5 hub files (Personal Growth, Camille, River, Cyrus, Household) are actively being written to
  - If any life area folder duplicates an Active project folder in scope, decide which is canonical and remove the other
  - **Done when**: Each Ongoing folder has a clear, non-overlapping purpose
- [ ] Check `A - The Observatory/` for duplicate structural layers
  - Look for nested folders that restate their parent (e.g. `Sources/Books/Books/` or `Archive/Archive/`)
  - Flatten any accidental double-nesting
  - **Done when**: No folder name appears consecutively in any path

### Naming Cleanup
Goal: consistent, scannable names across all active areas. Names should be plain English — no decorative emoji, no auto-generated titles, no version numbers in note names.

- [ ] Audit emoji usage across all folder names
  - Acceptable: the 3 ACE root prefixes (A, C, E) and the Ongoing life area hubs (these use emoji as visual anchors)
  - Remove: emoji from subfolders inside The Observatory, The Foundry project folders, and any task files
  - **Done when**: Emoji appear only on ACE root folders and the 5 Ongoing life area hubs — nowhere else
- [ ] Scan for auto-generated or low-quality note names in `A - The Observatory/`
  - Flag: notes named after URLs, notes titled "Untitled", notes with only a date as the title, notes whose name is a sentence fragment
  - For each: rename to a clear topic title, merge into a related note, or delete if stale/empty
  - **Done when**: Every note in The Observatory has a human-readable, topic-based title
- [ ] Standardize active project hub note names in `E - The Foundry/Active/`
  - Pattern: `[Project Name].md` — no dates, no version suffixes, no status words in the filename
  - **Done when**: All Active project hub files follow the pattern
- [ ] Standardize task file names in `E - The Foundry/Tasks/`
  - Pattern: lowercase-kebab-case describing the action, e.g. `build-portfolio-site.md`
  - No date prefixes in task filenames (dates live in frontmatter)
  - **Done when**: All task files follow kebab-case naming with no date prefixes
- [ ] Review `C - Signal Relay/Inbox/` for stale or misfiled notes
  - Any note older than 30 days that has not been processed: file it, archive it, or delete it
  - **Done when**: Inbox contains only notes from the last 30 days

### Tag and Link Strategy
Goal: reduce tag sprawl to a manageable, intentional set. Wikilinks should form a meaningful knowledge graph — not random cross-references.

- [ ] Inventory all tags currently in use
  - Grep the vault for all `#tag` instances; compile a unique list
  - Identify: duplicates (e.g. `#task` vs `#tasks`), single-use tags, tags that overlap with folder structure (redundant), and tags with no clear meaning
  - **Done when**: Master tag list exists as a note, with each tag's current count and a keep/merge/remove decision
- [ ] Define a 3-tier tag taxonomy and document it
  - Tier 1 — Type: `note`, `task`, `project`, `source`, `template`
  - Tier 2 — Area: `personal`, `work`, `family`, `music`, `finance`, `health`
  - Tier 3 — Status: `active`, `someday`, `archive` (only where status is not captured in frontmatter)
  - Write the taxonomy to `A - The Observatory/Documentation/Wiki De Arechiga/Vault Tag Taxonomy.md`
  - **Done when**: Taxonomy note exists and is linked from `Constellation.md`
- [ ] Apply the taxonomy — remove or replace all tags that fall outside it
  - Work folder by folder: Observatory first, then Foundry, then Signal Relay
  - **Done when**: No tag exists in the vault that is not in the taxonomy
- [ ] Audit wikilinks in all MOC notes (`A - The Observatory/MOCs/`)
  - Remove links to notes that no longer exist (show as red/unresolved in Obsidian)
  - Add links to notes that clearly belong in the MOC but are not yet linked
  - **Done when**: All MOC notes have zero broken links and represent current vault contents
- [ ] Establish a linking principle for new notes going forward
  - Rule: link to a note only when the connection is meaningful and bidirectional — not just because a word matches a note title
  - Document this rule in `Vault Tag Taxonomy.md` under a "Linking Philosophy" section
  - **Done when**: Rule is written and David has agreed to it

---

## Notes
- Restructure completed through Phase 8 (commit `d33f4ab`) — ACE prefixes, Archive/Attachments/Templates all consolidated into The Observatory
- ~1,942 git changes pending — mostly deletions from old paths after moves
- Organization Simplification added 2026-03-29 — intended as a second pass after git cleanup is done
