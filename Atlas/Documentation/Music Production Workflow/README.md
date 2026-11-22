# Music Production System Documentation & Migration

This vault folder is the canonical working record for the computer's music-production environment: installed software and plug-ins, Ableton workflow and migration history, compatibility incidents, and Dave's personalized mixing and mastering documentation.

## Documentation map

- [Installed software inventory](inventory/music-production-software.md) — machine-verified applications and plug-in formats
- [Plug-in catalog](inventory/plugin-catalog.md) — vendor families, installed products, and normalization caveats
- [MIDI local migration](migrations/midi-local-migration.md) — verified migration slices, source preservation, and remaining work
- [Storage and project lifecycle](workflows/storage-and-project-lifecycle.md) — external archive, local active-work policy, and project migration checklist
- [Arturia FX incident and recovery](arturia-fx-recovery.md) — diagnosis, repair, and remaining compatibility checks
- [Personalization profile](personalization-profile.md) — confirmed details that should shape recommendations for Dave
- [Claude/Codex collaboration protocol](COLLABORATION.md) — ownership, handoffs, and rules that prevent duplicate or conflicting documents
- [Mixing and Mastering Guide](Mixing%20and%20Mastering%20Guide.md) — canonical cheatsheet, currently maintained with Claude

## Current status

- Ableton Live version under test: **12.4.16**
- Arturia software instruments: generally working
- Arturia FX Collection 6: repaired through Arturia Software Center on 2026-11-20
- Root cause identified on 2026-11-20: the relocated Arturia data tree contained incomplete product folders for the affected FX
- Rev PLATE-140 AU restore and Rev SPRING-636 VST3 creation both pass in Ableton Live 12.4.16
- Post-repair audit: every current Arturia FX folder has install metadata, populated resources, and a cached VST3 executable
- Nine unrelated Arturia updates remain and were intentionally not included in the FX repair
- Loudstakk Metal vs Punk drum MIDI collection: **2,322 of 2,322 clips copied and verified locally** on 2026-11-20
- Loudstakk MIDI playback tested successfully; its original mapping does not match DRUMS, but Dave can handle the remapping
- The larger MIDI library migration is paused; the 17,988-file chord archive and other non-drum collections remain lower priority
- Storage policy confirmed: the external drive is primarily the archive; ongoing work and projects brought back into use live locally
- Google Drive is the preferred backup-backed location for active projects; a dedicated folder name is proposed but not yet created
- No files have been deleted and no Ableton cache has been reset

## Project boundary

Everything produced by Claude and Codex for this project belongs in this folder. Link to legacy notes elsewhere instead of maintaining competing current copies.

## Safety rule

Do not delete the current plug-ins, Ableton database, or `/Users/Shared/Arturia` tree. The repair succeeded in place; preserve the working symlink and populated product folders while the remaining project-compatibility checks are completed.
