---
name: resume
description: Load session context at the start of a new conversation. Reads CLAUDE.md for permanent vault memory and recent entries from the Session Log. Use when the user runs "/resume", starts a new session, or says "catch me up" / "what were we working on". Supports optional args: number of sessions (e.g. /resume 5) and/or topic filter (e.g. /resume auth, /resume 5 career).
version: 1.0.0
allowed-tools: [Read, Glob, Grep, Bash]
argument-hint: "[N] [topic]"
---

# Resume Skill

Load context from the vault's permanent memory and recent session history so you can pick up where you left off without re-explaining the project.

## Vault Root
`$HOME/Constellation/`

## Arguments (all optional)
- **N** — number of recent session entries to load (default: 3)
- **topic** — keyword to search for in session history (e.g. "career", "auth", "frmwrk")
- Combined: `/resume 5 career` → last 5 entries + search for "career"

---

## Step 1: Parse Arguments
From the user's input after `/resume`:
- If a number is present, use it as N (default 3)
- If a word/phrase is present (not a number), use it as the topic filter
- Both can be combined

## Step 2: Read Permanent Memory (CLAUDE.md)
Read `$HOME/Constellation/CLAUDE.md`.

Extract and hold in working memory:
- Vault structure overview (ACE method, folder purposes)
- Core rules (wikilinks-only, no Dataview, TaskNotes system)
- Any "Permanent Learnings" or "Decisions" sections if present
- Active project names and current focus areas

This is the stable foundation — always load it.

## Step 3: Read Recent Session Log Entries
Read `C - Signal Relay/Session Log.md`.

The log contains entries in reverse-chronological order, each formatted as:
```
### YYYY-MM-DD HH:MM — [topic summary]
**Summary:** [1-sentence summary]
**Files:** [[Note 1]], [[Note 2]]
```

Extract the **last N entries** (most recent first).

If a **topic filter** was provided, also grep the file for that keyword and include any matching entries not already in the last N.

## Step 4: Synthesize Context Summary

Output a concise briefing:

```
🔄 Session Context Loaded — [today's date]

📋 Vault: Constellation (ACE method — Atlas/Calendar/Efforts)
[1-2 lines on any permanent decisions or rules worth flagging]

🕐 Recent Sessions:
  [Date] — [Topic]: [1-line summary of what was done]
  [Date] — [Topic]: [1-line summary]
  [Date] — [Topic]: [1-line summary]
  [... up to N entries]

[If topic filter matched additional entries:]
🔍 Matching "[topic]":
  [Date] — [relevant entry summary]

📌 Last open action: [most recent "Next:" item from session log, if any]
```

Keep the output scannable — this is a quick orientation, not a full report.

## Step 5: Offer Next Steps
End with a single line: "Ready — what are we working on today?" or surface the last open action if one was found.

## Notes
- If `Session Log.md` doesn't exist yet, just load CLAUDE.md and note that no session history exists
- Don't read individual vault notes during resume — this is a lightweight context load only
- If N > 10, cap at 10 to avoid flooding context
