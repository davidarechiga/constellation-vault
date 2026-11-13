---
type: note
tags: [music, samples, splice, workflow, reference]
created: 2026-11-13
---

# Samples and Splice Workflow

Best practices for sample-based work in Logic Pro with Splice, for [[Sprawling]]. Companion to [[Genre Production Guide]] and [[Plugin Inventory and Best Practices]]. Web research Nov 13, 2026; Splice's own pages are the source for licensing claims, so read the actual terms before a commercial release. This is not legal advice.

## What's installed

- **Splice** desktop app, **Splice INSTRUMENT** (AU/VST3/AAX plus standalone), and **SpliceBridge** (AU/VST3). `~/Splice` holds app data (~580 MB) and an `INSTRUMENT/presets` folder. The local `sounds` folder was empty when I scanned, so downloaded samples may live elsewhere (check Splice's settings for the download location).
- Logic Pro projects from Splice packs already exist (for example "140bpm-Ebmin-Neostep-Anthem-Stems").

## Using Splice in Logic Pro

1. **Install Bridge** through Splice Desktop (Apps & Plugins), then add **Splice Bridge** on a MIDI track in Logic. With the desktop app open it connects automatically. Logic requires opening the Bridge window to enable audio.
2. **Preview in your project.** With Bridge connected, previews match your project's tempo and sync to the DAW's playback, so you can audition loops in context before using credits.
3. **Smart Tempo warning:** dragging a loop into Logic may change the *project tempo* to the loop's BPM. Check the tempo and Smart Tempo/Flex settings before dragging in, especially in a project that's already set.
4. **Known Logic issue:** one user reported samples going out of sync after switching Project Alternatives. I found no official fix, so save before switching alternatives and listen afterward.
5. Bridge availability depends on plan; two Splice pages disagree about which plans include it. Check your plan.

## Choosing and fitting samples

- **Match key, tempo and mood before committing.** Filter by genre, instrument, key and BPM.
- **Choose loops near your target BPM.** Heavy stretching and big pitch shifts degrade audio. Close material stays clean.
- **Pitch-shifting changes character**, not just the key. Use a sample in a nearby key instead of dragging it far.
- **Use one-shots to build your own sounds:** layer a punchy kick under your main kick for weight; layer a snap on a snare for crack.
- **Treat samples as ingredients.** Chop, re-pitch, filter and re-arrange them so the result is yours. Derivative work is better creatively and for originality.
- **Process to fit.** EQ and compress the sample to sit with your other parts. High-pass loops that carry unneeded lows, and make room for kick and bass.
- **Avoid stacking multiple full loops** with their own drums and bass. Pick one source for each role.
- **Check phase** when layering kicks or bass layers.

## Sample chopping and flipping

- Isolate a one- or two-bar section and repeat it. Use filters, phasing, flanger or chorus to turn one short sample into different sections.
- Slice individual hits out of a loop and re-sequence them (Logic's Quick Sampler or Drum Machine Designer, Kontakt, Battery or Maschine).
- Reverse, pitch down, time-stretch and resample. Bounce the result back to audio and keep the good version.
- Cut vocal chops into short phrases and pitch to the track's key. Great for UK garage and electronic.
- Keep the original stems folder so you can go back.

## Licensing and housekeeping

- Splice states its Sounds samples are **royalty-free**: you can use them in your own compositions and recordings for commercial or non-commercial use under its Terms of Use, with no further clearance or royalties. It can supply documentation if you need to prove the license.
- Royalty-free still has limits: don't resell or redistribute the samples themselves (including as a competing pack), and watch any pack-specific restrictions.
- **"Free to download" is not the same as "free to use commercially."**
- **Real records are different.** Sampling part of a commercial song (including loops off streaming) needs clearance. Splice's license doesn't cover that.
- **Keep records:** note which Splice packs and samples each release uses, in the project or in a note. Splice's own log is useful for this.
- If you use a recognizable sample or AI/stems tool (LANDR Stems, etc.) on someone else's music, treat it as clearance territory.

Sources: [Splice: how to use Bridge](https://splice.com/blog/how-to-use-splice-bridge), [Splice support: adding Bridge to Logic Pro](https://support.splice.com/en/articles/8652861-adding-splice-bridge-to-logic-pro), [Splice: Logic Pro workflow tips (SEIDS)](https://splice.com/blog/logic-pro-workflow-tips-seids/), [Violet Recording: how to use samples](https://violetrecording.com/how-to-use-samples-in-music/), [Violet Recording: loop and sample packs](https://violetrecording.com/best-loop-and-sample-packs/), [Splice: tips for creating your own sample pack](https://splice.com/blog/tips-for-creating-your-own-sample-pack).

## Open

- Confirm your Splice plan (credits and Bridge).
- Decide where Splice downloads go and keep that folder tidy.
- Before releasing "Only Talks 2 Ghosts," list every sample source used.
