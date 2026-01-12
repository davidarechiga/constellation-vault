# Frameloop - Project Roadmap

## Project Overview
Browser-based image and video frame looper for live visual performance. Similar to Ableton Live's session view but for visuals. Features 4 independent image tracks plus a main output track, synchronized to BPM with comprehensive controls.

**Status:** Active - Early Prototype
**Priority:** #4
**Completion:** ~25%
**Created:** January 2026
**Target:** Desktop web browser (Chrome/Firefox)
**Codebase:** `~/Dropbox/1_projects/frameloop`

---

## Progress Summary

**Phase 1 - Complete:** Foundation & Core Rendering
- ✓ React project with Zustand setup
- ✓ Basic component structure
- ✓ Responsive layout (CSS Grid/Flexbox)
- ✓ Image upload to 4 tracks
- ✓ Layer compositing with visibility control
- ✓ Geometric shape effects (Color Fill & Mask modes)
- ✓ Output controls (opacity, brightness, contrast)
- ✓ Session persistence
- ✓ YouTube video content ready

**Current Phase (2-3):**
- Playback engine and BPM-synced timing
- Strobe effects
- Shape morphing transitions
- Animation system

**Next Major Milestones:**
- Phase 4: Basic track controls
- Phase 5: Strobe effects
- Phase 6: Shape system with morphing
- Phase 7: Main output effects
- Export functionality

**YouTube Series:**
See [[Phase Summary - YouTube]] for video documentation of each phase.

---

## Core Features (MVP Scope)

### Transport & Playback
- Global BPM control
- Play/Stop transport controls
- Beat-synced timing engine
- Aspect ratio selector (16:9, 9:16, 4:3, 3:4)
- Export resolution (1080p, 4K)

### Main Output Track
- Opacity control
- Brightness control
- Contrast control
- Strobe effect (BPM-synced intervals)
- Shape overlay system
- Color grading controls
- Processes final composite from all 4 tracks

### Individual Tracks (4 total)
**Clip Management:**
- Image/video frame upload
- Static thumbnail preview
- Loop length (1-64 beats)
- Drag-to-reorder track stack (top = front)

**Visibility Controls:**
- Visibility toggle (hard on/off)
- Fade in button
- Fade out button
- Global fade duration setting

**Strobe Effect:**
- Enable/disable toggle
- BPM interval selector (1/4, 1/8, 1/16, etc.)
- Overrides visibility when active

**Shape System:**
- 4 basic shapes: circle, square, rectangle, triangle
- Select 1-4 shapes for morphing sequence
- Drag to reorder morph sequence
- Morph interval (BPM-synced: 4 bars, 2 bars, 1 bar, 1/4, 1/8, 1/16)
- Smooth interpolation between shapes
- Color fill / Mask mode toggle
- Hex color input

**Timeline & Arrangement:**
- Expandable timeline per track
- Beat grid ruler
- Automation parameter selector
- Click-to-add automation points
- Drag to edit points
- Snap to beat grid
- Automate all track parameters

### Canvas & Output
- Collapsible preview (expands full-width from top-right)
- Canvas rendering with proper aspect ratio
- Layer compositing based on track order
- Preview/export aspect sync toggle

### Export Functionality
- Video file (WebM or MP4)
- Animated GIF
- Duration = full loop cycle
- 1080p and 4K resolution options
- Progress indicator

---

## Technical Architecture

### State Management: Zustand Store Structure
```javascript
{
  // Global
  bpm: 120,
  isPlaying: false,
  aspectRatio: '16:9',
  exportResolution: '1080p',
  fadeDuration: 500,

  // Main Output
  mainOutput: {
    opacity: 100,
    brightness: 0,
    contrast: 0,
    strobe: { enabled: false, interval: '1/4' },
    shape: {
      enabled: false,
      selectedShapes: [],
      morphInterval: '1/4',
      mode: 'color',
      color: '#ffffff'
    },
    colorGrading: {}
  },

  // Tracks (array of 4)
  tracks: [
    {
      id: 'track-1',
      order: 0,
      clip: {
        type: null,
        src: null,
        thumbnail: null,
        loopLength: 4
      },
      visibility: true,
      fadeIn: false,
      fadeOut: false,
      strobe: { enabled: false, interval: '1/4' },
      shape: {
        selectedShapes: [],
        morphInterval: '1/4',
        mode: 'color',
        color: '#ffffff'
      },
      timeline: {
        expanded: false,
        selectedParam: null,
        automationPoints: []
      }
    }
    // ... 3 more tracks
  ]
}
```

