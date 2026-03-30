---
aliases:
tags:
type:
status: draft
related:
created: 2026-03-08
modified: 2026-03-08
---
# Deep memory for Claude Code through Obsidian vaults

**The most effective pattern emerging in 2026 treats CLAUDE.md as a lightweight router — not a warehouse — pointing Claude Code into a layered vault where each tier trades token cost for detail depth.** This architecture, independently converged upon by dozens of practitioners, achieves **90–97% token savings** over naive context loading while preserving full knowledge access. The core insight: Claude Code’s skills system provides zero-cost-at-rest knowledge packages (~100 tokens each in metadata) that expand to full instructions only when invoked,  making it the ideal bridge between a rich Obsidian vault and a constrained context window.  The practical ceiling is about **10,000 tokens of always-loaded memory** (5% of a 200K context window), with everything else accessed on demand through progressive disclosure. 

## The five-tier memory architecture that keeps emerging

Every serious implementation converges on the same layered model, inspired by MemGPT’s OS-style memory hierarchy  and adapted for Claude Code’s specific loading mechanics. Understanding what loads when — and at what token cost — is the foundation of the entire system.

**Tier 0 — CLAUDE.md (always loaded, survives compaction).** This file enters Claude’s system prompt at every session start  and, critically, **re-injects from disk after `/compact`**, making it the most durable instruction surface. Official guidance targets **under 200 lines** (~4,000 tokens); longer files measurably reduce instruction adherence.  The obsidian-memory-for-ai project puts it bluntly: “Treat CLAUDE.md as a Tier 0 router, not a warehouse.”  In practice, this means vault overview, folder structure with one-line descriptions, naming conventions, key file pointers, and a handful of critical rules — nothing more. The `@import` syntax can pull in additional files (up to **5 hops of recursive imports**), but imported content expands inline at launch, so every import directly grows the always-loaded budget. 

**Tier 1 — .claude/rules/ (always loaded, path-scoped).** Every `.md` file in this directory loads alongside CLAUDE.md with equal priority.  The key differentiator: YAML frontmatter with a `paths:` field enables **conditional loading** scoped to file patterns  (e.g., `paths: src/api/**/*.ts`). This means API guidelines only consume tokens when Claude works on API files.  For vault-based systems, rules files can encode per-folder conventions — how daily notes should be formatted, how project files should be structured — without bloating the root CLAUDE.md.

**Tier 2 — Auto memory and MEMORY.md (~1–3K tokens).** Claude Code’s auto memory  (stored in `~/.claude/projects/<project>/memory/`) captures patterns and preferences across sessions automatically.  Only the **first 200 lines of MEMORY.md** load at startup; topic files (debugging.md, patterns.md) load on demand. This tier handles session-to-session continuity without manual intervention.

**Tier 3 — Skills (zero cost at rest, ~100 tokens metadata each).** This is the architectural sweet spot for bridging vault knowledge to Claude Code. At startup, Claude scans all skill directories but loads only each skill’s **name and description from YAML frontmatter** into an `<available_skills>` section.  The full SKILL.md body  (recommended under **500 lines**) loads only when Claude determines it’s relevant  — triggered by the description matching the current task. Supporting reference files and scripts load only if the skill instructions call for them. A vault with 20 skills installed costs roughly **2,000 tokens** at rest while providing access to potentially hundreds of kilobytes of knowledge. The gapmiss/obsidian-plugin-skill project calls this philosophy: “The context window is a public good.” 

**Tier 4 — Vault files (on-demand via Read/Grep/Glob tools).** Everything in the Obsidian vault is accessible through Claude Code’s filesystem tools but costs nothing until read.  The Read tool has a default limit of **25,000 tokens per file**  and adds approximately **70% overhead** from line-number formatting.  This makes per-folder index files critical — they let Claude scan a manifest of what exists (~200 tokens) rather than reading every file in a folder (~thousands of tokens).

## How to structure the vault for both humans and agents

The community has settled on a hybrid PARA + Zettelkasten structure with numbered prefixes,  where PARA provides navigable folder hierarchy and Zettelkasten provides atomic note methodology within it. The numbered prefixes serve double duty: they establish visual hierarchy for humans and sort order for agents scanning directories. 

```
vault/
├── CLAUDE.md                    # Tier 0 router (~150 lines)
├── .claude/
│   ├── rules/                   # Tier 1 path-scoped rules
│   │   ├── daily-notes.md       # paths: 06-Daily/**
│   │   └── project-conventions.md
│   └── skills/                  # Tier 3 on-demand knowledge
│       ├── vault-navigator/     # Skill: finds relevant notes
│       ├── weekly-review/       # Skill: runs review workflow
│       ├── session-persist/     # Skill: saves session learnings
│       └── inbox-processor/     # Skill: GTD-style inbox triage
├── 00-Inbox/                    # Quick capture, unsorted
├── 01-Projects/                 # Active work with deadlines
│   └── project-name/
│       ├── index.md             # Per-folder manifest
│       ├── context.md           # Project-specific AI context
│       └── decisions/
├── 02-Areas/                    # Ongoing responsibilities
├── 03-Resources/                # Reference materials
├── 04-Permanent/                # Zettelkasten atomic notes
├── 05-Fleeting/                 # Unprocessed captures
├── 06-Daily/                    # Periodic notes (YYYY/MM/)
│   └── 2026/03/
├── 07-Agent-Workspace/          # Agent outputs, session logs
│   ├── sessions/
│   └── tasks/
└── _meta/
    ├── VAULT-INDEX.md           # Live dashboard, read-first file
    └── templates/
```

