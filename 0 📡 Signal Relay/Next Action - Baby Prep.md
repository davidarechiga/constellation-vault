---
tags:
  - dashboard
  - next-action
  - baby
---

```dataview
TABLE WITHOUT ID
  ("**Next:** " + next-action) AS "Action",
  ("**Due:** " + dateformat(date(deadline), "MMM dd")) AS "Deadline"
FROM "1 🔨 The Foundry/1 Baby Prep - Cyrus"
WHERE file.name = "1 Baby Prep - Cyrus"
LIMIT 1
```
