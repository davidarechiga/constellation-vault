---
aliases:
tags:
  - music
  - production
  - ableton
type: project
status: active
related:
  - "[[🎨 Design & Creative Work]]"
created: <% tp.date.now("YYYY-MM-DD") %>
modified: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

> **BPM:** &nbsp;&nbsp;&nbsp; **Key:** &nbsp;&nbsp;&nbsp; **Genre/Vibe:** &nbsp;&nbsp;&nbsp; **References:**

---

## Vision & Direction

*What should this track feel like? What's the emotional core?*

---

## 0. Session Prep

> Get the session clean before touching a single plugin. Non-critical listening work — grind through mechanically.

- [ ] Rename all tracks
- [ ] Trim silence / clean up regions — fade edges to kill clicks
- [ ] Bounce virtual instruments to audio
- [ ] Delete duplicate and unused tracks
- [ ] Check sample rate consistency (Splice samples vs. session rate)
- [ ] Comp all takes — don't mix a placeholder performance
- [ ] Crossfades everywhere — hard edits cause misleading clicks
- [ ] Time align drums (close mics + overheads phase relationship)
- [ ] Set tempo and drop section markers (intro, verse, drop, break, outro)
- [ ] Note plugin dependencies for collaborators

---

## 1. Prepare & Balance

> Get organized and set a clean starting balance.

- [ ] Confirm the arrangement is final — every element earns its place
- [ ] Bus related channels together (drums, bass, FX, instruments, vocals) and color-code
- [ ] Create 4 send channels: large / mid / short reverb + delay
- [ ] Pull all faders down, then bring up in order of importance
- [ ] Use reference tracks to calibrate levels — A/B with analyser
- [ ] Set each fader at the threshold where it's just audible, then fine-tune ±dB
- [ ] Remove masked / purposeless sounds (aim for ≤5 non-drum elements at once)
- [ ] High-pass everything that doesn't need sub frequencies
- [ ] Shape drum transients — automate or fade tails to prevent bleed

> [!tip] Reverb types
> Plates/springs → drums (metallic, unnatural). Chambers/cathedrals → large spaces, choir vocals. Rooms → close instruments, bass.

---

## 2. Detect & Fix Problems

> Surgical fixes. Digital for cuts, analog for color. Always gain-stage & A/B.

- [ ] Sidechain bass & colliding elements from kick/snare
- [ ] Check for frequency masking — try rebalancing faders first
- [ ] EQ cut masking frequencies (cutting > boosting). Multiband sidechain as alt.
- [ ] Muddy bass? Check 200–500 Hz for buildup, cut carefully
- [ ] Use minimum processing — less is cleaner
- [ ] Dynamic elements hiding/peaking? Decide: compression vs automation
- [ ] Overly dynamic frequency band → multiband comp (only the band that needs it)
- [ ] Gate background noise from recordings / analog processing
- [ ] Piercing vocals? De-ess or multiband compress the high end
- [ ] Find & remove problematic frequencies / volume spikes with analyser + ears

---

## 3. Bus Processing

> Glue groups together and add weight where it counts.

- [ ] Saturate sub bass to add low-mid harmonics (for phone/laptop playback)
- [ ] Glue compress dynamic buses (e.g. bass bus) for cohesion
- [ ] Ensure sub peaks are consistent on spectrum analyser (higher ratio, longer release)
- [ ] Compress drum bus — protect transients, avoid pumping. Parallel comp/distort for punch.
- [ ] Lightly excite drum high end for clarity (don't overdo it)
- [ ] Multiband comp on groups if needed — transparent, don't upset balance
- [ ] Limit drum & bass buses to stabilize before the master

---

## 4. Stereo Balance

> Place things in the stereo field and protect your mono signal.

- [ ] Pan same-frequency elements apart to avoid masking
- [ ] Reference orchestra layout for panning ideas
- [ ] Keep backbone elements centered & narrow (vocals, kick, snare, lead)
- [ ] Check mono compatibility — phase meter should stay positive
- [ ] Narrow or mono some channels so panned elements stand out more
- [ ] Use M/S EQ to fix phase issues: reduce side, boost mono on fundamentals

---

## 5. Depth & Character

> Place elements in 3D space with reverb and delay.

- [ ] Drum reverb always under 10% wet
- [ ] Decide front-to-back placement for each element via reverb amount
- [ ] Sidechain reverbs from drum transients to keep clarity
- [ ] Sidechain delays from vocals/leads so tails don't mask the source

---

## 6. Basic Mastering

> Final polish on the stereo bus before it leaves the DAW.

- [ ] Optional: route through a pre-master bus with light glue compression
- [ ] Mono everything below 100–150 Hz
- [ ] Linear-phase HPF at 25 Hz, LPF at 20 kHz (gentle slopes)
- [ ] Enhance the track's feeling with subtle EQ (±1–2 dB max)
- [ ] Balance frequency bands — not too bassy, not too bright
- [ ] Limit to commercial loudness (≤5 dB gain reduction). Serial limiters for transparency.

---

## 7. Reference & Finalize

> Sanity-check against commercial releases before you bounce.

- [ ] Final balance pass — every element audible when it should be
- [ ] Match RMS / LUFS to reference tracks
- [ ] Compare frequency curve against references on analyser
- [ ] Mono check both tracks — if elements collapse, go back to step 4

---

## Handoff Notes

*Vibe, references, what you want the track to feel like, what you're unsure about:*

---

## Session Log

| Date | Notes |
|------|-------|
| <% tp.date.now("YYYY-MM-DD") %> | Project started |