**Per-folder index.md files are doing 80% of the navigation work.** Multiple practitioners report this independently. Each folder’s index lists its contents with one-line summaries and links, letting Claude scan a dozen files’ worth of context in ~200 tokens instead of reading each file individually. The WhyTryAI guide emphasizes: configure CLAUDE.md to instruct Claude to update these indexes whenever it creates or deletes files, making Claude its own librarian. 

**Atomic notes of 300–500 words are optimal for AI consumption** because they fit cleanly into context without truncation, have a single clear purpose for relevance filtering, and their link structure enables progressive disclosure — read one note, follow wikilinks for depth. The A-MEM academic paper (arXiv:2502.12110) validated this empirically, showing Zettelkasten-style atomic memory with dynamic linking outperforms flat memory approaches across six foundation models.  

**Frontmatter is the metadata layer that prevents expensive full-text scanning.** The critical fields for AI consumption are `type` (note, project, meeting, daily), `status` (active, draft, archived), `tags`, and most importantly a `summary` field — a one-line description that lets Claude assess relevance without reading the body. Ben Newton’s token analysis of the Obsidian CLI shows the difference: finding all notes tagged “project” costs **~1.2 million tokens** via raw file scanning versus **~200 tokens** via the metadata cache. That is a three-to-four order of magnitude difference.  

## Token-efficient context injection: the progressive disclosure pattern

The single most impactful pattern is progressive disclosure — organizing information in layers of increasing detail where the agent starts at the lightest layer and drills down only when needed.  The Claude-Mem project provides concrete numbers: traditional full-context loading fetches **25,000 tokens** to find **200 relevant tokens** (0.8% efficiency), while progressive disclosure shows an 800-token index, the agent identifies the relevant item, then fetches only the needed **155 tokens** (near-100% efficiency). 

The practical implementation has four layers. Layer 1 is the index (~500–800 tokens): titles, dates, types, and token counts for each knowledge item. Layer 2 is summaries (2–3 sentences per item). Layer 3 is full observation or note details (~120–200 tokens each). Layer 4 is source files referenced by the notes.  Each layer loads only if the previous layer indicated it was needed.

**The CLAUDE.md → Skills → Vault Files chain implements this natively in Claude Code.** CLAUDE.md provides the top-level map. Skills provide domain-specific knowledge packages that activate on demand. Vault files provide deep reference material accessed through explicit Read tool calls. This three-stage chain means a vault containing megabytes of knowledge presents only ~5,000–8,000 tokens of always-loaded context while keeping everything accessible.

**Manus’s todo.md pattern addresses a subtler problem: attention degradation over long sessions.** With ~50 tool calls per task, agents drift off-topic because the original plan gets buried in the middle of context where attention is weakest. By having the agent continuously rewrite a short todo.md file (~200–500 tokens), the global plan lands at the end of context — where transformer attention is strongest — combating the “lost-in-the-middle” effect.  Several Claude Code practitioners now include explicit instructions in CLAUDE.md: “Before each major action, re-read and update `07-Agent-Workspace/tasks/current.md` with your current plan and progress.”

For state files that Claude reads and writes frequently (task lists, progress trackers), **JSON outperforms Markdown** — Anthropic’s own team found models are less likely to accidentally reformat or corrupt JSON structures during read-modify-write cycles. 

## Write-back patterns: what to auto-save versus manually trigger

The write-back question splits cleanly along a volatility axis. High-frequency, low-stakes observations belong in auto-save; low-frequency, high-stakes decisions require human review before promotion to permanent knowledge.

**Auto-save candidates** include session summaries (captured via Claude Code hooks on the `Stop` event), task completion checkpoints, error patterns and debugging lessons, discovered codebase quirks, and daily note entries. The claude-note project by crimeacs demonstrates the passive approach: a background service watches Claude Code sessions via hooks (`PostToolUse`, `UserPromptSubmit`, `Stop`), auto-extracts knowledge, and routes it to the vault — inbox for unsorted items, specific notes for recognized topics, new notes for novel concepts.  The user never manually saves; the system captures everything.

**Manual-trigger candidates** include architectural decisions (which should follow the decision-record format with rationale, alternatives considered, and revisit triggers), project conventions and coding rules, cross-project learnings promoted from session-specific to permanent knowledge, and any changes to CLAUDE.md or skills files themselves. The CONTINUITY MCP server project provides a concrete checkpoint workflow: `continuity_checkpoint()` every 3–5 tool calls, `continuity_log_decision()` for architectural choices, and `continuity_save_session()` at session end. 

