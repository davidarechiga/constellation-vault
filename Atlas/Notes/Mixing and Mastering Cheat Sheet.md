---
type: note
tags: [music, mixing, mastering, reference]
created: 2026-11-13
---

# Mixing and Mastering Cheat Sheet

Personal quick reference for [[Sprawling]] releases. Original write-up of standard practice, not a copy of anyone's product. Starting points only: trust your ears, and change a setting only when you can name the problem it fixes.

## The loop (every move)

1. **Name the problem** ("vocal is buried", "kick and bass fight").
2. **Pick the tool** that fixes that problem.
3. **Make it too much**, then back off until it helps.
4. **Level-match** with and without the move. Louder always sounds better.
5. **Check in context**, not solo.

## Mix prep

- Bounce or consolidate stems from the same start point. Name and color-code tracks.
- Delete dead takes and clips. Fix clicks and edit points.
- Set all faders to 0 dB, then pull the gain so peaks sit around **-18 to -12 dBFS** per track (gain staging).
- Leave **-6 dB or more of headroom** on the master bus. No limiter on it while mixing.
- Reference track loaded, level-matched, in a separate track that bypasses the master chain.
- Rough balance first with faders only, in mono, before any plugins.

## Mix order (low end first)

1. **Kick and bass.** Get these locked, since everything sits on top of them.
2. **Drums**, then the main rhythm elements.
3. **Lead** (vocal or main synth). It's the center of the mix.
4. **Support**: pads, guitars, keys, fx.
5. **Depth and space**: reverb, delay, panning.
6. **Automation**, then final level pass.

## Frequency map

| Range | Name | Notes |
|-------|------|-------|
| 20-60 Hz | Sub | Felt more than heard. Only kick and 808s or sub bass live here |
| 60-200 Hz | Bass / punch | Weight and thump. Too much sounds boomy |
| 200-500 Hz | Low mids | Mud and boxiness. Most common cut zone |
| 500 Hz-2 kHz | Mids | Body and honk. Where instruments crowd each other |
| 2-5 kHz | Presence | Clarity, attack, intelligibility. Too much is harsh |
| 5-10 kHz | Brilliance | Sibilance (vocal "s") and edge |
| 10-20 kHz | Air | Shimmer and openness |

## EQ

- **Subtract before you add.** Cut what's wrong first, boost only to flavor.
- **Find a problem:** boost with a narrow Q, sweep until it sounds awful, then cut there.
- **Add character:** gentle wide boost (Q ~0.7-1, 1-3 dB).
- **High-pass** everything that doesn't need lows (vocals ~80-100 Hz, guitars/keys ~80-150 Hz). Keep kick and bass free for the low end.
- **Carve space:** if two sounds clash, cut one where the other needs to shine (a small cut on the supporting sound).
- Small moves (1-3 dB) are usually enough. If you need 8+ dB, reconsider the recording or the tool.
- Check by toggling the EQ off at matched level.

## Compression

| Control | What it does | Starting point |
|---------|--------------|----------------|
| Threshold | Where compression starts | Set so you see 3-6 dB of gain reduction on peaks |
| Ratio | How hard it squeezes | 2:1 gentle, 4:1 firm, 8:1+ limiting |
| Attack | How fast it grabs | Slow (20-30 ms) keeps punch, fast (1-5 ms) flattens transients |
| Release | How fast it lets go | Match the groove. Should "breathe" with the tempo |
| Makeup gain | Restores level | Match output to input level |

- **Hear it:** crank the ratio and threshold, set the attack and release until the sound is pumping, then back off.
- **Vocals:** ~3-6 dB reduction, 3:1 to 4:1, medium attack so consonants cut through. Often two stages (a fast peak compressor, then a gentle leveler) beat one heavy one.
- **Drums:** slower attack keeps the transient. Parallel compression adds weight without losing punch.
- **Bus compression:** 1-2 dB of glue, low ratio (1.5:1 to 2:1), slow attack.
- **Sidechain** the bass or pads to the kick to clear room.

