---
description: TaskNotes frontmatter spec, file structure, and nested subtask standard for Constellation vault
paths:
  - "Constellation/E - The Foundry/Tasks/**"
  - "Constellation/E - The Foundry/Active/**"
  - "Constellation/E - The Foundry/Ongoing/**"
---

# TaskNotes Spec

## Frontmatter

```yaml
tags:
  - task
  - [project-tag]   # e.g., baby, music, career, household
title: Task Name
status: open | in-progress | done
priority: high | normal | low
due: YYYY-MM-DD
owner: David | Camille | Shared
projects:
  - "[[Project Name]]"
```

## File Structure (top to bottom)

1. **Context Section** — scannability at the top
   - Why critical / why this matters
   - Done when (acceptance criteria)
   - Related links (`[[Wikilink]]`)
   - Pro tips (optional)

2. **Strategy / Overview** — high-level approach, key resources or constraints

3. **Task Breakdown** — action items grouped by category or phase
   - Nested checkboxes for sub-items
   - Clear, specific actions

4. **Source / References** — at the bottom

## Nested Subtask Standard (Feb 2026)

Use **collapsible nested subtasks** for any task with 3+ steps or checklist items:

```markdown
- [ ] Parent task
  - **Context**: Why this matters
  - **Done when**: Clear acceptance criteria
  - **Related**: [[Wikilink]]
  - [ ] Subtask 1
  - [ ] Subtask 2
```

**When to use nested subtasks:**
- Multi-step workflows (3+ sequential actions)
- Checklists (shopping, packing, inventory)
- Category groupings (related items checked off individually)

**Progress indicators:** `[ ]` none · `[/]` partial · `[x]` complete

## Storage Locations

- Task files: `E - The Foundry/Tasks/[Project Name]/`
- Unclassified tasks: `E - The Foundry/Tasks/Inbox/` (temporary)
- Project dashboards: `.base` files co-located with project hub notes

## Key .base Files

- `E - The Foundry/Dashboard/Signal Relay Dashboard.base` — all tasks across projects
- `E - The Foundry/Active/Career Transition 2026/career-tasks.base`
- `E - The Foundry/Ongoing/2 🥰 Camille/relationship-tasks.base`
- `E - The Foundry/Dashboard/Projects List.base` — all `#project` tagged notes
