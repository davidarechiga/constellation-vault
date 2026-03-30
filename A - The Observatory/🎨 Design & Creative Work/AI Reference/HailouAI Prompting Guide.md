---
aliases:
tags:
  - contentcreation
  - ai
  - hailouai
type: reference
status: draft
related:
created: 2026-03-08
modified: 2026-03-08
---
# The definitive Hailuo AI Director Mode reference guide

**Hailuo AI’s Director Mode gives filmmakers precise, bracket-syntax camera control over AI-generated video — but the real power lies in combining its 15 official commands with natural language modifiers, intensity shaping, and a disciplined production pipeline.** This guide covers every documented command, the modifiers and tricks that actually work, the full production workflow from concept to final output, and scene-specific prompt templates tailored to the “Sprawling Cosmic Blip” animation project. It synthesizes official MiniMax API documentation, the Hailuo knowledge base, community testing from hundreds of generations, and cinematic theory mapped directly to Director Mode syntax.

-----

## Part 1: The complete command reference

### All 15 official camera movements

Director Mode accepts camera instructions inside square brackets within the prompt string.  These are the **15 canonical commands** per MiniMax’s API documentation at platform.minimax.io:  

| #   | Command           | Type       | What it does                                                                      |
| --- | ----------------- | ---------- | --------------------------------------------------------------------------------- |
| 1   | `[Truck left]`    | Horizontal | Camera body slides left (lateral dolly)                                           |
| 2   | `[Truck right]`   | Horizontal | Camera body slides right                                                          |
| 3   | `[Pan left]`      | Horizontal | Camera pivots left on a fixed axis                                                |
| 4   | `[Pan right]`     | Horizontal | Camera pivots right on a fixed axis                                               |
| 5   | `[Pedestal up]`   | Vertical   | Camera body rises vertically                                                      |
| 6   | `[Pedestal down]` | Vertical   | Camera body lowers vertically                                                     |
| 7   | `[Tilt up]`       | Vertical   | Camera pivots upward on a fixed axis                                              |
| 8   | `[Tilt down]`     | Vertical   | Camera pivots downward on a fixed axis                                            |
| 9   | `[Push in]`       | Depth      | Camera moves forward toward subject (dolly in) — changes perspective and parallax |
| 10  | `[Pull out]`      | Depth      | Camera moves backward from subject (dolly out)                                    |
| 11  | `[Zoom in]`       | Depth      | Lens focal length changes to magnify — camera stays put, perspective flattens     |
| 12  | `[Zoom out]`      | Depth      | Lens focal length widens — camera stays put                                       |
| 13  | `[Shake]`         | Special    | Camera vibration/instability effect                                               |
| 14  | `[Tracking shot]` | Special    | Camera follows a moving subject                                                   |
| 15  | `[Static shot]`   | Special    | Camera remains completely fixed                                                   |

**The critical Push vs. Zoom distinction:** `[Push in]` physically moves the camera through space, creating parallax and depth  — the viewer feels they are *walking toward* the subject. `[Zoom in]` magnifies via focal length without moving,  compressing the background and creating a voyeuristic, observational feel.   **For A24-style intimacy, prefer Push. For surveillance or paranoia, prefer Zoom.** The AI sometimes confuses these; combining the command with a subject-framing directive  (“maintaining focus on the character’s eyes”) increases reliability.

### The “Follow” and “Fix” parameters

**`[Follow]`** is an alias for `[Tracking shot]`, not a separate 16th command. The fal.ai API documentation uses `[Follow]` in examples like `[Push in, Follow]A stylish woman walks down a Tokyo street...`  and it functions identically to `[Tracking shot]`.  MiniMax’s own docs categorize it as “Follow: `[Tracking shot]`.” 

**`[Fix]`** does not appear in any official documentation across MiniMax, PiAPI, fal.ai, Replicate, or getimg.ai. This parameter is either undocumented or does not exist in the current Director Mode implementation.

### Bracket syntax rules

The syntax is precise and unforgiving in API calls. **No space between the closing bracket and the prompt text**: `[Push in]walking man` is correct; `[Push in] walking man` may fail. Camera commands are comma-separated within brackets for simultaneous execution: `[Push in,Pedestal up]`.  Maximum **3 movements per bracket set**.  The prompt field supports up to **2,000 characters**.  

### Preset cinematic shot combinations

Hailuo’s UI offers curated presets that combine multiple commands.   These represent tested, reliable combinations:

|Preset        |Commands                                |Use case                                    |
|--------------|----------------------------------------|--------------------------------------------|
|Left Circling |`[Truck left, Pan right, Tracking shot]`|Orbital reveal around subject               |
|Right Circling|`[Truck right, Pan left, Tracking shot]`|Orbital reveal, opposite direction          |
|Upward Tilt   |`[Push in, Pedestal up]`                |Dramatic reveal, ascending toward subject   |
|Left Walking  |`[Truck left, Tracking shot]`           |Side-by-side following shot                 |
|Right Walking |`[Truck right, Tracking shot]`          |Side-by-side following, opposite            |
|Downward Tilt |`[Pedestal down, Tilt up]`              |Descending while maintaining subject framing|
|Stage Left    |`[Pan left, Zoom in]`                   |Dramatic side reveal with emphasis          |
|Stage Right   |`[Pan right, Zoom in]`                  |Dramatic side reveal, opposite              |
|Scenic Shot   |`[Truck left, Pedestal up]`             |Wide environmental reveal                   |

### Simultaneous vs. sequential movements

This is one of Director Mode’s most powerful but least-understood features. **Simultaneous execution** places all commands in a single bracket set — they fire together: `[Push in, Pan right, Tilt down]`. **Sequential execution** places separate bracket sets at different points in the prompt text — the first completes before the second begins:  

