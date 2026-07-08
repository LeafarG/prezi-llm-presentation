#!/usr/bin/env python3
import sys

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_marker = '<!-- ============ CUSTOS ============ -->'
start_idx = html.find(start_marker)
print(f'start_idx = {start_idx}')

close_pattern = '</div>\n      </div>\n  </div><!-- /.viewport -->'
close_idx = html.find(close_pattern, start_idx)
print(f'close_idx = {close_idx}')

if start_idx == -1 or close_idx == -1:
    print('ERROR: markers not found')
    sys.exit(1)

DOLLAR = chr(36)

new_custos = '''<!-- ============ CUSTOS ============ -->
      <div class="section" id="sec-custos" data-id="custos"
           style="left: 8000px; top: 200px; width: 1400px; height: 1100px;">
        <div class="frame">
          <div class="poster">
            <div class="poster-num">// ORÇAMENTO</div>
            <div class="poster-title">Pensar caro<br>ou pensar barato?</div>
            <div class="poster-sub">Opus 4.6 · GLM 5.2 · GPT-5 — preço por capacidade.</div>
          </div>

          <div class="content-body">
            <p style="font-size:0.78rem;line-height:1.4;margin:0 0 0.7rem"><span style="color:var(--warning);font-weight:600">Regra de bolso:</span> o modelo <em>mais capaz</em> raramente é o mais <em>custo-efetivo</em>. Pague Opus só pra nuance + raciocínio profundo — use GLM ou GPT-5 mini pra todo o resto.</p>

            <!-- ============ BIG-NUMBER MODEL CARDS ============ -->
            <div class="cost-model-cards">
              <div class="cmc cmc-opus">
                <div class="cmc-name"><span class="purple">Opus 4.6</span></div>
                <div class="cmc-price">''' + DOLLAR + '''5 <span class="cmc-unit">/M in</span></div>
                <div class="cmc-price">''' + DOLLAR + '''25 <span class="cmc-unit">/M out</span></div>
                <div class="cmc-meta">Adaptive · 3–5× thinking</div>
                <div class="cmc-score">Score 84 · <span style="color:var(--warning)">''' + DOLLAR + '''/$ = 3.4</span></div>
              </div>
              <div class="cmc cmc-glm">
                <div class="cmc-best">★ melhor $/Score</div>
                <div class="cmc-name"><span class="success">GLM 5.2</span></div>
                <div class="cmc-price">''' + DOLLAR + '''1.40 <span class="cmc-unit">/M in</span></div>
                <div class="cmc-price">''' + DOLLAR + '''4.40 <span class="cmc-unit">/M out</span></div>
                <div class="cmc-meta">Reasoning · ''' + DOLLAR + '''1/''' + DOLLAR + '''3.20</div>
                <div class="cmc-score">Score 83 · <span style="color:var(--success)">''' + DOLLAR + '''/$ = 17.5</span></div>
              </div>
              <div class="cmc cmc-gpt">
                <div class="cmc-name"><span class="accent">GPT-5</span></div>
                <div class="cmc-price">''' + DOLLAR + '''1.25 <span class="cmc-unit">/M in</span></div>
                <div class="cmc-price">''' + DOLLAR + '''10 <span class="cmc-unit">/M out</span></div>
                <div class="cmc-meta">o-series · 5–20× thinking</div>
                <div class="cmc-score">Score 72 · <span style="color:var(--accent)">''' + DOLLAR + '''/$ = 8.0</span></div>
              </div>
            </div>

            <p style="font-size:0.7rem;text-align:center;margin:0.5rem 0 0.7rem;color:var(--text-dim)"><em>GLM 5.2 entrega <strong style="color:var(--success)">5× mais valor por dólar</strong> que Opus 4.6 — com score quase igual.</em></p>

            <!-- ============ 2H ESTIMATE - BIG VISUAL ============ -->
            <h4 style="color:var(--warning);margin:0.6rem 0 0.4rem;font-size:0.85rem;letter-spacing:0.05em;text-align:center">⏱ CUSTO DE 2 HORAS DE ATIVIDADE AGÊNTICA</h4>

            <div class="cost-scenario-cards">
              <div class="csc csc-light">
                <div class="csc-tag">LIGHT</div>
                <div class="csc-desc">sem thinking · só leitura + plan</div>
                <div class="csc-numbers">
                  <div class="csc-row">
                    <span class="csc-label">Opus 4.6</span>
                    <span class="csc-val">''' + DOLLAR + '''5.05</span>
                  </div>
                  <div class="csc-row csc-winner">
                    <span class="csc-label">GLM 5.2</span>
                    <span class="csc-val">''' + DOLLAR + '''1.42</span>
                  </div>
                  <div class="csc-row">
                    <span class="csc-label">GPT-5</span>
                    <span class="csc-val">''' + DOLLAR + '''1.92</span>
                  </div>
                </div>
              </div>

              <div class="csc csc-medium">
                <div class="csc-tag">MEDIUM</div>
                <div class="csc-desc">thinking moderado (5× output)</div>
                <div class="csc-numbers">
                  <div class="csc-row">
                    <span class="csc-label">Opus 4.6</span>
                    <span class="csc-val">''' + DOLLAR + '''15.60</span>
                  </div>
                  <div class="csc-row csc-winner">
                    <span class="csc-label">GLM 5.2</span>
                    <span class="csc-val">''' + DOLLAR + '''3.24</span>
                  </div>
                  <div class="csc-row">
                    <span class="csc-label">GPT-5</span>
                    <span class="csc-val">''' + DOLLAR + '''5.52</span>
                  </div>
                </div>
              </div>

              <div class="csc csc-heavy">
                <div class="csc-tag">HEAVY</div>
                <div class="csc-desc">Opus extended max thinking</div>
                <div class="csc-numbers">
                  <div class="csc-row csc-pink">
                    <span class="csc-label">Opus 4.6</span>
                    <span class="csc-val">''' + DOLLAR + '''37.50</span>
                  </div>
                  <div class="csc-row csc-winner">
                    <span class="csc-label">GLM 5.2</span>
                    <span class="csc-val">''' + DOLLAR + '''7.38</span>
                  </div>
                  <div class="csc-row">
                    <span class="csc-label">GPT-5</span>
                    <span class="csc-val">''' + DOLLAR + '''13.88</span>
                  </div>
                </div>
              </div>
            </div>

            <p style="font-size:0.68rem;text-align:center;margin:0.5rem 0 0.4rem;color:var(--text-dim)"><em>Premissas: 8 user turns · 15 model calls/turn · 8K input + 600 out + 3K thinking/call · <strong style="color:var(--success)">cache 80% corta 5×</strong></em></p>

            <!-- ============ ROUTE: WHEN USE WHAT ============ -->
            <div class="cost-route">
              <div class="route-step route-simple">
                <div class="route-num">1</div>
                <div class="route-text">Tarefa <strong>simples</strong>?</div>
                <div class="route-arrow">→</div>
                <div class="route-action" style="color:var(--success)">GLM 5.2 · GPT-5 mini</div>
              </div>
              <div class="route-step route-complex">
                <div class="route-num">2</div>
                <div class="route-text"><strong>Complexa</strong>?</div>
                <div class="route-arrow">→</div>
                <div class="route-action" style="color:var(--accent)">GLM reasoning · GPT-5 o3</div>
              </div>
              <div class="route-step route-deep">
                <div class="route-num">3</div>
                <div class="route-text">Precisa <strong>nuance</strong>?</div>
                <div class="route-arrow">→</div>
                <div class="route-action" style="color:var(--purple)">Só então Opus 4.6</div>
              </div>
            </div>

            <!-- ============ FOOTER ============ -->
            <p style="font-size:0.62rem;color:var(--text-dim);margin-top:0.4rem;text-align:center;border-top:1px solid var(--border);padding-top:0.3rem">
              Preços jul/2026 · Anthropic, OpenAI, Zhipu AI · por milhão de tokens · Thinking = output rate · Cache corta até 90%
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