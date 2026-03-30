---
tags:
  - task
  - frmwrk
title: "DJ Overlay — Photoshop Production Build"
status: in-progress
priority: high
due: "2026-03-30"
owner: David
projects:
  - "[[frmwrk_]]"
---

# DJ Overlay — Photoshop Production Build

Build the static DJ overlay PNG from the approved v3 mockup. This is the foundational asset — all other overlay layouts reference its window chrome and grid system.

## Canvas Setup

- [ ] **Create 1920×1080 artboard at 72ppi, RGB, 8-bit**
  - Set background fill to Desktop BG `#c8c0a8`
  - Add guides at x: 14, 670, 796, 1132, 1906 and y: 34, 478, 648, 470, 1066
  - Load frmwrk_ color swatches (Oil Green, Coral Red, Glaucous Blue, Sulphur Yellow, Ash Violet, Persimmon, Celadon, Raw Umber, Cream, Desktop BG)

## Window Chrome Smart Object

- [ ] **Build reusable window chrome as a Smart Object**
  - 1px bevel: top/left `#ffffff` at 60% opacity, bottom/right `#2a2a2a` at 60% opacity
  - Title bar: 2px horizontal stripes alternating Oil Green `#6b6b2a` / Cream `#f0ead6`
  - Inactive variant: solid Ash Violet `#7a6472` title bar
  - Pixel-drawn window controls (minimize / maximize / close) — top-right of title bar
  - Checker fill swatch (2×2px, Desktop BG + 10% darker) for background regions
  - Save as `window-chrome.psb` linked Smart Object

## Taskbar

- [ ] **Build bottom taskbar strip (1920×30 @ x:0 y:1050)**
  - Oil Green base fill
  - Start button (Press Start 2P, 8pt, Cream text)
  - Clock readout right-aligned (VT323, 12pt)
  - Active window buttons (window chrome bevel, truncated titles)

## Face Cam Window

- [ ] **Build face cam window (648×436 @ x:14 y:34)**
  - Window chrome applied
  - Title bar label: "CAM_FEED.EXE" (Press Start 2P, 6pt, Cream)
  - Interior: solid black placeholder (camera feed will show through in OBS)
  - Note: static layer only — no animation

## VU Meter Window

- [ ] **Build VU meter window (118×436 @ x:670 y:34)**
  - Window chrome applied
  - Title bar label: "VU.EXE" (Press Start 2P, 6pt, Cream)
  - Two vertical channel columns (L / R), centered with 4px gap
  - Each column: 38 segments, 2px tall, 1px gap between segments
  - Segment colors: bottom 28 = Celadon `#9db89a`, top 6 = Sulphur Yellow `#c9b84c`, top 4 = Coral Red `#d4614a`
  - Inactive segments: Desktop BG with bevel inset
  - Label: "L" / "R" in VT323 below columns
  - ⚠️ Animation (segment levels) will be built separately in After Effects

## Deck PIP Window

- [ ] **Build deck PIP window (328×210 @ x:796 y:34)**
  - Window chrome applied
  - Title bar label: "DECK_A.EXE" (Press Start 2P, 6pt, Cream)
  - Interior: solid black placeholder (video PIP feed in OBS)

## Game Feed Window

- [ ] **Build game feed window (328×218 @ x:796 y:252)**
  - Window chrome applied
  - Title bar label: "GAME_FEED.EXE" (Press Start 2P, 6pt, Cream)
  - Interior: solid black placeholder (game capture in OBS)

## Session Info + Chat Window

- [ ] **Build session info + chat window (774×436 @ x:1132 y:34)**
  - Window chrome applied
  - Title bar label: "SESSION_INFO.EXE // CHAT.EXE" (Press Start 2P, 6pt, Cream)
  - 2-column layout with 1px Oil Green vertical divider at center
    - Left col: session info (track name, BPM, key, set time) — VT323 labels
    - Right col: chat feed area — solid black placeholder (chat overlay in OBS)
  - Interior row divider lines: 1px Ash Violet, every 24px

## Waveform Window

- [ ] **Build waveform window (984×170 @ x:14 y:478)**
  - Window chrome applied
  - Title bar label: "WAVEFORM.EXE" (Press Start 2P, 6pt, Cream)
  - Interior: solid black placeholder with center hairline (1px Celadon, 50% opacity)
  - Playhead indicator: 1px vertical Coral Red line at horizontal center
  - ⚠️ Animated waveform will be built separately in After Effects

## EQ Spectrum Window

- [ ] **Build EQ spectrum window (900×170 @ x:1006 y:478)**
  - Window chrome applied
  - Title bar label: "EQ_SPECTRUM.EXE" (Press Start 2P, 6pt, Cream)
  - Interior: solid black placeholder
  - Frequency labels along bottom (SUB / BASS / MID / HI) in VT323, 10pt, Ash Violet
  - ⚠️ Animated spectrum bars will be built separately in After Effects

## Bottom Bar / Ticker

- [ ] **Build ticker bar (1920×28 @ x:0 y:1022)**
  - Oil Green fill, 1px Cream top border
  - Scrolling placeholder text area (VT323, 11pt, Cream)
  - Left badge: "frmwrk_" wordmark lockup (Press Start 2P, 8pt)
  - Right badge: Twitch handle + social icons

## CRT Effects Layer

- [ ] **Build CRT post-processing stack (top of layer order)**
  - Scanlines: 1px black lines every 2px, 8% opacity, Multiply blend mode
  - Vignette: radial gradient, black edges, 18% opacity, Multiply blend mode
  - Noise: Add Noise filter, 2%, Monochromatic, on merged stamp layer
  - Group all CRT layers into "CRT_FX" group — toggle off for clean export variant

## Export & OBS Test

- [ ] **Export final PNG**
  - Flatten visible, hide CRT group → export `frmwrk_overlay_dj_clean.png`
  - Show CRT group → export `frmwrk_overlay_dj_crt.png`
  - Both: PNG-24, no compression, 1920×1080
- [ ] **OBS test**
  - Import PNG as Browser Source / Image Source at 1920×1080
  - Verify all black placeholder regions show through correctly as transparent
  - Check window chrome bevel reads correctly at stream resolution
  - Adjust any elements that look too small or cluttered at preview size

---

**Why matters:** The DJ overlay is the foundation for the entire frmwrk_ visual system. Every other asset — alerts, social templates, motion graphics — derives window chrome rules and color usage from this file. Getting it right before building downstream assets saves rework across the whole package.

**Done when:** 1920×1080 PNG exported and tested in OBS. All nine windows placed correctly. Window chrome Smart Object saved for reuse. CRT and clean export variants both exist.

**Related:** [[frmwrk_]] • [[frmwrk_ Production Spec]] • [[frmwrk_ Aesthetic Brief]]
