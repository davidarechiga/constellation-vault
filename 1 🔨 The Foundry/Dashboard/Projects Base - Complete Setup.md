# Projects Base - Complete Setup ✅

**Updated:** February 8, 2026
**Status:** All 10 projects now discoverable in projects.base

---

## 🎯 Your Complete Project Ecosystem

### 🟢 6 Active Projects (Visible in Active Dashboard)

| #   | Project                           | Status | Priority | Progress | Due     |
| --- | --------------------------------- | ------ | -------- | -------- | ------- |
| 1   | 👶 Baby Prep - Cyrus              | Active | High     | 35%      | Mar 9   |
| 2   | 💼 Career Transition 2026         | Active | High     | 5%       | Jun 1   |
| 3   | 🎨 Music Releases 2026            | Active | Medium   | 15%      | Dec 31  |
| 4   | 🎬 Pixel Glitch Studio Operations | Active | Medium   | 40%      | Ongoing |
| 5   | 🖼️ Frameloop                     | Active | Medium   | 25%      | Jun 30  |
| 6   | 📱 Constellation Mobile           | Active | Medium   | 10%      | Apr 15  |

### ⏸️ 4 Future/On-Hold Projects (Visible in other views)

| # | Project | Status | Timeline | Concept |
|---|---------|--------|----------|---------|
| 7 | 🎲 SOAR Board Game | On Hold | 2027 | Complete game rules, needs prototyping |
| 8 | 📝 Making A Zine - Dilettante | Planning | 2027 | Explore "dilettante" concept in print |
| 9 | 🌐 Personal Website Redesign | Planning | Sep 2026 | Portfolio site refresh (post-job) |
| 10 | 🎤 Perform A Live Set | Planning | Dec 2026+ | Music + visual performance event |

---

## ✨ What's Fixed

### ✅ Title Display
- All 10 projects now have `title:` field in frontmatter
- Active Dashboard now shows **project names clearly**
- Column width optimized for readability

### ✅ Complete Project Coverage
- **6 active projects** → Show in "Active Dashboard" view
- **4 future projects** → Show in "By Category & Owner" and archive views
- All tagged with `tags: [project]` for automatic discovery

