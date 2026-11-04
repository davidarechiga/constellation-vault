---
type: source
created: 2026-11-04
author: Claude Code
tags: [gear, workflow, stream-deck, procreate, ableton]
---

# Creative Workspace Blueprint

How the desktop station (M1 Max Mac, 32 GB) and the mobile sketchbook (iPad mini + Apple Pencil) fit together with the Stream Deck + and the 8BitDo Micro.

> Written from Claude's existing knowledge, not live research. Items marked **[verify]** may have changed with firmware or app updates; check them on the device.
>
> Not on [[Priorities]] right now. School catch-up and the "Only Talks 2 Ghosts" release come first.

**What to do first:** build Page 2 (AI prompts) and the Micro K-mode map. Both take under an hour and pay off daily. Leave Page 3 until you actually stream.

---

## 1. Connections between devices

### Desktop: M1 Max ports

The M1 Max gives each Thunderbolt 4 port its own controller. Spread the load across ports, not across hubs.

| Port | Device(s) | Why |
|---|---|---|
| **TB port A** | Audio interface, alone | Audio data has to arrive on time. Keep it off any hub shared with drives or cameras. |
| **TB port B** | Project/sample SSD (NVMe in a TB or USB 3.2 enclosure) | Ableton streams samples from disk while you play. A busy drive on the interface's bus causes dropouts. |
| **TB port C** (or a powered TB dock) | Webcam/capture card, Stream Deck +, other low-speed devices | Cameras use bandwidth but tolerate small delays. The Stream Deck + needs steady power, not bandwidth. |
| Mac Studio USB-A / MBP HDMI | Second display | Keeps monitor traffic off the shared ports. |

**Stream Deck + rules**
- It only needs USB 2.0 speeds but draws a lot of power for its screen and touch strip. Never use an unpowered hub; it will brown out and reset mid-session. Plug it into the Mac or a powered dock.
- Don't chain it behind the audio interface's hub.
- If it vanishes after sleep, relaunch the Stream Deck app. Turning off "Put hard disks to sleep" in Energy settings also helps.
- **Check for dropouts before a stream:** in Ableton, Preferences › Audio › run CPU Usage Simulator at 50% while OBS records the camera. Watch Activity Monitor › Disk during playback.

### Mobile: 8BitDo Micro + iPad mini + Apple Pencil

**Mode switch (slider on the back: S / D / K)**
- Each slider position shows up as a separate Bluetooth device with its own pairing. Pair each mode once: set the slider, hold **Select** about 3 seconds until the LED flashes fast, pair in iPad Settings › Bluetooth.
- After that, moving the slider switches modes without re-pairing. Don't tap "Forget" on either entry.
- **K mode** = Bluetooth keyboard. Use it for Procreate.
- **Gaming:** try **S mode** with Delta first. **[verify]** whether iPadOS sees the Micro as a game controller on your firmware. Fallback: Delta accepts keyboard input, so you can stay in K mode and map keys in Delta › Settings › Controllers.

**Known quirks**
1. **The on-screen keyboard disappears in K mode.** iPadOS hides it while any hardware keyboard is connected. Fix: tap the keyboard icon in the bottom-right shortcut bar, or turn the Micro off while typing.
2. **Pencil + controller on Bluetooth** usually coexist fine. Jitter or dropped presses come from crowded 2.4 GHz Wi-Fi. Use 5 GHz and keep the Micro within about 1 m.
3. **Wake from sleep:** the first press can be lost. Wake it with a harmless button, not Undo.
4. **Pencil Pro squeeze and barrel roll** (iPad mini A17 Pro) can take a job off the Micro, for example squeeze for the quick menu.

---

## 2. Procreate layout for the Micro (left hand, Pencil in right)

### Setup
1. Install **8BitDo Ultimate Software V2** (iOS). Update the Micro's firmware first.
2. Slider to **K**, connect in the app, map buttons, **save to the controller**. The mapping lives on the device.
3. In Procreate, hold ⌘ (if mapped) to see the live shortcut sheet. Confirm each key below against it.
4. **[verify]** If Ultimate Software can't send combos like ⌘Z, use single-key shortcuts only and fall back on two-finger tap (undo) and three-finger tap (redo).

### Grip
Micro in the left palm, D-pad under the thumb, index finger on L/L2, middle finger on R/R2. Frequent actions go under resting fingers. Mode changes go on the face buttons.

### Button map

