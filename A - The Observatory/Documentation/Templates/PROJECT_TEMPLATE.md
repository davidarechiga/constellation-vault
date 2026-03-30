<%*
const folderPath = tp.file.folder(true);
const projectName = tp.file.title;
const baseContent = `filters:
  and:
    - file.hasTag("task")
    - file.path.contains("${folderPath}")
formulas:
  priorityWeight: if(priority=="none",0,if(priority=="low",1,if(priority=="normal",2,if(priority=="high",3,999))))
  daysUntilDue: if(due, ((number(date(due)) - number(today())) / 86400000).floor(), null)
  daysSinceModified: ((number(now()) - number(file.mtime)) / 86400000).floor()
  isOverdue: due && date(due) < today() && status != "done"
  isDueToday: due && date(due).date() == today()
  isDueThisWeek: due && date(due) >= today() && date(due) <= today() + "7d"
  dueDateCategory: if(!due, "No due date", if(date(due) < today(), "Overdue", if(date(due).date() == today(), "Today", if(date(due).date() == today() + "1d", "Tomorrow", if(date(due) <= today() + "7d", "This week", "Later")))))
  urgencyScore: if(!due, formula.priorityWeight, formula.priorityWeight + max(0, 10 - formula.daysUntilDue))
  dueDateDisplay: if(!due, "", if(date(due).date() == today(), "Today", if(date(due).date() == today() + "1d", "Tomorrow", if(date(due).date() == today() - "1d", "Yesterday", if(date(due) < today(), formula.daysUntilDue * -1 + "d overdue", if(date(due) <= today() + "7d", date(due).format("ddd"), date(due).format("MMM D")))))))
  priorityEmoji: if(priority=="high","⏫",if(priority=="normal","🔼",if(priority=="low","🔽","⚪")))
  statusDisplay: if(status=="done","✅ Done",if(status=="in-progress","🔄 In Progress",if(status=="open","📋 Open","⚪ None")))
views:
  - type: tasknotesKanban
    name: 📋 All Tasks
    filters:
      and:
        - status != "done"
    groupBy:
      property: priority
      direction: ASC
    order:
      - status
      - priority
      - due
      - owner
      - projects
      - file.tags
      - file.name
    sort:
      - property: formula.urgencyScore
        direction: DESC
    hideEmptyColumns: true
  - type: tasknotesTaskList
    name: 🚨 Urgent & Overdue
    filters:
      and:
        - status != "done"
        - or:
            - formula.isOverdue
            - formula.isDueToday
            - formula.isDueThisWeek
    order:
      - status
      - priority
      - due
      - owner
      - file.name
    sort:
      - property: formula.urgencyScore
        direction: DESC
  - type: table
    name: ✅ Completed
    filters:
      and:
        - status == "done"
    order:
      - title
      - priority
      - due
      - owner
    sort:
      - property: file.mtime
        direction: DESC
`;
await app.vault.create(folderPath + "/tasks.base", baseContent);
_%>
---
tags:
  - project
title: <% tp.file.title %>
status: someday
priority: normal
owner: David
deadline:
progress: 0
current-focus:
next-action:
time-estimate:
deliverables:
related-files:
---

# <% tp.file.title %>

> **Quick Access:** [[Constellation/E - The Foundry/Someday/YoCatchPhrase/tasks.base|Tasks]]
> **Target Date:**

---

## Overview

[2-3 sentences on what this project is and why it matters]

**Done when:**
- [ ] [Specific measurable outcome 1]
- [ ] [Specific measurable outcome 2]

---

## 📋 Tasks

![[Constellation/E - The Foundry/Someday/YoCatchPhrase/tasks.base]]

---

## 📅 Timeline

| Phase | Date | Milestones |
|-------|------|------------|
| Phase 1 | | |
| Phase 2 | | |

---

## 🔗 Related Notes & Resources

- [[Related Note]] - [Description]

---

## 📝 Notes & Decisions

### <% tp.date.now("YYYY-MM-DD") %> — Project Created

-

---

## 💰 Budget *(if applicable)*

**Budget:** $

---

---

> [!warning] Promoting to Active?
> When moving this project to `E - The Foundry/Active/`, update the `file.path.contains` filter in `tasks.base` to match the new folder path.

> [!note] Archiving this project?
> 1. Set `status: done` or `status: canceled` in frontmatter
> 2. Move folder to `E - The Foundry/Archive/`
> 3. No other changes needed — it will automatically drop out of all active dashboards

*Last Updated: <% tp.date.now("YYYY-MM-DD") %>*
