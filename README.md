# LLM Presentation

Site estático em PT-BR cobrindo a história, os tipos e o ecossistema atual dos Large Language Models.

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

Previsto: **Vercel**, conectado ao repositório GitHub.

```bash
vercel --prod
```

(Vercel auto-detecta o `index.html` na raiz e serve como static site.)

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