### Component Structure
```
App
├── Transport (BPM, play/stop, aspect ratio, export)
├── Canvas (collapsible, renders composited output)
├── MainOutput (opacity, brightness, contrast, strobe, shape, color grading)
└── TrackList
    └── Track (x4)
        ├── Thumbnail
        ├── Controls (visibility, fades, strobe, shape, loop)
        └── Timeline (expandable, automation)
```

### Rendering Approach
- **Canvas-based** for main output (performance, export capability)
- **DOM/CSS** for UI controls (ease of development)
- Hybrid approach for scalability and performance

---

## Development Phases

### Phase 1: Foundation & Core Setup
- [x] Set up React project with Zustand
- [x] Implement Zustand store
- [x] Build basic component structure
- [x] Basic responsive layout (CSS Grid/Flexbox)
- [x] Static UI only, no functionality

### Phase 2: Transport & Playback Engine
- [ ] Connect Transport controls to store
- [ ] Implement play/stop functionality
- [ ] Build BPM-based timing engine
- [ ] Beat counter/grid system

### Phase 3: Image Upload & Display
- [ ] Image upload functionality per track
- [ ] Generate static thumbnails
- [ ] Store image data in Zustand
- [ ] Display images in canvas (no effects)
- [ ] Basic layer compositing (stack order)

### Phase 4: Basic Track Controls
- [ ] Visibility toggle
- [ ] Fade in/out buttons
- [ ] Loop length selector (1-64 beats)
- [ ] Track reordering (drag & drop)
- [ ] Apply controls to canvas output

### Phase 5: Strobe Effect
- [ ] Strobe toggle per track
- [ ] Interval selector
- [ ] Sync to BPM timing

### Phase 6: Shape System - Basic
- [ ] Shape selection UI (checkboxes)
- [ ] Drag to reorder shapes
- [ ] Morph interval selector
- [ ] Color/Mask mode toggle
- [ ] Hex color input
- [ ] Render single static shape
- [ ] Shape morphing animation
- [ ] BPM-synced morphing

### Phase 7: Main Output Controls
- [ ] Opacity slider
- [ ] Brightness slider
- [ ] Contrast slider
- [ ] Strobe (same as track)
- [ ] Shape overlay (same as track)
- [ ] Color grading controls

### Phase 8: Canvas & Aspect Ratio
- [ ] Aspect ratio switching
- [ ] Canvas collapse/expand
- [ ] Full-width canvas when expanded
- [ ] Preview/export aspect sync toggle

### Phase 9: Timeline & Arrangement
- [ ] Expandable timeline per track
- [ ] Timeline ruler with beat markers
- [ ] Clip placement on timeline
- [ ] Playhead scrubbing

### Phase 10: Automation
- [ ] Parameter selector dropdown
- [ ] Click-to-add automation points
- [ ] Drag points to edit
- [ ] Snap to beat grid
- [ ] Automation playback

### Phase 11: Export Functionality
- [ ] Export resolution selector
- [ ] Calculate export duration
- [ ] Render to video (WebM/MP4)
- [ ] Render to animated GIF
- [ ] Progress indicator

### Phase 12: Polish & Testing
- [ ] UI polish and responsive refinements
- [ ] Performance optimization
- [ ] Cross-browser testing
- [ ] Bug fixes

---

## Future Iterations (Post-MVP)

See [[Frameloop - Future Features]] for post-MVP roadmap including:
- Media Manager & asset organization
- Audio integration & visualizers
- Advanced modulation (LFOs, envelopes)
- Live input (webcam, feedback loops)
- Shader system
- MIDI controller support

---

## Development Principles
- **Keep it simple, prove it, iterate** - Start with minimal viable features
- **One feature at a time** - Fully implement before moving on
- **Responsive from start** - Build mobile-ready even if desktop-first
- **Structure first** - Plan architecture before coding
- **Test as you build** - Validate each phase before moving forward

---

## Related
- Similar to: Ableton Live (session view) but for visuals
- Reference: VJ apps with polyphonic layers, shader systems, audio reactivity
- Part of: [[pixel glitch creative studio]]
