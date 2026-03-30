---
tags:
  - wiki
  - family
---

# Wiki De Arechiga

> A living family wiki — part operations manual, part reference database, part knowledge base. This is our household's shared brain: how we do things, where to find things, and what matters to us as a family. Built to grow with us and eventually be a legacy document for Cyrus.

---

## How To Use

- Browse by category below, or search `#wiki` to find all entries
- Each entry follows the [[Wiki Entry Template]] format
- Add new entries anytime — keep them in this folder, tag with `#wiki` and `#family`
- Set `wiki-category` in frontmatter to `operations`, `reference`, or `knowledge`

---

## 🧠 Family Knowledge Base

Values, traditions, recipes, and what makes us *us*.

- [[Arechiga Family North Star]]
- [[About the Arechigas]]
- [[Arechiga Family Values]]
- [[Holiday Traditions]]
- [[Gift Giving Guide]]
- [[Family Favorite Recipes]]
- [[Meal Planning System]]

---

## 📚 Family Reference Database

Contacts, medical info, documents, and essential reference material.

- [[Emergency Contacts & Procedures]]
- [[River - Care Guide]]
- [[Cyrus - Care Guide]]
- [[Important Documents Locations]]
- [[Family Medical Reference]]
- [[Insurance & Benefits Overview]]
- [[Pediatrician & Doctors List]]

---

## 🏠 Operations Manual

Procedures, routines, and checklists — how we run our household.

- [[Cleaning The House in 30 Minutes]]
- [[Booking Flights Step by Step & Timeline]]
- [[Laundry System]]
- [[Kitchen Deep Clean Procedure]]
- [[Seasonal Home Maintenance Checklist]]
- [[Mail & Package Handling]]
- [[Car Maintenance Schedule]]
- [[Morning Routine - Household]]
- [[Evening Routine - Household]]
- [[Weekly Reset Routine]]

---

## All Wiki Entries

```dataview
TABLE wiki-category AS "Category", file.mtime AS "Last Updated"
FROM "A - The Observatory/Documentation/Wiki De Arechiga"
WHERE file.name != "Wiki De Arechiga"
SORT wiki-category ASC, file.name ASC
```

---

## Related

- [[MOC - Family]]
- [[Family & Parenting Hub]]
- [[Partnership Hub]]
