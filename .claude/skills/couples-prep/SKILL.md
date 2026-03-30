---
name: couples-prep
description: Use this skill when the user runs "/couples-prep" or asks to prepare for couples therapy, a couples session, or wants to know what to bring up with Camille in therapy. Scans journals for relationship dynamics and the Camille ongoing area, then writes a structured prep note with appreciations and talking points.
version: 1.0.0
allowed-tools: [Read, Glob, Grep, Bash, Write, Edit]
---

# Couples Therapy Prep Skill

You are a thoughtful personal assistant helping David prepare for a couples therapy session with Camille. When this skill is invoked, you autonomously gather relationship context from the vault, synthesize appreciations and meaningful talking points, and write a prep note — no questions asked.

## Vault Root
`/Users/davidarechiga/Constellation/Constellation/`

## Output Path
`A - The Observatory/🌟 Lifestyle & Personal/Therapy/Therapy Prep/Couples Therapy Prep [YYYY-MM-DD].md`

---

## Step 1: Determine Today's Date
Use today's date in `YYYY-MM-DD` format for file naming and date calculations.

## Step 2: Read Journal Entries (Last 14 Days)
Use Glob to find daily notes in `C - Signal Relay/Daily/` for the past 14 days. For each note, read and extract:
- The **Journal** section — look specifically for mentions of Camille, relationship moments, shared experiences, conflicts, decisions made together, times David felt connected or disconnected
- Emotional tone around the relationship: appreciation, frustration, longing, gratitude, tension
- Specific moments worth naming in therapy (both positive and growth-oriented)

If a daily note has no Journal section or is blank, skip it.

## Step 3: Read the Camille Ongoing Area
Read the hub/folder note in `E - The Foundry/Ongoing/2 🥰 Camille/`. Note:
- Relationship goals, shared projects, ongoing concerns
- Any recurring themes or patterns flagged in the notes
- Upcoming milestones, decisions, or areas needing attention

Also read any sub-notes in that folder that seem relevant to the current relationship state.

## Step 4: Scan Relationship Tasks
Glob `E - The Foundry/Tasks/**/*.md`. Collect tasks where:
- `tags` includes `camille` OR `relationship`
- `status: open` or `status: in-progress`

Note: overdue or high-priority relationship tasks may indicate areas of friction or neglect worth naming.

## Step 5: Synthesize Appreciations and Talking Points

### Appreciations (3 items)
Pull out **specific, concrete moments or qualities** from the past 2 weeks to appreciate. These should be:
- Named moments from journal entries ("The walk we took on Tuesday")
- Qualities Camille demonstrated that stood out
- Times David felt supported, loved, or connected
Do not write generic appreciations like "she's supportive" — ground them in real observed moments.

### Growth Areas / Talking Points (3 items)
Identify **specific patterns, unresolved tensions, or things to work through together**:
1. What keeps coming up in journals as friction or disconnection?
2. Are there relationship tasks that are stuck or overdue, suggesting something isn't getting addressed?
3. Are there shared decisions or life areas where alignment is needed?
4. What's one thing David wants Camille to understand, or wants to understand about Camille?

Be honest but constructive. The goal is productive therapy conversation, not complaint.

## Step 6: Write Prep Note

Write a prep note to:
`A - The Observatory/🌟 Lifestyle & Personal/Therapy/Therapy Prep/Couples Therapy Prep [YYYY-MM-DD].md`

Use this format exactly:

```markdown
---
tags:
  - therapy
  - couples
  - camille
date: YYYY-MM-DD
---

# Couples Therapy Prep — [Day, Month DD, YYYY]

## Appreciations
- [Specific moment or quality — name it concretely]
- [Second appreciation]
- [Third appreciation]

## Growth Areas / Talking Points
1. [Most important pattern or tension to address]
2. [Second growth area]
3. [Third point — question, alignment need, or thing to understand]

## Recent Patterns (from journals)
[2–3 sentences on relationship dynamics observed in recent journal entries. Be specific about themes, not just "there were some rough moments".]

## Open Tasks Together
[Any shared tasks or Camille-area items worth flagging for context — e.g., decisions pending, things promised but not done.]
```

Only include sections that have real content.

## Step 7: Print Terminal Summary

After writing the note, print:

```
💑 Couples Therapy Prep — [Day, Date]

📋 Prep note written: A - The Observatory/🌟 Lifestyle & Personal/Therapy/Therapy Prep/Couples Therapy Prep [date].md

💛 Appreciations:
  - [Appreciation 1]
  - [Appreciation 2]
  - [Appreciation 3]

💬 Talking Points:
  1. [Point 1]
  2. [Point 2]
  3. [Point 3]

📊 Key pattern: [1-liner on the dominant relationship dynamic observed this period]
```
