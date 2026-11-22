# Storage and Project Lifecycle

## Working rule

**External storage is primarily the archive. Local storage is the active workspace.**

New and ongoing projects should be worked on locally. When an existing archived project becomes active again, copy its complete project folder to local storage, validate the local copy, and work from that copy. Do not edit the archived copy in place.

This policy favors day-to-day stability and performance while keeping older projects available without crowding the local drive.

## Storage roles

| Location | Role | Expected contents |
|---|---|---|
| Local Google Drive storage | Active project workspace | Ongoing projects, project-owned recordings, and working exports |
| Local Ableton User Library | Active reusable assets | Currently needed MIDI, presets, racks, and other reusable content |
| `/Volumes/Storage 2TB/Music Production & Performance/Ableton` | Archive | Inactive projects, older libraries, preserved source material, and completed project snapshots |

## Proposed active-project folder

Google Drive for desktop is currently mounted at:

`/Users/davidarechiga/Library/CloudStorage/GoogleDrive-archiestencils@gmail.com/My Drive`

Recommended dedicated project root:

`/Users/davidarechiga/Library/CloudStorage/GoogleDrive-archiestencils@gmail.com/My Drive/Music Production/Active Ableton Projects`

This folder is **proposed, not yet created or confirmed**. An existing `My Drive/C Files/Ableton` folder contains templates and sample-library material, so active projects should not be mixed into it.

A second dated Google Drive mount also exists at `GoogleDrive-archiestencils@gmail.com (9-11-26 23:21)`. Do not use that duplicate-looking mount for new project work unless its role is deliberately confirmed. The undated, current mount above is the working candidate.

## Google Drive safeguards

Cloud synchronization adds an off-computer copy, but it is not the same as an independent archive: accidental deletion or corruption can synchronize too. The external archive remains the preserved project snapshot.

For every active Ableton project in Google Drive:

- Mark the complete project folder **Available offline**. Never rely on streamed placeholders for an active set or its audio.
- Open the set on only one computer at a time. Let Google Drive finish syncing before opening it elsewhere.
- Wait for sync completion after closing Ableton and before shutting down, disconnecting, or re-archiving.
- Keep the entire Ableton project together. Do not place the `.als` file in Drive while leaving project-owned recordings in an untracked temporary folder.
- Resolve Google Drive conflict copies manually; do not assume the newest modification date contains every edit.
- Keep the Ableton User Library local. Sync project folders through Google Drive, not the entire live User Library database and its thousands of small reusable assets.
- Continue using the external archive for verified inactive snapshots. Google Drive protects active access; it does not replace the archive lifecycle.

## Activate an archived project

Use this workflow whenever an older project is brought back into active work.

1. **Identify the complete project folder.** Include the `.als` file and its Project Info, Samples, recorded audio, presets, and other project-owned subfolders.
2. **Copy the project folder to local storage.** Keep the external archive unchanged during activation.
3. **Make the Google Drive project folder available offline and wait for download completion.**
4. **Open the local `.als` file.** Confirm Ableton's title bar or Recent Sets entry points to the local Google Drive copy, not the external drive.
5. **Resolve missing media.** Use Ableton's file manager if required. Do not save over the archived set while resolving files.
6. **Verify plug-ins.** Confirm important instruments and effects load, presets restore, and relocated resources are found.
7. **Use Collect All and Save when needed.** Collect samples that are required for portability, especially files referenced from temporary, download, desktop, or external-library locations. Avoid needlessly duplicating large factory libraries.
8. **Run a playback check.** Test the beginning, a dense section, automation, tempo changes, and any important resampling or routing.
9. **Continue work only from the local copy.** Treat it as the active version for the duration of the work cycle.

## Archive an active project

Archiving is a separate, deliberate operation. Do not automatically overwrite the preserved external copy.

1. Save and close the local project.
2. Wait for Google Drive to finish synchronizing the project.
3. Confirm the project opens cleanly and contains the intended media.
4. Decide whether this is a new archived revision or a replacement for an older snapshot.
5. Copy the complete local project folder to the external archive using a clearly distinguishable project or revision name.
6. Compare the source and archived copy before considering the archive current.
7. Keep the local copy until the archived revision has been verified and no immediate work remains.

Deletion is not part of the normal activation or archive workflow. Cleanup should be a separate decision after verification.

## Version-authority rule

Only one copy should be treated as editable at a time:

- **Archived:** external copy is the preserved reference; no active local working copy is assumed.
- **Active:** local copy is authoritative for new edits; external copy remains a preserved snapshot.
- **Ready to re-archive:** local work is complete but has not yet been verified on the external drive.

If both copies have been edited, stop and compare them before saving or copying either direction. Modification dates alone are not enough to decide which work should win.

## Libraries and reusable assets

Reusable content can be migrated in useful slices rather than all at once. The Loudstakk drum MIDI collection is the first verified example: 2,322 clips were copied locally and tested, while the much larger chord archive remains external.

The same principle applies to samples, presets, racks, and packs:

- Keep locally what is actively used or required by current projects.
- Keep archival or rarely used material on the external drive.
- Copy and verify a complete, named collection when it becomes useful.
- Record each completed migration in this documentation folder.

## Project activation record

For each migrated project, record:

```text
Project:
Activation date:
Archived source:
Local working copy:
Primary .als opened:
Missing media: none | resolved | unresolved
Plug-in issues: none | details
Collect All and Save: not needed | completed | intentionally skipped
Playback verification:
Archive remains unchanged: yes | no
Status: active | ready to re-archive | archived
```
