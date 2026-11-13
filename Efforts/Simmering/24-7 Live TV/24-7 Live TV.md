---
type: effort
status: simmering
created: 2026-11-12
related:
  - "[[Priorities]]"
  - "[[The Lodge]]"
---

# 24/7 Live TV

A private, 90s-style cable TV channel lineup on the Mac mini ([[The Lodge]]), so Dave controls what Cyrus watches instead of all-you-can-eat streaming.

## Goal

Old-school cable with a TV guide: a fixed schedule, a few channels, no endless scroll. Less algorithm, more attention span.

## Decisions (Nov 12, 2026)

- **Household only.** Nothing is public. Home videos stay private, always. The site is reachable only on the home network (or behind a password).
- **Content:** a mix of DVDs, VHS tapes, CDs, records and home videos, plus Sprawling visuals. Some channels are home videos on repeat.
- **Look:** a retro TV guide grid, channel up/down, static between channels. Reference site: spelunkertv.online (the layout and behavior are the inspiration; build from scratch, don't copy its code, fonts or branding, and leave out ads and tracking).

## How it works (from studying the reference)

- Each channel is a looping playlist. All channels share one clock, so a show is already in progress when you tune in.
- The guide is computed in the browser from the clock and each video's length.
- Player is a plain HTML5 video element.

## Open questions

- Which software: build a small custom site, or start from ErsatzTV or Tunarr (free tools that make scheduled channels from your own files) and style the guide?
- How to digitize: DVD rips, a VHS capture setup, CD and record audio. Audio-only channels need something to show on screen.
- Which device Cyrus watches on (TV, Apple TV, iPad?).
- Which machine is the server. [[The Lodge]] is listed for sale (Nov 12), and [[Razorleaf]] is always on below the living room TV. Razorleaf could run the first test.

## Next step

Pick the software approach. Nothing here beats school catch-up, so this stays Simmering until the Fall term ends.

## Log
-
