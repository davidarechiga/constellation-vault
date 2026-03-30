# Organize Inbox - Detailed Reference

## Vault Information

### Full Path
```
/Users/davidarechiga/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)
```

**Important**: Always use quoted paths in bash commands due to spaces in the path.

### Complete Folder Structure

```
Second Brain (iCloud)/
├── 0 📥 Inbox/                     # Capture area for uncategorized notes
├── 1 📗 Projects (Relevant Goals)/ # Active time-bound projects
├── 2 🗺️ Areas (Of Responsibilities)/
│   ├── 1 🛫 Personal Growth/       # Self-improvement, cooking, health
│   ├── 2 🥰 Camille/               # Relationship notes
│   ├── 3 🐶 River/                 # Pet notes
│   └── Events/
├── 3 📚 Resource (Interests & Building Blocks)/
│   ├── Book Notes/
│   ├── Computer Science/
│   ├── Design/
│   ├── IdeasThoughtsWritingPoetry/
│   ├── Habits & Productivity/
│   ├── Personal Reminders/
│   ├── Travel/
│   ├── Writing/
│   └── [many other topic folders]
├── 4_Archive/                      # Completed/inactive items
├── Attachments/                    # Media files
└── Home.md                         # Main navigation dashboard
```

## Obsidian Plugins

The vault uses these community plugins:
- **dataview** - Query and display data from notes
- **obsidian-tasks-plugin** - Task management with advanced querying
- **omnisearch** - Enhanced full-text search
- **homepage** / **home-tab** - Custom homepage functionality
- **obsidian-icon-folder** - Custom icons for folders

## Linking Conventions

- Use wikilinks: `[[Note Title]]` to create bidirectional links
- Links resolve by note title, not file path
- Liberal use of links between related concepts for connected thinking
- Cross-reference related notes at bottom of consolidated notes

## Common Bash Operations

### Moving Files
```bash
cd "/Users/davidarechiga/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)/0 📥 Inbox"

# Single file
mv "Note Title.md" "../1 📗 Projects (Relevant Goals)/"

# Multiple files with loop
for file in "File1.md" "File2.md" "File3.md"; do
  [ -f "$file" ] && mv "$file" "../2 🗺️ Areas (Of Responsibilities)/2 🥰 Camille/"
done
```

### Listing Inbox Contents
```bash
ls "/Users/davidarechiga/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)/0 📥 Inbox"

# Count files
ls -1 "/Users/davidarechiga/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)/0 📥 Inbox" | wc -l
```

### Finding Files
```bash
# Find all markdown files in inbox
find "/Users/davidarechiga/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)/0 📥 Inbox" -type f -name "*.md"

# Search for specific pattern
grep -r "keyword" "/Users/davidarechiga/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)/0 📥 Inbox"
```

## Consolidation Patterns

### Common Consolidation Opportunities

1. **Relationship Notes** → "Camille - Master Note.md"
   - Notes On Camille
   - Things I love about Camille
   - What matters most to Camille
   - Nice Things I've done For Camille

2. **Daily Practices** → "Daily Practices & Reminders.md"
   - Daily Reminders
   - Daily Ritual
   - Daily Thoughts
   - Weekly Question Review
   - Weekly Recap

3. **Movie/TV Lists** → "Movies & TV To Watch.md"
   - What Do I Watch Next
   - Favorite Movies of All Time
   - Favorite Movies About [Topic]
   - NY Times 100 Best Movies
   - Movie Dice Roll (genre selector)

4. **Recipes** - Generally keep separate
   - Each recipe is a standalone reference
   - Easier to find and use individually
   - Can be linked together with wikilinks

### Consolidated Note Template

```markdown
# [Topic] - Master Note

A comprehensive collection of [description].

---

## 🌟 Section 1 Title

[Content from first source note]

---

## 💝 Section 2 Title

[Content from second source note]

---

## 📝 Section 3 Title

[Content from third source note]

---

*Related notes: [[Related Note 1]], [[Related Note 2]], [[Related Note 3]]*
```

## Decision Tree for Classification

```
Is it time-bound with a deadline?
├─ YES → 1 📗 Projects
└─ NO → Continue

Is it about Camille/relationship?
├─ YES → 2 🗺️ Areas/2 🥰 Camille
└─ NO → Continue

Is it about personal development, health, or habits?
├─ YES → 2 🗺️ Areas/1 🛫 Personal Growth
└─ NO → Continue

Is it about River (pet)?
├─ YES → 2 🗺️ Areas/3 🐶 River
└─ NO → Continue

Is it ongoing life management (finance, car, home)?
├─ YES → 2 🗺️ Areas
└─ NO → Continue

Is it reference material, lists, or creative ideas?
├─ YES → 3 📚 Resource
│   ├─ Entertainment → Resource root
│   ├─ Music/Audio → Resource root
│   ├─ Creative writing → IdeasThoughtsWritingPoetry/
│   ├─ Work/Career → Resource root
│   └─ Knowledge topics → Resource root
└─ NO → Continue

Is it completed or outdated?
├─ YES → 4_Archive
└─ NO → Keep in inbox for review
```

## Files to Always Delete

- Test notes (e.g., "Test Note.md")
- Stub notes with minimal content and no clear purpose
- Temporary codes or one-time info (e.g., "one medical code.md")
- Concert/event notes with past dates (archive or delete)
- Minimal jots that should be in a larger note

## Progress Tracking Best Practices

Always use TodoWrite to show progress:

```
1. Analyze inbox notes and categorize them
2. Identify notes that can be consolidated
3. Present categorization plan to user
4. Create consolidated note: [Name]
5. Move files to Projects folder
6. Move files to Areas/Camille folder
7. Move files to Areas/Personal Growth folder
8. Move recipe files to cooking area
9. Move files to Resources folders
10. Move finance and life management files
11. Archive or organize daily notes
12. Provide organization summary
```

Mark todos as in_progress immediately before starting, then completed right after finishing each task.

## Quality Checks

Before completing organization:

- [ ] Inbox contains only "0 📥 Inbox.md" index file [migrated]
- [ ] All consolidated notes are well-formatted with sections [migrated]
- [ ] Related notes are linked using wikilinks [migrated]
- [ ] File moves were verified successful [migrated]
- [ ] No content was lost during consolidation [migrated]
- [ ] Emoji prefixes preserved in folder names [migrated]
- [ ] Summary provided to user with before/after counts [migrated]
