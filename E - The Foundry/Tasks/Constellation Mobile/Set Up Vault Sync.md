---
status: done
priority: medium
tags:
  - task
  - personal
projects:
  - "[[Constellation Mobile]]"
due: 2026-03-31
completedDate: 2026-03-19
taskSourceType: taskNotes
owner: David
---

# Set Up Vault Sync (Phase 4)

- [ ] Configure iCloud/Dropbox sync on server
- [ ] Enable sync on mobile device
- [ ] Test bidirectional file updates
- [ ] Document sync workflow

**Why matters**: Vault sync ensures changes made via Claude Code on the server appear on the mobile Obsidian app and vice versa. Without this, you'd have two diverging copies.

**Done when**: Changes made via Claude Code on server appear in Obsidian mobile app within minutes, and changes in mobile app sync back to server.

**Related**: [[Constellation Mobile]] • [[integrate-claude-code]]

---

## Sync Options to Evaluate
- **iCloud** — Already syncing vault via iCloud. Server needs iCloud Drive access.
- **Dropbox** — Alternative if iCloud is unreliable on Linux server.
- **Git** — Most robust but requires commit discipline. Good for version history.