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

### Cover — entry point
- **Capa** — overview + 3 macro-cards (clickable → tour)
- Each macro-card launches a **guided tour** that walks through the
  cluster's sections with brief pauses + "→ próximo" overlay

## Visual canvas layout (cluster regions)

```
Canvas 6000 × 3600

┌─────────────── 6000 ────────────────┐
│ (100,280)                          (5400,280)
│  ┌──────────────┐    ┌──────────────┐
│  │  HISTÓRIA    │    │   TIPOS      │
│  │  (NW blue)   │    │   (NE purp)  │
│  └──────────────┘    └──────────────┘
│  (100,1260)           (3700,1180)
│  ┌──────────────┐    ┌──────────────┐
│  │ FRAMEWORKS   │    │  THINKING    │
│  │ (SW blue)    │    │  (SE purp)   │
│  └──────────────┘    └──────────────┘
│
│  (100,2200) (1700,2200) (3350,2200)
│  ┌─────────┐ ┌──────────┐ ┌──────────┐
│  │  TOOLS  │ │   MCP    │ │ HARNESS  │
│  └─────────┘ └──────────┘ └──────────┘
│
│        (1900, 2950) — CAPA large, bottom-center
│        ┌──────────────────────┐
│        │       CAPA           │
│        │  + 3 macro cards     │
│        │  (tour launching)    │
│        └──────────────────────┘
└────────────────────────────────────┘
```

Cluster colors tint (radial gradient):
- Fundamentos: blue, NW corner
- Modelo: purple, NE corner
- Construções: green, southern band
- Capa: pink, south-center

### Cluster backgrounds
- Fundamentos: subtle blue radial-gradient sphere around NW corner
- Modelo: subtle purple radial-gradient around NE
- Construções: subtle green/pink gradient along bottom
- Arrows SVG overlay: connects Fundamentos → Modelo (curves NE-ish)

## Navigation modes

1. **Free zoom** — navigate linearly via prev/next buttons; linear order is:
   Capa → História → Tipos → Thinking → Frameworks → Tools → MCP → Harness.
2. **Top-nav jump** — click any section in the top-right list.
3. **Guided tour** — click a cluster card on Capa → auto-advances through
   that cluster with 2.5s pauses + "→ Próximo" hint. ESC ends the tour.
4. **Overview** — Home button fits the entire 6000×3000 canvas.
5. **Hash deep-link** — `#historia`, `#mcp`, `#historia?event=transformer`,
   `#cluster:fundamentos` (tour), `#cluster:construcoes` (tour).

## UX details

### PC-only enforcement
- `@media (max-width: 1280px), (max-height: 720px)` → shows fullscreen
  "PC apenas" overlay hiding everything else. This is intentional: the
  presentation is designed for projector / desktop screens.

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

10 entries with click-to-expand detail panels:
- 1958 Perceptron · Rosenblatt
- 1969 1º AI Winter · Minsky & Papert
- 1986 Backprop · Rumelhart/Hinton/Williams
- 1987 2º AI Winter · LISP crash
- 2012 AlexNet · ImageNet
- 2017 Transformer
- 2020 GPT-3 · 175B
- 2022 ChatGPT · RLHF
- 2024 o1 + MCP
- 2026 MS Cowork

Detail view has back button, ESC closes, click anywhere outside the detail
panel closes. Deep-link `?event=<id>` opens detail directly.

## Critical notes for future work

- Canvas dimension constants must agree between CSS (`.canvas { width: 6000;
  height: 3600; }`) and JS (`computeOverviewFit` uses `canvasH = 3600`).
  If you expand the canvas, update both.
- `getSectionRect` reads CSS `style.left/top/width/height` (inline) — keep
  these in sync with `SECTIONS` table if you ever want to dedup.
- Prezi navigation must use the CSS transition on `.canvas` (350ms) — never
  apply transforms directly without `transitionTo(fit, animate=true)`.
- For deep-link in-page clicks (no `init()` re-run), wire `hashchange` AND
  `popstate` listeners (lesson from this session's bug, see memory/2026-07-07).
