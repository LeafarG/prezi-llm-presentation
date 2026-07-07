# LLM Presentation

Site estático em PT-BR cobrindo a história, os tipos e o ecossistema atual dos Large Language Models.

> **Variantes:**
> - `main` — apresentação **linear** (scroll vertical, hero + 7 seções).
> - `feat/prezi-style` — apresentação **estilo Prezi** (canvas zoomável, navegação espacial por seções espalhadas num canvas 6000×3000).
>
> A `main` é a versão canônica; a branch Prezi é um preview paralelo.

## Rodar local

Basta abrir o arquivo no navegador:

```bash
# Windows
start index.html

# macOS / Linux
open index.html
```

Nenhuma dependência, nenhum build. Um único arquivo `index.html` contém HTML, CSS e JS.

## Deploy

**Vercel** com auto-deploy via push no `main` → produção (https://llm-presentation-beta.vercel.app).

Qualquer `git push` em `main` dispara um deploy de produção automaticamente. Push em outras branches cria preview deploys (URL por commit).

Setup inicial (já feito): Vercel GitHub App instalada no LeafarG + projeto linkado via `/v9/projects/{id}/link`.

Para deploy manual (se precisar):

```bash
vercel --prod
```

## Estrutura

- `SPEC.md` — especificação do conteúdo
- `index.html` — o site completo
- `README.md` — este arquivo

## Conteúdo

1. Capa
2. História (timeline 1958 → 2026)
3. Tipos de LLM (SLM, LLM, Frontier)
4. Thinking vs No-thinking
5. Frameworks (Chat, Agent, Harness)
6. Ferramentas (function calling)
7. MCP (Model Context Protocol)
8. Harness (Claude Code, GitHub Copilot, Microsoft 365 Copilot, Microsoft Cowork)

## Licença

Uso pessoal / apresentação.