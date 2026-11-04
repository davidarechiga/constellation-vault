# Agent Log

> Shared log for every AI agent working in this vault. Newest entry on top. Format and rules: `AGENTS.md`.

### 2026-11-03 · Claude Code (root cleanup)
- Did: Moved [[Owning It - A Repair Check-In]] to `x/Templates/` and Units for Transformation to `+ Inbox/`. Moved `Test.md` (a one-line Wispr Flow test) to `.trash/` at Dave's request, so it can still be recovered.
- Open / needs Dave: Item (1) on the list below is done. Next is (2), the Templates core plugin folder.

### 2026-11-03 · Claude Code (one-thing rule)
- Did: Added "One thing at a time" to the Rules in `AGENTS.md`, at Dave's request.
- Open / needs Dave, in order: (1) Root notes: which ones move to `+ Inbox/`. (2) Should the Templates core plugin point at `x/Templates`? (3) Turn community plugins back on (the list is empty on this computer). (4) Weekly template and Periodic Notes weekly paths. (5) `/evening` skill paths.

### 2026-11-03 · Claude Code (Periodic Notes)
- Did: Pointed Periodic Notes' daily notes at `Calendar/Daily` with `x/Templates/Daily Note Template`. Dave says daily notes come from Periodic Notes, not the core Daily notes plugin.
- Open / needs Dave: `community-plugins.json` is empty on this computer, so Periodic Notes is off here right now. The weekly template and folder settings still use old paths.

### 2026-11-03 · Claude Code (daily template)
- Did: Moved `Daily Note Template.md` from the archive to `x/Templates/` and pointed `.obsidian/daily-notes.json` at it.
- Decided: Left the template's content as is.
- Open / needs Dave: The Daily notes core plugin is off and no community plugins are enabled, so nothing uses this setting yet. The Templates core plugin's folder still points at the old archived path. `/evening` still references the old template path.

### 2026-11-03 · Claude Code (ACE folders + inbox)
- Did: Created `+ Inbox/`, `Atlas/`, `Calendar/Daily/`, `Efforts/` (On, Ongoing, Simmering, Sleeping) and `x/` (Templates, Attachments). Pointed new notes at `+ Inbox`, attachments at `x/Attachments`, daily notes at `Calendar/Daily` in `.obsidian/`. Added ACE rules to `CLAUDE.md`.
- Decided: Added the rules to the existing `CLAUDE.md` instead of replacing it, so `@AGENTS.md` still loads.
- Open / needs Dave: Confirm which root notes move to `+ Inbox/`. The daily-notes template path still points at a folder that's now archived.

### 2026-11-03 · Codex
- Did: Read the shared agent guidance, priorities, recent log, Family North Star, current school catch-up notes, BUS 10 AI policy, and the archived system overview and Fair Play reference.
- Decided: Use the post-reset priorities and current notes; treat archived workflows and dated plans as historical context. Support follow-through without adding systems. No git operations.
- Open / needs Dave: School status needs a fresh check before planning: the Nov 2 catch-up table marks Module 2 complete, while Priorities and the older checklist still list it as open. No priority or instruction files changed.

### 2026-11-03 · Claude Code (Obsidian Sync + git)
- Did: Committed Dave's new notes and the deletions he confirmed (empty `Attachments.md` and the TaskNotes views, which kept erroring). Updated `AGENTS.md` and `CLAUDE.md` for the new setup.
- Decided: Dave is starting Obsidian's configuration from scratch. Obsidian Sync moves files between his computer(s) and iPhone. Git is only for Claude Code, run from one computer via Claude remote control. The Obsidian Git plugin is off. Claude Code commits snapshots of Dave's edits, since nothing else does, and never switches branches in the main folder (Sync would copy that to every device).
- Open / needs Dave: Turn off Obsidian Git on every device, especially the other machine that made the "Vault Sync / Backup" commits. Decide whether to add `.obsidian/` to `.gitignore`.

