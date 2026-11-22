# Building Browser-Based 3D Guide Apps (F1, Anatomy, Solar System, Mechanical Builds): Best Practices for 2026

The best approach for a solo developer in late 2026 is to build one subject-agnostic "guide engine" on Three.js + React Three Fiber (R3F) + drei. Content (steps, camera poses, highlighted parts, labels, quizzes) should live in data files, never in components. Assets go through a strict glTF pipeline (named nodes → gltf-transform → Meshopt + KTX2). Render on demand, and keep every lesson usable without the 3D canvas. The learning research backs 3D for spatial understanding, but the gains are modest and depend on design: learner-paced segments, signaling, and interactivity matter more than visual fidelity.

## TL;DR

- **Stack (confirmed, current):** three.js r187 (Oct 30, 2026) with `WebGPURenderer` (automatic WebGL 2 fallback), R3F 9.8.x on React 19, drei, GSAP (free for commercial use since April 30, 2025), glTF/GLB through gltf-transform. WebGPU now ships in Chrome, Edge, Safari 26 and Firefox (Windows/macOS), so treat it as an upgrade path, not a requirement. Firefox on Linux/Android and pre-26 iOS devices still need the WebGL 2 path.
- **Pedagogy (evidence-based):** 3D beats 2D mainly for *spatial* knowledge (pooled d≈0.50 vs. d≈0.30 for factual knowledge in Yammine & Violato's 2015 meta-analysis), and low-spatial-ability learners can be disadvantaged. Design every guide as learner-paced segments with highlighting/signaling, one change per step, and a free-explore mode unlocked after the guided tour. That follows Mayer's segmenting/signaling principles and Agrawala et al.'s assembly-instruction principles.
- **Biggest leverage for a solo dev:** a data-driven step schema (JSON/MDX) that drives camera, visibility, highlight, explode-offset and annotation state, plus an asset convention (stable node names = content IDs). That one decision makes the same engine serve F1, anatomy (BodyParts3D is now CC BY 4.0), solar system (JPL Horizons + Solar System Scope CC BY 4.0 textures) and furniture/LEGO-style builds.

---

## 1. Survey: What's Out There and What to Learn From Each

| App / site | Domain | What it teaches well | UX / tech lessons | Worth studying for |
|---|---|---|---|---|
| **BioDigital Human** | Anatomy | Layered anatomy with highlight, isolate, dissect (remove), transparency, annotations, guided "tours" | Early WebGL pioneer. Exposes an embeddable Viewer API (iframe + postMessage, e.g. `human.camera.flyTo`, pick events, annotations API). Initial view shows skeleton only and lets users add systems (progressive disclosure) | The canonical **verb set** (highlight / isolate / dissect / x-ray / annotate / tour) and the idea of an API-first viewer |
| **Zygote Body** | Anatomy | Whole-body layer slider (skin → muscle → skeleton) | A 2014 WebGL comparison paper reported Zygote loaded the whole body up front and managed memory better than BioDigital at the time | A single "depth" slider as a simple mental model |
| **Complete Anatomy (Elsevier/3D4Medical)** | Anatomy | Fast labeling, cross-sections, educator authoring | Heavy native-first app with a web presence. Strong curriculum/authoring tooling | Authoring workflows for teachers (content as data) |
| **Z-Anatomy** | Anatomy (open) | Open atlas built on BodyParts3D, with Terminologia Anatomica names | Blender template + web/Android viewers | A free, inspectable reference dataset and naming scheme |
| **NASA's Eyes on the Solar System** | Space | Real-time and time-scrubbed (1950–2050) positions of planets, moons and 150+ missions "using the most accurate data" | Browser-based. Time controls (rewind/fast-forward), mission "ride-alongs", simple mode | **Time as a first-class control**, and ephemeris-driven accuracy (positions derived from JPL/NAIF SPICE data) |
| **Solar System Scope** | Space | Approachable orrery + night sky, embeddable | Publishes its planet textures under CC BY 4.0 | Readable-scale presentation; texture source |
| **Bartosz Ciechanowski (ciechanow.ski)** | Mechanics/physics | Builds understanding from first principles (crank → piston → valves → cam timing), with one slider-controlled demo per idea | Hand-written WebGL. Models made in Shapr3D with Blender post-processing, animations done by hand. Many small focused canvases, not one giant scene | **Gold standard for explanatory pacing**: each demo isolates *one* variable the reader controls |
| **Animagraffs** | Mechanics | Animated exploded/cutaway explainers (engines, vehicles) | Mostly pre-rendered video/GIF, not real-time | Visual vocabulary: exploded views, cutaways, color-coding by subsystem |
| **IKEA / LEGO-style digital instructions** | Assembly | One step per frame, parts-to-add callout, arrows showing attachment | LEGO Builder app adds rotate/zoom per step | Step granularity, parts-list-per-step, "what changed" emphasis |
| **`<model-viewer>` (Google)** | Product/general | Hotspot annotations, AR handoff | Web component with built-in keyboard rotation, `alt` text, and screen-reader interaction prompts | **Accessibility baseline** for any 3D viewer |
| **Sketchfab** | General | Annotations with camera "stops" (a tour baked into the model page) | Embed API, per-model license filters | Annotation-as-camera-bookmark pattern |
| **Product configurators (cars, furniture)** | Commerce | Variant switching, explode/inspect | Typically Three.js/Babylon/PlayCanvas with heavy asset optimization | Performance discipline on mobile |

**Takeaways (my synthesis):**
1. The strongest *teaching* examples (Ciechanowski, NASA Eyes, BioDigital tours) all **constrain the scene to answer one question at a time**. The weakest experiences dump a full model and an orbit control on the user.
2. Anatomy apps converge on the same small set of verbs: **highlight, isolate, hide/dissect, x-ray, label, section, tour**. Build those once and reuse them for F1 (aero, power unit), engines, and furniture.
3. NASA Eyes shows that for dynamic systems, **a time scrubber is the primary control**. The F1 equivalent is the lap/sector timeline or the gearbox/ERS cycle, and the assembly equivalent is the step timeline.

---

## 2. Instructional Design for 3D: What the Evidence Says

### 2.1 3D vs. 2D for learning (anatomy literature)
- **Confirmed (peer-reviewed):** Yammine & Violato's 2015 meta-analysis (*Anatomical Sciences Education*, 36 studies, 2,226 participants) found 3D visualization technologies improved factual knowledge (d≈0.30) and, more strongly, spatial knowledge (d≈0.50), with higher satisfaction (d≈0.28). Students with **lower spatial ability were at a significant disadvantage** with 3D tools.
- **Confirmed:** Bogomolova et al. (2021, *Medical Education*) found stereoscopic 3D helped (ES≈0.54) **only when the 3D model was interactive** (the learner manipulates or explores). Stereopsis had no effect with non-interactive 3D images.
- **Mixed/contested:** A 2024 meta- and regression analysis in *BMC Medical Education* (PMC11055294) and a network meta-analysis (Research Square preprint, not yet peer-reviewed) found that VR/AR improved test scores while desktop "3D technology" did **not** reach statistical superiority over traditional methods. In a randomized trial by Keedy et al. (2011, *Anatomical Sciences Education*, n=46, hepatobiliary anatomy), students rated an interactive 3D module higher (4.5 vs. 3.7 out of 5, P=0.02). Yet the module "neither enhanced nor inhibited learning… compared to an informationally equivalent traditional textbook style approach."
- **Interpretation:** 3D is not automatically better. It pays off for **spatial relationships** (what's behind/inside/connected to what), and only when the learner actively manipulates it. Pair 3D with 2D labels and diagrams, and support low-spatial-ability users with guided camera moves and orientation cues.

### 2.2 Cognitive load principles that map directly to 3D guides
From Mayer's cognitive theory of multimedia learning and Wouters, Paas & van Merriënboer's (2008) review of animated models:
- **Segmenting (confirmed):** learners do better with learner-paced segments than with continuous animation. Mayer & Moreno report positive transfer effects in five of five tests. Rey et al.'s meta-analysis (2019, *Educational Psychology Review*) covered 56 investigations with 88 pairwise comparisons and found "a significant segmenting effect with small to medium effects for retention and transfer performance." → Every guide step is a discrete, user-advanced segment ("Next" button, not autoplay).
- **Pre-training (confirmed):** learning goes better when learners know the names and characteristics of key components first. → Start each guide with a "meet the parts" step (e.g., F1: chassis, power unit, floor, wings) before showing interactions.
- **Signaling/cueing (confirmed):** highlight what matters to prevent visual search. → Outline or color-highlight the active part, dim the rest (x-ray/ghost), point leader lines at it.
- **Contiguity (confirmed):** put text near the thing it describes, at the same time. → Labels anchored in 3D space, or a side panel that updates in sync with the camera.
- **Start simple, increase complexity (Wouters et al.):** begin with low element interactivity. → Progressive disclosure: show the subsystem, then the assembly, then the whole.
- **Germane-load techniques:** prediction prompts ("what happens to the valve next?"), subgoal grouping, and imagination. → Cheap quiz/check interactions between segments.

### 2.3 Assembly/build sequencing (mechanical, furniture, LEGO-style)
Agrawala et al.'s SIGGRAPH 2003 "Designing Effective Step-by-Step Assembly Instructions" (and the 2004 Heiser et al. validation) derive principles from cognitive psychology experiments:
- **One diagram per step, no omitted steps.**
- **Clear, explicit order** (numbered steps).
- **Parts added in each step must be visible.** Rotate the camera so they aren't occluded.
- **Arrows/guidelines to show attachment.**
- **Group parts hierarchically** (sub-assemblies first), and keep orientation consistent between steps.

In 3D this translates to: each step animates incoming parts from an exploded offset along an attachment vector, auto-frames the camera so the new parts face the viewer, ghosts already-placed parts, and shows a "parts for this step" tray.

### 2.4 Technique toolbox (when to use which)

| Technique | Best for | Implementation note |
|---|---|---|
| Exploded view | Assemblies (engine, gearbox, furniture) | Store per-part explode vectors in data. Animate `0→1` factor. |
| Cutaway / cross-section | Internals (cylinders, organs, F1 monocoque) | Clipping planes (`material.clippingPlanes`) plus cap rendering. Anatomy apps use section planes extensively. |
| X-ray / ghosting | Context while focusing on an inner part | Lower opacity + `depthWrite=false` on context parts. Watch transparency sorting. |
| Isolate / hide | Reducing clutter | Visibility map keyed by node ID |
| Labels + leader lines | Naming parts | HTML overlays (drei `<Html>`) for accessibility and crisp text. Declutter by priority. |
| Hotspots | Optional deep-dives | Focusable DOM buttons, not canvas-only sprites |
| Scripted camera moves | Guided tours | Data-defined camera poses with eased transitions. Respect reduced motion. |
| Scroll-driven storytelling | Linear narratives (marketing-style explainers) | GSAP ScrollTrigger. Pair with explicit step controls so it stays learner-paced. |
| Quizzes/checks | Retention | "Click the part that…" pick-tests reuse the selection system |

**Guided vs. free exploration:** the evidence on guided discovery and segmenting favors **guided first, free-explore second**. Unstructured exploration helps experts and high-spatial-ability users, but novices get lost. Offer "Tour" and "Explore" modes over the same scene.

---

## 3. UX and Interaction Patterns

**Camera controls**
- Use drei `CameraControls` (or `OrbitControls`) with **constraints**: min/max distance, polar angle limits (don't let users go under the floor of the F1 car), and pan limits. Unconstrained orbit is the #1 way users get lost.
- Always provide a **"reset view"** button and a "focus selected" (fly-to) action. BioDigital's API exposes `camera.flyTo` for this reason.
- Touch: one-finger orbit, two-finger pinch zoom/pan. Avoid hijacking page scroll unless the canvas is fullscreen. In scroll-story layouts, disable orbit while scrolling.
- **Onboarding:** a short interaction hint that fades after first use. `<model-viewer>`'s `interaction-prompt` (shown after 3s of no interaction by default, and announced to screen readers) is a good reference.

**Selection and highlighting**
- Pointer events via R3F raycasting. Highlight with an outline post-process or an emissive tint. Dim non-selected parts.
- A **part tree / search panel** (DOM) mirrors the scene graph: click a name → highlight + fly-to. This is also the main accessibility path.

**Timelines**
- Assembly: a step scrubber with discrete stops.
- Solar system: a continuous time scrubber with rate controls (NASA Eyes lets users "control space and time").
- F1: lap timeline / sector markers / engine-cycle phase.

**Scale (solar system)**
- True scale makes planets invisible specks. Provide a **"readable scale" vs. "true scale" toggle**, and label which mode is active. Many open-source orreries implement a continuous teaching↔true-scale blend. Use logarithmic distance compression or separate size/distance scaling, and say so on screen so you don't teach misconceptions.
- Use a floating origin / camera-relative rendering for huge coordinate ranges, so float32 precision doesn't jitter.

**Accessibility (non-negotiable for education)**
- Every step's content must exist as **DOM text** (headings, descriptions, part names). The canvas is an enhancement. This also gives you a non-3D fallback (static images per step, generated from the same step data).
- Keyboard: Tab through hotspots/part list, arrow keys to orbit (as `<model-viewer>` does), Enter to select, keys for Next/Previous step.
- Screen readers: `alt`/`aria-label` on the canvas region describing the current view, and live-region announcements on step change. Scott Vinkle's testing of `<model-viewer>` found NVDA/JAWS virtual-cursor arrow keys conflict with model rotation, so test with real screen readers.
- `prefers-reduced-motion`: replace fly-throughs with cuts or short fades. Disable auto-rotate.
- Color: don't encode systems by color alone (arteries red / veins blue is fine *with* labels). Check label contrast against varied 3D backgrounds by using solid label backgrounds.

---

## 4. Tech Stack and Architecture

### 4.1 Library comparison (status as of Nov 2026)

| Option | Status / version | Strengths | Weaknesses | Verdict for this project |
|---|---|---|---|---|
| **Three.js** | r187, Oct 30, 2026. ~12.2M weekly npm downloads (≈39× `@babylonjs/core`, per Utsubo, Sept 2026) | Largest ecosystem. `WebGPURenderer` with automatic WebGL 2 fallback (zero-config since r171). TSL node materials | Breaking changes every release (e.g., r183 renamed `PostProcessing`→`RenderPipeline`; r186 removed `PCFSoftShadowMap`) | **Core** |
| **React Three Fiber + drei** | R3F 9.8.x stable (React 19.0–19.3 compatible). v10 in alpha | Declarative scene graph = natural fit for data-driven steps. `frameloop="demand"`, PerformanceMonitor, `<Html>`, `CameraControls`, `Bounds`, `useGLTF` | Couples React upgrades to R3F majors (v9 ↔ React 19) | **Core (the user's plan is sound)** |
| **Babylon.js** | Active, strong WebGPU support | Batteries-included engine, inspector, GUI, physics | Smaller web-dev ecosystem than three | Good alternative if you prefer an engine over a library |
| **PlayCanvas** | Active, ships WebGPU | Editor + engine, excellent mobile perf, Gaussian splats | Editor-centric workflow | Consider for editor-driven teams |
| **`<model-viewer>`** | Web component on three.js | Fastest path to accessible single-model viewing + AR | Not built for multi-step choreography | Use for **fallback/embed** views |
| **Needle Engine** | Unity/Blender → three.js export | Author scenes in Blender/Unity | Commercial licensing tiers. Adds tool dependency | Optional if you'd rather author in Blender |
| **Spline** | Design tool with web export | Very fast for stylized marketing scenes | Less control over performance and data-driven logic | Prototyping only |

### 4.2 WebGPU vs. WebGL 2 in 2026
- **Confirmed:** WebGPU ships by default in Chrome/Edge (113+), Firefox 141+ on Windows (July 2025) and later macOS, and Safari 26 (Sept 2025, macOS/iOS/iPadOS/visionOS). Firefox on Linux and Android remains incomplete, and devices that can't update to iOS 26 don't get WebGPU.
- **Recommendation:** `import * as THREE from 'three/webgpu'` and use `WebGPURenderer`. It falls back to WebGL 2 automatically. Don't use WebGPU-only features (compute) for core teaching content. For a guide app, WebGPU's benefits (compute, lower CPU overhead) are nice-to-have, not essential. One caution: some drei/postprocessing helpers are still WebGL-oriented. If your outline/bloom stack depends on `@react-three/postprocessing`, verify compatibility or stay on `WebGLRenderer` until it's ported (speculative: check at build time).

### 4.3 State management for steps/scenes
- **Zustand** (pmndrs, same ecosystem) for guide state: `currentStep`, `mode` (tour/explore), `selection`, `visibility`, `explode`, `time`. Components subscribe to slices. Animation code reads state transiently in `useFrame` without React re-renders. (R3F docs: "never setState" inside `useFrame`.)
- Model the guide as a **state machine** (XState or a simple reducer): steps are states, and transitions trigger camera/visibility/animation tweens. That makes back/forward, deep links (`?step=7`) and analytics trivial.
- **URL as state:** encode step + selection in the URL for shareable deep links and LMS embedding.

### 4.4 Scene-graph organization for part hierarchies
- Keep the glTF node hierarchy **semantic**: `F1_Car > PowerUnit > MGU-K`, `Body > Skeletal > Skull > Mandible`, `Engine > Head > Camshaft_Intake`. Node names are **stable IDs** referenced by content files.
- Load once, then **index nodes by name** into a map (`gltfjsx` generates typed JSX with named nodes and is good for hand-tuned components). For data-driven apps, walk the scene and build `Map<id, Object3D>` instead.
- Separate **semantic hierarchy** (for UI/tree) from **render optimization** (merged/instanced meshes). Store merged-mesh-to-part mappings (e.g., per-part face ranges or a `BatchedMesh` per-instance ID) if you merge.

### 4.5 Animation
- **glTF animations** (`useAnimations`) for authored motion (pistons, suspension travel, valve timing), scrubbed by setting `action.time` from the step/time state.
- **GSAP** for camera choreography, explode factors and UI timelines. Since April 30, 2025, GSAP and all former Club plugins are free including commercial use. Note it's a proprietary "no charge" license, not MIT.
- **Theatre.js** for visually keyframed camera sequences. It's useful, but check maintenance status before depending on it (not verified for 2026 in this research).
- Springs (`@react-spring/three` or `maath/easing.damp`) for interruptible UI-driven motion. Interruptibility matters when users click "Next" mid-transition.

### 4.6 Annotations and post-processing
- Labels: drei `<Html>` (DOM, accessible, crisp) with occlusion. Use `<Billboard>`/`<Text>` (SDF text) only for many in-scene labels. Leader lines: drei `<Line>` from anchor to label, with a label-collision/priority pass.
- Outlines/selective bloom: `@react-three/postprocessing` (Outline, SelectiveBloom) on WebGL. On `WebGPURenderer`, use three's node-based `RenderPipeline` (renamed in r183) passes. Post-processing is expensive on mobile, so make it toggleable via PerformanceMonitor.
- Physics: rarely needed for guides. If needed (falling parts, suspension demo), `@react-three/rapier`. Prefer authored animation for teaching accuracy.

---

## 5. 3D Asset Pipeline

**Standard:** glTF 2.0 / GLB everywhere. glTF is in meters, Y-up. Convert CAD (mm) and medical (mm) data accordingly.

**Blender workflow conventions (recommended):**
1. **Name every interactive object** with a stable ID: `pu_mguk`, `fma_9611_mandible`, `step03_side_panel_L`. Names are your content keys.
2. **Hierarchy = teaching hierarchy** (system → subsystem → part). Apply transforms. Set pivots at real rotation axes (wheel hubs, hinge pins, crank center) so animations are correct.
3. Use **custom properties → glTF `extras`** for metadata: `{"step": 3, "explode": [0,0.2,0], "fma": "FMA:52748", "label": "Mandible"}`.
4. Separate materials per subsystem for color-coding. Keep material count low.
5. Export one GLB per "chapter" or LOD tier rather than one monolith.

**Optimization (confirmed commands, glTF-Transform docs):**
```bash
npm i -g @gltf-transform/cli
gltf-transform inspect in.glb                       # find where bytes are
gltf-transform optimize in.glb out.glb --compress meshopt --texture-compress ktx2 --texture-size 2048
# finer control: UASTC for normal/ORM, ETC1S for color
gltf-transform uastc in.glb a.glb --slots "{normalTexture,occlusionTexture,metallicRoughnessTexture}"
gltf-transform etc1s a.glb out.glb --quality 128
```
- **Meshopt vs. Draco:** Meshopt decodes faster and also compresses animations/morph targets, and it is now `optimize`'s default. Draco often gives smaller static geometry. Either works; Meshopt is the better default for animated guides.
- **Caution:** `optimize` by default **joins/flattens/simplifies** meshes. That will destroy your named, individually selectable parts. For interactive models, disable `--join`/`--flatten`/`--simplify` (check `gltf-transform optimize -h` for your version) or run individual steps. This is the most common pipeline mistake in guide apps.
- **KTX2/Basis:** reduces *GPU memory*, not just download size. That's critical on mobile. WebP/AVIF shrink downloads but decode to full RGBA in VRAM.
- **LOD:** drei `<Detailed>` or separate low/high GLBs. Load low first, swap in high (progressive loading).
- **Instancing:** bolts, fasteners, LEGO bricks, rivets, asteroid belts → `InstancedMesh`/`BatchedMesh`.

**CAD → web (mechanical builds, F1 parts):**
- STEP/IGES are exact B-rep surfaces and must be **tessellated**. **occt-import-js** v0.0.23 (Open CASCADE compiled to WASM, LGPL-2.1) parses STEP in the browser or Node and returns a node hierarchy with per-part meshes and colors. Its `.wasm` file is 7.6 MB. Several 2026 open-source viewers use it in Web Workers. Note that it hasn't had a release since Dec 3, 2024, and Snyk marks it "INACTIVE," so pin it and plan for maintenance risk. Mayo (Qt + OpenCascade, desktop/CLI) also converts STEP ↔ glTF in batch.
- Recommended: **convert offline at build time** (Node script: STEP → occt-import-js → glTF-Transform → Meshopt), not in the user's browser. Choose tessellation deflection deliberately: CAD exports are often wildly over-tessellated on fillets.
- Preserve the CAD assembly tree as glTF nodes. That *is* your assembly order scaffold, though real assembly order still needs human curation.

**Photogrammetry/scans:** decimate (Blender Decimate / Instant Meshes), retopologize if parts must be separable, bake high-poly detail to normal maps, and remove floaters. Scans are a single fused mesh, so segment manually if you need part-level interaction.

**Medical imaging → anatomy meshes (subagent research, confirmed from primary docs):**
- **TotalSegmentator** v2.18.0 (Aug 12, 2026): code is Apache-2.0. The default `total` CT task segments **117 classes**, and `total_mr` segments **50 classes** on MR. Input can be a NIfTI file or a folder/zip of DICOM slices. **Licensing caveat:** some subtasks (e.g., `heartchambers_highres`, `appendicular_bones`, `tissue_types`) require a license, free for non-commercial use, commercial license by contact. It's "not a medical device."
- **3D Slicer:** Segmentations → "Export to files" writes STL/OBJ. The **SlicerOpenAnatomy** extension's OpenAnatomy Export "exports a model hierarchy or segmentation node… into a single glTF or OBJ file, including all the model colors and opacities; and for glTF also model hierarchy and model names." It can produce decimated low-poly output, and it exports in meters (mm→m root transform). Shading converts to PBR, so colors shift slightly.
- Pipeline: **DICOM → TotalSegmentator → Slicer segmentation → OpenAnatomy glTF export → gltf-transform**. Patient data must be de-identified, and you need rights to the scan.

---

## 6. Freely Licensed Asset Sources (research, not legal advice)

| Source | Domain | License (as researched) | Attribution / caveats |
|---|---|---|---|
| **BodyParts3D (DBCLS)** | Anatomy (adult male, every mesh keyed to FMA ID) | **CC BY 4.0** per the official DBCLS license page updated **2025-02-27**. Earlier releases: CC BY-SA 2.1 JP | Credit line: "BodyParts3D, © The Database Center for Life Science licensed under CC Attribution 4.0 International." The OBJ files themselves still carry the old BY-SA header, so document which license you rely on. |
| **Z-Anatomy** | Anatomy (most complete layered model, built on BodyParts3D) | **CC BY-SA 4.0** | ShareAlike: derivatives must stay BY-SA. Some bundled sub-models are **NC** (inner ear CC BY-NC-SA, kidney CC BY-NC), and the definitions come from Wikipedia (BY-SA). Strip the NC parts for commercial use. |
| **Open 3D Model (anatomytool.org)** | Anatomy (built on Z-Anatomy) | CC BY-SA | Same ShareAlike implications |
| **Human Reference Atlas 3D (HuBMAP)** | ~26 organs, male + female | CC BY 4.0 (per repo LICENSE, as reported) | Good for female anatomy gap |
| **NIH 3D (3d.nih.gov)** | Biomedical models (GLB available) | **Per-entry**: Public Domain/CC0, CC BY, CC BY-NC, even NC-ND observed | Terms: "NIH 3D does not enforce license terms… Users must review and comply with the licensing terms associated with each file." Check every model. |
| **Open Anatomy Project (SPL atlases)** | Regional atlases (brain, abdomen, knee) | 3D Slicer License, not a CC license | Read terms before use |
| **NASA 3D Resources** | Spacecraft, planets, textures | "Free and without copyright" (generally not subject to US copyright) | NASA insignia/logos are **protected**. Don't imply endorsement. |
| **Solar System Scope textures** | Planet maps (equirectangular) | **CC BY 4.0**: "use, adapt, and share… even commercially" | Attribution required |
| **JPL Horizons API** | Ephemerides | Public data service (JSON/text API) | Cite JPL. Precompute rather than calling live per user. |
| **GrabCAD Community** | CAD parts | **Non-commercial by default**: "content submitted by the Contributors is for non-commercial use only, unless otherwise agreed in writing" | Commercial use needs explicit designer permission. Trademarked products (e.g., real F1 parts) are a further risk. |
| **Thingiverse / Printables** | Printable models | Per-model CC (often NC). Prusa also uses its own Open Community License on some designs | Filter for CC0/CC BY. MyMiniFactory announced on Feb 12, 2026 (GlobeNewswire press release) that it "has acquired 100% of Thingiverse from Ultimaker." |
| **Poly Haven** | HDRIs, textures, models | CC0 (widely known, not re-verified here) | No attribution required, but appreciated |
| **Kenney** | Stylized game assets | CC0 (widely known, not re-verified here) | Good for LEGO-style/blocky builds |
| **Sketchfab** | Everything | Per-model. Filter by "Downloadable" + license (CC0, CC BY, CC BY-SA, CC BY-NC…) | Many F1 car models are fan-made replicas of trademarked liveries: commercial use risky |

**License hygiene for a solo dev:** keep a `CREDITS.json` alongside each asset (source URL, license, author, date downloaded, modifications) and render it into an in-app credits page automatically. Avoid mixing NC assets into anything you might monetize, and isolate BY-SA assets so ShareAlike obligations don't spread to assets you don't want under BY-SA.

**F1-specific caveat:** team names, liveries and car designs are trademarked/IP. A generic, unbranded "2026-regulation-style" car model is safer for anything public or commercial.

---

## 7. Performance (Especially Mobile)

### 7.1 Budgets (practitioner guidance; adjust after profiling)

| Metric | Mobile target | Desktop target | Source / status |
|---|---|---|---|
| Draw calls | ≤ ~100–200 | a few hundred | R3F docs: "no more than 1000 as the very maximum, and optimally a few hundred or less" (confirmed). Mobile figure is practitioner consensus. |
| Triangles on screen | ~100k–500k | 1–3M | Practitioner rule of thumb (widely reported) |
| Texture resolution | 1k–2k max per map, KTX2 | 2k–4k | `gltf-transform optimize` caps at 2048 by default |
| Initial download (first meaningful 3D) | < 3–5 MB | < 10–15 MB | Rule of thumb. Stream the rest. |
| GPU texture memory | keep well under ~256 MB on low-end phones | — | Speculative/device-dependent: test |
| Frame time | 16.7 ms (60 fps), or 33 ms acceptable when static | 16.7 ms | Standard |

### 7.2 Techniques
- **`frameloop="demand"`** (confirmed, R3F docs): render only when something changes. Drei controls call `invalidate()` automatically, and you call `invalidate()` after imperative changes. A guide is idle most of the time, so this is the single biggest battery/thermal win. During tweens, render continuously, then return to demand.
- **Adaptive quality:** drei `<PerformanceMonitor onIncline/onDecline flipflops={3} onFallback>` stepping DPR (e.g., 1→1.5→2) and toggling post-processing. `<Canvas dpr={[1, 2]}>` caps pixel ratio. `regress()` lowers quality while orbiting ("Mere calls to regress() will not change or affect anything!" — your app must listen to `performance.current`).
- **Lazy loading:** per-chapter GLBs with `useGLTF.preload` for the *next* step only. Suspense fallbacks with real progress (`useProgress`). Show a low-poly proxy or poster image first.
- **Memory/disposal:** R3F auto-disposes on unmount, but cached `useGLTF` assets persist. Call `useGLTF.clear(url)` when leaving a chapter. Custom `Object3D` subclasses must call `super.dispose()` (changed in r186).
- **Avoid per-frame allocation** in `useFrame`. Never `setState` there.
- **Transparency is expensive** (overdraw, sorting). X-ray modes on hundreds of anatomy meshes are a classic mobile frame-killer, so reduce to a few merged "context" meshes when ghosted.
- **Profiling:** three's built-in Inspector (since r181, works on both backends), `stats-gl`, `renderer.info`, Spector.js (WebGL).
- **Testing:** real low-end Android (e.g., 3–4 GB RAM devices) and an older iPhone on iOS < 26 (forces the WebGL 2 path). Watch thermal throttling over 10-minute sessions, not just a 30-second benchmark.
- **PWA/offline:** service worker (Workbox) caching GLB/KTX2 by chapter. Explicit "download for offline" for classroom use. Serve with Brotli/gzip (Meshopt reaches its best ratio when combined with HTTP compression) and long-lived immutable cache headers with hashed filenames.

---

## 8. Data-Driven Accuracy and Content Authoring

**Solar system**
- Use **JPL Horizons** (`https://ssd.jpl.nasa.gov/api/horizons.api`, JSON output, `EPHEM_TYPE=VECTORS` or `ELEMENTS`) at **build time** to generate state vectors or orbital elements over your supported date range. Ship compact tables and interpolate client-side. NASA's Eyes uses SPICE kernels from NAIF, the same data mission planners use.
- For a lightweight app, Keplerian elements (JPL's approximate planetary elements) propagated client-side are accurate enough for visualization. Use Horizons vectors for spacecraft and close encounters.
- Display the active scale mode and the epoch/date. Note that JPL Horizons is authoritative, but simplified Kepler propagation drifts over centuries.

**Anatomy**
- Key every part by a **controlled vocabulary**: FMA IDs (BodyParts3D already maps every mesh to an FMA ID) and **Terminologia Anatomica (TA2, 2019)** names. Z-Anatomy distributes TA2 terms. Store Latin + English + lay names. This enables search, localization and quizzes from the same data.
- Add an "educational, not a medical device" disclaimer, as NIH 3D's and TotalSegmentator's terms both do.

**F1 / mechanical**
- Assembly order: start from the CAD assembly tree, then have it reviewed by a domain expert. Encode precedence constraints (A before B) in data and validate that each step's prerequisites are visible.
- F1 regulations change (2026 rules introduced a new power unit and active aero). Version your content by season.

**Content authoring workflow (recommended)**
```jsonc
// guides/f1-power-unit/steps/03-mguk.json
{
  "id": "mguk",
  "title": "MGU-K: harvesting braking energy",
  "body": "mdx:./03-mguk.mdx",
  "camera": { "position": [1.2, 0.6, 2.1], "target": [0, 0.3, 0.4], "fov": 35 },
  "show": ["pu_*", "chassis_floor"],
  "ghost": ["chassis_*"],
  "highlight": ["pu_mguk"],
  "explode": { "pu_*": 0.3 },
  "labels": [{ "node": "pu_mguk", "text": "MGU-K", "priority": 1 }],
  "animation": { "clip": "brake_regen", "loop": true },
  "check": { "type": "pick", "prompt": "Click the component that recovers braking energy", "answer": "pu_mguk" }
}
```
- Text in **MDX** (with Velite or Contentlayer-style content collections, or Astro content collections), schemas validated with **Zod**, so typos in node IDs fail the build.
- Build a tiny **in-app "author mode"** (dev only): orbit to a view → "copy camera pose" → paste into JSON. This cuts authoring time dramatically.
- A headless CMS (Sanity, Payload, Strapi, or Git-based Decap/TinaCMS) is optional. For a solo dev, Git + JSON/MDX + Zod validation is simpler and versioned.

---

## 9. Common Pitfalls and Anti-Patterns

1. **"Here's a model, good luck"**: full scene + orbit controls with no guided path. Novices and low-spatial-ability learners get lost (Yammine & Violato's spatial-ability finding).
2. **Autoplaying continuous animation** instead of learner-paced segments (contradicts the segmenting principle).
3. **Too much on screen at once**: all labels, all systems, bloom, particles. Violates coherence/signaling. Decorative effects add extraneous load.
4. **Running `gltf-transform optimize` with defaults** on interactive models: it merges your named parts into one mesh and breaks selection.
5. **Content hard-coded in components**: every edit needs a code change. You can't reuse the engine across subjects.
6. **Unconstrained camera** (inside meshes, under the floor, lost at infinity) and **no reset button**.
7. **Rendering every frame for a static scene**: drained batteries, hot phones.
8. **Canvas-only content**: invisible to screen readers and search engines, and no fallback when WebGL/WebGPU fails.
9. **Ignoring motion sensitivity**: long swooping camera moves with no reduced-motion alternative.
10. **Silent scale distortion** in solar-system apps, which teaches the wrong mental model.
11. **License contamination**: mixing NC/SA assets (e.g., parts of Z-Anatomy) into a commercial product, or GrabCAD models used commercially without permission.
12. **Monolithic 100 MB GLB** with uncompressed PNG textures. Long load, mobile crash from VRAM exhaustion.
13. **Transparent x-ray across hundreds of meshes**: sorting artifacts plus overdraw.
14. **Chasing the latest three.js release mid-project** without pinning. Releases land every 7–11 weeks with breaking changes.

---

## 10. Recommended Starter Architecture and Checklist

### 10.1 Architecture

```
/apps/web                 (Vite or Next.js/Astro + React 19)
/packages/guide-engine    (subject-agnostic)
  GuideCanvas.tsx         Canvas(frameloop="demand", dpr capped) + PerformanceMonitor + Suspense
  SceneRegistry.ts        loads GLB(s), builds Map<nodeId, Object3D>, glob matching ("pu_*")
  store.ts                Zustand: step, mode, selection, visibility, ghost, explode, time
  StepController.tsx      applies step JSON → visibility/ghost/highlight/explode/animation
  CameraDirector.tsx      CameraControls + data-defined poses, reduced-motion aware, reset/focus
  Highlighter.tsx         outline/emissive selection (WebGL or WebGPU path)
  Labels.tsx              <Html> labels + leader lines + declutter by priority
  SectionPlane.tsx        clipping planes + caps
  Timeline.tsx            discrete step scrubber OR continuous time scrubber
  PartTree.tsx            DOM tree + search (accessibility backbone)
  Quiz.tsx                pick-the-part / multiple choice
  A11yLayer.tsx           live region, keyboard shortcuts, static-image fallback
  AuthorMode.tsx          dev-only: copy camera pose / node id
/packages/content-schema  Zod schemas for Guide, Step, Label, Check, Credits
/content/{f1,anatomy,solar,ikea-chair}/   steps/*.json + *.mdx + credits.json
/assets-pipeline          Blender export conventions, STEP→GLB (occt-import-js), DICOM→GLB notes,
                          gltf-transform scripts (no join/flatten for interactive parts), KTX2
/public/models/<guide>/<chapter>.glb (hashed, immutable cache)
```

Subject-specific "plugins" only add what's unique: `OrbitPropagator` (solar), `TerminologyIndex` (anatomy), `ExplodeAlongAxis` + `PartsTray` (assembly), `LapTimeline` (F1).

### 10.2 Checklist
- [ ] Pin three, R3F, drei versions. Use `WebGPURenderer` with WebGL 2 fallback, or `WebGLRenderer` if your post-processing requires it.
- [ ] `frameloop="demand"`, `dpr={[1,2]}`, PerformanceMonitor, controls with `regress`.
- [ ] Node naming convention documented. Every content ID validated against the GLB at build time.
- [ ] gltf-transform pipeline: Meshopt + KTX2, textures ≤2k, no merging of interactive parts, LOD for heavy chapters.
- [ ] Per-chapter lazy loading + preload next step + progress UI + poster fallback.
- [ ] Step schema (Zod) + MDX text + author mode.
- [ ] Tour mode (learner-paced) and Explore mode. Reset view. Focus-on-part.
- [ ] Pre-training "meet the parts" step at the start of each guide.
- [ ] Signaling: highlight + ghost + leader-line labels. One change per step.
- [ ] Checks every 3–5 steps (pick-the-part).
- [ ] Accessibility: DOM text for all content, keyboard nav, live regions, reduced motion, contrast, static fallback.
- [ ] `CREDITS.json` per asset, auto-rendered credits page. No NC assets in monetized builds.
- [ ] Test on a low-end Android and on iOS < 26 (WebGL 2 path). 10-minute thermal test.
- [ ] PWA caching for classroom/offline use.

### 10.3 Top 10 Best Practices (ranked)
1. **Data-driven steps**: camera, visibility, highlight, explode, labels and checks defined in validated JSON/MDX, never hard-coded.
2. **Learner-paced segments with one change per step** (segmenting principle). Guided tour first, free exploration second.
3. **Signal relentlessly**: highlight the active part, ghost the context, label with leader lines, and move the camera to make the new thing visible (Agrawala's visibility principle).
4. **Stable, semantic node names** as the contract between Blender/CAD/medical assets and content.
5. **Render on demand + adaptive DPR**: the biggest mobile battery/thermal win.
6. **Meshopt + KTX2 via gltf-transform, without merging interactive parts**. Lazy-load per chapter.
7. **Constrained camera with reset and focus-on-part**. Scripted moves that respect `prefers-reduced-motion`.
8. **DOM-first accessibility**: part tree/search, keyboard control, live regions, and a non-3D fallback built from the same step data.
9. **Accuracy from authoritative data**: JPL Horizons/SPICE for orbits (and state your scale mode), FMA/TA2 for anatomy, CAD trees + expert review for assembly order.
10. **License ledger from day one**: prefer CC0/CC BY sources (BodyParts3D CC BY 4.0, Solar System Scope CC BY 4.0, NASA), quarantine SA/NC assets, and avoid trademarked F1 liveries in public builds.

---

## Caveats
- **Version facts** (three.js r187, R3F 9.8.x, WebGPU availability) come from release notes and 2026 developer blogs (Utsubo, GitHub/npm). The three.js API changes frequently, so re-check before upgrading.
- **Learning evidence** is strongest for anatomy and for the general multimedia principles (segmenting, signaling, pre-training). Effects are modest and heterogeneous, and some recent meta-analyses find no desktop-3D advantage over traditional methods. Transfer of these findings to F1 or solar-system content is reasonable inference, not directly tested.
- **Performance budgets** beyond the R3F draw-call guidance are practitioner rules of thumb. Profile on your own target devices.
- **Licensing** information is research, not legal advice. Licenses change (BodyParts3D moved from BY-SA to BY in 2025), and per-model terms (NIH 3D, Sketchfab, Thingiverse, Printables) must be checked individually. Confirm with a lawyer before commercial release.
- Some items were not re-verified in this research cycle (Poly Haven/Kenney CC0, Theatre.js maintenance status, `@react-three/postprocessing` WebGPU support) and are marked as such above.