```
[Push in]A man picks up a book from the table, [Pan right]then turns toward the window.
```

The placement of brackets within the prompt text determines *when* each movement triggers.   This enables multi-stage shots within a single 6-second generation — a slow push in that transitions to a pan, for instance. However, keep sequences short. Camera movements should ideally complete within **5–6 seconds** to avoid generation failures. 

### The one rule that breaks everything

**`[Static shot]` cannot be combined with any other movement.**   This is a hard constraint. If you need a mostly-static shot with a subtle drift, use natural language (“nearly still camera with barely perceptible drift”) rather than `[Static shot]`.

-----

## Part 2: Speed, intensity, and natural language modifiers

### The MiniMax API has no speed parameter

There is no `speed: "fast"` or `intensity: 0.8` field in the API. All speed and intensity control happens through **natural language within the prompt text**. This is both a limitation and an opportunity — the model is remarkably responsive to cinematographic vocabulary.

### Confirmed speed and intensity modifiers

These modifiers have been validated through official Hailuo knowledge base articles and extensive community testing across hundreds of generations:

**Speed modifiers that work reliably:**

- **“Slow”** — The most reliably effective speed modifier. “Slow dolly in,” “slow pan left” consistently reduce camera velocity. 
- **“Fast”** — Works for high-energy movements. Best paired with action-heavy prompts.
- **“Subtle”** — One of three officially recommended “Precision Modifiers.” Constrains the motion envelope.  Critical for close-ups. 
- **“Steady”** — Another official precision modifier. “Steady horizontal pan from left to right” is given as a professional directive. 
- **“Sweeping”** — Recommended for wide shots that “require more aggressive intensity modifiers to overcome the vastness of the frame.” 
- **“Gentle”** — Used in official prompts for restrained movement.
- **“Smooth”** — Confirmed style modifier. “Smooth dolly-in” is explicitly described as more effective than conversational equivalents. 
- **“Rapid”** — Alternative to “fast” for wide shots.
- **“Fluid”** — Substitutable for “smooth” when generating variations.

**Style and quality modifiers:**

- **“Handheld”** — Introduces deliberate jitter and natural shake. The official tip: “If the zoom feels too robotic, add the modifier ‘Handheld’ to introduce a slight, natural shake.” 
- **“Steadicam”** — Implies smooth, stabilized movement with less randomness than handheld.
- **“Tripod mounted” / “Locked-off shot”** — Signals mechanical stability to avoid unwanted bobbing. 
- **“Cinematic”** — The third official precision modifier. Constrains output toward professional-looking results.
- **“Micro-movement”** — Recommended for extreme close-ups requiring maximal restraint. 

### Controlling Shake intensity

The `[Shake]` command is **binary** — it’s either on or off. You cannot write `[Shake 50%]`. However, intensity is controlled through the natural language surrounding the command:

- **Light shake:** Pair with “subtle handheld sway” or “gentle tremor in the frame” in the prompt text near `[Shake]`
- **Heavy shake:** Pair with “the frame shakes violently with each blast” or action-heavy descriptions (explosions, impacts) 
- **Alternative approach:** Skip the bracket entirely and use pure natural language: “subtle handheld micro-shake” for organic feel, or “violent handheld shaking” for intensity
- **Post-production fallback:** Add **1–2% digital handheld shake** in your NLE for clips that came out too stable 

The official Hailuo knowledge base confirms that the descriptive text *around* camera commands significantly influences their interpretation. The model reads narrative context to calibrate motion intensity.

### Cinematic terms the model understands

Beyond the 15 bracket commands, Director Mode responds to professional cinema vocabulary used in natural language:

- **“Dolly shot” / “Dolly in”** — Physical camera movement (maps to Push behavior)
- **“Crane shot”** — “Crane shot rising above the battlefield as smoke clears” works as a natural language prompt 
- **“Dutch tilt” / “Dutch angle”** — Confirmed in official examples: “light Dutch tilt for visual imbalance”  
- **“Shallow depth of field”** — Works for visual style control
- **“Over-the-shoulder”** — Confirmed as combinable for dialogue scenes 
- **“Bird’s eye view”** — Supported as perspective instruction 
- **“POV shot”** — Successfully used in community prompts 
- **“Rack focus”** — Part of the cinematic vocabulary the model was trained on
- **“Whip pan”** — Often creates too much motion; use with caution

### Lens language that shapes output

The model responds to lens-equivalent descriptions that influence framing and perspective:

- **Wide (24–35mm)** — Exaggerated spatial depth, more environment visible. Risk of face distortion in close-ups.
- **Standard (35–50mm)** — Natural perspective. Official recommendation: “Use 35–50mm look for most talking and reaction shots.”
- **Short telephoto (50–85mm)** — Flattering portraits, strong background separation. 
- **Anamorphic** — Triggers widescreen bokeh and lens flare characteristics.

### Scale-relative motion intensity

This is a critical discovery from Hailuo’s own benchmarking across **500+ generations**: the model interprets motion intensity relative to implied scene scale. 

**Wide shots** need more aggressive intensity modifiers (“sweeping,” “rapid”) because the frame vastness absorbs movement — a slow pan across a cityscape barely registers. **Close-ups** need extreme restraint (“subtle,” “micro-movement”) because even a tiny camera shift translates to a massive change in the pixel grid.  This scale-relative calibration is perhaps the single most important insight for consistent Director Mode results.

### The subtractive prompting principle

The official Hailuo knowledge base calls this “the most significant discovery in the Director Mode workflow.” **Less is more.** If the camera isn’t following your intent, remove contradictory terms rather than adding new ones. Use a single clear action verb with one definitive style modifier:

- ✅ `"Smooth dolly-in"`
- ❌ `"The camera moves closer to the person very slowly and nicely"` 

