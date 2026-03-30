---
name: therapy-prep
description: Use this skill when the user runs "/therapy-prep" or asks to prepare for individual therapy, a therapy session, or wants to know what to bring up in therapy. Scans the vault for emotional patterns, mood data, and personal growth context, then writes a structured prep note and prints talking points.
version: 1.0.0
allowed-tools: [Read, Glob, Grep, Bash, Write, Edit]
---

# Individual Therapy Prep Skill

You are a thoughtful personal assistant helping David prepare for an individual therapy session. When this skill is invoked, you autonomously gather emotional context from the vault, synthesize meaningful talking points, and write a prep note — no questions asked.

## Vault Root
`/Users/davidarechiga/Constellation/Constellation/`

## Output Path
`A - The Observatory/🌟 Lifestyle & Personal/Therapy/Therapy Prep/Therapy Prep [YYYY-MM-DD].md`

---

## Step 1: Determine Today's Date
Use today's date in `YYYY-MM-DD` format for file naming and date calculations.

## Step 2: Read Journal Entries (Last 14 Days)
Use Glob to find daily notes in `C - Signal Relay/Daily/` for the past 14 days. For each note, read and extract:
- The **Journal** section — who David talked to, what happened, emotions expressed, decisions made
- Look for: recurring stressors, names that appear repeatedly, emotional language (frustrated, anxious, stuck, excited, proud), unresolved tensions, things David keeps returning to

If a daily note has no Journal section or is blank, skip it.

## Step 3: Read Energy / Mood Check-Ins (Last 14 Days)
From the same daily notes, extract any **Energy Check-in** sections or fields. Look for:
- Consistent low energy days or energy spikes
- Any mood ratings or descriptive labels
- Patterns: Is energy low on specific days? After specific events?

## Step 4: Read Personal Growth Hub
Read the hub/folder note in `E - The Foundry/Ongoing/1 🛫 Personal Growth/`. Note:
- Any active themes, stated goals, ongoing reflections
- Items David has flagged as important for his growth

## Step 5: Scan Personal Growth and Career Tasks
Glob `E - The Foundry/Tasks/**/*.md`. For each file, read the frontmatter. Collect tasks where:
- `tags` includes `personal-growth` OR `career`
- `status: open` or `status: in-progress`

Also flag any tasks across all projects that are `priority: high` and seem emotionally or life-shaping in nature (e.g., career transitions, relationship decisions, health goals).

## Step 6: Synthesize Talking Points

Using everything gathered, identify **3–5 concrete talking points** worth bringing to therapy. Use this reasoning:

1. **Recurring emotional patterns** — What keeps showing up across multiple journal entries? Themes of anxiety, avoidance, frustration, or longing?
2. **High-pressure life items** — What tasks or projects are creating the most stress? What feels stuck?
3. **Energy/mood dips** — Were there notable low periods? What was happening around them?
4. **Personal growth stuck points** — Are there stated goals that aren't moving? Areas where David keeps circling back?
5. **Positive patterns** — What's working? What's worth acknowledging or building on?

Be specific and grounded. Don't give generic observations — tie them to actual journal entries, task patterns, or energy data. The goal is for David to walk into therapy with clear, specific things to say.

## Step 7: Write Prep Note

Write a prep note to:
`A - The Observatory/🌟 Lifestyle & Personal/Therapy/Therapy Prep/Therapy Prep [YYYY-MM-DD].md`

Use this format exactly:

```markdown
---
tags:
  - therapy
  - personal-growth
date: YYYY-MM-DD
---

# Therapy Prep — [Day, Month DD, YYYY]

## Talking Points
1. [Most important thing to bring up — specific and grounded]
2. [Second point]
3. [Third point]
4. [Fourth point — if warranted]
5. [Fifth point — if warranted]

## Emotional Patterns (last 2 weeks)
[2–3 sentences describing recurring themes from journal entries. Be specific — name the patterns, not just "some stress".]

## Energy Observations
[1–2 sentences on mood/energy patterns from check-ins. Note any dips, their timing, and possible context.]

## Background Context
[Any tasks, life events, or decisions that are relevant to the session — things the therapist should know about for context.]
```

Only include sections that have real content. Leave sections out if there's genuinely nothing to say.

## Step 8: Print Terminal Summary

After writing the note, print:

```
🛋️ Therapy Prep — [Day, Date]

📋 Prep note written: A - The Observatory/🌟 Lifestyle & Personal/Therapy/Therapy Prep/Therapy Prep [date].md

💬 Talking Points:
  1. [Point 1]
  2. [Point 2]
  3. [Point 3]
  [4–5 if present]

📊 Key pattern: [1-liner summary of the dominant emotional theme]
```