### 2026-11-03 · Claude Code (restore + sync)
- Did: Restored `Scuba/Scuba.md` and `Bicycle/Bicycle.md` in the archive from git; Dave didn't know who deleted them. Synced `main`, GitHub and all three worktrees.
- Decided: Left `.obsidian/plugins/` settings uncommitted (Obsidian rewrites them). The Folder Notes plugin now has `autoCreate: true` and a template path to the old `Constellation/A - The Observatory/Documentation/Templates/` folder, which no longer exists. That plugin likely made or removed those stub folder notes.
- Open / needs Dave: Decide whether Folder Notes auto-create should stay on before reorganizing. Dave wants a fresh start on a vault reorganization.

### 2026-11-03 · Claude Code (Claude chat shelved)
- Did: Marked Claude chat as "not set up" in the `AGENTS.md` agents table and added a shelved banner to [[Claude Chat Instructions]].
- Decided: Dave is dropping the Claude Project "Constellation" plan and will find another way for Claude chat. This replaces the earlier "create the Project" to-do below.
- Open / needs Dave: The replacement for Claude chat is undecided.

### 2026-11-03 · Claude Code (commit rules)
- Did: Added "Commit and sync rules" to `AGENTS.md`. Found why other sessions missed updates: `main` had diverged from GitHub (4 ahead, 7 behind from the other machine's Obsidian Git backups), and three worktrees in `.claude/worktrees/` sit on old commits with old copies of `AGENTS.md`. Merged and pushed `main`.
- Decided: Rule changes get committed and pushed in the same turn. Vault work happens on `main` in the main folder, not in worktrees.
- Open / needs Dave: The three worktrees (two `bridge-…` ones are locked) still hold old copies. I left them alone because other sessions may own them. Also left uncommitted on purpose: Obsidian plugin data, and the deleted `Scuba.md` and `Bicycle.md` archive notes (say the word if those deletions are intended).

### 2026-11-03 · Claude Code (time rule)
- Did: Added a rule to `AGENTS.md`: check the real date, weekday and time before saying "tonight" or "tomorrow" or naming a deadline. I had told Dave BUS 10 met tonight (Tue); the next class is actually Wed Nov 4 at 6:30pm.

### 2026-11-03 · Claude Code
- Did: Added three Claude Code subagents in `.claude/agents/`: `vault-reader` (read-only Q&A with cited notes), `vault-connector` (vault + web research, suggests wikilinks, no edits) and `vault-editor` (in-place cleanup, gives feedback only on schoolwork).
- Decided: Only the editor can write. All three read [[Priorities]] first and follow the AGENTS.md schoolwork rules.
- Open / needs Dave: Try them out. School catch-up is still #1.

### 2026-11-03 · Claude Code
- Did: Wrote [[Claude Chat Instructions]] so Claude chat follows the same rules as AGENTS.md, and added Claude chat to the agents table.
- Open / needs Dave: Create the "Constellation" Project in Claude, paste the instructions, and upload `Priorities.md` + `AGENTS.md`. Re-upload `Priorities.md` whenever it changes.

### 2026-11-02 · Claude Code (Canvas check)
- Did: Read Canvas through Dave's Chrome (he signed in himself) and added a live status table to the top of [[Catch Up Plan]]. Nothing was submitted.
- Open / needs Dave: BUS 10 has 3 missing items (Exam #1, Module 3 quiz, Hondo case), none locked. SMM "Virality and Memes" is due tonight at 11:59pm.

### 2026-11-02 · Claude Code (later)
- Did: Filled in [[Priorities]] with Dave: school catch-up (BUS 10 class Mon/Wed 6:30pm), family, health & fitness (180 lbs, bed by 11pm), and releasing "Only Talks 2 Ghosts".
- Open / needs Dave: BUS 10 catch-up before tonight's class. `/morning`, `/evening` and `/weekly` still point at pre-reset folders.

### 2026-11-02 · Claude Code
- Did: Fixed the vault's git backup, which had been stuck since Apr 1 on a merge conflict; the vault and GitHub now match. Created `AGENTS.md` (shared instructions for all agents), `CLAUDE.md` and `GEMINI.md` (both point to `AGENTS.md`), [[Priorities]], and this log.
- Decided: Build in the fresh vault after Dave's Nov 2 reset and keep it minimal. The old system stays in `Starting Over Archive/`.
- Open / needs Dave: Confirm the ❓ items in [[Priorities]]. The `/morning`, `/evening` and `/weekly` skills still point at pre-reset folders. Gemini isn't connected yet.
