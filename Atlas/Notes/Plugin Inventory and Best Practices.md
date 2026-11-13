---
type: note
tags: [music, plugins, mixing, reference]
created: 2026-11-13
---

# Plugin Inventory and Best Practices

> **Stale soon (Nov 13, 2026):** Dave is moving his plugins from a shared drive to local storage. Rescan `/Library/Audio/Plug-Ins` after the move and rebuild the inventory. The best-practices section should still hold.

What's installed on Dave's Mac (scanned Nov 13, 2026 from `/Library/Audio/Plug-Ins`) and which plugin to reach for first. Companion to [[Mixing and Mastering Cheat Sheet]], [[Genre Production Guide]] and [[Samples and Splice Workflow]].

**Main DAW:** Logic Pro (projects in `~/Music/Logic`, including "OT2G Premix Mastering"). An `Ableton` folder exists too, but no Ableton app is installed. Formats installed: AU, VST3, VST, AAX, CLAP (MiniMeters only).

**The big takeaway:** you own far more than you need. Pick one tool per job and learn it, don't browse. See "Short list" at the bottom.

## Inventory by job

Vendor is listed only where the folder or plugin name makes it clear. Anything I'm unsure of is in "Not sure what these are" below.

### Synths and samplers
- **Serum, Serum 2** (Xfer): main workhorse for bass, leads, pads.
- **Vital**: free-style wavetable synth, good Serum alternative.
- **Massive, Massive X, FM8, Absynth 5, Reaktor 6** (Native Instruments): Massive for classic dubstep/electro bass, FM8 for FM bass and bells, Absynth for atmospheres.
- **Kontakt 5/7/8, Battery 4, Maschine 2**: samplers and drum machines. **Komplete Kontrol** is the wrapper for NI instruments.
- **Arturia V Collection**: Prophet-5 V, Jup-8 V4, CS-80 V, Mini V, Matrix-12, Synclavier, DX7 V, Wurli V, Stage-73, B-3, Piano V, Mellotron V, Solina V, and more. **Analog Lab V** browses them all. **MiniFreak V** and **Acid V** also present.
- **Augmented** series (strings, voices, grand piano, brass): quick orchestral beds.
- **Splice INSTRUMENT**, **LANDR Sampler**: sound libraries and sampling.

### Compressors and dynamics
- **Arturia Comp FET-76** (1176-style), **Comp DIODE-609**, **Comp TUBE-STA** (Fairchild/Pultec style), **Comp VCA-65** (dbx style).
- **Solid Bus Comp / Solid Dynamics** (NI): SSL-style bus compression.
- **Goodhertz Vulf Compressor**: tape-style "vulf" compression, great on drums and parallel.
- **Melda** `MCompressor`, `MRatio` (and `MRatioMB`, multiband), plus **Bus FORCE / PEAK / TRANSIENT** (Arturia) and Audified **U73b**.
- **Duck**, **Poltergate** (gate), **Smooth Operator Pro**: dynamics helpers.

### EQs
- **Solid EQ, Passive EQ, Enhanced EQ** (NI), **EQ SITRAL-295** (Arturia, Siemens style), **Audified 1A Equalizer**.
- **Melda MEqualizer**, **Goodhertz Tone Control / Tiltshift / Lohi**.
- Logic's own **Channel EQ** also covers surgical work.

### Saturation, distortion and tape
- **Soundtoys Decapitator** (the go-to saturator for drums, bass, vocals).
- **Arturia Tape J-37, TAIP**, **Dist TUBE-CULTURE / OPAMP-21 / COLDFIRE**, **Pre 1973 / Pre V76 / Pre TridA** (console preamps), **Tape MELLO-FI**, **Audified U78 Saturator**, **Super VHS**.
- **Melda MSaturator, MWaveFolder, MWaveShaper**.
- **Guitar Rig 5/6** (NI), **Supercharger/Supercharger GT**, **Driver**, **Dirt**, **Bite**: guitars, distortion, amp sim.

### Reverbs, delays and space
- **Soundtoys LittlePlate** (plate), **Arturia Rev PLATE-140, SPRING-636, LX-24 (Lexicon-style), INTENSITY**, **Raum** (NI), **Linda IronVerb**, **Goodhertz Megaverb**, **Melda MConvolutionEZ / MCharmVerb**.
- **Delays:** Arturia **Delay TAPE-201, BRIGADE, ETERNITY**; NI **Replika / Replika XT**; Melda MDelay.
- **Efx AMBIENT / FRAGMENTS / MOTIONS / REFRACT** (Arturia) and **Texturize**: textures and shoegaze washes.

### Modulation, pitch and creative
- **Soundtoys LittleAlterBoy** (vocal pitch/formant), **Tremolator**, **LittleRadiator**.
- **Arturia Chorus JUN-6 / DIMENSION-D, Flanger BL-20, Phaser BI-TRON, Rotary CLS-222, Pitch SHIFTER-910.**
- **Waves Tune Real-Time** and **Key Detector** (Waves; the full Waves shells are installed so more may be available through Waves Central).
- **VocAlign 6 Pro** (aligns doubles/backing vocals to the lead). **LANDR VoxChain, Stems, FX Bass, Composer, Mastering Pro, ReHance.**
- **Super VHS, Pure LoFi, Pitch Drift, Wow Control (Goodhertz), Lossy (Goodhertz)**: lo-fi flavors.

