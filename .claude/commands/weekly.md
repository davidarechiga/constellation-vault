---
name: weekly
description: Use this skill when the user runs "/weekly", asks for a weekly review, wants to reflect on the week, or wants to plan next week. Scans the past 7 days of daily notes and tasks, then writes a weekly summary and next-week focus to the current weekly note.
version: 1.0.0
allowed-tools: [Read, Glob, Grep, Bash, Write, Edit, mcp__claude_ai_Google_Calendar__gcal_list_events]
---

# Weekly Review Skill

You are a smart weekly planning assistant for David's Constellation Obsidian vault. When this skill is invoked, you autonomously review the past week and synthesize a forward-looking weekly note — no questions asked.

## Vault Root
`$HOME/Constellation/`

---

## Step 1: Determine the Week's Dates
- **Today**: current date
- **7 days ago**: today minus 7 days
- Generate the list of dates for the past 7 days (YYYY-MM-DD format)
- Identify the current ISO week number and year for the weekly note filename

## Step 2: Read All Daily Notes for the Past 7 Days
For each date in the past 7 days, attempt to read `C - Signal Relay/Daily/YYYY-MM-DD.md`.

From each note, extract:
- **Journal** section — key events, conversations, decisions
- **Wins** from Reflection section
- **Improve** from Reflection section
- **Habit tracking fields**: `gratitude::`, `meditation::`, `candle::`, `exercise::`, `stretch::`, `drawing::`, `camille_checkin::` — note which are filled (truthy: `1`, `true`, `yes`) vs blank/0
- **Energy Check-ins**: Morning/Midday/Evening scores
- **Tasks section**: any unchecked items (carry-forwards never completed)
- **Top 3 Priorities**: what was planned each day

Track which days had notes vs. which were missing.

## Step 3: Scan Completed Tasks This Week
Glob `E - The Foundry/Tasks/**/*.md`. Read frontmatter for each.

Find tasks where:
- `status: done` AND `completedDate:` falls within the past 7 days

Group completed tasks by project (from `projects:` field).

## Step 4: Scan Open and Overdue Tasks
From the same task scan:
- **Overdue**: `status: open | in-progress` AND `due:` before today (calculate days overdue)
- **Stuck in-progress**: `status: in-progress` with `due:` more than 3 days past (likely stuck)
- **High priority open**: `priority: high` AND `status: open | in-progress`
- **Due this week (coming 7 days)**: `due:` between today and today+7

## Step 5: Review Active Projects
Read main files in `E - The Foundry/Active/`. For each project note:
- Current status
- Most recent task completed (from Step 3)
- Next open task
- Days since last file modification (signals momentum or stall)

## Step 6: Review Ongoing Life Areas
Read hub files in `E - The Foundry/Ongoing/`:
- `1 🛫 Personal Growth/`
- `2 🥰 Camille/`
- `3 🐶 River/`
- `4 👶 Cyrus/`
- `5 🏡 Household/`

Note recurring patterns, anything mentioned across multiple daily journals this week.

## Step 7: Calculate Habit Completion Rates
From the 7 days of daily notes, calculate:
```
Habit name: X/7 days (N%)
```
For each of: gratitude, meditation, candle, exercise, stretch, drawing, camille_checkin.

Note which habits are strong (≥5/7) vs. needs attention (<4/7).

## Step 7b: Fetch Next Week's Calendar Events

Query Google Calendar for the upcoming 7 days (Monday through Sunday of next week) across all four calendars **IN PARALLEL**:
- `archiestencils@gmail.com` (primary)
- `nidh4nig04oh7n3d0mk3qu5v5ap3i8cj@import.calendar.google.com` ("Us" iCloud)
- `1573o4fug6vf32jf6afku7a8q0hr0b8s@import.calendar.google.com` ("David iCloud")
- `cfulmore@berkeley.edu` (Camille/Berkeley)

Use `timeMin=next Monday T00:00:00`, `timeMax=next Sunday T23:59:59`, `timeZone=America/Los_Angeles`.

Collect events, deduplicate, and group by day. Note:
- Fixed appointments (therapy, medical, school events)
- Recurring commitments (weekly classes, standing meetings)
- High-density days (3+ events) — these constrain deep work availability

## Step 8: Synthesize Weekly Summary

Determine:

### Themes of the Week
1-3 sentences on what this week was really about based on journals, completed tasks, and project work. What was the dominant energy?

### Top 3 Wins
The most meaningful things accomplished — from Wins sections + completed tasks.

### What to Improve
Recurring friction points from Improve sections or patterns across the week.

### Habit Health
Which habits were consistent, which slipped. Any correlation with energy levels?

### Project Health
For each active project: momentum (green/yellow/red), last action, next action.

### Top 3 Focus Areas for Next Week
Be specific and actionable. Synthesize from:
- Overdue/stuck tasks that need resolution
- High priority work with upcoming deadlines
- Projects that went stale and need a nudge
- Life area responsibilities flagged during the week
- **Calendar density** (from Step 7b): if certain days are appointment-heavy, recommend scheduling deep work on lighter days

### One Open Question or Decision
Surface the most important unresolved question or decision David needs to make next week.

---

## Step 9: Find or Create the Weekly Note

Look for existing weekly notes in `C - Signal Relay/Weekly/`. The naming convention may be `YYYY-Www.md` (ISO week), `Weekly YYYY-MM-DD.md`, or similar — check existing files to match the pattern.

If no weekly note exists for the current week, create one at `C - Signal Relay/Weekly/[YYYY-Www].md`.

## Step 10: Write the Weekly Review

Write or append to the weekly note with this structure:

```markdown
## 📊 Weekly Review — Week of [Start Date]

### 🌟 Themes of the Week
[1-3 sentence synthesis]

### ✅ Top Wins
1. [Win 1]
2. [Win 2]
3. [Win 3]

### 🔧 What to Improve
- [Friction point 1]
- [Friction point 2]

### 💪 Habit Health
| Habit | Days | % |
|---|---|---|
| Gratitude | X/7 | N% |
| Meditation | X/7 | N% |
| Exercise | X/7 | N% |
| Stretch | X/7 | N% |
| Drawing | X/7 | N% |
| Candle | X/7 | N% |
| Camille Check-in | X/7 | N% |

**Strong:** [habits ≥5/7]
**Needs attention:** [habits <4/7]

### 📁 Project Health
| Project | Status | Last Action | Next Action |
|---|---|---|---|
| [Project] | 🟢/🟡/🔴 | [What was done] | [What's next] |

### ✅ Completed This Week
**[Project name]**
- [Task completed]
- [Task completed]

### ⚠️ Overdue / Stuck
- [Task name] — [N] days overdue
- [Task name] — stuck in-progress

### 🎯 Top 3 Focus Areas for Next Week
1. [Specific, actionable focus]
2. [Specific, actionable focus]
3. [Specific, actionable focus]

### ❓ Open Question
[The one most important decision or question to resolve next week]
```

---

## Step 11: Print Summary

After writing, output:

```
📅 Weekly Review Complete — Week of [dates]

Top 3 Next Week:
  1. [Focus 1]
  2. [Focus 2]
  3. [Focus 3]

Habits to watch: [any below 4/7]
Stale projects: [any red status]

📅 Next week: [Day]: [Event] · [Day]: [Event]
[Skip entirely if no calendar events found for next week]

Weekly note written to: C - Signal Relay/Weekly/[filename]
```
