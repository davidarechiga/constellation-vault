---
name: session-persist
description: Save session learnings to the vault — writes a session summary to today's daily note and promotes durable insights to memory files. Use when the user says "save session", "log what we did", "capture this session", or at natural end-of-conversation checkpoints.
version: 1.0.0
---

# Session Persist Skill

## Purpose

Capture what happened in this Claude Code session before context is lost. Writes a human-readable summary to today's daily note and promotes any durable learnings (decisions, patterns, corrections) to the appropriate memory files.

## Workflow

### Step 1 — Identify today's daily note
- Path: `C - Signal Relay/Daily/YYYY-MM-DD.md` (use today's date)
- If it doesn't exist, create it with the standard daily note structure

### Step 2 — Summarize the session
Collect from this conversation:
- **What was worked on** (files created/modified, tasks completed, topics discussed)
- **Decisions made** (any architectural or system choices)
- **Patterns or corrections** (if David corrected an approach, note what was wrong and what was right)
- **Files touched** (wikilinks to key notes created or significantly modified)

### Step 3 — Write session entry to Session Log
Append to `C - Signal Relay/Session Log.md` (create if missing with `# Session Log` header):

```markdown
### YYYY-MM-DD HH:MM — [1-line topic summary]
**Worked on:** [bullet list of what was done]
**Files touched:** [[Note 1]], [[Note 2]]
**Decisions:** [any choices made and why]
**Next:** [clear next action if any was identified]
```

### Step 4 — Promote durable learnings to memory
For each learning, route to the correct memory file:

| Learning type | Memory file |
|---------------|-------------|
| Correction to Claude's behavior | `memory/feedback.md` (create if missing) |
| Architectural or system decision | `memory/decisions.md` |
| New project status or blocker | `memory/current-work.md` |
| New fact about David's context | `memory/vault-overview.md` |

Only promote things that will be useful in **future sessions** — not ephemeral task details.

### Step 5 — Output summary
Tell David:
- Where the session log was written (wikilink to daily note)
- What (if anything) was promoted to memory files and why

## When NOT to create entries
- Don't log sessions that were purely Q&A with no vault changes
- Don't promote corrections that were already in memory
- Keep session log entries brief — 5–8 bullet points max
