#!/usr/bin/env python3
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- ============ CUSTOS ============ -->'
start_idx = html.find(start_marker)
print(f'start_idx = {start_idx}')

close_pattern = '</div>\n      </div>\n\n    </div><!-- /.canvas -->'
close_idx = html.find(close_pattern, start_idx)
print(f'close_idx = {close_idx}')

if start_idx == -1 or close_idx == -1:
    print('ERROR: markers not found')
    sys.exit(1)

DOLLAR = chr(36)
BACKSLASH = chr(92)

new_custos = '''<!-- ============ CUSTOS ============ -->
      <div class="section" id="sec-custos" data-id="custos"
           style="left: 8000px; top: 200px; width: 1400px; height: 1100px;">
        <div class="frame">
          <div class="poster">
            <div class="poster-num">// ORÇAMENTO</div>
            <div class="poster-title">Pensar caro<br>ou pensar barato?</div>
            <div class="poster-sub">Opus 4.6 · GLM 5.2 · GPT-5 — quando cada um compensa.</div>
          </div>

          <div class="content-body">
            <p style="font-size:0.72rem;line-height:1.4;margin-bottom:0.4rem"><span style="color:var(--warning);font-weight:600">Premissa:</span> o modelo <em>mais capaz</em> raramente é o mais <em>custo-efetivo</em>. "Thinking" multiplica o output em 3–20×. Veja a régua antes de chamar Opus pra classificar um e-mail.</p>

            <!-- ============ TABELA DE PREÇOS ============ -->
            <div class="cost-table">
              <div class="cost-row cost-head">
                <div>Modelo</div>
                <div>In · ''' + DOLLAR + '''/M</div>
                <div>Out · ''' + DOLLAR + '''/M</div>
                <div>Thinking</div>
                <div>Score</div>
                <div>Score/''' + DOLLAR + '''</div>
              </div>
              <div class="cost-row">
                <div><span class="purple">Opus 4.6</span> <span class="dim">·Anthropic</span></div>
                <div>''' + DOLLAR + '''5.00</div>
                <div>''' + DOLLAR + '''25.00</div>
                <div>Adaptive · 3–5×</div>
                <div>84</div>
                <div><strong style="color:var(--warning)">3.4</strong></div>
              </div>
              <div class="cost-row">
                <div><span class="success">GLM 5.2</span> <span class="dim">·Zhipu</span></div>
                <div>''' + DOLLAR + '''1.40</div>
                <div>''' + DOLLAR + '''4.40</div>
                <div>Reasoning · ''' + DOLLAR + '''1/''' + DOLLAR + '''3.20</div>
                <div>83</div>
                <div><strong style="color:var(--success)">17.5</strong></div>
              </div>
              <div class="cost-row">
                <div><span class="accent">GPT-5</span> <span class="dim">·OpenAI</span></div>
                <div>''' + DOLLAR + '''1.25</div>
                <div>''' + DOLLAR + '''10.00</div>
                <div>o-series · 5–20×</div>
                <div>~72</div>
                <div><strong style="color:var(--accent)">8.0</strong></div>
              </div>
            </div>

            <p style="font-size:0.7rem;margin-top:0.3rem;line-height:1.4"><strong>Score</strong> = benchmark agregado (BenchLM, jul/2026). <strong>Score/''' + DOLLAR + '''</strong> = qualidade por dólar de output. <em style="color:var(--success)">GLM 5.2 entrega 5× mais valor por dólar que Opus 4.6</em>, quase empatado em score bruto.</p>

            <!-- ============ DECISION GRID 2 COL ============ -->
            <div class="cost-grid-2col">
              <div>
                <h4 style="color:var(--success);margin:0.5rem 0 0.3rem;font-size:0.78rem;letter-spacing:0.05em">✓ MESMO RESULTADO (USE O MAIS BARATO)</h4>
                <ul style="font-size:0.7rem;line-height:1.45;margin:0">
                  <li><strong>Classificação, extração, formatação, FAQ</strong> — GLM ≈ GPT ≈ Opus &gt;95%</li>
                  <li><strong>Refatorar 1–2 arquivos</strong> — GLM 5.2 reasoning resolve</li>
                  <li><strong>Resumir texto</strong> — Sonnet 4.6 empata Opus</li>
                  <li><strong>Code review superficial</strong> — GPT-5.4 mini basta</li>
                </ul>

                <h4 style="color:var(--pink);margin:0.5rem 0 0.3rem;font-size:0.78rem;letter-spacing:0.05em">✕ PAGUE MAIS (PRECISA DE OPUS)</h4>
                <ul style="font-size:0.7rem;line-height:1.45;margin:0">
                  <li><strong>Arquitetura multi-componente</strong> — coerência de longo prazo</li>
                  <li><strong>Escrita criativa longa / nuance editorial</strong></li>
                  <li><strong>Análise jurídica / contratual</strong> — Adaptive Thinking calibra incerteza</li>
                  <li><strong>Debug race condition / sistema distribuído</strong></li>
                </ul>
              </div>

              <div>
                <h4 style="color:var(--warning);margin:0.5rem 0 0.3rem;font-size:0.78rem;letter-spacing:0.05em">⚠ THINKING MULTIPLICA</h4>
                <div class="diagram" style="font-size:0.66rem;line-height:1.35;margin-bottom:0.4rem">
<span class="warning">[ 500 out visíveis ]</span>
  <span class="purple">Opus 4.6</span>  (sem)  <strong>''' + DOLLAR + '''0.0125</strong>
  <span class="success">GLM 5.2</span>  (sem)  <strong>''' + DOLLAR + '''0.0022</strong>
  <span class="accent">GPT-5</span>    (sem)  <strong>''' + DOLLAR + '''0.0050</strong>

<span class="warning">[ 500 out + 2.000 thinking ]</span>
  <span class="purple">Opus 4.6</span>  (5×)   <strong>''' + DOLLAR + '''0.0625</strong> +400%
  <span class="success">GLM 5.2</span>  (rea)  <strong>''' + DOLLAR + '''0.0085</strong> +286%
  <span class="accent">GPT-5</span>    (o3)   <strong>''' + DOLLAR + '''0.0550</strong> +1000%</div>

                <h4 style="color:var(--accent);margin:0.5rem 0 0.3rem;font-size:0.78rem;letter-spacing:0.05em">★ ROTEIRO</h4>
                <div style="font-size:0.7rem;line-height:1.45;color:var(--text-secondary)">
                  <strong>[1]</strong> Tarefa simples? → GLM 5.2 ou GPT-5.4 mini<br>
                  <strong>[2]</strong> Complexa? Tente GLM 5.2 reasoning primeiro (''' + DOLLAR + '''1/''' + DOLLAR + '''3.20)<br>
                  <strong>[3]</strong> Falhou? Escale pra GPT-5 (o3)<br>
                  <strong>[4]</strong> Precisa de nuance? Só então Opus 4.6<br>
                  <strong>[5]</strong> Cache (90% off) + batch sempre que possível
                </div>
              </div>
            </div>

            <!-- ============ 2H ESTIMATE - HIGHLIGHTED ============ -->
            <h4 style="color:var(--warning);margin:0.7rem 0 0.4rem;font-size:0.85rem;letter-spacing:0.05em">⏱ ESTIMATIVA REAL · 2 HORAS DE ATIVIDADE AGÊNTICA</h4>
            <p style="font-size:0.66rem;margin-bottom:0.3rem;line-height:1.4"><strong>Premissas:</strong> 8 user turns · 15 model calls/turn (fanning out) · 8K input/call · 600 out visíveis · 3K thinking/call. <em>Fonte: Calcis + Cursor + Copilot benchmarks, jul/2026.</em></p>

            <div class="agent-estimate">
              <div class="ae-row ae-head">
                <div>Cenário</div>
                <div>Input</div>
                <div>Out+Think</div>
                <div>Opus 4.6</div>
                <div>GLM 5.2</div>
                <div>GPT-5</div>
              </div>
              <div class="ae-row ae-light">
                <div><strong>Light</strong> <span class="dim">sem thinking</span></div>
                <div>960K</div>
                <div>72K</div>
                <div><strong>''' + DOLLAR + '''5.05</strong></div>
                <div><strong style="color:var(--success)">''' + DOLLAR + '''1.42</strong></div>
                <div><strong>''' + DOLLAR + '''1.92</strong></div>
              </div>
              <div class="ae-row ae-medium">
                <div><strong>Medium</strong> <span class="dim">thinking 5×</span></div>
                <div>960K</div>
                <div>432K</div>
                <div><strong>''' + DOLLAR + '''15.60</strong></div>
                <div><strong style="color:var(--success)">''' + DOLLAR + '''3.24</strong></div>
                <div><strong>''' + DOLLAR + '''5.52</strong></div>
              </div>
              <div class="ae-row ae-heavy">
                <div><strong>Heavy</strong> <span class="dim">Opus ext. max</span></div>
                <div>1.5M</div>
                <div>1.2M</div>
                <div><strong style="color:var(--pink)">''' + DOLLAR + '''37.50</strong></div>
                <div><strong style="color:var(--success)">''' + DOLLAR + '''7.38</strong></div>
                <div><strong>''' + DOLLAR + '''13.88</strong></div>
              </div>
            </div>

            <p style="font-size:0.7rem;margin-top:0.4rem;line-height:1.4"><strong style="color:var(--success)">Cache 80%</strong> corta custos ~5×. <strong>GLM 5.2 Medium cached:</strong> <strong style="color:var(--success)">''' + DOLLAR + '''0.65</strong> · <strong>Opus 4.6 Medium cached:</strong> <strong>''' + DOLLAR + '''3.12</strong>. <em>Real stats: Calcis = ''' + DOLLAR + '''0.09-0.32/turn · Cursor (88% cache) Opus = ''' + DOLLAR + '''0.90/req · heavy 4-6h/dia user = ''' + DOLLAR + '''20-200/mês em Claude Code/Copilot Max.</em></p>

            <!-- ============ FOOTER ============ -->
            <p style="font-size:0.66rem;color:var(--text-dim);margin-top:0.5rem;border-top:1px solid var(--border);padding-top:0.4rem;line-height:1.4">
              <strong>Preços</strong>: Anthropic, OpenAI, Zhipu AI · jul/2026 · <em>por milhão de tokens</em>. <strong>Benchmarks</strong>: BenchLM agregados (8 categorias). <strong>Thinking</strong> = output rate. <strong>Cache</strong> corta input em até 90%.
            </p>
          </div>
        </div>
      </div>'''

new_html = html[:start_idx] + new_custos + html[close_idx + len(close_pattern):]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print('OK - replaced custos section')
print(f'Old size: {len(html)}')
print(f'New size: {len(new_html)}')