## Reverb and delay

- Use **sends**, not inserts, so one or two reverbs glue the mix.
- **Short room or plate** (0.3-1.2 s) for cohesion. **Long hall** (2 s+) for special moments.
- **Pre-delay** (20-80 ms) keeps the dry sound upfront with space behind it.
- **EQ the return:** high-pass ~200-400 Hz and low-pass ~6-10 kHz to keep it out of the mud and harshness.
- **Delay timing:** sync to tempo (1/4, 1/8, dotted 1/8). Filter the repeats and keep the feedback low. Throw a delay on vocal ends for space without wash.
- **Depth recipe:** dry and bright = close, darker with more reverb = far.

## Panning and width

- Keep **kick, bass, lead vocal, snare** center.
- Pan supporting parts in pairs (L/R mirrors) for balance.
- Widen with stereo doubles, short delays, or stereo effects. Check mono compatibility.
- Don't widen low end: keep everything under ~120 Hz in mono.

## Vocal chain (starting order)

1. Clean up: edits, breaths, clicks, de-ess if needed.
2. High-pass ~80-100 Hz, cut mud (~200-400 Hz).
3. Compression (leveling), then a second compressor if needed.
4. Presence boost (~3-5 kHz) and air (~10 kHz+) gently.
5. De-esser (5-8 kHz) after boosting the highs.
6. Sends: short reverb/plate and tempo delay.
7. Automate fader rides so every word is heard.

## Common problems

| Problem | Likely cause | Try |
|---------|--------------|-----|
| Muddy | Buildup 200-500 Hz | Cut there on competing tracks, high-pass |
| Harsh | Too much 2-5 kHz | Cut on the offender, check monitor volume |
| Thin | Weak low mids/bass | Check polarity, add warmth ~100-250 Hz |
| Vocal buried | Competing mids or low level | Carve the guitars/keys around 1-4 kHz, automate |
| Boomy low end | Overlap of kick and bass | Pick which owns the sub, sidechain, high-pass the other |
| Flat, lifeless | Over-compressed or all one level | Reduce compression, add dynamics automation |
| Sibilant | Harsh "s" | De-esser, or dip 5-8 kHz |
| Phasey/hollow | Phase issue between mics | Flip polarity, nudge timing |

## Before you export the mix

- Listen on **multiple systems**: monitors, headphones, phone, car.
- Check in **mono**.
- Fresh ears: take a break, then re-listen at a low volume.
- Compare with the reference at matched level.
- Leave the master bus **without limiting** if sending out for mastering. Peaks around **-6 dBFS**. Export 24-bit WAV at the session sample rate.

## Mastering

Goal: translate the mix across systems and set the final level. Small moves only. If it needs big fixes, go back to the mix.

**Order (typical):**
1. Reference and level-match.
2. Corrective EQ (small cuts, high-pass ~20-30 Hz).
3. Dynamics: gentle compression (1-2 dB) for glue.
4. Tone: subtle broad EQ or saturation for warmth and excitement.
5. Stereo: mid/side tweaks (tighten the low sides, a touch of air in the sides).
6. **Limiter last**: set the ceiling to **-1.0 dBTP**, push gain until it's loud without distortion or pumping.
7. Dither when reducing bit depth (24 to 16 bit).

**Loudness targets** (streaming normalizes, so don't chase loudness):
- Spotify/YouTube: about **-14 LUFS** integrated.
- Apple Music: about **-16 LUFS**.
- Club/DJ-oriented: louder (-8 to -10 LUFS) can be right, but stay clear of clipping.
- Ceiling -1 dBTP to avoid distortion after lossy encoding.

**Limiter stress test:** push the limiter hard on purpose. Whatever falls apart first (kick, vocal, hi-hats) is the mix problem to fix at the mix stage.

**Final checks:** track order and gaps, fades, consistent levels across the album, metadata (title, artist, ISRC), and the final export format for each platform.

## Related

- [[Sprawling]]
- Release project: "Only Talks 2 Ghosts" (see [[Priorities]])
