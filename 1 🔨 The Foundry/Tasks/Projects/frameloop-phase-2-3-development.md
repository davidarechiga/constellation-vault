---
tags:
  - task
  - project
  - frameloop
  - development
title: "Frameloop - Phase 2-3 Development"
status: open
priority: low
due: "2026-03-31"
owner: David
projects:
  - "[[Frameloop]]"
  - "[[pixel glitch creative studio]]"
---

# Frameloop - Phase 2-3 Development

Complete playback engine and BPM-synced timing for Frameloop visual performance tool.

## Phase 2: Transport & Playback Engine

- [ ] **Implement BPM-synced timing engine**
  - Create timing system based on BPM input
  - Calculate beat intervals (60000 / BPM = ms per beat)
  - Implement requestAnimationFrame loop
  - Sync visual updates to beat grid

- [ ] **Add play/stop transport controls**
  - Play button (starts playback)
  - Stop button (stops and resets to start)
  - Pause button (stops but maintains position)
  - Tempo control (BPM input field)

- [ ] **Create beat grid system**
  - Visual beat indicator (flashes on beat)
  - Bar/measure counter (shows current bar)
  - Beat subdivision options (1/4, 1/8, 1/16 notes)

- [ ] **Test timing accuracy at different BPMs**
  - Test at 60 BPM (slow)
  - Test at 120 BPM (medium)
  - Test at 140 BPM (fast)
  - Verify consistent timing across BPM ranges

## Phase 3: Animation & Strobe System

- [ ] **Implement strobe effects**
  - On/off flashing at beat intervals
  - Adjustable strobe speed (per beat, half note, etc.)
  - Color strobe options
  - Opacity strobe (fade in/out)

- [ ] **Create shape morphing transitions**
  - Smooth transitions between geometric shapes
  - Easing functions for organic movement
  - Sync shape changes to beat grid
  - Shape overlay compositing modes

- [ ] **Build animation system**
  - Keyframe-based animation timing
  - Tween library integration
  - Animation curve editor (optional)
  - Preview animations in real-time

**Why matters:** Phases 2-3 are foundational for Frameloop functionality. Without playback engine and BPM sync, the tool is unusable as a live performance instrument. These phases unlock the core value proposition.

**Done when:** Can play/stop with BPM-synced timing, strobe effects work at beat intervals, and shape morphing transitions sync to music tempo.

**Related:** [[Frameloop]] • [[Phase Summary - YouTube]] • [[pixel glitch creative studio]]

---

## Project Context

**Current Status:** Phase 1 complete (~25% done)
- ✅ React project setup with Zustand
- ✅ Basic component structure
- ✅ Image upload to 4 tracks
- ✅ Layer compositing with visibility
- ✅ Geometric shape effects
- ✅ Output controls (opacity, brightness, contrast)
- ✅ Session persistence

**Codebase Location:** `~/Dropbox/1_projects/frameloop`

**Target Platform:** Desktop web browser (Chrome/Firefox)

---

## Technical Architecture

**Key Technologies:**
- **React** - UI components and state management
- **Zustand** - Global state (BPM, playback state, track data)
- **Canvas API** - Visual rendering and compositing
- **RequestAnimationFrame** - Smooth animation loop
- **Web Audio API** (future) - Music sync and analysis

**Timing System:**
```javascript
// BPM to milliseconds per beat
const msPerBeat = 60000 / BPM;

// Animation loop synced to beats
const beatProgress = (timestamp % msPerBeat) / msPerBeat;
```

---

## Development Principles (From Frameloop Notes)

1. **Keep it simple** - Prove concept before adding complexity
2. **One feature at a time** - Don't parallelize development
3. **Responsive from start** - Mobile-friendly even for desktop tool
4. **Structure first, test as you build** - Architecture before features

---

## Phase 2-3 Milestones

**Milestone 1: Basic Playback (Week 1)**
- Play/stop buttons work
- BPM input changes tempo
- Beat indicator flashes on beat

**Milestone 2: Timing Accuracy (Week 2)**
- Consistent timing across BPM ranges
- No drift over long playback sessions
- Visual feedback matches beat precisely

**Milestone 3: Strobe Effects (Week 3)**
- On/off strobe at beat intervals
- Adjustable strobe speed
- Color and opacity strobe modes

**Milestone 4: Animation System (Week 4)**
- Shape morphing transitions
- Smooth easing and timing
- Real-time preview

---

## Testing Strategy

**Manual Testing:**
1. Play at different BPMs (60, 120, 140 BPM)
2. Let run for 5+ minutes - check for timing drift
3. Test strobe effects sync to beat
4. Verify shapes morph on beat boundaries
5. Test in Chrome and Firefox

**User Testing (Optional):**
- Share prototype with VJ friends
- Get feedback on timing feel
- Adjust based on real-world use

---

## Timeline Flexibility

**Target:** March 31, 2026

**Priority:** Low (after baby prep and career transition)

Frameloop is passion project with flexible timeline. Can shift to April-May or Q2 2026 if needed. No external deadline pressure.

---

## Next Major Phases (After 2-3)

**Phase 4:** Basic track controls (individual track play/stop)
**Phase 5:** Enhanced strobe effects (color modes, patterns)
**Phase 6:** Shape system expansion (more shapes, morphing options)
**Phase 7:** Main output effects (blur, pixelate, kaleidoscope)
**Phase 8:** Export functionality (WebM/MP4, GIF, 1080p/4K)

---

## Resources

- Project notes: [[Frameloop]]
- YouTube content plan: [[Phase Summary - YouTube]]
- Brand integration: [[pixel glitch creative studio]]
- Codebase: `~/Dropbox/1_projects/frameloop`
