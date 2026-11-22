# Arturia FX incident and recovery plan

## Symptom

Arturia instruments load, but affected Arturia audio effects failed to instantiate in Ableton Live 12.4.7. The representative Rev PLATE-140 repair was subsequently verified in Live 12.4.16.

Confirmed examples:

- Rev PLATE-140 AU fails to restore and create.
- Rev PLATE-140 VST3 loads its processor binary, then fails during processor initialization.
- Rev SPRING-636 VST3 fails at the same initialization step.

## Evidence and diagnosis

The Arturia data location is currently redirected:

```text
/Library/Arturia -> /Users/Shared/Arturia
```

That link was created on **2026-11-13 at 21:58:56**. Ableton 12.4.6 restored Rev PLATE-140 successfully earlier on November 13, then logged its first restore failure at 22:27 that night. Live 12.4.7 continues to fail.

The affected relocated product folders are incomplete. For example, `/Users/Shared/Arturia/Rev PLATE-140` has:

- zero files in `Install`
- zero files directly or recursively under `resources`
- an empty `Rev PLATE-140.vst3/Contents/MacOS` directory

By contrast, a working, later-reinstalled instrument such as Prophet-VS V has install metadata, thousands of resource files, and a complete cached VST3 bundle. This explains the instrument/FX split: many instruments were repopulated after the relocation, while the older FX folders were not.

The AU and VST3 bundles in `/Library/Audio/Plug-Ins` are present. Ableton can discover them, but the plug-ins depend on their matching `/Library/Arturia/<product>` resources during initialization.

Code-signature verification currently reports modified/invalid signatures for both tested FX and tested working instruments. That is therefore not the discriminator for this incident, though a clean reinstall should also restore vendor-authentic bundles and is preferable to ad-hoc re-signing.

## Originally incomplete Arturia FX folders

The pre-repair audit found these FX product folders with no install metadata, no resource files, and no cached VST3 executable. They were repopulated by the FX Collection 6 repair on 2026-11-20:

- Bus EXCITER-104
- Bus FORCE
- Bus PEAK
- Bus TRANSIENT
- Chorus DIMENSION-D
- Chorus JUN-6
- Comp DIODE-609
- Comp FET-76
- Comp TUBE-STA
- Comp VCA-65
- Delay BRIGADE
- Delay ETERNITY
- Delay TAPE-201
- Dist COLDFIRE
- Dist OPAMP-21
- Dist TUBE-CULTURE
- EQ SITRAL-295
- Efx AMBIENT
- Efx FRAGMENTS
- Efx MOTIONS
- Efx REFRACT
- Filter M12
- Filter MINI
- Filter MS-20
- Filter SEM
- Flanger BL-20
- Mix DRUMS
- Phaser BI-TRON
- Pitch SHIFTER-910
- Pre 1973
- Pre TridA
- Pre V76
- Rev PLATE-140
- Rev SPRING-636
- Rotary CLS-222
- Tape J-37

Several legacy instrument folders are also incomplete (for example CS-80 V3, Memory V, Mini V3, Piano V2, Prophet V3, SEM V2, and Wurli V2). They should be treated separately from the current instrument versions.

Newer FX with populated relocated folders include Rev LX-24, Rev INTENSITY, and Tape MELLO-FI. They are useful controls when testing.

## Staged recovery

1. Quit Ableton Live before installing or changing plug-ins.
2. In Arturia Software Center, reinstall **Rev PLATE-140 only** as the representative repair.
3. Verify that its relocated product folder now contains install metadata, resource files, and a VST3 executable.
4. Start Ableton and force a plug-in rescan from Settings > Plug-Ins (hold Option while clicking Rescan for a full rescan).
5. In a disposable Live Set, load the VST3 version of Rev PLATE-140 on an audio track and pass audio through it.
6. Save, close, reopen, and confirm the device restores correctly.
7. Test the AU version only if AU compatibility is needed for older projects.
8. If the representative repair passes, reinstall the remaining incomplete FX through Arturia Software Center in manageable batches.
9. After each batch, rescan and test one plug-in from that batch before proceeding.

## Controlled repair result — 2026-11-20

Rev PLATE-140 was updated individually through Arturia Software Center to 1.7.1.6566.

Before repair, its relocated folder contained zero install files, zero resource files, and no cached VST3 executable. After repair it contained:

- 6 install metadata files
- 625 resource files
- 1 cached VST3 executable

Ableton Live 12.4.16 then opened the current template and restored the existing Rev PLATE-140 AU instance successfully. The device appeared active on return track `B-Rev PLATE-140`, and the Arturia plug-in window opened with the saved `AH - Warm Vintage Plate` preset. The Live log records `Audio Unit v2: Restored: Rev PLATE-140` with no corresponding failure in that launch.

This validated the diagnosis and the repair method.

## FX Collection batch result — 2026-11-20

Arturia Software Center then completed the FX Collection 6 Pro update queue. The collection contains 39 products; the updater repaired every FX that it marked as needing an update and finished without a reported installation error. Nine unrelated Arturia updates remained afterward and were intentionally left alone.

The post-repair filesystem audit found nonzero install metadata, resource files, and one cached VST3 executable for every current FX product. Representative counts include:

| Product | Install files | Resource files | VST3 executables |
| --- | ---: | ---: | ---: |
| Comp FET-76 | 5 | 537 | 1 |
| Delay BRIGADE | 5 | 387 | 1 |
| Efx FRAGMENTS | 5 | 326 | 1 |
| Filter MINI | 5 | 357 | 1 |
| Pre 1973 | 5 | 341 | 1 |
| Rev PLATE-140 | 4 | 625 | 1 |
| Rev SPRING-636 | 6 | 500 | 1 |

Ableton Live 12.4.16 completed a 226-of-226 plug-in scan after the batch. With the browser filtered to VST3, `Rev SPRING-636` appeared as a single result and loaded successfully as an active device on the test audio track. The Live log records version 1.6.1.6566 as `plugin processor successfully loaded` followed by `Created: Rev SPRING-636`. This directly clears the earlier VST3 processor-initialization failure.

The documentation workflow now treats the FX repair itself as complete. Remaining work is compatibility validation: reopen representative older projects, confirm their AU/VST2/VST3 variants restore, and record which legacy formats must remain installed.

## Avoid for now

- Do not manually copy a working instrument's files into an FX folder.
- Do not ad-hoc code-sign the Arturia bundles.
- Do not delete Ableton's entire preferences folder.
- Do not remove VST2 copies until older projects have been inventoried; historical Ableton logs show Rev SPRING-636 projects using VST2 as well as AU and VST3.
- Do not remove the `/Library/Arturia` link while installed products depend on it.

## Success criteria

- Rev PLATE-140 AU restores in the existing template. **Passed 2026-11-20.**
- Rev SPRING-636 VST3 creates as an active Live device. **Passed 2026-11-20.**
- Pass audio through Rev PLATE-140 and Rev SPRING-636, then save/reopen a disposable Live Set to confirm audio processing and state restoration.
- The repaired product folders remain populated after reboot.
- Existing projects using AU, VST2, or VST3 variants open without missing-device warnings.
- A final inventory records which formats are retained for backward compatibility.