The AI recognizes technical cinematography terms more reliably than conversational descriptions.  Keep camera motion prompts **under 15 words** to maintain token weight on the instructions that matter. 

### The prompt_optimizer toggle

Setting `prompt_optimizer: false`  in the API gives more precise, literal control over camera commands. Setting it to `true` (the default) lets the AI enhance your prompt,   which may adjust motion behavior unpredictably.   **For Director Mode work where camera control is paramount, set this to `false`.**

-----

## Part 3: The prompt engineering framework

### The core formula

Every Director Mode prompt should follow this structure:

```
[Camera Movement(s)] + Main Subject + Action/Motion + Environment + Lighting/Atmosphere + Style Reference
```

Or the professional variant:

```
[Subject/Action] + [Environment] + [One Primary Motion] + [One Intensity Modifier] + [Atmosphere]
```

The “One Primary Motion Rule” is the most reliable approach for 4–6 second clips: **lead with one dominant motion descriptor and one intensity modifier.** Attempting to layer three different motion types with contradictory intensity descriptors (“rapid yet gentle zoom with a subtle tilt”) causes model glitching or subject deformation. 

### Prompt placement determines timing

Camera brackets placed at the **beginning** of a prompt apply throughout the clip. Brackets placed **mid-prompt** trigger sequentially at that narrative point.  This means you can choreograph multi-stage camera work:

```
[Push in]A detective leans forward to examine the document, [Pan right]then glances toward the door where a shadow appears.
```

### Optimal prompt length and structure

The sweet spot is **40–60 words total**,  with the camera instruction portion specifically kept under 15 words. The AI’s attention mechanism prioritizes early text, so **start prompts with the most important element**  — typically the subject and their key visual traits. 

### The base prompt + motion modifier strategy

For consistent multi-shot sequences, establish a reusable base and swap only the camera instruction: 

**Base block (constant across all shots):**

```
Cinematic, shot on Arri Alexa, photorealistic, 35mm lens, natural lighting, subtle film grain.
```

**Motion modifier (changes per shot):**

- Depth: “Slow dolly in,” “Steady push forward”
- Parallax: “Slow lateral pan,” “Trucking shot left”
- Focus: “Subtle tilt up,” “Low angle hero shot” 

### Negative prompting

To prevent common AI video issues, append constraints: 

- `"No camera shake, no jitter, no visual glitches"`
- `"No cartoon, no anime, no illustration"` (critical for photorealistic projects) 
- `"Sharp focus"` or `"High shutter speed"` to prevent unwanted motion blur on fast movements  

### The double-parentheses weight system

Community members report success using `((double parentheses))` to emphasize key visual elements the AI should prioritize:  `((olive green puffer jacket))`, `((chain mail face veil))`. This tells the model to “latch onto” these features with higher attention weight.

-----

## Part 4: The model ecosystem and how models work together

### The complete Hailuo model family

|Model              |Type                |Input                         |Best for                                       |
|-------------------|--------------------|------------------------------|-----------------------------------------------|
|**T2V-01**         |Text→Video          |Text                          |Core generation from descriptions              |
|**I2V-01**         |Image→Video         |Image + text                  |Animating keyframes/illustrations              |
|**I2V-01-Live**    |Image→Video         |Image + text                  |2D art/animation; preserves line art integrity |
|**S2V-01**         |Subject→Video       |Reference image + text        |Character consistency across clips             |
|**T2V-01-Director**|Text→Video + Camera |Text with `[commands]`        |Precise camera control from text               |
|**I2V-01-Director**|Image→Video + Camera|Image + text with `[commands]`|Camera control anchored to reference frame     |
|**Hailuo 02**      |T2V + I2V           |Text or image + text          |1080p, 10s clips, last-frame conditioning      |
|**Hailuo 2.3**     |T2V + I2V           |Text or image + text          |Enhanced motion, micro-expressions, stylization|
|**Hailuo 2.3 Fast**|I2V only            |Image + text                  |Rapid iteration at ~50% cost                   |

### How T2V-01-Director vs. I2V-01-Director differ

Both support identical bracket syntax and all 15 commands.  The differences:

**T2V-01-Director** generates entirely from text — no image input.   Resolution is capped at **720p**, duration at **6 seconds**, frame rate at **25fps**.  Best for exploratory generation when you don’t have a reference frame.

**I2V-01-Director** requires a `first_frame_image`  (JPG/PNG/WebP, <20MB, short edge >300px, aspect ratio 2:5 to 5:2) plus a text prompt.  Same 720p/6s/25fps constraints. Best for **controlled generation** where you’ve established a specific frame composition. Starting with a high-quality reference image via I2V reduces unwanted motion by **60–70%** compared to T2V because the AI only calculates temporal changes rather than hallucinating the entire scene. 

The newer **Hailuo 02 and 2.3** models accept the same bracket camera commands natively while offering **1080p resolution**  and clips up to **10 seconds at 768p**.  These effectively supersede the original Director models for most production work, though the dedicated Director models remain available.

### S2V-01 and Director Mode cannot yet be combined directly

This is a significant current limitation. S2V-01 (subject reference) and Director Mode are **separate models**  that cannot be merged in a single API call. The workaround is a multi-step pipeline:

1. Generate a character-consistent clip with S2V-01 using your reference image
2. Extract the last frame of that clip
3. Feed that frame into I2V-01-Director as the `first_frame_image`
4. Apply camera commands in the Director Mode prompt

This is cumbersome but functional. Community feedback strongly desires integration, and MiniMax’s roadmap suggests eventual merger. 

### S2V-01 API structure

```json
{
  "prompt": "A figure walks through a rain-soaked alley at night.",
  "subject_reference": [
    {
      "type": "character",
      "image": ["https://example.com/casper-reference.jpg"]
    }
  ],
  "model": "S2V-01",
  "prompt_optimizer": false
}
```

