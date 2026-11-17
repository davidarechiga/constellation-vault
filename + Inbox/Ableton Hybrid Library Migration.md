---
aliases:
  - Ableton Library Migration
tags:
  - music-production
  - ableton
  - checklist
type: project
status: active
created: 2026-11-14
modified: 2026-11-14
---

# Ableton Hybrid Library Migration

## Goal

Keep performance-critical software and content local while preserving the SMB share for large shared assets, backups, and files that should remain accessible from iPhone and iPad.

## Current safe state

- [x] Original Ableton and instrument files preserved on the SMB drive
- [x] Ableton User Library copied to the Mac for testing
- [x] Ableton temporarily pointed to the local User Library
- [x] Arturia resource location changed to `/Users/Shared/Arturia`
- [x] Arturia plug-ins installed locally
- [x] Native Instruments plug-in files installed locally
- [x] Native Access applications remain on the Mac
- [x] Native Instruments content remains configured on the SMB share
- [x] No original shared libraries deleted
- [ ] Confirm the SMB drive reconnects normally

## Current next action — Arturia

- [ ] Install one Arturia instrument individually
- [ ] Open its standalone application
- [ ] Load several presets and play for a few minutes
- [ ] Open the same instrument in Ableton
- [ ] Save, close, and reopen the Ableton project
- [ ] Repeat the test with the SMB share disconnected
- [ ] If successful, install **V Collection 11 Pro**
- [ ] Install the newest activated **FX Collection**
- [ ] Skip products marked **Expired** or **Not activated**
- [ ] Install legacy versions only when an older project specifically needs them
- [ ] Keep the original Arturia folder on the SMB drive

## Native Instruments — paused for now

No additional SSD is being added yet. Do not relocate or reinstall the Native Instruments library at this stage.

- [x] Keep Native Instruments applications and plug-ins on the Mac
- [x] Leave large Kontakt, Maschine, Reaktor, and expansion content on the SMB share
- [ ] Mount the SMB share before opening projects that use Native Instruments libraries
- [ ] Avoid **Install All** while internal storage is limited
- [ ] If Kontakt causes freezes, note the affected library and stop the test
- [ ] Preserve the existing Native Instruments folder on the SMB share
- [ ] Keep mobile-friendly WAV files, stems, MIDI, and exports in shared folders

### Future option: dedicated Native Instruments SSD

Revisit only when desired or when network streaming becomes too unreliable.

- [ ] Inventory the existing NI library before purchasing a drive
- [ ] Consider a 2 TB minimum or 4 TB external SSD
- [ ] Use a directly attached USB-C or Thunderbolt SSD
- [ ] Format it as APFS, non-case-sensitive, with GUID Partition Map
- [ ] Copy and verify libraries before changing Native Access
- [ ] Use Native Access **Add Product Content** or **Locate**
- [ ] Test Kontakt standalone and in Ableton with SMB disconnected
- [ ] Keep SMB originals as backup until the new setup is fully proven

## Final hybrid setup

- [ ] Keep plug-in applications and plug-in files on the Mac
- [ ] Keep Arturia resources on the Mac
- [ ] Decide whether the tested local Ableton User Library becomes permanent
- [ ] Keep large general sample collections and mobile-accessible assets on SMB
- [ ] Keep shared WAV files, stems, MIDI, presets, and exports accessible to iPhone and iPad
- [ ] Configure reliable SMB mounting
- [ ] Confirm the Mac and any future external drive are included in backups

## Safety rules

- [ ] Do not delete the original Ableton library
- [ ] Do not delete the SMB Arturia folder
- [ ] Do not delete or relocate the SMB Native Instruments libraries
- [ ] Do not manually drag installed plug-in files between system folders
- [ ] Do not use **Install All** indiscriminately
- [ ] Do not finalize the Ableton library switch until projects pass testing

## Notes

- Native Access currently points its content location to `/Volumes/Storage 2TB/Music Production & Performance/Native Instruments`.
- The external-SSD migration is intentionally deferred.
- Immediate focus: finish and verify the Arturia local installation.
