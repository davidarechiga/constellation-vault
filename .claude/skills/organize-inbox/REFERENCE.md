# Organize Inbox - Detailed Reference

## Vault Information

### Vault Root
```
$HOME/Constellation/
```

Always use quoted paths in bash commands due to spaces in folder names.

### Folder Structure (ACE Method)

```
Constellation/
├── A - The Observatory/     # Atlas — knowledge & reference
│   ├── Documentation/       # Guides, templates, wiki
│   ├── Sources/             # Books, articles, media notes
│   ├── 🌟 Lifestyle & Personal/  # Therapy, personal notes
│   ├── Archive/             # Completed/inactive items
│   └── Attachments/         # Media files
├── C - Signal Relay/        # Calendar — time-based entries
│   ├── Daily/               # Daily notes (YYYY-MM-DD.md)
│   ├── Weekly/              # Weekly reviews (YYYY-Www.md)
│   └── Inbox/               # ← Primary capture inbox
├── E - The Foundry/         # Efforts — active work
│   ├── Active/              # Time-bound projects
│   ├── Ongoing/             # Life area hubs (5 areas)
│   │   ├── 1 🛫 Personal Growth/
│   │   ├── 2 🥰 Camille/
│   │   ├── 3 🐶 River/
│   │   ├── 4 👶 Cyrus/
│   │   └── 5 🏡 Household/
│   ├── Someday/             # Future/maybe items
│   ├── Tasks/               # TaskNotes by project
│   └── Dashboard/           # .base dashboard files
└── Constellation.md         # Vault hub/MOC
```

## Common Bash Operations

### List inbox contents
```bash
ls "$HOME/Constellation/C - Signal Relay/Inbox/"
```

### Move a file
```bash
mv "$HOME/Constellation/C - Signal Relay/Inbox/Note.md" \
   "$HOME/Constellation/A - The Observatory/Sources/"
```

### Find all inbox markdown files
```bash
find "$HOME/Constellation/C - Signal Relay/Inbox" -type f -name "*.md"
```

## Decision Tree for Classification

```
Is it a daily/weekly note?
├─ YES → C - Signal Relay/Daily/ or Weekly/
└─ NO → Continue

Is it reference material, a resource, or knowledge?
├─ YES → A - The Observatory/
│   ├─ Personal/health/therapy → 🌟 Lifestyle & Personal/
│   ├─ Books/articles/media → Sources/
│   └─ General knowledge → Documentation/
└─ NO → Continue

Is it an active time-bound project?
├─ YES → E - The Foundry/Active/
└─ NO → Continue

Is it an ongoing life area (relationship, pet, household)?
├─ YES → E - The Foundry/Ongoing/[area]/
└─ NO → Continue

Is it a future/maybe idea?
├─ YES → E - The Foundry/Someday/
└─ NO → Archive in A - The Observatory/Archive/
```

## Linking Conventions

- Use wikilinks: `[[Note Title]]` — never markdown links for internal notes
- No Dataview queries — use `.base` files instead
- Update `_index.md` in the destination folder after moving files

## Files to Always Delete

- Test notes (e.g., "Test Note.md")
- Stub notes with minimal content and no clear purpose
- Temporary one-time info (codes, one-off reminders already acted on)
- Duplicates of notes that exist elsewhere in the vault