**Pre-compaction flush is a critical pattern.** Before Claude Code’s context window fills and triggers `/compact`, the agent should be instructed to persist any durable memories to disk.  OpenClaw implements this by detecting context pressure and automatically prompting the agent to save learnings before the window resets.   Include this instruction in CLAUDE.md: “When context usage exceeds 70%, save current session learnings to `07-Agent-Workspace/sessions/` before using /compact.”

The Obsidian-Claude-PKM project demonstrates a mature version of this with Claude Code hooks: a `session-init` hook loads relevant context at startup, a post-tool hook auto-commits changes to git, and specialized agents (Goal-Aligner, Weekly-Reviewer, Vault-Hygienist) maintain vault integrity across sessions. Each agent maintains cross-session memory in Claude Code’s native `memory:project` store. 

## Existing projects worth studying and borrowing from

The landscape of ready-to-use implementations has grown rapidly. The most architecturally instructive projects, ordered by the sophistication of their context management:

**obsidian-memory-for-ai** (jrcruciani) provides the best conceptual framework.  Its ContextSummary.md pattern — a semantic index per folder — solves the “agent doesn’t know what it doesn’t know” problem. It uses wikilinks with verb relationships (extends, supports, contradicts) to create a navigable knowledge graph. Its design principles are sound: “Zero infrastructure. No database, no embeddings, no server”  and “You’re the retrieval algorithm, and you’re smarter than cosine similarity.” 

**Obsidian-Claude-PKM** (ballred) is the most complete implementation. Four specialized agents with cross-session memory, 10 skills, hooks for auto-commit and session initialization, path-specific rules, and a goal-cascading system from 3-year vision down to weekly tasks.  Its per-project CLAUDE.md pattern — each project directory gets its own context file — is directly implementable. 

**kepano/obsidian-skills** (16.9K stars) represents the official direction. Created by Obsidian’s CEO, these five skills teach Claude Code the three major Obsidian file formats.  The Obsidian CLI (v1.12) adds programmatic vault access: `obsidian read`, `obsidian create`, `obsidian search`, `obsidian tasks`  — benchmarked at **54x faster than grep** for vault operations.  

**QMD** (by Tobias Lütke, Shopify CEO) fills the semantic search gap.  BM25 + vector embeddings + LLM reranking on local markdown files,  with measured **60%+ token reduction** versus grep/glob for agent context retrieval.   Multiple projects (ClawVault, various Claude Code skill configurations) now integrate QMD as their search layer. 

## The token budget question: upfront cost versus downstream efficiency

Anthropic’s own context engineering guidance recommends a **hybrid approach**: load stable, cheap context upfront (CLAUDE.md, key rules) while using dynamic tools for just-in-time exploration.   The key metric from Manus’s production experience is the **100:1 input-to-output ratio** in agentic systems — input token optimization is the primary efficiency lever, not output optimization. 

The practical budget allocation for a deep memory system looks like this. Always-loaded context (CLAUDE.md + rules + auto memory) should stay under **8,000–10,000 tokens** — roughly 5% of a 200K window.   Skills metadata adds ~100 tokens per installed skill, so 20 skills cost ~2,000 tokens at rest. On-demand reads should be budgeted at **1,000–5,000 tokens per retrieval** (a typical markdown note plus the Read tool’s line-number overhead). Session working space needs the remaining **~180,000 tokens** for conversation, tool outputs, and actual work. 

The counterintuitive finding from ETH Zurich’s March 2026 research: **LLM-generated context files actually degrade performance by ~3%** and increase inference costs by 20%+. Even human-written AGENTS.md files showed only marginal 4% improvement.  The implication is that context files should contain only information Claude genuinely cannot infer from the codebase — custom build commands, tooling quirks, vault-specific conventions, and pointers to where deep knowledge lives. Architecture overviews that duplicate what’s visible in the file structure waste tokens without helping. 

**KV-cache optimization is the hidden multiplier.** Cached input tokens cost **$0.30/MTok versus $3.00/MTok uncached** — a 10x cost difference. To exploit this: keep your CLAUDE.md and system prompt prefix stable across sessions (avoid timestamps at the top), make context append-only where possible, and ensure deterministic serialization of any structured data.  This means the order and content of your always-loaded files should rarely change.

## Conclusion: a practical implementation sequence

The most effective path forward is not building the entire system at once but layering it incrementally, validating each tier before adding the next. Start with a well-crafted CLAUDE.md under 150 lines that maps vault structure and points to key files   — this alone delivers the majority of the value.  Add per-folder index.md files next, with instructions for Claude to maintain them.   Then build 3–5 skills for your most common workflows (weekly review, session persistence, inbox processing), exploiting the zero-cost-at-rest property to keep your token budget lean. The write-back system comes last: hooks for passive session capture, explicit skills for decision logging, and a pre-compaction flush instruction to prevent knowledge loss.

The deeper insight across all these implementations is that the vault structure matters less than the **routing layer** — how efficiently Claude can determine what exists and where to find it without reading everything. Index files, summary layers, and skill descriptions are all forms of routing.  The winning architecture is not the one with the most knowledge stored but the one where Claude spends the fewest tokens finding the right knowledge at the right time.