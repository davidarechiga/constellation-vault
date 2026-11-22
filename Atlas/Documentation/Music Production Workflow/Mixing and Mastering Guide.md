---
type: note
created: 2026-11-13
tags: [music, mixing, mastering, sprawling]
source: "[[Mixing and Mastering Cheat Sheet Binder]]"
status: draft (v1, core workflow)
---

# Mixing and Mastering Guide

Dave's working guide to mixing and mastering his own music (Sprawling). It is a condensed, reworded study guide built on the [[Mixing and Mastering Cheat Sheet Binder]] (Mastering.com). Page numbers like (p48) point to that PDF, so open it when a diagram helps. Treat the numbers as starting points and trust your ears.

Use this guide when finishing "Only Talks 2 Ghosts" or any track. Part 1 is the mix, Part 2 is the master, Part 3 explains each tool.

## The big idea

- **Musical goals:** the arrangement and composition work, and the listener feels something. **Technical goal:** it sounds good on any speaker. (From Dave's old note "5 objectives of mixing".)
- **Five drivers of mixing** (Dave's old note): balance, fix, enhance, shape, space. The binder's order matches: volume first, then fixes, then enhancements, then reverb and delay last.
- Picture the mix as a **cube** (p69): **height** is tone (low to high frequencies), **width** is stereo placement, **depth** is front-to-back, made by volume, transients and reverb.
- **Mixing is not editing.** Tuning, timing, comping and clean-up finish before the mix starts (p48). **Mastering is not mixing.** If the mix needs big moves, go back to the mix (p63).
- **Ears first, meters second.** Decide by listening, then check the meter (p42).

## Part 1: Mixing workflow

Order of work (p50). Don't skip ahead.

1. **Session setup** (p48): match sample rate and BPM, set a big buffer (1024) for a light CPU load, delete empty tracks, group by instrument (drums, bass, guitars, keys, vocals), color-code the same way every time, put 10 ms fades on every region to stop clicks, label song sections, and route tracks to group buses.
2. **Import 2 to 4 references** (p49): same genre, lossless files, chosen for specific jobs (low end, vocal presence, width). Route them *around* the mix bus so your processing doesn't touch them. The point is to guide balance, dynamics and depth, not to copy.
3. **Gain staging** (p51): this is about headroom, not loudness. Loop the loudest section, select all tracks, and move them together until the kick peaks at **-5 dBFS**. Keep their relationships. If anything else peaks above the kick and snare, pull that one down on its own. Use clip gain for this.
4. **Build the foundation** (p52-53): mute everything, then bring in kick, then bass, then snare.
   - Kick and snare transients peak around **-5 dBFS**.
   - Kick plus bass reach the genre's low-end target on a VU meter (calibrated to -18 dBFS). The binder puts genres on a scale, from singer-songwriter and folk at the low end to hip-hop and EDM at the high end.
   - The gap between the transient peak and the low end is the song's **foundation depth**. Everything else sits inside that gap.
   - Beginners hit the targets with volume and EQ. Later, use a transient shaper (attack vs. sustain) to push a sound forward or back.
5. **Foundation stress test** (p54): put a brick-wall limiter on the mix bus with a loudness meter after it. With only kick, snare and bass playing, push to **-9 to -11 short-term LUFS** at the loudest part. Either it holds up, or depth collapses, or the sounds change character. If you see more than 4 dB of gain reduction, fix the foundation first (usually kick and bass are stacking). Leave the limiter on for the rest of the mix.
6. **Volume-only mix** (p55): no plugins. Set the vocal about 2 dB below the snare peak (tucked in) or 2 dB above it (vocal-forward). Add each remaining element one at a time, either by importance or in the order they enter the song. Pan as you go: kick, snare, bass and vocal stay center, and everything else fills the empty spots.
7. **Solve problems** (p56-57): one instrument group at a time, and *consistent* problems before *momentary* ones.
   - **Consistent:** mud and rumble (high-pass what doesn't need lows, cut low-mid buildup), masking (cut the less important sound where the important one lives), tonal imbalance (broad, gentle EQ in context, not solo). If a fix needs more than about ±6 dB, it's a production problem.
   - **Momentary:** uneven level (clip gain or automation first, then FET compressor into an opto compressor), resonance and harshness (sweep to find it, then notch it, or use dynamic EQ), sibilance (clip gain, then a de-esser).
   - Always bypass to check. If it didn't help the lead or consistency, remove it.
8. **Enhance** (p58): additive EQ for air or weight, volume automation for story, transient shaping, stereo imaging, saturation, parallel compression. Same order, group by group.
9. **Reference check-in**, then **spatial processing** (p59): reverb and delay come last, "the cherry on top," because they can hide problems. Run each one through the five questions below.
10. **Assess the emotional arc** (p60): is there one clear focal point in every section, does the energy rise and fall, do transitions connect, does the biggest moment feel biggest? Steer attention with level (loud), depth (dry and close), tone (bright) and width (center).
11. **Final check, then export** (p61): rest your ears, check on other speakers, and check against the reference once more.

### Export the mix (p61)

- Bypass the limiter and leave **5 to 6 dB of headroom**. Bounce two files: one without the limiter (this is what you master) and one with it (the reference).
- WAV or AIFF, same bit depth and sample rate as the session, normalize off. Leave about 1 bar of silence at the start and let tails ring out at the end. Listen all the way through for pops and clicks.
- Naming: `Title_Artist_24bit_48kHz_Mix.wav` and `..._Ref.wav`.

## Part 2: Mastering workflow

Best practice is a **separate mastering session** with one stereo file (p65). You can't keep nudging the mix, you hear it fresh, and you see the waveform. If you master inside the mix session, skip the stress test and add only enhancements before the limiter.

1. **Setup** (p63): import the mix plus 2 or 3 professionally mastered references. Match the session to the file. Check for 5 to 6 dB headroom, clicks and clipping. Put loudness and spectrum meters on the stereo out. Processing hits the mix only, never the reference.
2. **Limiter stress test** (p66): read the reference's short-term LUFS at its loudest part. Put a limiter on your track (ceiling -0.3) and push to the same number. Three outcomes:
   - *Holds up:* just enhance.
   - *Gets there, but...:* depth narrows, upper mids get harsh, or kick and bass pump. This points to a frequency or dynamics problem.
   - *Won't get there:* energy is stacked in the lows and low mids and eats the headroom.
3. **Fix problems** (p67): problems are either frequency balance or dynamic balance. Use the least destructive tool.
   - *Frequency:* muddy low end or harsh mids get broad static EQ, or dynamic EQ if it only happens in one part. Boxy gets a medium-Q cut. Dull gets a gentle high shelf.
   - *Dynamics:* limiter pumping gets a clipper before the limiter, a longer release, or multiband on the lows. Lost punch gets a transient shaper and less limiting. One hot kick or snare that triggers everything gets handled in the mix.
   - If it needs extreme EQ or heavy compression, stop and go back to the mix. Mastering works with "broad and gentle brushstrokes."
4. **Enhance** (p68-72): take your hands off the mouse and listen as a fan. A/B against the unprocessed version, and if nothing is needed, leave it. Think in the cube:
   - **Height:** low-shelf for weight, wide presence bell for vocal and leads, high shelf for air. Small moves only (±3 dB is a lot). Boost what the reference has and yours lacks.
   - **Width:** width comes from contrast with the center. Cut the lows on the sides to keep the low end mono, add a little high-side lift, and widen only in choruses. Always check mono.
   - **Depth:** slower compressor attack keeps punch, parallel compression adds body, saturation adds density (tube for weight, tape for air).
5. **Stem mastering** (p73-74), optional: 4 to 8 stems (vocals, bass, drums, everything else) from the *original session*. AI stem-splitters add artifacts. Process each stem, then sum into the master bus.
6. **Export the master** (p75):
   - True peak never above **-0.1 dBTP**, limiter ceiling at -0.3 or lower.
   - Loudness: about **-7 S-LUFS** at the loudest part is typical. It's a bit lower for acoustic genres and louder for some electronic ones. Match a reference, don't chase a number.
   - Trim to a short lead-in, fade the tail to digital silence.
   - WAV or AIFF, 24-bit, same sample rate as the session. Dither only when reducing bit depth, once, as the very last step.
   - QC: re-import the file into a fresh session and listen through. Name it `Title_Artist_24bit_48kHz_Master.wav`.

## Part 3: The tools, in plain terms

**EQ** (p18-21)
- **Cut** to fix and carve space. **Boost** to add character. Broad, gentle moves sound natural, and narrow ones are for surgery.
- Find problems by boosting a narrow band about 10 dB and sweeping across the spectrum. If a spot sounds nasty, cut there.
- Make room: dip 2 to 4 kHz on guitars or snare for the vocal, cut about 250 Hz on competing tracks so kick and bass stay clear, and high-pass things that don't need lows.
- If EQ is doing all the rescuing, the real fix is in the recording or production.

**Compression** (p22-26)
- *Hear it first:* ratio up high, threshold down for 10 to 15 dB of reduction, then find the attack (fast sounds rounder, slow sounds punchier), then the release (fast pumps, slow squashes). Back off until it's subtle. Listen to the delta (what's being removed) and bypass to A/B.
- *Types:* FET (fast, aggressive, snares and punchy vocals), opto (smooth leveling, lead vocals and bass), VCA (precise, tight glue and drum bus), vari-mu or tube (warm mix-bus glue), clean digital (transparent).
- *Bus glue:* ratio about 1.5 to 3 for glue, or 4+ for control. Slow attack, release timed so it breathes with the groove. Level-match when you A/B.

**Saturation** (p27-28): adds harmonics and soft compression, so a sound feels fuller and louder without a higher peak. Tape is gluey, tube is warm, solid-state is biting, digital is precise. Match output level to judge it fairly.

**Reverb** (p29-32)
- Five questions before adding any (p31): what's the *goal*, which *style* (room, plate, hall, chamber, spring), *near or far*, how *wide*, how *bright or dark*.
- *Near:* longer pre-delay (20+ ms), mostly early reflections, low send. *Far:* short pre-delay, mostly late reflections, higher send.
- Put each reverb on its own aux at **100% wet** and control amount with the send. Tame the return with EQ (high-pass the mud, damp the highs). If a vocal loses clarity, add pre-delay. If sibilance splashes, de-ess before the reverb.
- Starting points (p30): lead vocal plate or room, pre-delay 40 to 80 ms, decay 0.5 to 1.5 s. Drum or vocal "glue" is a short, tight room. Transitions and fade-outs use big halls with long decay.

**Delay** (p33-35): put on an aux at 100% wet. Under 50 ms thickens or widens, 60 to 150 ms is slapback, and tempo-synced gives rhythmic echoes. Feedback 0 to 15% for a few natural repeats, 20 to 40% for a trail. Low-cut the repeats around 300 Hz and high-cut around 3 kHz so they sit behind the dry sound. Raise the send until you notice it, then back off a few dB so it's "felt, not heard."

**Depth recipe** (p13): to push something back, lower the volume, darken the EQ, soften the transients and add reverb. To bring it forward, do the opposite.

**Panning** (p14): hard (LCR) panning gives clean separation, and intermediate panning gives a more detailed soundstage. Either way, kick, bass, lead vocal and snare anchor the center.

**Mid/Side** (p36): high-pass the side channel (about 100 to 150 Hz) so the low end stays mono, and compress the sides to control wide elements. Keep verses slightly narrower and open up in the hook. It's a scalpel, not a rescue. If the correlation meter dips below zero, back off.

**Clipper** (p37-38): chops peaks instead of turning them down. Use it for short, fast transients (drums, 808s) with about 1 to 3 dB of shaving, set just below the limiter. If you hear distortion, back off.

**Limiter** (p39-40): last plugin on the master bus, and only meters come after it. Ceiling -1.0 to -0.3 dBFS for inter-sample peaks. Aim for 2 to 4 dB of gain reduction on the loudest parts, and use auto-release. Constant heavy reduction means raise the threshold.

**Metering** (p41-42): put meters after all processing, and send the reference through the same meters. The essentials are a frequency analyzer, a dynamics meter and a loudness (LUFS) meter. Add a correlation meter whenever you widen things.

**Automation** (p43): ride macro level between sections before compression, and ride micro moves on words or notes the compressor would otherwise chase. Any plugin parameter can be automated (reverb send on the last word, saturation drive in the last chorus).

## The five reverb questions (cheat card)

Goal, Style, Placement (near or far), Width, Tone. Ask them for every reverb.

## Quick problem fixes (p57)

| Problem | Try |
|---|---|
| Kick muddy | cut around 300-400 Hz, boost 40-60 Hz |
| Snare lacks snap | transient shaper, fast-release gate |
| Bass thin | boost near the fundamental (150-300 Hz), or add harmonics with saturation |
| Vocal harsh | de-esser, dip 5-10 kHz, or dynamic EQ above 8 kHz |
| Vocal masked by instruments | carve 1-3 kHz in the instruments and pan for separation |
| Mix cluttered | mute or filter non-essential layers; "clarity often comes from subtraction" |
| Limiter pumping | lower the low end, or use multiband or dynamic EQ on the lows |

## Dave's own notes and tools

- Seeds from the old vault: `Bass I usually cut to 30. Guitars 150 and around, vocals 75ish` (his high-pass habits) and `Ableton Audio Effects and Tips`, a friend's Ableton-specific walkthrough (return tracks, ghost-kick sidechain, M/S master EQ, 6 dB of headroom before mastering). Both live in `Starting Over Archive/E - The Foundry/Ongoing/1 🛫 Personal Growth/Music Performance_Production/`. They agree with this guide and are not yet merged into it.
- Reference track idea already saved: *Wave Rider* by Your Old Droog.
- Listening gear and room: Sony 7506 headphones; room treatment idea in the same archive folder. The binder's room layout is on p6 (listening position about 1/3 from a short wall, bass traps in corners, absorbers at first reflection points).

## Still to add (future sessions, one at a time)

- A short "Ableton version" of Part 1 (which Live devices do each job).
- Chapter notes from *The Mixing Engineer's Handbook* (2nd ed.) in the same `Music Production` share folder.
- The *Music Production Cheat Sheet Binder* (50 pages, also in `Docs/`) for the production side.
- A checklist for "Only Talks 2 Ghosts": which references, target LUFS, and who masters it.
