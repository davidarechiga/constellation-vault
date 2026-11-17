---
name: learn-capture
description: Capture hobbies, skills or tools Dave wants to learn (Blender, a new instrument, a language, a craft) into one list with an "only one Active" rule. Use when Dave runs "/learn", or says things like "I want to learn X", "I should get into X", "add X to my learn list", "I'm thinking about picking up X", or "I want to switch to X". Capture first, plan second.
version: 1.0.0
---

# Learn Capture

Dave sometimes hops from hobby to hobby with no structure. This skill gets each new "I want to learn X" onto one list and keeps only one thing Active at a time.

**Capturing is the job.** It should take one reply. Planning and lesson help happen only when he asks.

## Where it lives

One note: `Atlas/Notes/Skills To Learn.md` ([[Skills To Learn]]). Don't add folders, templates or per-skill notes. If the note is missing, recreate it from its own structure: sections **Active**, **Parked**, **Done or dropped**.

Entry format, one bullet each:

```markdown
- **Skill** · why · what I'd make · first step · date added
```

Skip fields Dave didn't give. Never invent them. Use `?` for a missing *what I'd make* or *first step*, since those are what make something ready to go Active.

## Workflow

1. **Check the clock.** Run `date` before writing the date added or talking about "tonight" or "this week".
2. **Capture it into Parked** by default. Reply with one line: what you added and where.
3. **Dedupe.** If it's already on the list, update that entry instead of adding another.
4. **Ask at most one question**, and only when it blocks the entry. Usually the useful one is "what's one small thing you'd want to make with it?"
5. **Switching check, one line max.** If Dave wants to make something **Active** while another is Active, name the current one and ask whether to park it (with where he stopped). If a top item in `x/Priorities.md` is overdue (school catch-up, family baseline, bed by 11pm), say so in one line and let him decide. Capturing never needs this check.
6. **Active needs three things:** a why, a what-I'd-make, and a first small step. If one is missing, help him fill it in before moving the entry.

## When Dave asks for more

Only on request:

- **Learning plan**: suggest a short path of small steps, each finishable in one sitting, ending in the thing he said he'd make. Add it under the entry, not in a new note.
- **Resources**: find a few well-regarded tutorials or courses with WebSearch and add links to the entry. Keep it to two or three.
- **Review** ("what's on my list"): show the Active one first, then Parked.
- **Drop or finish**: move the entry to **Done or dropped** with the date and where he stopped. Never delete it.

## Rules

- Never delete entries.
- Wikilinks `[[Note]]` for vault notes, normal links for the web. No Dataview.
- Don't create files at the vault root or new folders.
- A buildable project (an album, an app, a class he's enrolling in) belongs in `+ Inbox/` and then `Efforts/Simmering/`, not here. Say so in one line. A skill he wants for a project stays here.
- Don't log each capture in `x/Agent Log.md`. Log only when this skill itself changes.
- Commit rule: Claude Code commits the note change at the end of the session. Skill edits are committed and pushed in the same turn, following `x/AGENTS.md`.
