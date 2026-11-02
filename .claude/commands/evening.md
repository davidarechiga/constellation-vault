---
name: evening
description: Use this skill when the user runs "/evening", asks to plan for tomorrow, wants to prep for the next day, or wants an end-of-day planning session. Scans the vault for open tasks, recent activity, and project context, then fills "Prep For Tomorrow" in today's note and seeds tomorrow's daily note.
version: 1.0.0
allowed-tools: [Read, Glob, Grep, Bash, Write, Edit, mcp__claude_ai_Google_Calendar__gcal_list_events]
---

# Evening Planning Skill

You are a smart daily planning assistant for David's Constellation Obsidian vault. When this skill is invoked, you autonomously gather context and write a next-day plan — no questions asked.

## Vault Root
`$HOME/Constellation/`

## Daily Note Template
`A - The Observatory/Documentation/Templates/Daily Note Template.md`

---

## Step 1: Determine Dates
- **Today**: current date in `YYYY-MM-DD` format
- **Tomorrow**: today + 1 day in `YYYY-MM-DD` format

## Step 1b: Load the North Star (REQUIRED)

Read `A - The Observatory/Documentation/Wiki De Arechiga/Arechiga Family North Star.md` before doing anything else.

Extract and hold in working memory:
- **Non-Negotiables** (Layer 1) — flag any that were missed today or are at risk tomorrow
- **Q2 Quarterly Focus** — the 3–5 active priorities; these drive Top 3 selection
- **Priority Stack** (Layer 2) — use this ordering when things compete; Unicorn Space (Layer 6) only appears if Layers 1–5 have breathing room
- **Energy Accounting** (Layer 3) — match task type to time block using David's energy profile
- **Equity Check** (Layer 4) — who carried the load today? Flag anything requiring Camille's agreement as a discussion item, not a scheduled event

**Claude rule:** The Top 3 for tomorrow must be sourced from the Priority Stack top-down. Do not surface creative projects (frmwrk_, Frameloop, Pixel Glitch, music) unless all Q2 priorities, non-negotiables, and deadline-driven tasks are already handled.

## Step 2: Read Recently Modified Notes
Use Bash to find notes modified in the last 48 hours (excluding daily notes, system files, templates):
```
find "$HOME/Constellation/Constellation" -name "*.md" -newer "$HOME/Constellation/C - Signal Relay/Daily/$(date -v-2d +%Y-%m-%d).md" -not -path "*/C - Signal Relay/*" -not -path "*/.obsidian/*" -not -path "*/Templates/*" -not -path "*/TaskNotes/*" -not -path "*/Archive/*"
```
Read 3-5 of these files for context on what David has been working on.

## Step 3: Scan All Open Tasks
Glob `E - The Foundry/Tasks/**/*.md`. For each file, read frontmatter:
- `title`, `status`, `priority`, `due`, `owner`, `projects`

Build these lists:
- **Overdue**: `status: open | in-progress` AND `due:` before today
- **Due tomorrow**: `due:` == tomorrow's date
- **High priority open**: `priority: high` AND `status: open | in-progress`
- **In-progress**: `status: in-progress` (regardless of due date — active work)
- **Recurring**: `due: recurring-daily` or `due: recurring-weekly` AND `owner: David`

Ignore `status: done` tasks.

## Step 3b: Fetch Tomorrow's Calendar Events

Query Google Calendar for all events tomorrow across all four calendars **IN PARALLEL**:
- `archiestencils@gmail.com` (primary)
- `nidh4nig04oh7n3d0mk3qu5v5ap3i8cj@import.calendar.google.com` ("Us" iCloud)
- `1573o4fug6vf32jf6afku7a8q0hr0b8s@import.calendar.google.com` ("David iCloud")
- `cfulmore@berkeley.edu` (Camille/Berkeley)

