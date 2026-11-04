@AGENTS.md

## Claude Code notes

- You own git maintenance for this vault. Obsidian Sync handles device sync and the Obsidian Git plugin is not used, so you commit and push, including snapshots of Dave's edits. Follow the "Commit and sync rules" in `AGENTS.md`. If git gets stuck (merge conflict, diverged branch), resolve it without losing notes and push.
- The skills in `.claude/skills/` (`/morning`, `/evening`, `/weekly`, etc.) and `.claude/rules/` were written for the pre-reset ACE layout and point at folders that now live in `Starting Over Archive/`. Don't trust their paths until they're updated.

## Vault structure (ACE, set Nov 3, 2026)

Rules for any AI agent working in this vault:

- Never create files at the vault root.
- `+ Inbox/` is the only intake. Process inbox items by moving them to:
  - `Atlas/Notes/`: atomic knowledge
  - `Atlas/Sources/`: reference material
  - `Efforts/<state>/` (`On`, `Ongoing`, `Simmering`, `Sleeping`): active work
  - `Calendar/Daily/`: date-based notes
- Never delete notes. If unsure where something goes, leave it in `+ Inbox/` and flag it.
- Never modify `.obsidian/` without explicit instruction.
- Every folder has a folder note named after it (`Atlas/Atlas.md`, `+ Inbox/+ Inbox.md`, etc.). Keep them, even when empty. They'll become that folder's index, overview and progress tracker. When processing the inbox, skip `+ Inbox.md`.
