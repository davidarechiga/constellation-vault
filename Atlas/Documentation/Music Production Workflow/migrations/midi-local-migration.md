# MIDI Local Migration

## Objective

Make drum MIDI available from the local Ableton User Library first, so grooves can be tested with the installed DRUMS plug-in without waiting for the entire external MIDI archive.

## Verified migration slice

| Field | Value |
|---|---|
| Date | 2026-11-20 |
| Collection | LoudstakkMetalVSPunkMIDICollection1 |
| Source | `/Volumes/Storage 2TB/Music Production & Performance/Ableton/User Library/MIDI/LoudstakkMetalVSPunkMIDICollection1` |
| Destination | `/Users/davidarechiga/Music/Ableton/User Library - Local Test/MIDI/LoudstakkMetalVSPunkMIDICollection1` |
| Source MIDI count | 2,322 |
| Destination MIDI count | 2,322 |
| Verification | `rsync --dry-run --itemize-changes` returned no differences |
| Source disposition | Preserved; nothing deleted or moved |
| Status | Complete; playback tested successfully in Ableton |

`.DS_Store` metadata was excluded from the copy. MIDI files and the collection's supporting folder structure were preserved.

## Why this collection moved first

The source MIDI tree contains 23,161 MIDI clips. Most are not drum grooves: `ldrolez-free-midi-chords-main` alone contains 17,988 files. Copying the entire tree delayed the immediate goal because thousands of tiny files create high filesystem overhead even though their total byte size is modest.

The migration was therefore narrowed to the 2,322-file Loudstakk drum collection. This makes useful material available now and keeps the larger archive migration optional.

## Ableton test path

1. In Ableton's browser, open the local User Library.
2. Navigate to `MIDI/LoudstakkMetalVSPunkMIDICollection1`.
3. Create or select a MIDI track containing the DRUMS plug-in.
4. Drag a copied groove onto the track.
5. Confirm note mapping, tempo behavior, playback, and whether kick/snare/cymbal articulations land on the expected pads.

If a groove plays but triggers the wrong drums, the transfer is still valid; that indicates a drum-map mismatch between the MIDI pack and the plug-in, not file corruption.

## Test result

Dave confirmed on 2026-11-20 that the copied MIDI plays successfully. The Loudstakk note mapping does not match the DRUMS plug-in's layout, but Dave can handle that remapping. This is a compatibility detail, not a migration failure.

## Remaining library

The earlier full-tree copy was intentionally stopped after the drum collection was prioritized. Some additional files may already be present locally from that partial pass, but no other collection is considered migrated until its source and destination counts and dry-run comparison are recorded here.

Next candidates should be migrated one collection at a time, in this order only if they are useful to the workflow:

1. Niko's Free MIDI Pack — 1,476 files
2. Chords and Progressions — 1,324 files
3. HIJIKI 50 Neo-Soul MIDI Chord Progressions — 52 files
4. Vocal Exercises — 12 files
5. `ldrolez-free-midi-chords-main` — 17,988 files; defer unless there is a clear need
