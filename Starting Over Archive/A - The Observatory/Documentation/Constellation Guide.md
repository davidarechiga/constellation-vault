# Constellation Guide

> A comprehensive guide to navigating and using your personal knowledge management system.

---

## What Is This?

This is **Constellation** — a personal knowledge management system built in Obsidian. It's designed to capture, organize, and connect everything important in your life: projects, ideas, poetry, learning, relationships, and career development.

**Core Philosophy:**
- **Capture everything** worth remembering
- **Organize** using the ACE method (Atlas, Calendar, Efforts)
- **Connect** ideas through wikilinks and Maps of Content
- **Review** regularly to maintain and grow
- **Find through links** — notes are discovered through connections, not folder browsing

---

## The ACE Method

Constellation is organized using the **ACE method** — a system that organizes information by function rather than category. Unlike PARA (which sorts by actionability), ACE creates three distinct spaces for thinking, tracking time, and doing work.

### A — The Observatory (Atlas)
**Location:** `A - The Observatory/`

**What:** Your knowledge space. Reference materials, learning, creative collections, and documentation. Notes here are organized by connections and Maps of Content, not rigid categories.

**Key Subdirectories:**
- `MOCs/` — Maps of Content (topic index notes for Music, Health, Creative Work, Cooking, Career, Family)
- `Sources/` — Book notes, articles, literature notes
- `Documentation/` — System docs, this guide, and Templates
- `Archive/` — Completed or inactive items
- `Attachments/` — Media files and embedded resources
- `TaskNotes/` — Plugin config for the TaskNotes system

**Topic Folders:**
- `✍️ Ideas, Thoughts & Poetry/` — Poetry collection (560+ files)
- `Personal Reminders/` — Reminders and reference (229+ files)
- `🎵 Music & Audio Production/` — Music reference library
- `🎨 Design & Creative Work/` — Design learning and resources
- `🎮 Entertainment & Media/` — Media notes
- `🏃 Hobbies & Activities/` — Hobby reference
- `🌟 Lifestyle & Personal/` — Personal development
- `Habits & Productivity/` — Productivity systems
- `Writing/` — Writing craft reference
- `Travel/` — Travel planning and memories
- `Checklists/` — Reusable checklists

**When to use:** Saving reference material, learning notes, creative writing, or topical knowledge.

---

### C — Signal Relay (Calendar)
**Location:** `C - Signal Relay/`

**What:** Time-based entries and your daily workflow hub. This is where you interact with the system day-to-day.

**Structure:**
- `Daily/` — Daily notes (created from template)
- `Weekly/` — Weekly review notes
- `0 📡 Signal Relay.md` — Main navigation hub and dashboard (folder note)

**When to use:** Daily logging, weekly reviews, time-stamped entries, and as your starting point each session.

---

### E — The Foundry (Efforts)
**Location:** `E - The Foundry/`

**What:** All active work — projects, life areas, tasks, and dashboards. This is where things get done.

**Structure:**
- `Active/` — Current projects with deadlines
- `Ongoing/` — Life areas requiring continuous attention
- `Someday/` — Future or paused projects
- `Dashboard/` — Canvas dashboards, .base views, hub files
- `Tasks/` — TaskNotes organized by project subfolder

#### Active Projects
- `1 Baby Prep - Cyrus/` — Baby preparation
- `2 Music Releases/` — Current music release work
- `3 pixel glitch creative studio/` — Design studio
- `4 Frameloop/` — Frameloop project
- `6 Career Transition 2026/` — Career development
- `Constellation Mobile/` — Mobile app for the vault

#### Ongoing Life Areas
- `1 🛫 Personal Growth/` — Health, skills, self-improvement
- `2 🥰 Camille/` — Relationship
- `3 🐶 River/` — Pet care
- `4 👶 Cyrus/` — Baby/parenting
- `5 🏡 Household/` — Home management

**When to use:** Creating or managing project work, tracking tasks, maintaining life areas.

---

## Task Organization: TaskNotes + Bases

The vault uses a dual system for task management.

### TaskNotes (Individual Task Files)
Stored in `E - The Foundry/Tasks/[Project Name]/` with frontmatter metadata:

```yaml
tags:
  - task
  - [project-tag]  # e.g., baby, music, career
title: Task Name
status: open | in-progress | done
priority: high | normal | low
due: YYYY-MM-DD
owner: David | Camille | Shared
projects:
  - "[[Project Name]]"
```

