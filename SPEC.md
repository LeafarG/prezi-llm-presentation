# Prezi-style LLM Presentation — SPEC

## Overview
Static single-file HTML (PT-BR) presenting LLM history, types and ecosystem.
Two siblings:
- **v1 (original):** https://llm-presentation-beta.vercel.app
- **Prezi variant:** https://prezi-llm-presentation.vercel.app

This document covers the **Prezi variant** only.

## Stack
- **Single-file:** `index.html` with inline CSS + JS (no build, no deps)
- **Prezi pattern:** zoom-driven navigation over a 6000×3000 canvas
- **PC-only:** min viewport 1280×720, mobile fallback message
- **Font:** Inter + JetBrains Mono (Google Fonts)
- **No framework, no React, no Tailwind**

## Information architecture (clusters)

The canvas is organized into **3 macro-clusters** + 1 cover, each grouping related sections. This is the core narrative structure for v2.

### Cluster 1 — "Fundamentos" (blue accent)
The historical & scaffolding foundation. Linear cause/effect.
- **História** — timeline 1943→2026, click-to-expand per event
- **Frameworks** — TensorFlow / PyTorch / HuggingFace / Ollama

### Cluster 2 — "O Modelo" (purple accent)
The model architecture itself: variants & emergent reasoning.
- **Tipos de LLM** — encoder-only / decoder-only / encoder-decoder / MoE
- **Thinking** — CoT, ToT, o1, inference-time scaling

### Cluster 3 — "Construções" (green/pink accent)
What we build on top: tooling, protocol, agents.
- **Tools** — function calling, web search, RAG
- **MCP** — Model Context Protocol "USB-C for AI"
- **Harness** — Claude Code, Cursor, MS Cowork, Manus

### Cluster 4 — "Orçamento" (amber accent)
Practical cost-of-intelligence — which model for which task.
- **Custos** — Opus 4.6 vs GLM 5.2 vs GPT-5 price/performance comparison,
  thinking-token multiplier (3-20×), decision tree for routing,
  "when same result / when you must pay more" checklists.

### Cover — entry point
- **Capa** — overview + 4 macro-cards (clickable → tour)
- Each macro-card launches a **guided tour** that walks through the
  cluster's sections with brief pauses + "→ próximo" overlay

## Visual canvas layout (timeline)

```
Canvas 9500 × 1500 (timeline horizontal)

   100      950    1850 2750 3650 4550 5450   6400        8000  9400   (left edges)
   ├──┬──────┼─────┼───┼────┼────┼────┼─────────┼───────────┼─────┤
   │CAPA│  HIST   │TIPOS│THIN│FRA │TOOL│  MCP    │  HARNESS  │CUSTOS│ (timeline)
   │    │          │    │    │MEW │ S  │         │           │      │
   │750 │ 850      │850 │850 │850 │850 │ 900     │ 1500      │1400  │ (widths)
   │    │          │    │    │   │    │         │           │      │
   └────┴──────────┴────┴────┴───┴────┴─────────┴───────────┴──────┘
         ↗    →    →    →    →    →    →    →    ↘          (timeline flow)
   (pink)  (gray between-section arrows)               (amber lead-out)
```

**Geometry guarantee** — each section:
- Vertical: same top=200, height=1100 (canvas 1500 px tall, 200/300 px top/bottom margin)
- Horizontal: 50-100 px gap between adjacent sections
- Capa w=750 (smaller, intro column); Harness w=1500 (larger, finale column); others w=850-900
- Total horizontal span: 100 + 750 + 100 + 850*4 + 100 + 900 + 100 + 1500 = 7900 ✓
- Inter-section arrows drawn as small horizontal segments in each gap (50 px), pointing left-to-right (pink dashed for Capa→Historia lead-in, gray solid for the rest)

Cluster colors tint (vertical bands):
- Capa-area: pink radial-gradient behind the leftmost Capa column
- Fundamentos: blue vertical band (Historia + Frameworks columns)
- Modelo: purple vertical band (Tipos + Thinking columns)
- Construções: green vertical band (Tools + MCP + Harness columns)
- Orçamento: amber vertical band (Custos column)