S2V-01 analyzes facial geometry, skin tone, age, gender, and structural features from a **single reference image** and locks them throughout the generated video.  It currently supports single-subject references only. Set `prompt_optimizer: false` for precise control over the output. 

### Last-frame conditioning for clip chaining

Hailuo 02 supports **last-frame conditioning** — using the final frame of one clip as the first frame of the next. This enables frame-to-frame chaining for longer sequences with visual continuity. Supported at 6s or 10s at 768p, and 6s at 1080p.   Hailuo 2.3 does **not** currently support last-frame conditioning. 

-----

## Part 5: The complete production pipeline

### Phase 1 — Pre-production

**Character bible first.** Define immutable traits before any generation: age, ethnicity, hair, signature features, wardrobe anchors. For Casper: late-20s non-binary, olive green puffer jacket, chain mail face veil, blue over-ear headphones, anti-grav repulsion discs at waist, trail runners, graffiti-stained fingertips.

**Generate reference images** using Midjourney, FLUX.1, or similar T2I models. Create 1–3 angles (front, 3/4, profile) with consistent wardrobe. These become your S2V-01 anchors and I2V first frames. 

**Script and storyboard** with specific camera movements per shot. Use the Director Mode command vocabulary directly in your storyboard notes — this translates directly to prompts.

### Phase 2 — Generation workflow

1. **Establish hero shots** with S2V-01 using your reference image and `prompt_optimizer: false`
2. **Generate scene clips** with Hailuo 2.3 T2V/I2V using detailed prompts
3. **Apply camera control** via Director Mode brackets where needed
4. **Chain clips** using last-frame conditioning (Hailuo 02) or I2V with extracted end frames
5. **Batch generate** 3–9 variations per shot using the 3×3 rule (see below)

### The 3×3 rule for variation selection

This is the most efficient generation strategy for professional work:

1. Generate **3 variations** of your primary prompt
2. **Tweak phrasing slightly** (e.g., change “smooth” to “fluid”) and generate another 3
3. **Swap the action verb** (e.g., from “dolly” to “push-in”) and generate a final 3

This yields **9 clips total**, from which at least 1 production-ready shot is a highly efficient return. For complex movements like dolly zooms, success rates can drop **below 30%** per generation  — batch processing is not optional, it’s essential.

### The “Middle Two” temporal trimming strategy

AI clips often have startup noise in the first 0.5 seconds and latent-space divergence in the final 0.5 seconds. Generate a 4–6 second clip and **use the middle 2–3 seconds** for the best temporal coherence. The middle window has the cleanest frames. 

### The 60% frame-fill rule

The subject should occupy at least **60% of the frame area**. Below this threshold, the model prioritizes background textures over subject fidelity, leading to identity drift and detail loss. 

### The I2V consistency anchor

Starting with a high-quality reference image via Image-to-Video is the single most effective technique for reducing unwanted artifacts. The AI only needs to compute temporal changes rather than hallucinating the entire scene from scratch.   For any shot where visual consistency matters, always use I2V over T2V.

### Phase 3 — Post-production pipeline

**Step 1: Upscaling with Topaz Video AI.** Native Hailuo output is 720p–1080p.   Recommended settings for AI-generated footage:

- Model: **Proteus** (most versatile) or Artemis High Quality
- Scale: **2×** (avoid 4× — diminishing returns)
- Anti-flicker: **HIGH** — the single most important setting. AI video almost always has temporal inconsistency; high anti-flicker directly addresses it 
- Grain recovery: Medium
- Denoise: 0.2–0.3
- Output: ProRes or high-bitrate H.265
- **Upscale BEFORE color grading** to preserve maximum quality

**Step 2: Assembly in DaVinci Resolve.** Arrange clips on the Edit page timeline.  Trim dead frames from clip starts and ends (AI clips typically have 0.5s of settling). Use **cross-dissolves of 0.5–1 second** between AI clips to mask slight inconsistencies. Apply speed ramping at transition points for smoother blending. For advanced blending or VFX between clips, use Resolve’s Fusion compositing page.

**Step 3: Color grading.** AI-generated clips from different generations will have subtle color and lighting differences.  Use **Group Grading** and **Shared Nodes** in Resolve’s Color page to apply consistent grades across all clips in a scene.  Resolve’s **Shot Match** feature can automatically align colors across clips.  Use **Magic Mask** to AI-isolate subjects for targeted grading.  AI video colors tend toward oversaturation — grade in Rec.709 or DaVinci Wide Gamut for accurate results. 

Node workflow for AI video:

- Node 1: Base correction (white balance, exposure)
- Node 2: Contrast and creative look
- Node 3: LUT or creative grade
- Parallel nodes for temperature and curves to avoid compounding corrections 

**Step 4: Frame interpolation and stabilization.** Hailuo outputs at 25fps. Use Optical Flow with Speed Warp in Resolve to smooth to 24fps (cinematic) or 30fps (web). Reducing playback speed to 50% via optical flow smooths micro-stutters.   Apply subtle grain overlays and sharpening for final polish. 

**Step 5: Audio.** MiniMax Speech 2.6/2.8 offers emotional voice synthesis with sentence-level emotional direction. MiniMax Music 2.5+ generates scoring. Use Resolve’s Fairlight page for mixing, syncing, and mastering. Sound design is crucial for unifying visually disjointed AI clips — continuous ambient audio and music create cohesion.

-----

## Part 6: Cinematic technique mapping

### How traditional shots map to Director Mode

