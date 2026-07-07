# PLAN v2 — Better LLM Prezi

3-step plan to elevate the Prezi-style LLM presentation to a polished,
narrative-driven, production-grade single-file site.

Status: **executing (2026-07-07 evening)**

---

## STEP 1 — Content that breathes (editorial polish)

**Goal:** Each section becomes something the boss *wants to show*, not
a fact-only panel.

**Concrete changes:**
- **História** — add 3 new events (`dartmouth1956`, `eliza1966`, `deepseekR1`)
  alongside existing 10 → 13 total events. Each new event gets a full
  detail panel (year, chips, title, 4 paragraphs).
- **Tipos de LLM** — convert the static 2×2 quad grid into
  click-to-expand cards (4 cards: SLM / LLM / Frontier / Reasoning).
  Each card opens a detail panel analogous to História's, with
  "quando usar" + exemplos + limitações.
- **Frameworks** — convert the 3 framework rows (CHAT / AGENT /
  HARNESS) into click-to-expand rows. Each opens a detail panel with
  concrete product examples + how-to.
- **Tools** — keep 8-card grid; add visual icons (currently just colored
  dots — replace with `lucide-style` inline SVG icons).
- **MCP** — keep the diagram; expand the
  **Capabilities por server** bullets into a richer table with examples.
- **Capa** — add a 1-fact-per-macro line under each macro card,
  replacing vague descriptions with concrete stats:
  - Fundamentos: "1958 → 2017: 59 anos do neurônio ao Transformer"
  - O Modelo: "4 arquiteturas dominantes em 2026: SLM / LLM / Frontier / Reasoning"
  - Construções: "8 ferramentas, 1 protocolo, 4 harnesses"

**Files touched:** `index.html` only (markup + CSS).
**Commit prefix:** `chore(prezi): step 1 — content polish`.

---

## STEP 2 — Interactivity that connects the clusters

**Goal:** The presentation becomes a *narrative*, not just a slideshow.

**Concrete changes:**
- **Universal click-to-expand** — reuse the História detail-panel
  pattern in Tipos, Frameworks, Tools, Harness, MCP. Single helper
  `setupDetailPanels(sectionId)` that wires the same back-button +
  ESC + click-outside behavior.
- **Narrative tour mode** — `tourNarrative()` walks *all* clusters
  in sequence (Fundamentos → O Modelo → Construções → Capa), with
  a "setas inter-cluster" SVG path animation that briefly highlights
  the connecting arrows during transitions. ~45s total.
- **Breadcrumb in bottom-bar** — extend `progress.textContent`
  with macro context: `MACRO 01 · FUNDAMENTOS · Historia 2/8`.
- **Visual timeline path** — overlay an SVG `polyline` on História
  connecting all event-year dots. Makes the timeline feel like a
  constellation in overview, not a list.

**Files touched:** `index.html`, SPEC.md.
**Commit prefix:** `feat(prezi): step 2 — interactivity`.

---

## STEP 3 — Production polish

**Goal:** Quality of "shipped product".

**Concrete changes:**
- **README.md** for `LeafarG/prezi-llm-presentation` — atalhos de
  teclado, deep-links disponíveis, comandos `git push prezi` vs
  `git push origin`.
- **OG / Twitter card meta tags + favicon.svg** — so links shared
  on Telegram/Twitter show a nice preview.
- **First-visit onboarding overlay** — small arrow pointing at the
  top-nav + ESC + deep-link hint, dismissed with "got it" button.
- **Accessibility pass** — `aria-label` on the canvas + nav,
  `:focus-visible` outline for keyboard users, skip-link.
- **SPEC.md update** with the v2 architecture (clusters +
  narrative + commit map).

**Files touched:** `index.html` (head meta), `README.md`,
`projects/llm-presentation/SPEC.md`.
**Commit prefix:** `chore(prezi): step 3 — production polish`.

---

## Execution cadence

Each step ends with:
1. Commit + push to `prezi` remote
2. Wait for Vercel deploy (~10 s)
3. Capture screenshot of the changed section(s)
4. Send preview to boss
5. Wait for go-ahead before next step

---

## Notes

- All commits stay on `feat/prezi-style`, Vercel auto-deploys on push.
- No build step — everything stays single-file.
- V1 site (`llm-presentation`) remains untouched on its `main` branch.
