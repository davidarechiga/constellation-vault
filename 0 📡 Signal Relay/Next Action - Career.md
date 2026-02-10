---
tags:
  - dashboard
  - next-action
  - career
---

```dataview
TABLE WITHOUT ID
  ("**Next:** " + next-action) AS "Action",
  ("**Due:** " + dateformat(date(deadline), "MMM dd")) AS "Deadline"
FROM "1 🔨 The Foundry/6 Career Transition 2026"
WHERE file.name = "6 Career Transition 2026"
LIMIT 1
```