|Traditional technique |Director Mode approach                                        |Emotional effect                                              |
|----------------------|--------------------------------------------------------------|--------------------------------------------------------------|
|Establishing/wide shot|`[Static shot]` or `[Pan left/right]` + “wide shot, 24mm lens”|Context, scale, isolation                                     |
|Close-up              |`[Push in]` + “close-up, 85mm, shallow DOF”                   |Intimacy, tension, emotional confrontation                    |
|Extreme close-up      |`[Zoom in]` + “macro, extreme close-up”                       |Revelation, obsession, hyper-focus                            |
|Over-the-shoulder     |`[Static shot]` + “OTS framing” described in text             |Dialogue, relationship dynamics                               |
|Dutch angle           |Describe “Dutch tilt, tilted frame” in natural language       |Unease, psychological tension                                 |
|Tracking/following    |`[Tracking shot]` + `[Truck left/right]`                      |Journey, empathy, character agency                            |
|Crane shot            |`[Pedestal up, Tilt down]`                                    |Dramatic reveal, grandeur, scale                              |
|Steadicam             |`[Tracking shot]` + “smooth, fluid movement”                  |Dreamlike, controlled immersion                               |
|Handheld              |`[Shake]` + “handheld, documentary”                           |Urgency, realism, chaos                                       |
|Low angle             |`[Tilt up]` + “low angle looking up”                          |Power, menace, heroism                                        |
|High angle            |`[Pedestal up, Tilt down]` + “high angle”                     |Vulnerability, insignificance                                 |
|POV shot              |`[Push in, Shake]` + “first-person POV”                       |Direct identification with character                          |
|Dolly zoom            |Describe “dolly zoom effect” in natural language              |Dread, psychological shift — extremely powerful, use sparingly|

### When to use static vs. moving camera

**Static works when** the scene demands contemplation, dread, documentation, or when you want the audience to observe without guidance.  A24 frequently uses static shots for characters processing emotion — the stillness forces focus. Static is also powerful for surveillance aesthetics. 

**Movement works when** motivated by character action, emotional shift, or spatial exploration. The principle of **“motivated camera movement”** holds: every camera move should have a narrative reason. Unmotivated movement reads as “AI-generated” — this is the key differentiator for professional results.

The **transition from static to moving** signals a narrative shift. The reverse — movement settling into stillness — signals resolution or emotional landing. These transitions are powerful storytelling tools that Director Mode supports through sequential bracket placement.

### Camera movement and character psychology

- **Fluid, soft movement** → tender moments, emotional connection
- **Frenetic, shaky movement** → chaos, instability, danger
- **Slow push in** → growing tension, dawning realization, building intimacy or dread
- **Circular/orbital movement** → enclosure, being trapped, cyclical patterns
- **Following from behind** → journey, mystery, shared perspective
- **Leading from front** → confrontation, the character approaches us

-----

## Part 7: Achieving specific film looks

### A24 cinematic realism

The A24 look is defined by **natural-seeming but meticulously planned lighting**,  emphasis on faces and skin, shallow depth of field, and handheld-to-fluid camera transitions that mirror character psychology.  Films like Moonlight, Everything Everywhere All at Once, and Ex Machina share these traits.

**Key prompt elements:**

```
Shot on ARRI Alexa, 35mm anamorphic lens, natural window light, 
practical light sources, shallow depth of field, subtle film grain, 
rich skin tones, intimate framing, motivated camera movement, 
muted palette with selective saturation
```

Camera should alternate between `[Static shot]` for contemplative beats, `[Push in]` (slow) for building tension, and `[Tracking shot]` with “smooth” modifier for intimate following shots.

### Cyberpunk aesthetic

Cyberpunk requires **neon lighting with color contrast** (cool cyan vs. warm magenta), wet reflective surfaces, volumetric atmosphere, and dense urban layering.  The “grounded” variant avoids maximalist neon overload — more Blade Runner 2049 than generic neon city.

**Key prompt elements:**

```
Dense neon billboards, wet asphalt reflecting colored lights, 
cool cyan key light, warm magenta rim lighting, low volumetric fog, 
light rain with visible droplets, neon-noir cinematic style
```

Always define **at least two distinct light colors and their roles** in the frame.  “Neon lights” alone produces generic results; “cool cyan key light from the left, warm magenta rim lighting from overhead signage” produces specificity. 

### Surveillance footage

```
[Static shot] Fixed security camera, high corner, wide-angle fish-eye 
distortion, 640×480, compression artifacts, cold fluorescent lighting, 
timestamp overlay, static camera, no warm tones, clinical desaturation
```

This look requires `[Static shot]` or `[Zoom in]` only. Any dynamic movement breaks the illusion. Add “frame drops” and “digital noise” for authenticity. 

### Documentary / found footage

Use `[Shake]` as the primary camera characteristic combined with “handheld documentary style, 16mm film grain, natural lighting.” For found footage specifically, add “VHS texture, scan lines, low resolution.” Omitting all motion keywords actually defaults the AI to a “handh eld drift” which can work for documentary but isn’t reliable for found footage intensity.

-----

## Part 8: Scene-specific prompts for “Sprawling Cosmic Blip”

The following templates incorporate the project’s A24 cinematic realism × grounded cyberpunk aesthetic, Casper’s specific character design, and the muted color palette (teal/cyan for digital systems, magenta for resistance, olive green for tactical gear, warm amber for analog tech). Each scene includes a recommended camera approach, a primary prompt template, and an alternate angle prompt.

### Universal character and style blocks

Copy these into every prompt for consistency:

**Character block:**

```
A non-binary person in their late 20s wearing ((olive green puffer jacket)), 
((chain mail face veil covering lower face)), ((blue over-ear headphones)) 
around neck, graffiti-stained fingertips, trail runners
```

**Style block:**

```
A24 cinematic realism meets grounded cyberpunk. Muted desaturated palette 
with selective warm amber accents. Shot on Arri Alexa, 35mm lens, subtle 
film grain. Photorealistic, hyper-detailed. No cartoon, no anime, no illustration.
```

-----

### Scene 1 — Casper tagging “COSMB” graffiti in an alley