**Task file structure:**
1. **Context** — Why it matters, acceptance criteria, related links
2. **Strategy** — High-level approach
3. **Task Breakdown** — Nested checkboxes with subtasks
4. **References** — Source material

### Bases (Query Dashboards)
`.base` files provide aggregated views of TaskNotes — task lists, kanban boards, and completion tracking.

**Key .base files:**
- `Signal Relay Dashboard.base` — All tasks across projects (in `E - The Foundry/Dashboard/`)
- `baby-prep-tasks.base` — Baby prep tasks
- `career-tasks.base` — Career tasks
- `relationship-tasks.base` — Relationship tasks
- `Projects List.base` — All projects tagged with `#project`

### How They Work Together

- **TaskNotes** = detailed action plans (individual files with checklists)
- **Bases** = aggregated views across multiple tasks (dynamic queries)
- **Project hubs** embed the relevant .base and link to TaskNotes
- **Weekly Dashboard** (Canvas) embeds per-project .base files for at-a-glance priority view

---

## Navigation

### Start Point: Signal Relay Dashboard
**Location:** `C - Signal Relay/0 📡 Signal Relay.md`

Your main command center. Start every session here.

---

### Maps of Content (MOCs)
**Location:** `A - The Observatory/MOCs/`

MOCs are topic index notes that organize related content by theme. Use them to discover and navigate notes.

**Available MOCs:**
- [[MOC - Career]] — Career path and development
- [[MOC - Music]] — All music content
- [[MOC - Creative Work]] — Creative projects and expression
- [[MOC - Health & Wellness]] — Health and wellness
- [[MOC - Family]] — Family and parenting
- [[MOC - Cooking]] — Recipes and meal planning

**How to use MOCs:**
1. Open a MOC for the topic you're interested in
2. Browse the organized sections and wikilinks
3. Follow links to specific notes
4. Check "Related" sections for connected topics

---

## Daily Workflows

### Morning Routine

1. **Open Signal Relay Dashboard** → Click today's daily note
2. **Review last night's prep** — Check what you planned yesterday evening
3. **Set top 3 priorities** — What must get done today?
4. **Check schedule** — Calendar appointments and time blocks
5. **Start working** — Navigate via MOCs or project hubs to relevant content

### Evening Routine

1. **Open tomorrow's daily note** — Fill out "Tonight's Prep" section
2. **Complete today's recap** — Log habits, energy, reflection
3. **Review tomorrow** — Check calendar, identify #1 priority, write intentions

### Weekly Review

**When:** Sunday evenings

1. **Create weekly review note** from template in `C - Signal Relay/Weekly/`
2. **Review:** Wins, habit consistency, project progress, energy/wellness
3. **Plan ahead:** Top 3 priorities, scheduled events, weekly intention
4. **System check:** What worked, what needs adjustment

---

## Creating Notes

### Where Should This Go?

| Question | Location |
|----------|----------|
| Is it a time-based entry? | **C - Signal Relay** (Daily/Weekly) |
| Is it project work with a deadline? | **E - The Foundry/Active** |
| Is it an ongoing life responsibility? | **E - The Foundry/Ongoing** |
| Is it a task or action item? | **E - The Foundry/Tasks/[Project]** |
| Is it reference or knowledge? | **A - The Observatory** (find the right topic folder) |
| Is it completed or inactive? | **A - The Observatory/Archive** |

### Using Wikilinks

```markdown
[[Note Title]]                              — Basic link
[[Note Title|Display Text]]                 — Custom display text
[[Note Title#Section Header]]               — Link to a section
```

Wikilinks resolve by note title, not file path. Moving files doesn't break links.

---

## Special Collections

### Poetry Collection (560+ files)
**Location:** `A - The Observatory/✍️ Ideas, Thoughts & Poetry/`

**Folders:**
- **📝 Song Lyrics & Music Writing** — Song-structured pieces
- **💭 Personal Reflections** — Life observations and wisdom
- **💔 Relationship & Love Poetry** — Romance and connection
- **🌊 Abstract & Experimental** — Stream-of-consciousness
- **✨ Completed Pieces** — Polished, finished work
- **🔨 Works in Progress** — Actively being developed
- **📋 Ideas & Fragments** — Quick captures and inspiration

**Workflow:** Fragments → Works in Progress → Completed Pieces

### Personal Reminders (229+ files)
**Location:** `A - The Observatory/Personal Reminders/`

