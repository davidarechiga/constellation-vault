# Agent Log

> Shared log for every AI agent working in this vault. Newest entry on top. Format and rules: `x/AGENTS.md`.

### 2026-11-12 · Claude Code (school catch-up walkthrough)
- Did: Built a catch-up plan from a ChatGPT read-only Canvas report (Nov 10) and walked Dave through BUS 10 Appendix A with short question-and-answer steps (dispute settling, contract requirements, breach remedies). Added the Nov 10 Canvas status and book page map to [[Catch Up Plan]], and drafted [[SMM Late Work Email Draft]] (not sent).
- Decided: One small step at a time, and Dave writes all graded work. Order was Nov 11 deadlines first (SWOT 100 pts, Exam #2 50 pts), then Exam #1, Hondo, Module 3 quiz, UGC, SMM. Listening to the book (ElevenReader) is fine for study time while watching Cyrus.
- Open / needs Dave: Exam #2 and the SWOT were due Nov 11; I don't know if they got done. Exam #2 may also include OpenStax Chapter 6 (page 201); check the syllabus. Appendix A still to cover: internet regulation, consumer protection and taxes (PDF pp 623-625). Email to the SMM instructors still needs his review and send. The OpenStax PDF (148 MB) sits in the Intro To Business folder in the main vault; it isn't tracked in git.

### 2026-11-12 · Claude Code (Simmering inbox)
- Did: Made [[Simmering]] the project inbox (updated its note and [[Efforts]]). Tried a separate Projects Inbox folder, then reverted it as redundant with `+ Inbox/`. Stopped tracking `.obsidian/` in git and added it to `.gitignore`.
- Decided: New project ideas go to `+ Inbox/`, then into Simmering; they move to On or Ongoing when they get real. Added the one-task-per-Claude-Code-session rule to `x/AGENTS.md` and `.claude/CLAUDE.md` so context windows don't bloat; also documented Simmering as the project inbox and `.obsidian/` as untracked.
- Open / needs Dave: Brainstorm scheduled tasks for the vault in a fresh session.

### 2026-11-12 · Claude Code (Home Network)
- Did: Added `Atlas/Notes/Home Network.md` (router, command center, server, TVs table; network tracker idea parked). Corrected [[Razorleaf]]: it is the MacBook Pro (M1 Max, 32 GB, macOS 26.5.2) that Claude Code runs on, not an iPad.
- Open / needs Dave: eero count and models. Razorleaf is still marked `placement: carried`; change if it stays put. Everything on the 24/7 TV and network tracker waits until school catch-up is done.

### 2026-11-12 · Claude Code (24/7 Live TV scope)
- Did: Studied spelunkertv.online (looping playlists on a shared clock, a guide computed in the browser). Rewrote [[24-7 Live TV]] with Dave's scope.
- Decided: Household-only and private, never public. Its purpose is controlling what Cyrus watches: a mix of DVDs, VHS, CDs, records and home videos, away from all-you-can-eat streaming. Stays Simmering.
- Open / needs Dave: Custom site vs ErsatzTV or Tunarr; how to digitize the media; which device Cyrus watches on.

### 2026-11-12 · Claude Code (24/7 Live TV)
- Did: Added [[24-7 Live TV]] to `Efforts/Simmering/` (build a 24/7 live TV channel on the Mac mini, [[The Lodge]]). Linked from `Efforts.md` and `Simmering.md`.
- Decided: Simmering, not On, because school catch-up is still #1 in [[Priorities]].
- Open / needs Dave: What the channel shows and where it streams. Say if it should be On instead.

### 2026-11-12 · Claude Code (Home dashboard)
- Did: Built `x/Home/Home.md` (folder note + dashboard) with two Bases, `Home Tasks.base` and `Home Notes.base`, embedded as sections. Turned on the Homepage plugin (added to `community-plugins.json`, pointed its `data.json` at `x/Home/Home`, Reading view).
- Decided: Note with embedded Bases instead of a canvas, because Bases inside canvas nodes weren't verifiable here and the note scrolls well on the phone.
- Open / needs Dave: TaskNotes `tasksFolder` still points at the pre-reset `E - The Foundry/Tasks/Inbox`, so new tasks would land in a stray folder. `obsidian-git` is still listed in `community-plugins.json` though it must stay off. Work was done on a worktree branch, so it must be merged to `main` to appear in Obsidian.

### 2026-11-10 · Claude
- Did: Talked through aversion to seafood smell on Cyrus
- Decided: Keep seafood in his diet; handle the smell with soap-and-water cleanup, not menu changes
- Open / needs Dave: Ask Camille about Dave taking bath duty on seafood days

### 2026-11-07 · Claude Code (Devices moved)
- Did: Moved `Devices/` to `Atlas/Devices/`. `Device Registry.md` is now the folder note `Devices.md` (alias: Device Registry), linked from `Atlas/MOCs/MOCs.md`. The iPad mini is now Punknife (Cyberpunk 2077); Kepler R went back to the Name Pool. (The file moves landed in commit 2d4cdc0, mislabeled "Log Devices move".)
- Open / needs Dave: Replace the four Dataview queries in the registry with a plain table. Add Cyberpunk 2077 to the registry's franchise table. Jackson rename still pending. Cydonia, The Eye, Neon and Argos Extractors break the one-franchise-per-domain rule.

### 2026-11-07 · Claude Code (AI Instructions)
- Did: Added `x/AI Instructions.md`, a pasteable short version of the rules for AIs that can't read the vault. Linked it from `x/AGENTS.md`. Snapshotted Dave's `Devices/` folder.
- Decided: Dataview isn't used (Dave confirmed). The four queries in `Devices/Device Registry.md` still need replacing.
- Open / needs Dave: The "Right now" lines in AI Instructions copy [[Priorities]]; update them when Priorities changes. Devices integration still pending: Jackson rename, Name Pool row, where to link the registry, and four notes whose franchise breaks the registry's domain rule (Cydonia, The Eye, Neon, Argos Extractors).

### 2026-11-07 · Claude Code (Efforts index)
- Did: Filled in `Efforts/Efforts.md` and the four state folder notes with wikilinks to every current effort.
- Found: An untracked `Devices/` folder (Barrett, Codec, Frontier, Name Pool…) is at the vault root. Left it alone and uncommitted.
- Open / needs Dave: Where `Devices/` belongs (vault root should hold only ACE folders).

### 2026-11-07 · Claude Code (Project Minimize)
- Did: Started [[Project Minimize]] in `Efforts/Simmering/`: sell and give away as much as possible before the ~July 2027 move (Camille graduates).
- Decided: Stays Simmering until the Fall term ends; the main push starts Jan 2027. School catch-up is still #1.
- Open / needs Dave: Whether Camille is on board with the scope; what's definitely kept.

### 2026-11-04 · Claude Code (Codex CLI)
- Did: Installed the Codex CLI with Homebrew (`codex` 0.166.0). It was already signed in with Dave's ChatGPT account. A read-only test run worked. Added a Codex row to the agents table in `x/AGENTS.md` with the command to use.
- Decided: Claude Code triggers Codex read-only by default; write access only when Dave asks.

### 2026-11-04 · Claude Code (Gemini on hold)
- Decided: Gemini onboarding waits. Dave isn't sure Gemini CLI fits, since it has no remote-control access from his phone. The onboarding prompt is ready in the Nov 4 Claude Code session when he wants it.

### 2026-11-04 · ChatGPT Codex
- Did: Onboarded to Constellation; read the shared rules, priorities, recent agent work, Family North Star, and sampled the active vault and pre-reset archive.
- Decided: Top 3 fits are (1) school catch-up and learning coach, never quizzes/exams or submitted writing; (2) family-first daily priority and accountability partner; (3) technical/research release operator for *Only Talks 2 Ghosts* once the daily baseline is covered.
- Open / needs Dave: Nothing; Claude Code can include this log entry in its next commit.

### 2026-11-04 · Claude Code (instruction files moved)
- Did: At Dave's request, moved `AGENTS.md` and `GEMINI.md` into `x/`, and `CLAUDE.md` into `.claude/CLAUDE.md` (Claude Code reads it there; its import now points at `../x/AGENTS.md`). Updated paths in `x/AGENTS.md`, the vault agents, `/resume` and this log's header. The vault root now holds only folders.
- Open / needs Dave: ChatGPT on the laptop won't find `AGENTS.md` at the root anymore; tell it to read `x/AGENTS.md`. When Gemini CLI gets set up, check that it picks up `x/GEMINI.md`, or point its `context.fileName` setting there.

### 2026-11-04 · Claude Code (root cleanup 2)
- Did: Moved `Priorities.md` and `Agent Log.md` into `x/` and updated their paths in `AGENTS.md` and the three vault agents. Wikilinks like [[Priorities]] still work. Snapshotted Dave's edits (deleted the quick-capture test note, added `Calendar/Daily/202611041309 Daily Note.md`).
- Decided: `AGENTS.md`, `CLAUDE.md` and `GEMINI.md` stay at the root; the tools only read them there.
- Open / needs Dave: Templater folder templates still point at archived paths (Dave will fix later). The new daily note is named `202611041309 Daily Note`, not `2026-11-04`, so whatever made it isn't using the Periodic Notes format. An empty `A - The Observatory/Attachments/` folder is back at the root; something may be recreating it.

### 2026-11-04 · Claude Code (general note template)
- Did: Added `x/Templates/New Note Template.md`, a general template with empty properties (aliases, tags, type, status, related, created, modified). Keys copied from the archived New Note Template.
- Found: Templater's folder template for `/` still points at the archived `A - The Observatory/Documentation/Templates/New Note Template.md`, and another rule points at an old `E - The Foundry` path. Dave's quick-capture widget issue is solved.
- Open / needs Dave: Point Templater's `/` folder template at `x/Templates/New Note Template.md` (Templater settings → Folder templates) so every new note gets it.

### 2026-11-04 · Claude Code (creative workspace blueprint)
- Did: Saved the Stream Deck + / 8BitDo Micro / Procreate / Ableton setup guide to [[Creative Workspace Blueprint]] in `Atlas/Sources/`. Snapshotted Dave's `202611040928 Testing Quick capture.md`.
- Decided: Reference only, not a priority. School and the release come first.
- Open / needs Dave: The quick-capture test note landed at the vault root, so quick capture is likely pointed at root instead of `+ Inbox/`. Items marked [verify] in the guide need checking on the devices.

### 2026-11-04 · Claude Code (Obsidian Git notice again)
- Found: Obsidian Git wrote a second conflict notice at 08:05 on Nov 4. It listed files as "Not a file" (the ones we moved), so the travel laptop's own git copy is stuck mid-merge. Dave says Obsidian Git is now off there. Moved the notice to `.trash`.
- Open / needs Dave: If it comes back, Obsidian Git is still on somewhere (check the iPhone too).

### 2026-11-04 · Claude Code (folder notes)
- Did: Committed the 17 empty folder notes in the new ACE folders. Added a `CLAUDE.md` rule to keep folder notes.
- Decided: Dave wants folder notes. They'll become indexes, overviews and progress trackers for each folder.

### 2026-11-04 · Claude Code (Obsidian Git source)
- Found: The old Obsidian Git backups came from `Mixeds-MacBook-Pro-2` (git user "Dee"), which Dave says is his travel laptop. That's the likely source of the Nov 3 conflict notice. This computer is `Razorleaf`.
- Open / needs Dave: Turn off Obsidian Git on the travel laptop (Settings → Community plugins → toggle Obsidian Git off).

### 2026-11-04 · Claude Code (root cleanup)
- Did: Moved `BCC Fall 2026/` to `Efforts/On/` and `Being A Better Husband/` to `Efforts/Ongoing/`; its empty `Untitled.md` went to `.trash`. Moved the TaskNotes views and the stray .wav out of `A - The Observatory/` and `TaskNotes/` into `x/`, and archived [[Claude Chat Instructions]]. Pointed the TaskNotes plugin at `x/TaskNotes`, so it stops recreating root folders. Updated paths in `AGENTS.md`, `vault-reader` and `.claudeignore`.
- Found: At 22:54 on Nov 3, Obsidian Git on another device wrote `conflict-files-obsidian-git.md` to the root, so Obsidian Git is still on somewhere. I checked the moved TaskNotes views: none have conflict markers. The notice is now in `.trash`.
- Open / needs Dave: Something (likely Notebook Navigator or Folder Notes) made empty folder notes in every new folder on Nov 3 at 21:06, including `+ Inbox/+ Inbox.md` and `x/x.md`. They're uncommitted. Dave decides whether they go to `.trash`.

### 2026-11-04 · Claude Code (Templater folder)
- Did: Pointed Templater's templates folder at `x/Templates`.
- Open / needs Dave: Templater's folder templates still point at archived paths. They're off, so nothing breaks.

### 2026-11-04 · Claude Code (plugins back on)
- Did: Turned the community plugins back on at Dave's request: BRAT, Editing Toolbar, Folder Notes, Notebook Navigator, Omnisearch, Slash Commander, Periodic Notes, Slash Complete, TaskNotes and Templater. Obsidian Git stays off.
- Open / needs Dave: Templater's templates folder still points at the old `A - The Observatory/Documentation/Templates`. Its folder templates point at archived paths too, but run-on-file-creation is off, so they don't fire.

### 2026-11-04 · Claude Code (weekly + /evening paths)
- Did: Moved `Weekly Review Template.md` to `x/Templates/`, made `Calendar/Weekly/`, and pointed Periodic Notes' weekly notes at both. In `/evening`, fixed the daily note, template and North Star paths.
- Decided: Left the `/evening` steps that read `E - The Foundry/` (Tasks, Ongoing, Active) and the Exercise Routine path alone. They have no new home until `Efforts/` has notes.
- Open / needs Dave: Only item (3) is left: community plugins are off on this computer. Re-enabling them is Dave's call, and Obsidian Git must stay off.

### 2026-11-04 · Claude Code (Templates folder)
- Did: Pointed the Templates core plugin at `x/Templates` (`.obsidian/templates.json`).
- Open / needs Dave: Item (2) is done. Next is (3): community plugins are off on this computer.

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