**Camera approach:** Start with a medium close-up of the hand/can action, then reveal the broader alley. The intimacy of creation matters — this is a private, defiant act.

**Primary prompt (close action):**

```
[Push in] Close-up of graffiti-stained hands gripping a spray can, pressing the nozzle against raw board-formed concrete. Cyan paint hisses out in controlled arcs, forming bold geometric letterforms "COSMB." Camera pushes in slowly on the emerging tag. A non-binary figure in ((olive green puffer jacket)) and ((chain mail face veil)) crouches at the wall's base. Dead-end alley at 3AM, sodium streetlight flickers overhead casting warm amber, mist hangs in the air. Paint drips are wet and reflective. Muted tones with selective cyan color pop on the tag. Shot on 16mm film, subtle grain, A24 indie realism. Photorealistic.
```

**Alternate (environmental reveal):**

```
[Pull out, Pedestal up] Starting on the fresh cyan graffiti tag "COSMB" on raw concrete, camera slowly pulls back and rises to reveal the figure in ((olive green puffer jacket)) stepping away from the wall, spray can in hand, checking their work. The alley stretches behind them — brutalist walls, fire escapes, distant amber streetlight glow. Muted desaturated palette, warm amber against cold concrete grey. Grounded cyberpunk atmosphere, contemplative mood. Photorealistic, shot on Arri Alexa, 35mm.
```

-----

### Scene 2 — Casper fighting armored guards in an alley

**Camera approach:** Handheld intensity. The fight should feel visceral and grounded — not Hollywood choreography but desperate, scrappy survival. Paint-splattered combat with spray cans as weapons demands close-quarters chaos.

**Primary prompt (action tracking):**

```
[Tracking shot, Shake] A figure in ((olive green puffer jacket)) and ((chain mail face veil)) swings a spray can at an armored guard in a narrow rain-soaked alley. Paint explodes on impact — cyan and magenta splatter across matte black tactical armor. Camera tracks laterally, handheld, raw and visceral. Wet concrete reflects sodium vapor light. Second guard advances from behind. Sweat and rain caught in harsh sidelight. Documentary-style urgency, A24 cinematic realism, muted earth tones punctuated by vivid paint splatter. Photorealistic, shot on Arri Alexa, 35mm.
```

**Alternate (tension build):**

```
[Push in] Medium shot of Casper backing against a concrete wall, breathing hard, ((chain mail face veil)) catching amber light. Three armored guards approach in silhouette. Camera pushes in slowly on Casper's eyes — steady, focused, calculating. They grip two spray cans at their sides. Paint-splattered brutalist walls. Single harsh overhead light creates deep shadows. Tension before violence. Slow, deliberate push in. Cinematic dread, photorealistic, subtle film grain.
```

-----

### Scene 3 — Casper leaping through a dimensional portal

**Camera approach:** This is the most VFX-heavy scene. The split-screen technique (cyberpunk city / bioluminescent forest) can be achieved by describing the frame division explicitly. Use a zoom out to reveal the scale of the dimensional crossing.

**Primary prompt (portal crossing):**

```
[Zoom out, Tilt up] A figure in ((olive green puffer jacket)) leaps through a vertical tear in reality — edges crackling with analog signal noise and VHS tracking lines. The portal shimmers with magnetic tape distortion. Through the opening, a bioluminescent forest glows with cool teal light — organic, alien, alive. The alley behind the figure is harsh brutalist concrete under sodium amber light. Camera zooms out to reveal the scale of the dimensional rupture. Cassette futurism aesthetic — the portal looks like unwinding magnetic tape and television static. Cool teal versus warm amber. Cinematic, photorealistic, dramatic volumetric lighting, shot on Arri Alexa.
```

**Alternate (split-screen dimensional boundary):**

```
[Pan right] The scene is divided into two halves separated by a boundary of crackling static and magnetic tape distortion. Left half: dense cyberpunk cityscape under cold fluorescent and neon cyan light — brutalist towers, wet streets, surveillance cameras. Right half: bioluminescent forest with warm amber-green organic glow — massive glowing fungi, hanging vines, soft mist. A figure in ((olive green puffer jacket)) walks from left to right, crossing the boundary. As they cross, their posture shifts from guarded to liberated. The boundary ripples like water. Camera pans slowly right, following the crossing. Photorealistic, cinematic, grounded cyberpunk meets natural wonder.
```

-----

### Scene 4 — Casper working with analog equipment in a bunker

**Camera approach:** Slow, contemplative push-in past equipment racks toward Casper. This is a sanctuary scene — the warmth of analog against the cold of the digital Dynasty. Camera should feel reverential, almost sacred.

**Primary prompt (environment push-in):**

```
[Push in, Pan right] Interior of a dimly lit concrete bunker. Walls lined with reel-to-reel tape machines, oscilloscopes displaying green waveforms, banks of toggle switches with amber indicator lights. Multiple ((CRT monitors)) display static and waveform patterns, their phosphor glow the primary light source. Cables snake across the floor. A figure in ((olive green puffer jacket)) sits at a mixing desk, ((blue headphones)) on ears, adjusting dials with graffiti-stained fingers. Camera pushes in slowly past equipment racks. Color palette: warm amber from CRT glow against cold concrete grey. Scan lines visible on monitors. VHS tape warmth. Shot on Arri Alexa, photorealistic, cassette futurism aesthetic. Contemplative mood.
```

**Alternate (intimate close-up):**

```
[Zoom in] Extreme close-up of a ((CRT monitor)) displaying scrolling green text with visible scan lines, phosphor glow, and color bleed at edges. Reflected in the curved glass is the silhouette of a figure wearing ((blue headphones)). The monitor sits on a metal desk surrounded by tangled patch cables, cassette tapes, and a reel-to-reel machine with slowly spinning reels. Warm amber desk lamp provides secondary light. Dust particles float through CRT light beams. Analog sanctuary, cassette futurism, photorealistic, contemplative, A24 intimate close-up style.
```