### Bass and low end
- **SubCulture, Sub Generator, Bass XXL**: the names suggest bass/sub tools. I didn't verify what they do; try them on a bass line.
- **Goodhertz Lohi, Midside, Midside Matrix** for mono-ing and M/S work.

### Mastering and metering
- **iZotope Ozone 10 and Ozone 11 Elements.**
- **LANDR Mastering Pro**, **Goodhertz Faraday Limiter, Good Dither, Loudness**.
- **MiniMeters** (8 meters: spectrum, spectrogram, stereometer, loudness, waveform, VU, scope). Install it on the master bus and leave it open.
- **Youlean Loudness Meter 2**, **Melda MLoudnessAnalyzer / MAnalyzer / MOscilloscope**.
- **Audified MixChecker / MixChecker Ultra**: checks the mix on simulated phone, laptop and car speakers. Best use: final checks before export.
- **Headphone Lab** (NI) and **Perfect Room 2**: room/headphone simulation. Use them for checks, not as a substitute for real monitors.

### Melda MeldaProduction folder
A big set of Melda utility plugins (the `M`-named ones appear to be their free effects): `MCompressor`, `MEqualizer`, `MDelay`, `MPhaser`, `MFlanger`, `MFreqShifter`, `MRingModulator`, `MStereoExpander`, `MTuner`, `MMetronome`, `MNotepad`, etc. Fine for utility work, but you don't need them if the tools above cover the job.

### Not sure what these are
`Atoms`, `Beat Slammer`, `Comeback Kid`, `Dragon Fire`, `God Mode`, `Humanoid`, `IHNY-2`, `Magic Dice`, `Magic Switch`, `Parallel Aggressor`, `Phasis`, `Spaced Out`, `Warp`, `Transit 2`, `Valvekult3L`, `Model5000L`, `PythorL`, `Rekraft-L`, `Samplex3-L`, `RX950`, `Rotary`, `Crystalline`, `Flair`, `Freak`, `Choral`, `Mix DRUMS`, `Bad Tape 2`, `Texturize`, `Motion Filter`. I didn't verify what each does. Open them once, play a loop through them, and note keepers here.

## Best practices

1. **One tool per job.** Don't stack three compressors because you have them. Choose by *color*: clean (Solid, Melda), punchy (FET-76, DIODE-609), smooth (TUBE-STA, VCA-65), crunchy (Decapitator).
2. **Saturation early, not late.** A little Decapitator or TAIP on drums, bass and vocals adds harmonics that help sounds cut through on small speakers. Keep Drive low, level-match with the Mix knob.
3. **Place EQ both before and after compression.** Before: remove what shouldn't trigger the compressor (low rumble). After: shape the finished tone.
4. **Use sends for reverb and delay.** Reverbs: one short plate (LittlePlate or Rev PLATE-140), one longer hall/room. Delays: tape (TAPE-201 or Replika) for warmth and tempo-synced.
5. **Mono the sub.** Use Goodhertz Lohi/Midside (or Logic's Gain plug-in) to keep content under ~100-120 Hz centered.
6. **Metering.** MiniMeters on the master bus for spectrum and stereo, Youlean or Ozone's loudness readout for LUFS. Watch the LUFS target in [[Mixing and Mastering Cheat Sheet]].
7. **Check the mix on bad speakers.** MixChecker Ultra at the end, and always check in mono.
8. **CPU and organization.** You have the same plugin as AU, VST3 and VST. In Logic, use the **AU** version. Freeze heavy synth tracks, bounce to audio when you're done editing, and don't run 20 Kontakt instances.
9. **Mastering plugins aren't a fix.** Ozone/LANDR can add polish but won't rescue a muddy mix. Master from a mix with peaks around -6 dBFS. Use the limiter last.
10. **Save your own presets** for chains you like (vocal chain, drum bus, master) so you don't rebuild every session.

## Short list (what to learn first)

| Job | First pick |
|-----|-----------|
| Synth | Serum 2 (plus Vital) |
| Drum bus | Solid Bus Comp, Vulf Compressor, Decapitator |
| Vocal comp | Comp FET-76 then Comp VCA-65 |
| Vocal pitch and character | LittleAlterBoy, Waves Tune Real-Time, VocAlign for doubles |
| Saturation | Decapitator, TAIP, Tape J-37 |
| Reverb | LittlePlate or Rev PLATE-140, plus Rev LX-24 for a bigger space |
| Delay | Delay TAPE-201, Replika XT |
| Guitar | Guitar Rig 6 |
| Glue / master | Solid Bus Comp, Ozone, Faraday Limiter |
| Metering | MiniMeters, Youlean, MixChecker |

## Open

- Open each "not sure" plugin and note what it does.
- Decide whether you'll stay on Logic only. No Ableton app is installed, so the `Ableton` folder in `~/Music` is probably old.