### ✅ Full Metadata
- **Title, Status, Priority, Category, Owner, Progress, Due Date**
- **Current Focus & Next Action** (what you're working on right now)
- **Task Count** (auto-calculated for Baby Prep and Career projects)
- **Staleness Detection** (warns if >30 days without update)

---

## 📊 Views Overview

### 🎯 Active Dashboard (6 projects)
**What you see:** Your current work sorted by priority and deadline
- Baby Prep (35%, critical in next week)
- Career Transition (5%, resume due Feb 15)
- Music Releases (15%, year-long release schedule)
- Pixel Glitch (40%, client work + studio ops)
- Frameloop (25%, visual tool development)
- Constellation Mobile (10%, infrastructure project)

### 📅 Timeline View
**What you see:** All projects grouped by completion month
- Shows workload distribution across months
- Identifies months where you're overcommitted
- Helps plan realistic timelines

### ⏸️ On Hold & Blocked
**What you see:** Future projects + any blocked dependencies
- SOAR Board Game (rules done, prototyping pending)
- Making A Zine, Website, Live Set (all planning phase)

### 👥 By Category & Owner
**What you see:** Projects grouped by type and who owns them
- All David projects visible
- Shared projects (Baby Prep with Camille)
- Easy to see workload distribution

---

## 🚀 How to Use It Now

### Daily
1. **Open:** `0 📡 Signal Relay/Projects.md`
2. **View:** Active Dashboard (default)
3. **Action:** See your 6 active projects ranked by importance
4. **Update:** Click progress % to change, or click row to open full project

### Weekly
1. **Switch to:** Timeline View
2. **Check:** When major projects are due
3. **Plan:** Next week's focus based on deadlines
4. **Update:** `last-updated` field if you've worked on a project

### As Ideas Emerge
1. **Create new project:** Copy PROJECT_TEMPLATE.md
2. **Add frontmatter:** title, status (planning/on-hold/active), category, owner
3. **Save in:** `1 🔨 The Foundry/`
4. **Base updates automatically**

---

## 📝 Project Frontmatter Reference

Every project has this structure:

```yaml
---
tags: [project]
title: "Project Name"
status: active | planning | on-hold | completed | archived
category: creative | work | studio | family | personal | education
priority: high | medium | low
owner: David | Camille | Shared
start-date: YYYY-MM-DD
last-updated: YYYY-MM-DD
progress: 0-100 (percent)
estimated-completion: YYYY-MM-DD (null if ongoing)
current-focus: "What you're actively working on"
next-action: "What needs to happen next"
time-estimate: "Duration" (e.g., "6 weeks", "12 months")
deliverables: [List of outputs]
---
```

---

## 🎯 Project Categories Explained

| Category | Projects | Use For |
|----------|----------|---------|
| **creative** 🎨 | Music, Frameloop, Zine, Live Set, Website | Art, music, design, creative coding |
| **work** 💼 | Career Transition | Job search, employment, professional |
| **studio** 🎬 | Pixel Glitch | Freelance operations, client work |
| **family** 👶 | Baby Prep | Shared family responsibilities |
| **personal** 🏠 | Constellation Mobile, SOAR | Hobbies, personal development, tools |

---

## 📈 Project Health Signals

The base automatically highlights:

| Signal | What It Means | Action |
|--------|---------------|--------|
| 🟢 Active | Project in progress | Keep momentum |
| ⏸️ On Hold | Paused, waiting for something | Check blockers |
| ⚠️ >30 days stale | No update in a month | Need status check |
| 🚨 >45 days stale | No update in 45 days | Likely forgotten |
| 📅 Unscheduled | No completion date | Set a target or mark someday |

---

## 🔄 Workflow: From Idea to Base

**Step 1: New Idea Emerges**
```
"I want to make a podcast about design decisions"
```

**Step 2: Create Project Stub**
```
1. Use PROJECT_TEMPLATE.md
2. Fill in title, category (creative), status (planning)
3. Save as "Design Decisions Podcast.md"
4. Add tags: [project]
```

**Step 3: Appears in Base Immediately**
```
- Base auto-discovers it (tags: [project])
- Shows in Planning view (status: planning)
- Visible in Category view
```

**Step 4: Work on It**
```
- Update progress % as you build it
- Update current-focus with what's happening now
- Update last-updated when you work on it
```

**Step 5: Complete**
```
- Change status: active → completed
- Set completion-date: YYYY-MM-DD
- Moves to Archive view (kept for reference)
```

---

## 💡 Real-World Scenarios

### Scenario 1: "What should I work on today?"
1. Open Projects.md
2. Look at Active Dashboard
3. See Baby Prep (35%, due Mar 9) is most critical
4. See Career needs resume by Feb 15
5. Decision: Career work today, baby prep tomorrow

### Scenario 2: "Am I overcommitting?"
1. Switch to Timeline View
2. See Apr-Jun packed (Career + Music + Frameloop)
3. Reality check: That's 3 major projects simultaneously
4. Decision: Defer Frameloop start or reduce scope

### Scenario 3: "I haven't touched Pixel Glitch in weeks"
1. Check Needs Attention view
2. It flags "Pixel Glitch: 35 days stale"
3. Decide: Is it genuinely on pause, or abandoned?
4. Update status or set next-action to restart

### Scenario 4: "I have a new creative idea"
1. Create quick project stub (5 min)
2. Status: planning
3. It shows in base immediately (not forgotten)
4. Comes back to it when ready

---

## 🎓 Why This Approach Works

### Before (Scattered Projects)
- Projects in different folders
- No central view of progress
- Hard to see if overcommitted
- Easy to forget things
- Unclear priorities

### After (Projects Base)
- ✅ All 10 projects visible in one place
- ✅ Instant priority/deadline awareness
- ✅ Automatic staleness detection
- ✅ Nothing falls through cracks
- ✅ Decision-making in seconds

---

## 📚 Related Resources

- **Main Guide:** [[Projects.md]]
- **Setup Details:** [[Projects Setup Summary.md]]
- **Consolidated List:** [[Consolidated List of Projects.md]]
- **Template:** [[Templates/PROJECT_TEMPLATE.md]]

---

```
★ Insight ─────────────────────────────────────
You now have a complete project ecosystem: 6 active projects with momentum (Baby Prep, Career, Music, Studio, Frameloop, Mobile) plus 4 future projects capturing long-term creative vision (Zine, Website, Live Set, Board Game). The base serves as a decision-making tool—instead of "what should I do?" you can see at a glance what's due soonest, most important, and most stale. The real power is that updates flow bi-directionally: when you update a project hub, the base recalculates; when you link tasks back (projects field), task counts auto-appear in the base.
─────────────────────────────────────────────────
```

---

*Projects Base setup complete: February 8, 2026*
*All 10 projects ready to track and navigate*