-----

### Scene 5 — Authority Bureau office scene

**Camera approach:** Cold, institutional, oppressive. The camera should feel clinical and detached — surveillance aesthetic. Two suited bureaucrats at a desk with CRT terminal, city skyline through window. This is the Dynasty’s world: sterile, controlled, inhuman.

**Primary prompt (institutional wide):**

```
[Pan left] A grey government office under harsh fluorescent strip lighting. Two men in identical dark suits sit at a heavy desk, faces partially in shadow. A ((CRT terminal)) between them displays data in monospaced green text. Behind them, floor-to-ceiling windows reveal a brutalist city skyline at dusk — geometric towers against overcast sky. The desk holds manila folders, a rotary phone, an institutional desk lamp. Camera pans slowly left across the room, cold and observational. No warmth in the lighting — fluorescent blue-white only. Institutional dread. Clinical desaturation, photorealistic, The Killing of a Sacred Deer meets The Wire aesthetic. Oppressive, bureaucratic.
```

**Alternate (surveillance POV):**

```
[Zoom in] High angle security camera perspective of the same office — slight wide-angle distortion, digital compression artifacts, timestamp overlay feel. Two suited figures at a desk, ((CRT terminal)) glowing between them. The feed has subtle static interference. Fluorescent lighting casts flat, shadowless illumination. The figures review documents without expression. Fixed camera, voyeuristic, detached. Cyberpunk surveillance state aesthetic, cold clinical palette, photorealistic.
```

-----

### Scene 6 — Young Casper studying at age 9 in a brutalist building

**Camera approach:** Tender, A24-intimate. A child alone in a monumental concrete space — vulnerability against architecture. Slow push-in toward the small figure to emphasize scale and isolation.

**Primary prompt (scale and intimacy):**

```
[Push in] Wide shot of a massive brutalist interior — exposed board-formed concrete walls, towering geometric pillars, monolithic beams overhead. At a small wooden desk in the center of this vast space sits a 9-year-old child, hunched over textbooks and notebooks, writing intently. A single practical light source — a warm amber desk lamp — creates an island of warmth in the cold concrete expanse. The child wears a too-large olive green sweater. Camera slowly pushes in from the wide establishing frame toward the small figure. The scale contrast is enormous — tiny human versus monumental architecture. Natural documentary intimacy, A24 cinematic realism, photorealistic, shallow depth of field as we approach, 50mm lens, subtle film grain. Contemplative, melancholic.
```

**Alternate (close study):**

```
[Static shot] Close-up of a child's hands turning pages of a worn textbook under warm amber lamplight. Pencil marks, eraser crumbs, dog-eared corners. In the soft background blur, raw board-formed concrete walls stretch upward into darkness. The child's face is partially visible — concentrated, young, earnest. A small portable radio near the desk plays quietly (implied). Warm intimate pool of light against cold brutalist void. A24 intimacy, photorealistic, 85mm lens, very shallow depth of field. Tender, isolated.
```

-----

### Scene 7 — Casper performing on stage in an underground venue

**Camera approach:** The orbital circling preset works powerfully here — the crowd becomes a swirling energy around the performer. Alternate with push-in close-ups of hands on equipment.

**Primary prompt (orbital performance):**

```
[Truck left, Pan right, Tracking shot] A dimly lit underground venue — exposed concrete ceiling, industrial pipes, thick haze from fog machines. A figure in ((olive green puffer jacket)) and ((chain mail face veil)) stands behind turntables and a mixing desk, ((blue headphones)) pressed to one ear. They manipulate vinyl records and faders with practiced precision. The small crowd moves in silhouette, packed close, bass energy visible in the haze. Camera orbits slowly around the performer. Single spotlight creates dramatic rim lighting through the chain mail. 16mm film grain, A24 indie concert aesthetic, muted amber and cyan lighting, photorealistic. Underground, raw, electric.
```

**Alternate (crowd perspective push-in):**

```
[Push in, Pedestal up] Shot from the back of a packed underground venue. Silhouetted heads and raised hands in the foreground. Beyond them, a figure in ((olive green puffer jacket)) commands the stage, backlit by a single overhead spot cutting through haze. Bass vibrations visible in the air. Camera pushes forward through the crowd and rises slightly. Magenta and amber light from small stage rigs. Concrete walls drip with condensation. Cinematic, photorealistic, raw underground energy, intimate concert film aesthetic.
```

-----

### Scene 8 — “SUBJECT: ABSENT” surveillance scene

**Camera approach:** This is the surveillance state in full display — a massive hall of monitors, Casper alone and watched. The camera should feel institutional: slow, clinical zoom toward the empty subject, or a static high-angle surveillance POV.

**Primary prompt (the hall):**

```
[Zoom in] A cavernous surveillance operations center — rows upon rows of ((CRT monitors)) covering every wall, each displaying different camera feeds. Fluorescent blue-white strip lighting overhead. In the center of this vast space, a single figure in ((olive green puffer jacket)) stands alone, back to camera, dwarfed by the wall of screens. One large central monitor displays "SUBJECT: ABSENT" in monospaced green text. The figure's reflection appears fractured across dozens of screens. Camera zooms in very slowly toward the figure and the central screen. Cold institutional palette, no warm tones, clinical surveillance aesthetic. Oppressive scale, photorealistic, Orwellian dread, grounded cyberpunk.
```

**Alternate (screen close-up):**

