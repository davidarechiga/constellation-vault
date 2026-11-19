---
name: activity-capture
description: Capture an activity Dave wants to try, visit, save, or book. Use for outings, classes, shows, trips, restaurants, and similar experiences. Capture first; research or booking help only when requested.
version: 1.0.0
---

# Activity Capture

Dave runs into things he'd like to do (a class, a show, a trail, a restaurant, a day trip, a gear demo) and loses them. This skill gets each one onto a single list fast, then helps him decide and book when he's ready.

**Capturing is the job.** It should take one reply. Research and booking help only happen when he asks.

## Where it lives

One note: `Atlas/Notes/Activities To Try.md`. Don't add folders, templates, or per-activity notes. If the note is missing, create it from the skeleton below.

Skeleton:

```markdown
---
type: note
created: YYYY-MM-DD
tags: [activities, planning]
---

# Activities To Try

Things Dave wants to try or book. Captured with the activity-capture skill. Newest first inside each section.

## Booked
## Soon
## Ideas
## Done
```

Entry format, one bullet each:

```markdown
- [ ] **Name** · where · who with · cost · when/deadline · [link](url) · why it's interesting
```

Skip fields Dave didn't give. Never invent them. Use `?` only when a missing field matters, such as a deadline or a booking window.

Sections:
- **Ideas**: default for anything new.
- **Soon**: Dave says he wants to do it in the next few weeks, or it has a date or booking deadline coming up.
- **Booked**: confirmed. Put the date, time and confirmation info (never card numbers) in the entry.
- **Done**: finished. Add the date and one line on how it went, and whether he'd do it again. Move the entry, never delete it.

## Workflow

1. **Check the clock.** Run `date` before saying anything about "this weekend", "tomorrow" or a deadline. Convert relative dates Dave gives ("next Saturday") to absolute dates in the entry.
2. **Capture it.** Pull what you can from what Dave said or pasted (link, screenshot, text). Add it to **Ideas** (or **Soon** or **Booked** if he said so). Reply with one line: what you added and where.
3. **Dedupe.** If the note already has it, update that entry instead of adding a second one.
4. **Ask at most one question**, and only when a missing detail blocks the entry (for example, "what's the date?" for something he says is booked). Otherwise don't ask.
5. **Tag who it fits.** Dave has a wife (Camille), a baby (Cyrus, born Feb 22, 2026) and a dog (River). If an activity is clearly solo, couples, or Cyrus-friendly, say so in the "who with" field. If it's unclear and matters (a late-night show, a long hike), note `Cyrus?` rather than guessing.
6. **Drift check, one line max.** Read `x/Priorities.md`. If Dave wants to *book* something that competes with a top priority (school catch-up, family baseline, being in bed by 11pm), name that in one line and let him decide. Capturing never needs this; it's always fine to write an idea down.

## When Dave asks for more

Only do these on request:

- **Research** ("what does it cost", "when is it open"): use WebSearch or WebFetch, add the facts and the source link to the entry. Keep it short.
- **Compare or pick** ("what should we do this weekend"): read the list, filter by who's available and the budget, and recommend one, not a menu. Say what it costs in time against school and family.
- **Booking help**: find the booking page or phone number, summarize the options and total cost, and give Dave the link. **Never book, pay, enter payment details, create accounts, or send messages for him.** Draft any email or message and let him send it. When he says it's booked, move the entry to **Booked** with the details.
- **Calendar**: offer to add a booked item to his calendar or today's daily note. Create the event only after he says yes.
- **Review** ("what's on my list"): list **Booked** and **Soon** first, then a couple of **Ideas**. Don't recite everything.

## Rules

- Never delete entries. Move finished ones to **Done**.
- Wikilinks `[[Note]]` for vault notes, normal links for the web. No Dataview.
- Don't create files at the vault root or new folders.
- If something Dave pastes is really a project idea (a build, a release, a class he's enrolling in), it belongs in `+ Inbox/` and then `Efforts/Simmering/`, not here. Say so in one line.
- Don't log each capture in `x/Agent Log.md`. Log only when this skill itself changes.
- Git ownership follows `x/AGENTS.md`: Claude Code owns routine commits; another agent uses git only when Dave explicitly requests it in that session.
