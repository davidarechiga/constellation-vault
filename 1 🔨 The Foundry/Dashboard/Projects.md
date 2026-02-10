---
tags: [project-hub]
title: Projects Master Base
---

# 📊 Projects Master Base

**Quick Stats:**
- 🟢 Active Projects: See Active Dashboard view
- ⏸️ On Hold: See On Hold & Blocked view
- ✅ Completed This Year: See Archive view
- 🚨 Needs Attention: See Needs Attention view

**Last Updated:** {{date:YYYY-MM-DD HH:mm}}

---

## 🎯 How to Use This Base

### Views at a Glance

| View | Purpose | Best For |
|------|---------|----------|
| **🎯 Active Dashboard** | Daily driver—what's in motion right now | Quick morning check-in, what to work on today |
| **📅 Timeline View** | See projects grouped by completion month | Planning your workload, seeing what's coming |
| **⏸️ On Hold & Blocked** | Surface stalled projects and blockers | Unblocking work, identifying forgotten projects |
| **🔄 Phase-Based Projects** | Multi-stage initiatives (Music, Baby Prep) | Complex projects with milestones |
| **🔄 Recently Updated** | Projects with newest activity | Quick pulse check on what's moving |
| **🚨 Needs Attention** | Projects stale >30 days | Prevent projects from falling through cracks |
| **⚡ High-Priority Focus** | Your urgent, active work | Execution mode—what demands attention NOW |
| **👥 By Category & Owner** | Workload distribution across categories | Seeing workload balance (David vs Camille vs Shared) |
| **📋 All Unfinished** | Everything that's not done or archived | Master inventory—all 10 projects at a glance |
| **✅ Archive** | Completed/inactive projects by year | Reference, learning, celebration |

### Frontmatter Schema

Create new projects with these required fields:

```yaml
---
tags: [project]
status: active | on-hold | inactive | completed | cancelled | archived
category: creative | work | personal | studio | family | education
priority: high | medium | low
owner: David | Camille | Shared
start-date: YYYY-MM-DD
last-updated: YYYY-MM-DD
progress: 0-100
estimated-completion: YYYY-MM-DD
current-focus: "What you're actively working on"
next-action: "What needs to happen next"
time-estimate: "X hours" | "X days" | "X weeks"
deliverables: ["Deliverable 1", "Deliverable 2"]
---
```

**Optional fields:**
- `completion-date:` When project was finished
- `collaborators:` [David, Camille, Others]
- `dependencies:` ["[[Blocking Project]]"]
- `phase:` Current phase name (for multi-phase projects)
- `tasks-folder:` Path to TaskNotes folder
- `related-files:` ["[[File 1]]", "[[File 2]]"]

### Creating a New Project

> [!tip]+ Quick Start
> 1. **Use template:** `Templates/PROJECT_TEMPLATE.md`
> 2. **Fill required fields:** title, status, category, priority, owner, start-date
> 3. **Save in:** `1 🔨 The Foundry/` with tag `project`
> 4. **Base updates automatically** when you add `tags: [project]`

### Editing Inline

- Click any cell in a view to edit directly (updates the source file)
- Change status, progress, dates, and focus inline
- Tags are auto-maintained

### Linking Projects to TaskNotes

In your TaskNotes frontmatter, link back to the project:

```yaml
projects: ["[[Project Name]]"]
```

This creates bidirectional links and makes task counts visible in the projects base.

---

## 📋 View Details

![[Projects List.base]]

---

## 📚 Related Resources

- [[PROJECT_TEMPLATE.md|Project Template]]
- [[0 📡 Signal Relay|Dashboard]]
- [[0 📡 Signal Relay/Tasks|TaskNotes System]]