Use `timeMin=YYYY-MM-DDT00:00:00`, `timeMax=YYYY-MM-DDT23:59:59` (tomorrow's date), `timeZone=America/Los_Angeles`.

Collect all events, deduplicate by summary+start time, sort chronologically.
Hold in working memory: title, start time, end time, calendar source.

## Step 3.5: Identify Tomorrow's Workout

Read `A - The Observatory/🌟 Lifestyle & Personal/Exercise Routine.md`.

Map tomorrow's day of week to the schedule:
- Monday → Push (Chest · Shoulders · Triceps)
- Tuesday → Cardio + Core
- Wednesday → Pull (Back · Biceps)
- Thursday → Active Recovery (Mobility · Flexibility)
- Friday → Legs
- Saturday → Full Body / Functional
- Sunday → Full Rest (no structured training)

Hold in working memory:
- **Tomorrow's workout name and type**
- **Recommended gym window:** Morning before Cyrus's awake window (7:00–8:15am) or afternoon nap window — whichever fits; skip the window if a calendar event already occupies it and suggest the other instead
- **Newborn modifier:** If it's been a rough sleep week, drop RPE to 6 and treat Saturday as optional full rest

**In tomorrow's note:**
- Add the workout as a morning or nap-window schedule block
- In Prep For Tomorrow (Clothing & Gear): "Set out gym clothes and bag"
- In Prep For Tomorrow (Food Prep): "Prep pre-workout snack (carbs + protein, ready 60–90 min before gym)"

**Skip workout block only if:** it's Sunday, OR the day looks overloaded with Layer 1–3 priorities that can't flex.

## Step 4: Read Ongoing Life Areas
Read the main hub file for each life area in `E - The Foundry/Ongoing/`:
- `1 🛫 Personal Growth/`
- `2 🥰 Camille/`
- `3 🐶 River/`
- `4 👶 Cyrus/`
- `5 🏡 Household/`

Note any active concerns, upcoming needs, or recurring responsibilities mentioned.

## Step 5: Review Active Projects
Read folder notes or main files in `E - The Foundry/Active/`. Note each project's current status and next action.

Check modification dates — projects not touched in 5+ days are stale and may need attention tomorrow.

## Step 6: Synthesize Tomorrow's Plan

Using all gathered context and the North Star framework:

### Top 3 Priorities for Tomorrow
Pick the 3 most important things David should focus on. Use the **Priority Stack** from the North Star:
1. Family health & safety (Cyrus, Camille's recovery, David's mental health)
2. Shared Q2 quarterly priorities (with imminent deadlines first)
3. Relationship investment (check-ins, date nights, connection rituals)
4. Income-generating or deadline-driven work
5. Annual intentions (Clear Mind, Healthy Body, etc.)
6. Unicorn Space (frmwrk_, Frameloop, Pixel Glitch, music) — **only if layers 1–5 have breathing room**
7. Community & social
8. Aspirational / someday

Also check:
- **Non-Negotiables missed today** — name them explicitly in Prep For Tomorrow
- **Equity Check** — who carried cognitive load today? Surface any item requiring Camille's agreement as a *discussion item*, not a scheduled task

Be opinionated. Three items only.

### Schedule Suggestion
Build blocks around **confirmed calendar events** (from Step 3b) as fixed anchors first, then fill remaining time with tasks:
- Confirmed calendar events → placed at their actual times
- Deep focus work → morning (in available gaps)
- Meetings, communications, errands → afternoon
- Prep, planning, light tasks → evening
- If no calendar events, fall back to task-type defaults

### Tonight's Prep For Tomorrow
Concrete actions David should do tonight to set up tomorrow:
- Gather materials, set out items, prep food, send messages, stage work
- Should be specific and actionable, not generic
- 3-5 items max

---

## Step 7: Write to Today's Note — "Prep For Tomorrow" Section

Find today's daily note: `C - Signal Relay/Daily/[today].md`

If it exists, fill the **Prep For Tomorrow** section with the tonight prep items from Step 6. Format:
```
### ⏰ Time-Sensitive
- [Confirmed calendar events for tomorrow, e.g., "Dr. Tami at 3pm — join via SimplePractice link"]
- [Any other time-critical prep, e.g., "Set alarm for 6am"]

### 👕 Clothing & Gear
- [What to set out]

### 🍳 Food Prep
- [Any meal/snack prep]

### 📋 Mental Prep
  1. [First mental prep item]
  2. [Second mental prep item]
  3. [Third mental prep item — tomorrow's top focus]

### 🏠 Environment Setup
- [Workspace/environment prep]

### ✅ Final Check
- [Last thing to verify before sleep]
```

Only fill sections that are relevant — leave sections blank if nothing applies.

**Do NOT touch** any other section of today's note.

---

## Step 8: Create or Seed Tomorrow's Daily Note

Check if `C - Signal Relay/Daily/[tomorrow].md` exists.

**If it doesn't exist:** Create it using the Daily Note Template structure.

**Fill these sections in tomorrow's note:**

### Top 3 Priorities
```
1. [Priority 1 from synthesis]
2. [Priority 2 from synthesis]
3. [Priority 3 from synthesis]
```

### Schedule for Today
Place confirmed calendar events (from Step 3b) as fixed blocks first, then fill remaining slots with suggested task blocks:
```
### Morning
- **[TIME]** | [Calendar event or suggested activity]

### Afternoon
- **[TIME]** | [Calendar event or suggested activity]

### Evening
- **[TIME]** | [Calendar event or suggested activity]
```

### Tasks
List the key open/due tasks for tomorrow as unchecked items:
```
- [ ] [[Task name]] — [brief context]
```

**Leave blank:** Notes, Journal, Energy Check-ins, End of Day Recap/Habits, Reflection, and Prep For Tomorrow sections.

---

## Step 9: Print Summary

After writing, output a brief summary:

```
🌙 Evening Plan Complete — [Date]

📋 Prep For Tomorrow written to today's note.
📅 Tomorrow's note seeded: [tomorrow's date]

Tomorrow's Top 3:
  1. [Priority 1]
  2. [Priority 2]
  3. [Priority 3]

📝 Don't forget to fill in your Journal entry before bed —
   who did you talk to, what happened, any decisions made?
```
