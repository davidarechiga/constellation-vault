---
tags:
  - moc
---

# MOC - Emergent Themes

> A map of recurring patterns, cross-domain connections, and emergent threads that surface across the vault. Unlike other MOCs which organize by topic, this one organizes by *meaning* — the themes that weave through music, career, relationships, creativity, and personal growth simultaneously.

## The Creative Technologist Identity

The thread connecting music, design, code, and career into a unified professional path.

- [[Career Transition 2026]]
- [[Frameloop]]
- [[pixelglitch creative studio]]
- [[Pixel Glitch Brand Aesthetic Guidelines]]
- [[Constellation Mobile]]
- [[🎵 Music & Audio Production]]
- [[Graphic Design is my next move]]
- [[IT Career Development]]

**Where it shows up:** Career search targets roles that unify all skills. Music releases need visual content (Pixel Glitch). Pixel Glitch tools (Frameloop) become portfolio pieces. Portfolio drives job search. Each project feeds the next.

## Breaking Inherited Patterns

Processing generational dynamics through creativity, therapy, and intentional parenting.

- [[Themes of Only Talks 2 Ghosts]]
- [[The Huberman Lab Podcast with Dr. Martha Beck]]
- [[Couples therapy]]
- [[Building Your Own Internal Support System]]
- [[Creating Conditions for Inner Safety]]
- [[1 Baby Prep - Cyrus]]
- [[Birth Plan - Camille & David]]
- [[Lost At Sea]]
- [[Nothing is Sacred]]
- [[Core Values]]

**Where it shows up:** Album tracks ("The Matriarch," "The Healer") process family dynamics. Therapy notes explore the "essential self" vs. inherited expectations. Baby prep is shaped by the desire to parent differently. Poetry captures emotional truths that inform all of it.

## Structure as Creative Freedom

The pattern of applying systems thinking to inherently messy, creative, and emotional domains.

- [[album release checklist]]
- [[(Overview) 2025 Release Schedule]]
- [[Album Roadmap]]
- [[Household Routines]]
- [[Daily Check-in Questions]]
- [[15 Min Daily Check-In with Camille]]
- [[Weekly Meal Routine]]
- [[Rough draft of morning routine]]
- [[Self-Care Rituals]]

**Where it shows up:** 561 poetry files organized with a workflow pipeline. Music releases follow phased checklists. Relationship maintenance is a tracked daily habit. Meal planning, morning routines, and household management all get structured systems. The structure doesn't constrain — it *frees*.

## Presence & Intentional Living

The recurring commitment to showing up fully — in relationships, creative work, and daily life.

- [[Camille - Master Note]]
- [[All the Reasons Why...]]
- [[Daily Habits that will help me show up for Camille]]
- [[Small things that say I love you]]
- [[Shower Gratitude Routine]]
- [[My Personal Promises]]
- [[Congruence]]
- [[Intrinsic Motivation]]
- [[Alan Watt Quotes]]
- [[The law of reversed effort]]

**Where it shows up:** Daily check-ins with Camille. Gratitude practices in the shower. Mindfulness birthing classes. The phrase "Peace is this moment without judgement." Career search filtering for work-life balance as non-negotiable.

## Values-First Sequencing

The pattern of designing life around priorities — not abandoning dreams, but ordering them by season.

- [[Top 5 goals to focus on]]
- [[Thoughts on What To Work On]]
- [[Career Transition 2026]]
- [[1 Baby Prep - Cyrus]]
- [[Relationship - Camille]]
- [[Bucket list]]
- [[Constellation/E - The Foundry/Dashboard/Projects]]

**Where it shows up:** Projects move to "Someday" when they don't fit the current life phase. Music output adjusts around parenting capacity. Career search targets sustainability. The live performance dream exists but waits until after baby adjustment. Nothing is abandoned — everything is *sequenced*.

## Documentation as Self-Knowledge

The practice of writing as a way to know yourself — not just to remember, but to *understand*.

- [[Journaling]]
- [[Field Notes of a Relationship]]
- [[Nothing is Sacred]]
- [[Lost At Sea]]
- [[Constellation Guide]]
- [[MOCs]]

**Where it shows up:** Poetry captures emotional snapshots. Task files capture intentions. MOCs capture knowledge structures. Therapy notes become creative material. The vault isn't just a filing system — it's a living archive of who you are and who you're becoming.

---

## Emergent Theme Tags

Use these tags across the vault to surface notes that participate in these cross-domain threads:

- `#theme/creative-technologist` — Notes where music, design, code, and career intersect
- `#theme/breaking-patterns` — Processing inherited dynamics, choosing differently
- `#theme/structure-as-freedom` — Systems, checklists, routines that enable creativity
- `#theme/presence` — Showing up fully, mindfulness, intentional living
- `#theme/sequencing` — Prioritizing by season, ordering dreams by readiness
- `#theme/self-knowledge` — Writing and documentation as tools for understanding

### Query: All themed notes

```dataview
TABLE WITHOUT ID
  file.link as "Note",
  filter(file.tags, (t) => startswith(t, "#theme/")) as "Themes"
FROM #theme/creative-technologist OR #theme/breaking-patterns OR #theme/structure-as-freedom OR #theme/presence OR #theme/sequencing OR #theme/self-knowledge
SORT file.name ASC
```

---

## Related

- [[MOC - Music]]
- [[MOC - Career]]
- [[MOC - Creative Work]]
- [[MOC - Health & Wellness]]
- [[MOC - Family]]
- [[Constellation Guide]]
