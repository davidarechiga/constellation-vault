# Plug-in catalog

Last inspected: **2026-11-20**

This catalog groups the raw AU, VST2, VST3, AAX, and CLAP bundles into product families. It is intentionally conservative: a bundle on disk is **installed**, not automatically activated, licensed, compatible, or preferred.

## Scan summary

| Measurement | Count |
| --- | ---: |
| Audio Unit v2 bundles | 260 |
| VST2 bundles | 185 |
| VST3 bundles | 196 |
| AAX bundles | 93 |
| CLAP bundles | 9 |
| Distinct AU/VST2/VST3 names before product normalization | 284 |

## Product families found

### Arturia

The scan found 91 distinct Arturia names across instruments and effects. Current instruments include Acid V, Analog Lab V, the Augmented series, CS-80 V4, Jup-8 V4, Mini V4, MiniFreak V, Prophet-5 V, Prophet-VS V, SQ80 V, Synthx V, and others. FX Collection products include the Bus, Chorus, Compressor, Delay, Distortion, Efx, EQ, Filter, Flanger, Mix, Phaser, Pitch, Preamp, Reverb, Rotary, and Tape families.

Legacy parallel versions remain installed, including CS-80 V3, Mini V3, Piano V2, Prophet V3, SEM V2, and Wurli V2. Do not remove them until old Live Sets have been checked. The complete relocated-resource audit is documented in [the Arturia recovery record](../arturia-fx-recovery.md).

### Baby Audio

Installed products found: Atoms, BA-1, BA-1 FX Strip, Beat Slammer, Comeback Kid, Crystalline, Humanoid, IHNY-2, Magic Dice, Magic Switch, Parallel Aggressor, Pitch Drift, Smooth Operator Pro, Spaced Out, Super VHS, TAIP, Transit 2, and Warp.

### Native Instruments

Installed families found: Absynth 5, Battery 4, Bite, Choral, Dirt, Driver, Enhanced EQ, Flair, FM8, Freak, Guitar Rig 5 and 6, Komplete Kontrol, Kontakt 5/7/8, Maschine 2, Massive, Massive X, Passive EQ, Phasis, Raum, RC 24, RC 48, Reaktor 6, Replika, Replika XT, Solid Bus Comp, Solid Dynamics, Solid EQ, SubCulture, Supercharger, and Supercharger GT.

Several entries have stereo, surround, FX, or multi-output variants. Those are formats/configurations, not separate purchases.

### MeldaProduction

The MFreeFX-style collection is present across AU/VST formats, including MAGC, MAnalyzer, MAutoPitch, MCompressor, MConvolutionEZ, MDelay, MEqualizer, MLoudnessAnalyzer, MOscilloscope, MSaturator, MStereoScope, MTuner, MUtility, and related modulation, routing, generator, and analysis tools.

### Goodhertz

Installed products found: CanOpener Studio 3, DC19 3, Faraday Limiter 3, Good Dither 3, Lohi 3, Lossy 3, Loudness 3, Megaverb 3, Midside 3, Midside Matrix 3, Panpot 3, Tiltshift 3, Tone Control 3, Trem Control 3, Tupe 3, Vulf Compressor 3, and Wow Control 3.

### Denise Audio

Installed products found: Bad Tape 2, Bass XXL, Dragon Fire, God Mode, Motion Filter, Perfect Room 2, Poltergate, and Sub Generator.

### LANDR

Installed plug-ins found: Composer, FX Bass, Mastering Pro, ReHance, Sampler, Stems, and VoxChain. Activation and service dependencies are pending.

### Soundtoys

Installed products found: Decapitator, Little AlterBoy, Little Plate, Little Radiator, and Tremolator. Soundtoys shell bundles are also present and should not be counted as additional effects.

### iZotope

Ozone 10 and Ozone 11 Elements bundles were found. Older iZotope preset libraries also exist under `~/Documents/iZotope`; those presets do not prove the matching legacy plug-in is still installed.

### Xfer Records

Serum and Serum 2 are both installed. Their project-compatibility roles need separate testing before the original Serum is considered removable.

### Metering and monitoring

- MiniMeters and its Audio Server, Loudness, Oscilloscope, Spectrogram, Spectrum, Stereometer, VU, and Waveform helpers.
- Youlean Loudness Meter 2.
- Beyerdynamic Headphone Lab.
- Goodhertz CanOpener Studio 3 and Loudness 3.
- Melda MAnalyzer, MLoudnessAnalyzer, MOscilloscope, and MStereoScope.

### Other installed products observed

- Audified: 1A Equalizer, MixChecker, MixChecker Ultra, U73b Compressor, U78 Saturator, and Linda IronVerb.
- Beatskillz / Tone Empire: Rekraft-L, Samplex3-L, LaCreme3L, Model5000L, PythorL, and Valvekult3L.
- Circles Audio: DRUMS preview/beta builds and standalone app.
- Devious Machines: Duck.
- Imaginando: VS2 and VS2fx.
- Inphonik: RX950.
- SoundGhost: Texturize.
- Splice: Bridge, INSTRUMENT, Sounds, and Sounds Listener.
- Synchro Arts: VocAlign 6 Pro.
- Vital Audio: Vital.

## Shells and incomplete enumeration

Waves WaveShell bundles for versions 10, 11, and 14 are installed. A shell does not reveal the licensed product list from its filename, so individual Waves products remain **pending enumeration** through Waves Central or a successful host scan.

Top-level `Audified`, `LANDR`, `MeldaProduction`, and `Soundtoys` VST folders are vendor containers, not individual products. They are excluded from normalized product totals.

## Compatibility labels to add

Each normalized product will eventually receive:

- Installed formats: AU, VST2, VST3, AAX, CLAP, standalone.
- Exact version and CPU architecture.
- Activation/license state.
- Ableton 12.4.16 load result.
- Used by known projects or templates.
- Classification: current, legacy-required, replaceable, unverified, or removal candidate.
- Preferred use in Dave's workflow, if any.
