# Music production software inventory

Last inspected: **2026-11-20**

This is a machine-verified inventory, not a purchase or license history. Presence means software or a plug-in bundle was found on disk; it does not yet guarantee activation, current licensing, Apple Silicon compatibility, or successful loading in every host.

## Installed hosts and workflow applications

| Application | Version found | Category | Verification status |
| --- | --- | --- | --- |
| Ableton Live 12 Suite | 12.4.16 | DAW / performance | Verified running and scanning plug-ins |
| Logic Pro | 13.0 | DAW | Installed; host compatibility pending |
| Logic Pro Creator Studio | 13.0 | DAW variant | Installed; relationship to Logic Pro pending |
| MainStage Creator Studio | 5.0 | Live performance host | Installed; compatibility pending |
| Reason 14 | 14.1d100 build 20457 | DAW / rack host | Installed |
| rekordbox | 7.2.18.0311 | DJ library / performance | Installed |
| djay Pro | Pending | DJ library / performance | Installed |
| OBS | 32.1.0 | Capture / streaming | Installed |
| TouchDesigner | Pending | Visual performance / AV | Installed |
| Splice | 5.4.14 | Samples and software | Installed |
| Splice INSTRUMENT | 3.1.1 | Software instrument | Installed |
| LANDR | Pending | Reference / mastering services | Installed |
| MiniMeters | Pending | Metering / visualization | Installed |
| KeyFinder | Pending | Key analysis | Installed |
| Youlean Loudness Meter 2 | Pending | Loudness metering | Standalone app and plug-in present |

## Installed managers, licensing, and hardware control

| Application | Version found | Purpose | Status |
| --- | --- | --- | --- |
| Arturia Software Center | 2.13.0 | Arturia install and activation | Verified running |
| AudioFuse Control Center | 2.2.1 | Arturia interface control | Hardware state pending |
| Baby Audio Manager | Not exposed | Baby Audio install manager | Installed |
| Native Access | Pending | Native Instruments install and activation | Installed |
| MPluginManager | Pending | MeldaProduction install manager | Installed |
| iLok License Manager | Pending | PACE licensing | Installed |
| Reason Companion | 3.2.0 | Reason install and account manager | Installed |

The application scan also found separate Creator Studio variants of Logic Pro, MainStage, and Final Cut Pro. Their relationship to the standard installations needs verification before they are treated as distinct production tools.

## System plug-in bundle counts

| Location | Format | Top-level bundles |
| --- | --- | ---: |
| `/Library/Audio/Plug-Ins/Components` | Audio Unit v2 | 260 |
| `/Library/Audio/Plug-Ins/VST` | VST2 | 185 |
| `/Library/Audio/Plug-Ins/VST3` | VST3 | 196 |
| `/Library/Application Support/Avid/Audio/Plug-Ins` | AAX | 93 |
| `/Library/Audio/Plug-Ins/CLAP` | CLAP | 9 |
| `~/Library/Audio/Plug-Ins/Components` | Audio Unit v2 | 0 |
| `~/Library/Audio/Plug-Ins/VST` | VST2 | 0 |

The AU, VST2, and VST3 folders contain **641 format-specific bundles**. After stripping those format extensions and merging exact duplicate names, they produce **284 distinct on-disk names**. That is still not a true product count: Native Instruments surround/output variants, Waves shells, helper plug-ins, and versioned legacy products need normalization.

The user VST3 path was not present in the first scan. Reason Rack Extensions, standalone content libraries, Max for Live devices, presets, sample libraries, audio drivers, MIDI utilities, and hardware firmware/control software still need dedicated passes.

See [the plug-in catalog](plugin-catalog.md) for vendor families and normalization work.

## Verified compatibility events

- Arturia FX Collection 6 resources were repaired through Arturia Software Center on 2026-11-20.
- Rev PLATE-140 AU restores in the current Ableton template.
- Rev SPRING-636 VST3 1.6.1.6566 loads and creates as an active device in Ableton Live 12.4.16.
- See [the Arturia recovery record](../arturia-fx-recovery.md) for evidence and remaining checks.

## Next inventory passes

1. Enumerate every AU, VST2, VST3, and AAX bundle by vendor, product, version, architecture, and code-signing state.
2. Reconcile duplicates across formats into one product record while preserving backward-compatibility requirements.
3. Inventory DAWs, plug-in managers, audio/MIDI utilities, drivers, and control-panel software.
4. Inventory Ableton Packs, Max for Live devices, templates, User Library content, and external sample libraries.
5. Record license/activation state only through each vendor's supported manager or a successful host load.
6. Classify each product: current, legacy-required, replaceable, unverified, or removal candidate. Removal always requires a separate compatibility decision.