**Folders:**
- **🧘 Wellness & Mindfulness** — Mental and physical health
- **💡 Productivity & Focus** — Work tips and strategies
- **💬 Inspirational Quotes** — Motivational sayings
- **📝 Practical Instructions** — How-tos and processes
- **🎨 Creative Guidance** — Artistic reminders
- **📞 Contact & Reference Info** — Contacts and reference numbers
- **🗂️ Misc & Unsorted** — Needs categorization

---

## Habit Tracking

**System:** Frontmatter fields in daily notes

**Tracked Habits:**
- `gratitude` — Gratitude practice
- `meditation` — Meditation
- `candle` — Candle ritual
- `exercise` — Physical exercise
- `stretch` — Stretching routine
- `drawing` — Creative drawing
- `camille_checkin` — Daily check-in with Camille

**How to log:** In your daily note, set habits to `1` for done:
```yaml
gratitude:: 1
meditation:: 1
exercise::
```

---

## Music Ecosystem

Music content spans across ACE (by design):

| Space | Location | Content |
|-------|----------|---------|
| **Efforts** | `E - The Foundry/Active/2 Music Releases/` | Current release work |
| **Atlas** | `A - The Observatory/🎵 Music & Audio Production/` | Reference library, theory, techniques |
| **Calendar** | Daily/weekly notes | Practice logs, session notes |

**Navigation:** Start at [[MOC - Music]] to navigate all music content.

---

## Career: Creative Technologist Path

**Active project:** `E - The Foundry/Active/6 Career Transition 2026/`

You're building a **Creative Technologist** identity combining:
- Design skills (Pixel Glitch Creative Studio)
- Technical development (Frameloop, Constellation Mobile)
- Creative production (Music releases)

**Navigation:** [[MOC - Career]]

---

## Search & Discovery

1. **Quick Switcher** (Cmd+O) — Type note name, fuzzy matching
2. **Omnisearch Plugin** — Enhanced semantic search
3. **Global Search** (Cmd+Shift+F) — Full-text search with regex
4. **Graph View** — Visual note connections
5. **Backlinks Panel** — All notes linking to current note
6. **MOCs** — Browse organized topic indexes

---

## Plugins

Key community plugins in use:
- **TaskNotes** — Task management with frontmatter metadata and .base views
- **Omnisearch** — Enhanced full-text search
- **Folder Notes** — Notes that represent folders (used for hub pages)
- **Smart Connections** — AI-powered semantic search and note linking
- **Smart Templates** — AI-assisted note templates
- **MCP Tools** — Model Context Protocol integration
- **Local REST API** — External tool access to the vault

---

## Best Practices

**Do:**
- Start from Signal Relay Dashboard each session
- Navigate via MOCs and project hubs, not folder browsing
- Link liberally with wikilinks
- Capture immediately, organize later
- Build the daily note habit
- Review weekly to maintain the system
- Use TaskNotes + .base files for task tracking

**Don't:**
- Over-organize — ACE + topic folders is enough structure
- Duplicate content — search before creating
- Orphan notes — link from at least one place
- Skip reviews — the system decays without maintenance
- Browse folders to find things — use links, MOCs, and search

---

## Troubleshooting

### "I can't find a note"
1. Quick Switcher (Cmd+O) — type partial name
2. Omnisearch — semantic search
3. Check relevant MOC — browse organized sections
4. Global Search — full-text keyword search

### "Where should this go?"
1. Time-based? → Signal Relay
2. Project with deadline? → The Foundry/Active
3. Ongoing responsibility? → The Foundry/Ongoing
4. Task/action item? → The Foundry/Tasks
5. Reference/knowledge? → The Observatory
6. Unsure? → Capture it anywhere and organize later

### "Links broke after moving files"
Wikilinks resolve by title, not path — they rarely break. If one does, the note may have been renamed or deleted. Search for the title to confirm.

---

**Welcome to Constellation!**

This system scales with your thinking, supports your creativity, and helps you navigate complexity. Start at Signal Relay, explore via MOCs, and build the daily note habit.

*The magic happens when you consistently capture, connect, and review.*

---

## Claude Code Integration

Constellation is wired for token-efficient Claude Code sessions using a 5-tier deep memory architecture. See [[Claude Code Deep Memory Architecture]] for full documentation.

**Quick reference:**
- Skills: `/morning`, `/evening`, `/weekly`, `/organize-inbox`, `/session-persist`, `/vault-navigator`
- Config: `.claude/rules/`, `.claude/skills/`, `.claude/hooks/`
- Memory: `~/.claude/projects/.../memory/` (persists across sessions)

---

#guide #meta #system