| Button | Finger | Procreate action | Key sent |
|---|---|---|---|
| **L** | Index (resting) | **Undo** | ⌘Z |
| **L2** | Index (pull) | **Redo** | ⇧⌘Z |
| **D-pad ↑** | Thumb | **Brush size up** | ] |
| **D-pad ↓** | Thumb | **Brush size down** | [ |
| **D-pad →** | Thumb | Opacity up | ⇧] **[verify]** |
| **D-pad ←** | Thumb | Opacity down | ⇧[ **[verify]** |
| **R** | Middle (resting) | **Eyedropper** (hold) | ⌥ hold **[verify]**, or set Procreate's □ modifier to eyedrop |
| **R2** | Middle (pull) | Brush ↔ Eraser toggle | E (or E/B) |
| **A** | Thumb reach | **Brush** | B |
| **B** | Thumb reach | **Eraser** | E |
| **X** | Thumb reach | **Smudge** | S |
| **Y** | Thumb reach | **Layers panel** (then tap a layer's checkbox to hide/show) | L **[verify]** |
| **Select (−)** | Thumb | Colour panel | C **[verify]** |
| **Start (+)** | Thumb | Full screen / hide UI | ⌘0 or Tab **[verify]** |
| **Home** | Thumb (rare) | Shortcut sheet / modifier | ⌘ (hold) |
| **Star** | Thumb (rare) | New layer, or flip canvas horizontally | per the ⌘-hold sheet |

**Less fatigue**
- Undo and redo sit under fingers that are already resting. Undo is about 40% of non-drawing input.
- Brush size on the D-pad lets you tap without looking. For big jumps, use the brush size slider.
- In Procreate › Actions › Prefs › Gesture controls, turn off touch-to-paint so a resting palm never makes marks.
- There's no standard single-key shortcut for layer visibility. Layers panel + Pencil tap is the fastest reliable path.

**Gaming profile:** if your firmware supports multiple profiles **[verify]**, keep Procreate on K and leave S/D on the default layout for Delta.

---

## 3. Stream Deck + profiles

Hardware: 8 LCD keys (2×4), 4 push dials, 1 touch strip. One profile, three pages. Set **profile auto-switch** per app (Ableton, browser with Claude/ChatGPT, OBS) so keystrokes never land in the wrong window. Key 8 on every page = page cycle.

### Page 1: Ableton Live

**Connection**
- Audio MIDI Setup › MIDI Studio › **IAC Driver** › "Device is online". Rename the bus `StreamDeck`.
- Install a **MIDI plugin** from the Marketplace (Trevliga Spel's "MIDI" **[verify current name]**).
- Live › Preferences › Link/Tempo/MIDI › IAC `StreamDeck` input › **Remote ON**.
- Keystrokes for things Live won't MIDI-map (scrub, zoom, views). MIDI for parameters.

| Control | Action | How |
|---|---|---|
| **Dial 1** | Scrub: rotate moves the insert marker, press = play | Hotkey dial ← / →, press Space |
| **Dial 2** | Zoom: rotate out/in, press = zoom to selection | Hotkey dial − / =, press Z |
| **Dial 3** | Parameter twist: CC 20 → macro on a "Control" rack | MIDI CC, relative |
| **Dial 4** | Tempo ±1, press = tap tempo | MIDI CC + note, mapped with ⌘M |
| Key 1 | Play/Stop | Space |
| Key 2 | Record | F9 |
| Key 3 | Loop selection | ⌘L |
| Key 4 | Session ↔ Arrangement | Tab |
| Key 5 | Clip ↔ Device view | ⇧Tab |
| Key 6 | Split | ⌘E |
| Key 7 | Consolidate | ⌘J |
| Key 8 | Page → | built-in |

- Touch strip: tap a dial's section to switch it to fine (×0.1) mode in the MIDI plugin's dial options.
- Sound design: make Dial 3 a **Dial Stack** so pressing it cycles Macros 1–4.

### Page 2: AI prompts and productivity

Don't use the built-in **Text** action for long prompts; it types slowly and breaks if focus changes. **Put the prompt on the clipboard, then paste.**

Setup: **Keyboard Maestro** (or Raycast Snippets) triggered from the Stream Deck.
1. Key → KM macro "Prompt – Refactor".
2. KM: set clipboard to the contents of a plain-text prompt file.
3. KM: paste (⌘V).
4. Optional: restore the previous clipboard after 0.5 s.

| Control | Action |
|---|---|
| Key 1 | System prompt: research mode |
| Key 2 | Code-refactor frame (KM wraps the current clipboard: header + clipboard + footer) |
| Key 3 | "Explain like a reviewer" critique frame |
| Key 4 | Clean paste: ⌥⇧⌘V (paste and match style) |
| Key 5 | Clear input: ⌘A → Delete |
| Key 6 | New Claude chat (⌘N **[verify]**) |
| Key 7 | ChatGPT companion window (⌥Space **[verify]**) |
| Key 8 | Page → |
| **Dial 1** | Clipboard history: rotate to scroll, press to paste |
| **Dial 2** | Scroll the chat (↑/↓ or Page Up/Down) |
| **Dial 3** | Switch windows of the same app (⌘` / ⇧⌘`) |
| **Dial 4** | System volume |

Tip: end each template with the variable part (`...Task:`) so you can type right after it lands.

### Page 3: Streaming + room lights (OBS + Hue)

**Plugins**
- **OBS Studio** (official Elgato). Turn on OBS › Tools › WebSocket Server Settings and set a password.
- **Philips Hue** (official Elgato **[verify]**, supports dials). Pair by pressing the bridge button when asked.

| Control | Action |
|---|---|
| Key 1 | Scene: Live / camera |
| Key 2 | Scene: Screen + cam |
| Key 3 | Scene: BRB (switch scene + mute mic + Hue dim 20%) |
| Key 4 | Mic mute (shows state) |
| Key 5 | Start/Stop stream (long press) |
| Key 6 | Start/Stop recording |
| Key 7 | Hue "Studio Bright"; long press = "Studio Mood" |
| Key 8 | Page → |
| **Dial 1** | Mic volume, press = mute |
| **Dial 2** | Music bus volume in OBS |
| **Dial 3** | Hue brightness, press = on/off |
| **Dial 4** | Hue colour temp / colour, press = switch mode |
| **Touch strip** | Live levels; swipe on Dial 3's section = fast brightness sweep |

**Ableton audio into OBS:** use **Loopback** (paid) or **BlackHole 2ch** (free). Set OBS to 48 kHz to match Live.

---

## 4. Weak points and safeguards

### Memory on 32 GB shared RAM

CPU and GPU share RAM, so a local model loaded on the GPU takes memory from Ableton.

| Workload | Rough RAM use |
|---|---|
| macOS + browser with AI tabs | 6–9 GB |
| Ableton, medium project + sampled instruments | 6–14 GB |
| OBS 1080p60, hardware encoder | 1–2 GB |
| Local LLM 7–8B (Q4) | ~5–6 GB |
| Local LLM 14B (Q4) | ~9–10 GB |
| Local LLM 32B (Q4) | ~20 GB, not compatible with a live Ableton session |

**Rules**
1. No local models during tracking or streaming. Use cloud Claude/ChatGPT then.
2. Ollama: `ollama stop <model>` after use, or `OLLAMA_KEEP_ALIVE=0`. LM Studio: auto-unload on.
3. Watch the **memory pressure** graph. Yellow = swapping, which competes with sample streaming.
4. Ableton: freeze/flatten finished synth tracks, keep long samples on disk streaming, purge unused Kontakt samples. Mix at 512 buffer, track at 128.
5. OBS: Apple VT hardware encoder, never x264.
6. Docker Desktop memory cap ~4 GB. Close Xcode/simulators before opening Live.
7. Don't raise the GPU memory limit (`iogpu.wired_limit_mb`) to fit bigger models.

### Other failure points
- Stream Deck keystrokes go to whatever window is in front. Keep per-app profile switching on.
- The IAC bus can disappear after macOS updates. Check Audio MIDI Setup.
- OBS websocket password can reset on reinstall; the plugin then fails silently.
- Hue bridges throttle around 10 commands a second. Set dial steps to 5–10%.
- Micro battery is small. Charge it with the iPad.

### Software list

| Tool | Role | Needed? |
|---|---|---|
| Stream Deck app + OBS and Philips Hue plugins | Page 3 | Yes |
| MIDI plugin + IAC Driver | Page 1 parameters | Yes |
| Keyboard Maestro (or Raycast) | Prompt macros | Yes for Page 2 |
| Clipboard manager: Raycast, Paste, or Maccy | Clipboard history dial | Strongly recommended |
| Loopback or BlackHole | Ableton → OBS audio | Yes for streaming |
| Bome MIDI Translator Pro | MIDI → keystroke, for a future hardware controller | Optional |
| 8BitDo Ultimate Software V2 (iOS) | Micro mapping + firmware | Yes |
| Delta | Retro emulation | For gaming |
