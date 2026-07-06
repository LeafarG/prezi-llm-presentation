# LLM Presentation — SPEC

Site estático (HTML único) que cobre o conhecimento essencial sobre Large Language Models para uso em apresentação.

## Objetivo

Material de apresentação que una história, tipos, frameworks e o ecossistema atual de LLMs em um único lugar — visual, didático, em PT-BR.

## Seções

1. **Capa** — título, subtítulo, número de versão.
2. **História** — timeline vertical do perceptron (1958) até a era dos agentes (2026), passando por AlexNet (2012), Transformer (2017), GPT-2/3/3.5, ChatGPT, GPT-4, Claude, Gemini, reasoning models (o1, R1), MCP e agentes.
3. **Tipos de LLM** — SLM, LLM, Frontier, Open vs Closed, arquiteturas (encoder-only / decoder-only / encoder-decoder).
4. **Thinking vs No-thinking** — comparação entre LLMs de resposta direta e modelos de raciocínio (CoT, inference-time compute).
5. **Frameworks** — Chat (UI), Agent (execução autônoma) e Harness (camada de produto).
6. **Ferramentas (Tools)** — function calling, structured output, loop de tool use, padrão ReAct.
7. **MCP** — Model Context Protocol, arquitetura host/client/server, capabilities.
8. **Harness** — Claude Code, GitHub Copilot, Microsoft 365 Copilot, Microsoft Cowork (recente).

## Tech

- **Formato**: `index.html` único com CSS e JS inline (sem build step).
- **Tema**: dark, tipografia limpa (system-ui + Inter via Google Fonts).
- **Idioma**: PT-BR.
- **Responsivo**: sim, mobile-friendly.
- **Sem dependências externas em runtime**: Google Fonts opcional.

## Estrutura de arquivos

```
projects/llm-presentation/
├── SPEC.md          ← este arquivo
├── README.md        ← instruções de uso e deploy
└── index.html       ← site completo (HTML + CSS + JS inline)
```

## Deploy

- **GitHub**: `github.com/LeafarG/llm-presentation` (a criar nesta task).
- **Vercel**: próximo passo, importação automática via GitHub.

## Princípios de conteúdo

- Linguagem técnica acessível — evita jargão sem explicação.
- Datas e nomes próprios conferidos (AlexNet 2012, Attention 2017, GPT-2 2019, etc.).
- Microsoft Cowork descrito com base no anúncio oficial de GA em 16/06/2026.
- Não inclui código executável — site puramente estático e didático.