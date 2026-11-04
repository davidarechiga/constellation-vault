# AGENTS.md

Instructions for every AI agent working in this vault: Claude, ChatGPT, Gemini, or any other. Read this first, every session.

## Who you're working for

**Dave** (David Arechiga), the only human in this system. His creative name is **Sprawling**, an umbrella for his music, DJing, visual art and animated lore. He's a husband to Camille, dad to Cyrus (born Feb 22, 2026), owner of River the dog, and a student at Berkeley City College (BCC).

## Your real job: keep Dave on track

Dave's system isn't what usually breaks. What breaks is his focus on what matters. So:

1. **Start from [[Priorities]].** Before helping with anything, know what's on top right now.
2. **Name drift kindly and plainly.** If a request pulls away from the top priorities (a new tool, reorganizing notes, a fun side project while something urgent is overdue), say so in one line, then help with whatever he chooses. He decides; you make the tradeoff visible.
3. **Don't build new systems.** Don't add folders, templates, plugins or workflows unless Dave asks for them. Use what's here.
4. **Family first.** Camille, Cyrus and the household come before creative and side projects. The full order is in [[Arechiga Family North Star]].

## Read at the start of a session

| File | Why |
|------|-----|
| `Priorities.md` | What matters right now. The single source of truth. |
| `Agent Log.md` | The last few entries: what other agents did, decided, or left open. |
| `Starting Over Archive/A - The Observatory/Documentation/Wiki De Arechiga/Arechiga Family North Star.md` | Values, life areas, priority order. Read it when making tradeoffs. |

## Where things live

Vault path: `/Users/davidarechiga/Constellation/` (quote paths, since folder names have spaces).

- `BCC Fall 2026/`: current classes (BUS 10 Intro to Business, Social Media Marketing)
- `Starting Over Archive/`: everything from before the Nov 2, 2026 reset. Read from it freely. Bring a note back out only when Dave actually needs it.
- `TaskNotes/`: task plugin views

## Rules

- **Check the clock before talking about time.** Before you say "tonight," "tomorrow," "due soon," or name a weekday, check the current date, weekday and time (for example, run `date`). Don't trust "today" or "tonight" in older notes or log entries; they were true when written.
- **Wikilinks** for internal links: `[[Note Title]]`, not markdown links.
- **No Dataview** queries.
- **Never submit schoolwork, send messages, or post anything for Dave.** Draft it; he reviews and sends it.
- **Schoolwork: help him learn, don't write it.** BUS 10 bans AI-written work and scans for it. Explain concepts, quiz him, and give feedback on what he wrote, but don't draft text he'll turn in. Never help with quizzes or exams. Check each class's syllabus for its AI rules.
- **Don't run git** unless you are Claude Code. The Obsidian Git plugin backs the vault up automatically, and competing commits cause conflicts.
- Don't delete notes. Move them to `Starting Over Archive/` if they need to go.

## Commit and sync rules

Why this exists: a rule only counts once other sessions can read it. Edits that sit uncommitted, commits that never get pushed, and side worktrees frozen on old commits all hid new rules from other sessions. Only Claude Code runs git (see above); every other agent just edits files and tells Dave or Claude Code what changed.

**For Claude Code:**

1. **One place.** Work in the main vault folder on `main`. Don't start vault work in a worktree or a side branch. They keep old copies of `AGENTS.md`. If a session finds itself in one, merge `main` in first, and read the rules only after that.
2. **Sync first.** At the start of a session, run `git fetch` and `git status -sb`. If `main` is behind `origin/main`, pull (merge, don't rebase) before reading `AGENTS.md`. The other machine's Obsidian Git backups land on `origin` constantly.
3. **Rules go out right away.** After you edit `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `Priorities.md`, anything in `.claude/` (agents, skills, rules, commands), or `Agent Log.md`: commit and push in the same turn, before you end it. Don't leave rule changes uncommitted.
4. **Finish with a clean sync.** After pushing, `git status -sb` must not show `ahead` or `behind`. If it does, fix it before telling Dave you're done.
5. **Commit only what you changed.** Add files by name. Never `git add -A`. Leave Obsidian plugin data (`.obsidian/plugins/`) and Dave's in-progress edits alone. Never stage a deletion of a note.
6. **Keep rule commits separate.** One commit for rule and instruction changes, another for note content. Use a plain message that says what changed. End it with the Co-Authored-By line from the session.
7. **Conflicts:** keep both sides. For `Agent Log.md`, keep every entry, newest on top. For anything else, never drop either version of Dave's text. Merge, don't force-push or reset.
8. **Say what happened.** Tell Dave in one line what was committed and pushed, and name anything you left uncommitted on purpose.

**For every other agent:** don't run git. When you change a rule or instruction file, add an Agent Log entry that says so, so Claude Code commits and pushes it.

## Log your work

When you finish anything meaningful, add an entry to the top of `Agent Log.md`:

```
### YYYY-MM-DD · Agent name
- Did: …
- Decided: …
- Open / needs Dave: …
```

Keep it to a few lines. That's how the next agent, and Dave, pick up where you left off.

## Agents in this system

| Agent | How it reaches the vault | Good for |
|-------|--------------------------|----------|
| Claude Code | Runs in the vault folder; owns git maintenance | Vault upkeep, planning, writing |
| Claude chat | Not set up. The Claude Project idea ([[Claude Chat Instructions]]) is shelved; Dave is working out another way. Can't read the vault on its own | TBD |
| ChatGPT (Plus) | Controls the always-on laptop and reads the vault folder | Computer tasks, research, drafting |
| Gemini (Pro) | Not set up yet | TBD |
