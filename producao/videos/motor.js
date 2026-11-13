// Motor de animação determinístico: cada vídeo define window.DURACAO e cenas(t).
// window.render(t) é chamado pelo renderizador para cada quadro (30 fps).
const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
const prog = (t, a, b) => clamp((t - a) / (b - a));
const E = {
  out: x => 1 - Math.pow(1 - x, 3),
  inOut: x => (x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2),
  back: x => { const c1 = 1.5, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); },
};
const $ = s => document.querySelector(s);

// Entrada (sobe e aparece) em tin; saída (some) em tout. Opções: dy, dx, s0 (escala inicial), dur, rot.
function entra(el, t, tin, tout = 1e9, o = {}) {
  if (typeof el === 'string') el = $(el);
  if (!el) return;
  const dur = o.dur ?? 0.5, dy = o.dy ?? 50, dx = o.dx ?? 0, s0 = o.s0 ?? 1, rot = o.rot ?? 0, outDur = o.outDur ?? 0.35;
  const a = (o.ease || E.out)(prog(t, tin, tin + dur));
  const b = E.inOut(prog(t, tout, tout + outDur));
  const op = a * (1 - b);
  el.style.opacity = op;
  el.style.visibility = op <= 0.001 ? 'hidden' : 'visible';
  const ty = (1 - a) * dy - b * (o.dyOut ?? 30);
  const tx = (1 - a) * dx;
  const sc = s0 + (1 - s0) * a;
  el.style.transform = `${o.base || ''} translate(${tx}px, ${ty}px) scale(${sc}) rotate(${rot}deg)`;
}

// Movimento lento de câmera (Ken Burns) num fundo
function kb(el, t, a, b, s0, s1, x0 = 0, x1 = 0, y0 = 0, y1 = 0) {
  if (typeof el === 'string') el = $(el);
  const p = E.inOut(prog(t, a, b));
  el.style.transform = `translate(${x0 + (x1 - x0) * p}px, ${y0 + (y1 - y0) * p}px) scale(${s0 + (s1 - s0) * p})`;
}

// Visibilidade simples de uma cena inteira (corte seco com leve fade)
function cena(el, t, a, b, fade = 0.25) {
  if (typeof el === 'string') el = $(el);
  const op = Math.min(prog(t, a, a + fade), 1 - prog(t, b - fade, b));
  el.style.opacity = op;
  el.style.visibility = op <= 0.001 ? 'hidden' : 'visible';
}

// Revela palavras de um elemento uma a uma (precisa de spans .w)
function palavras(el, t, tin, passo = 0.12, o = {}) {
  if (typeof el === 'string') el = $(el);
  [...el.querySelectorAll('.w')].forEach((w, i) => entra(w, t, tin + i * passo, o.tout ?? 1e9, { dy: o.dy ?? 30, dur: 0.35, base: '' }));
}
function quebraPalavras(el) {
  if (typeof el === 'string') el = $(el);
  const walk = n => {
    [...n.childNodes].forEach(c => {
      if (c.nodeType === 3) {
        const frag = document.createDocumentFragment();
        c.textContent.split(/(\s+)/).forEach(p => {
          if (!p) return;
          if (/^\s+$/.test(p)) frag.appendChild(document.createTextNode(p));
          else { const s = document.createElement('span'); s.className = 'w'; s.style.display = 'inline-block'; s.textContent = p; frag.appendChild(s); }
        });
        c.replaceWith(frag);
      } else if (c.nodeType === 1 && c.tagName !== 'BR') walk(c);
    });
  };
  walk(el);
}

// Cartão final padrão com a capa e o que vem no guia
function montaFinal(titulo, itens, cta = 'Toque no botão e veja por dentro') {
  const d = document.createElement('div');
  d.className = 'final cena'; d.id = 'final';
  d.innerHTML = `<img class="capa abs" id="f-capa" src="../../assets/site/capa-ceia.webp">
    <div class="tit abs" id="f-tit">${titulo}</div>
    <ul class="abs" id="f-ul">${itens.map(i => `<li>${i}</li>`).join('')}</ul>
    <div class="preco abs" id="f-preco">R$ 19,90</div>
    <div class="cta abs" id="f-cta">${cta}</div>`;
  document.body.appendChild(d);
}
function animaFinal(t, a) {
  cena('#final', t, a, 1e9, 0.3);
  entra('#f-capa', t, a + 0.1, 1e9, { dy: 80, s0: 0.9, dur: 0.6 });
  entra('#f-tit', t, a + 0.45, 1e9, { dy: 30 });
  [...document.querySelectorAll('#f-ul li')].forEach((li, i) => entra(li, t, a + 0.7 + i * 0.18, 1e9, { dy: 20, dx: -20, dur: 0.4 }));
  entra('#f-preco', t, a + 1.4, 1e9, { dy: 0, s0: 0.6, dur: 0.5, ease: E.back, base: 'translateX(-50%)' });
  entra('#f-cta', t, a + 1.8, 1e9, { dy: 20 });
}

// Cartão final da série de objeções (C21 em diante): fundo noite com luz quente, capa, uma frase, preço e chamada.
// Tudo entre y=250 e y=1580 (zonas seguras de Reels e Stories).
function montaFinal2(frase, cta = 'Toque em Saiba mais') {
  const d = document.createElement('div');
  d.className = 'cena'; d.id = 'final2';
  d.innerHTML = `<div class="cheio noite"></div><canvas class="luz" id="f2-luz"></canvas><div class="vinheta"></div>
    <img class="abs" id="f2-capa" src="../../assets/site/capa-ceia.webp" style="left:50%;top:330px;width:520px;margin-left:-260px;border-radius:8px;box-shadow:0 40px 80px rgba(0,0,0,.5);z-index:5">
    <div class="abs titulo" id="f2-frase" style="left:90px;right:90px;top:910px;text-align:center;font-size:66px;text-wrap:balance;color:var(--papel);z-index:5">${frase}</div>
    <div class="abs" id="f2-preco" style="left:50%;top:1150px;z-index:5;font-family:'Sans';font-weight:900;font-size:58px;padding:16px 46px;border-radius:999px;background:var(--pessego);color:var(--noite);white-space:nowrap">R$ 19,90</div>
    <div class="abs" id="f2-cta" style="left:90px;right:90px;top:1290px;text-align:center;font-family:'Sans';font-weight:800;font-size:36px;color:var(--ouro-suave);z-index:5">${cta}</div>`;
  document.body.appendChild(d);
}
function animaFinal2(t, a, luzOpc = {}) {
  cena('#final2', t, a, 1e9, 0.3);
  if (t >= a - 0.05) luz(document.getElementById('f2-luz'), Object.assign({ semente: 5, n: 34, min: 16, max: 100, alfa: .2, brilhos: [[0.5, 1.0, 560, .32]] }, luzOpc), t);
  entra('#f2-capa', t, a + 0.1, 1e9, { dy: 80, s0: 0.9, dur: 0.6 });
  entra('#f2-frase', t, a + 0.45, 1e9, { dy: 30 });
  entra('#f2-preco', t, a + 0.9, 1e9, { dy: 0, s0: 0.6, dur: 0.5, ease: E.back, base: 'translateX(-50%)' });
  entra('#f2-cta', t, a + 1.25, 1e9, { dy: 20 });
}