Inter-cluster arrows SVG overlay: 8 small horizontal arrows + arrowheads drawn in the 50-100 px gap between adjacent sections. The Capa→Historia lead-in is dashed pink; the Harness→Custos lead-out is dashed amber. During the narrative tour, one arrow briefly `.highlight`s (cyan accent) just before its right-side section focuses.

This layout replaces the previous v2 quadranted "U" (6000×3800) — boss feedback was that the U felt too rigid and unnatural. Timeline reads as a continuous narrative flow from Capa on the left to Harness on the right.

## Navigation modes

1. **Free zoom** — navigate linearly via prev/next buttons; linear order is:
   Capa → História → Tipos → Thinking → Frameworks → Tools → MCP → Harness.
2. **Top-nav jump** — click any section in the top-right list.
3. **Guided tour** — click a cluster card on Capa → auto-advances through
   that cluster with 2.5s pauses + "→ Próximo" hint. ESC ends the tour.
4. **Overview** — Home button fits the entire 9500×1500 canvas (9 sections in 4 clusters).
5. **Hash deep-link** — `#historia`, `#mcp`, `#historia?event=transformer`,
   `#cluster:fundamentos` (tour), `#cluster:construcoes` (tour).

## UX details

### Responsive (no PC-only gate)
- The presentation is **responsive on any viewport** — the v2 PC-only media gate
  was removed 2026-07-07 (`4ea5116`) on boss feedback. Smaller screens still get
  a usable experience; the canvas zooms out via the existing Prezi fit logic.
- The presentation was originally optimized for projector / desktop, but now
  adapts gracefully to mobile / tablet by scaling the canvas uniformly.

### Pre-compaction memory flush
- During aggressive memory compaction, `MEMORY.md` / `SOUL.md` / `AGENTS.md`
  become read-only — durable memory only goes to
  `D:\.openclaw\workspace\memory\YYYY-MM-DD.md`.

### Branch + deploy
- Working branch: `feat/prezi-style` (V1 and Prezi share the same local branch)
- Vercel project (Prezi): `prj_afadzrtQg2OjZPktLH3S1SiPt0jd`
- Auto-deploy via `git push prezi feat/prezi-style:main`
- See `MEMORY.md` 2026-07-07 for Vercel GitHub App link API pattern.

## Events timeline (current)

13 entries with click-to-expand detail panels:
- 1956 Dartmouth Workshop · McCarthy, Minsky, Rochester, Shannon
- 1958 Perceptron · Rosenblatt
- 1966 ELIZA · Weizenbaum (chatbot precursor)
- 1969 1º AI Winter · Minsky & Papert
- 1986 Backprop · Rumelhart/Hinton/Williams
- 1987 2º AI Winter · LISP crash
- 2012 AlexNet · ImageNet
- 2017 Transformer
- 2020 GPT-3 · 175B
- 2022 ChatGPT · RLHF
- 2024 o1 + MCP
- 2025 DeepSeek-R1 · open-source reasoning
- 2026 MS Cowork

Detail view has back button, ESC closes, click anywhere outside the detail
panel closes. Deep-link `?event=<id>` opens detail directly.

## Critical notes for future work

- Canvas dimension constants must agree between CSS (`.canvas { width: 9500;
  height: 2000; }`) and JS (`canvasW = 9500`, `canvasH = 2000`).
  If you expand the canvas, update both.
- `getSectionRect` reads CSS `style.left/top/width/height` (inline) — keep
  these in sync with `SECTIONS` table if you ever want to dedup.
- Prezi navigation must use the CSS transition on `.canvas` (350ms) — never
  apply transforms directly without `transitionTo(fit, animate=true)`.
- For deep-link in-page clicks (no `init()` re-run), wire `hashchange` AND
  `popstate` listeners (lesson from this session's bug, see memory/2026-07-07).