```
[Push in] Close-up of a CRT monitor displaying "SUBJECT: ABSENT" in flickering green monospaced text on a black screen. Scan lines roll slowly. The screen's phosphor glow illuminates the face of the figure reflected in the curved glass — ((chain mail face veil)), ((blue headphones)). Around this monitor, dozens of smaller screens show empty rooms, empty corridors, empty desks. All subjects: absent. Camera pushes in on the central screen. Digital surveillance hum. Cold cyan glow, clinical, photorealistic.
```

-----

### Scene 9 — Casper fighting armored guards in an office (bo staff, papers flying)

**Camera approach:** This fight happens in a civilized space being torn apart — the violence of resistance penetrating the sterile order of the Dynasty. Papers flying and office destruction create visual poetry. Use tracking and shake for chaos.

**Primary prompt (office destruction):**

```
[Tracking shot, Shake] A figure in ((olive green puffer jacket)) spins a bo staff in a government office — striking an armored guard across the torso, sending them crashing into a filing cabinet. Papers explode into the air. ((CRT monitors)) on desks shatter. Fluorescent lights flicker from the impact. Camera tracks laterally through the chaos, handheld, raw. Manila folders and documents flutter and spin through the frame. A second guard charges. The figure pivots, staff sweeping low. Office furniture topples. Harsh overhead fluorescent light, muted institutional greys suddenly punctuated by violence. Documentary intensity, A24 action realism, photorealistic, 35mm wide-angle.
```

**Alternate (aftermath stillness):**

```
[Static shot] Wide static shot of the destroyed office — overturned desks, scattered papers still settling, shattered CRT screens, cracked fluorescent tube dripping. In the center of the debris, Casper stands breathing hard, bo staff resting vertically against the floor, ((chain mail face veil)) slightly askew. Armored guards lie motionless around them. A single intact fluorescent tube buzzes overhead. Papers drift slowly down like snow. Complete stillness after violence. The static camera holds. Cold institutional palette disrupted by chaos. A24 contemplative aftermath, photorealistic, cinematic.
```

-----

## Part 9: Advanced workflow recommendations for SCB

### Building your prompt block library

Create a spreadsheet or document with reusable blocks that can be mixed and matched:

- **Character blocks** — Casper (full), Casper (partial/silhouette), Young Casper, Bureau agents
- **Environment blocks** — Alley/dead zone, Bunker/studio, Bureau office, Surveillance hall, Underground venue, Brutalist exterior, Portal threshold
- **Lighting blocks** — Warm amber analog, Cold fluorescent institutional, Neon cyberpunk, Single spotlight performance, Natural window A24
- **Camera blocks** — Each of the 15 commands with your preferred modifiers pre-written
- **Style blocks** — A24 realism, Surveillance, Concert, Action, Contemplative

### The generation order that maximizes consistency

1. **Generate Casper reference images first** via Midjourney/FLUX — front view, 3/4 view, detail views of key gear
2. **Lock identity** through S2V-01 with best reference image
3. **Generate hero shots** for each scene — the single most important frame
4. **Extend hero shots** into video using I2V-01-Director with camera commands
5. **Chain sequences** using last-frame extraction → I2V for continuity
6. **Generate B-roll** and environment shots with T2V-01-Director (no character consistency needed)

### Color coding the two worlds

Maintain strict color discipline across all prompts to reinforce the narrative contrast:

- **Casper’s world (resistance/analog):** Warm amber, olive green, magenta accents, VHS warmth, practical light sources, film grain
- **Dynasty’s world (authority/digital):** Cold fluorescent blue-white, clinical desaturation, no warm tones, harsh even lighting, digital artifacts, compression noise
- **Threshold/portal spaces:** Both palettes bleeding into each other, teal/cyan as the liminal frequency color

### Technical settings summary

|Setting               |Recommended value                              |
|----------------------|-----------------------------------------------|
|Model (camera control)|Hailuo 2.3 or I2V-01-Director                  |
|Model (character lock)|S2V-01                                         |
|`prompt_optimizer`    |`false` for Director Mode shots                |
|Resolution            |1080p (Hailuo 2.3) or 720p (Director models)   |
|Duration              |6 seconds per clip                             |
|Generations per shot  |3–9 (3×3 rule)                                 |
|Upscaling             |Topaz Video AI, Proteus, 2×, anti-flicker HIGH |
|Timeline              |DaVinci Resolve, 24fps for cinematic delivery  |
|Color space           |Rec.709 or DaVinci Wide Gamut                  |
|Export                |ProRes 422 HQ for mastering, H.265 for delivery|

-----

## Conclusion: What this toolkit actually enables

Hailuo’s Director Mode is not a virtual camera rig — it’s a **probabilistic interpretation engine** for cinematographic language. The 15 bracket commands provide the skeleton, but natural language modifiers supply the muscle, and disciplined prompt engineering creates the connective tissue. The most important principles are subtractive prompting (one primary motion, one intensity modifier, clear language), scale-relative calibration (wide shots need aggression, close-ups need restraint), and the I2V consistency anchor (always start from a reference frame when visual continuity matters).

For “Sprawling Cosmic Blip” specifically, the sharpest creative opportunity lies in using camera behavior itself as a storytelling device: **handheld shake and warm analog grain for Casper’s world of resistance and creation; clinical static shots and cold zoom-ins for the Dynasty’s surveillance apparatus.** When Casper crosses between worlds, the camera language should cross with them. That transition — from institutional stillness to human movement — is something Director Mode can express directly through sequential bracket commands within a single generation, making the camera itself an actor in the narrative.

The technology’s current limitation is the inability to merge S2V-01 character consistency with Director Mode camera control in a single pass. The multi-step workaround (S2V-01 → extract frame → I2V-Director) is functional but adds generation cycles. This gap will likely close as MiniMax integrates these capabilities. Until then, the most production-efficient path is to establish character identity early through strong reference images, maintain absolute prompt consistency across every generation, and let the 3×3 variation strategy absorb the stochastic nature of the output.