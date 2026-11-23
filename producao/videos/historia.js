// Peças dos vídeos de storytelling (C33, C34, C33b): bonequinho em SVG, cenários vetoriais, títulos e cartão de oferta.
// Tudo é desenhado em função de t (determinístico), para o render.js capturar quadro a quadro.
// Zonas (1080x1920): títulos entre y=230 e y=600; ilustração entre 620 e 1440; legenda queimada em 1500-1600.
const COR = { verde: '#1D4A32', noite: '#0f2619', papel: '#FFFAF2', creme: '#FFF4E3', pessego: '#F2B880', p200: '#F8D9B6',
  p100: '#FCEBD6', cta: '#C4532B', ctaEsc: '#A6421E', ouro: '#C9A45C', ouroSuave: '#E8D3A2', tinta: '#2A2522', linha: '#EAD9BD', teal: '#0F5C63' };

// ---------- bonequinho ----------
function boneco(id, cor = COR.cta, x = 540, y = 700, esc = 1) {
  const pele = '#E9A877';
  return `<svg id="${id}" class="abs boneco" viewBox="-110 -20 220 400" style="z-index:2;left:${x - 165 * esc}px;top:${y}px;width:${330 * esc}px;height:${600 * esc}px;overflow:visible">
  <g class="b-todo">
    <g class="b-perna-e"><rect x="-38" y="228" width="32" height="124" rx="16" fill="${COR.verde}"/><ellipse cx="-26" cy="352" rx="27" ry="13" fill="${COR.tinta}"/></g>
    <g class="b-perna-d"><rect x="6" y="228" width="32" height="124" rx="16" fill="${COR.verde}"/><ellipse cx="26" cy="352" rx="27" ry="13" fill="${COR.tinta}"/></g>
    <g class="b-tronco">
      <g class="b-braco-e"><rect x="-80" y="118" width="28" height="112" rx="14" fill="${cor}"/><circle cx="-66" cy="232" r="16" fill="${pele}"/></g>
      <g class="b-braco-d"><rect x="52" y="118" width="28" height="112" rx="14" fill="${cor}"/><circle cx="66" cy="232" r="16" fill="${pele}"/>
        <g class="b-cel" opacity="0"><rect x="50" y="196" width="40" height="66" rx="8" fill="${COR.noite}"/><rect x="55" y="203" width="30" height="50" rx="3" fill="#E3EFEE"/></g></g>
      <rect x="-58" y="108" width="116" height="140" rx="50" fill="${cor}"/>
      <path d="M-22 112 Q0 132 22 112" stroke="${COR.p200}" stroke-width="6" fill="none" stroke-linecap="round" opacity=".7"/>
      <g class="b-cabeca"><rect x="-14" y="92" width="28" height="22" rx="8" fill="${pele}"/>
        <circle cx="0" cy="58" r="52" fill="${pele}"/>
        <path d="M-52 52 Q-50 2 0 2 Q50 2 52 52 Q40 26 0 24 Q-38 26 -52 52Z" fill="#5a3a26"/>
        <g class="b-olhos"><ellipse cx="-18" cy="62" rx="6" ry="8" fill="${COR.tinta}"/><ellipse cx="18" cy="62" rx="6" ry="8" fill="${COR.tinta}"/></g>
      </g>
    </g>
  </g></svg>`;
}
// o = { bE, bD (graus dos braços, 0 = para baixo), andar (fase em s, ou null), olhar (-1..1), cel (0/1), pula (0..1) }
function animaBoneco(id, t, o = {}) {
  const r = document.getElementById(id);
  if (!r) return;
  const q = s => r.querySelector(s);
  const resp = Math.sin(t * 2 * Math.PI / 3.2);
  let bob = 0, pe = 0, pd = 0, be = o.bE ?? 0, bd = o.bD ?? 0;
  if (o.andar != null) {
    const f = Math.sin(o.andar * 2 * Math.PI * 1.6);
    pe = f * 18; pd = -f * 18; be += -f * 16; bd += f * 16; bob = -Math.abs(Math.cos(o.andar * 2 * Math.PI * 1.6)) * 8;
  }
  const pulo = (o.pula || 0) * -40;
  q('.b-todo').setAttribute('transform', `translate(0 ${bob + pulo})`);
  q('.b-perna-e').setAttribute('transform', `rotate(${pe} -22 232)`);
  q('.b-perna-d').setAttribute('transform', `rotate(${pd} 22 232)`);
  q('.b-tronco').setAttribute('transform', `translate(0 ${resp * 2.2}) `);
  q('.b-braco-e').setAttribute('transform', `rotate(${be} -66 126)`);
  q('.b-braco-d').setAttribute('transform', `rotate(${-bd} 66 126)`);
  q('.b-cabeca').setAttribute('transform', `translate(${(o.olhar || 0) * 6} ${resp * 1.2}) rotate(${(o.inclina || 0)} 0 100)`);
  // piscar a cada ~3,4 s (com variação) por 0,14 s
  const ciclo = (t + (o.fase || 0)) % 3.4, pisca = ciclo > 3.26 ? Math.abs(Math.sin((ciclo - 3.26) / 0.14 * Math.PI)) : 0;
  q('.b-olhos').setAttribute('transform', `translate(${(o.olhar || 0) * 5} 62) scale(1 ${1 - pisca * 0.9}) translate(0 -62)`);
  q('.b-cel').setAttribute('opacity', o.cel ? 1 : 0);
}

// figura de fundo (fila do mercado): silhueta simples
function figura(x, y, esc, cor) {
  return `<svg class="abs" viewBox="-60 -10 120 300" style="left:${x}px;top:${y}px;width:${120 * esc}px;height:${300 * esc}px">
    <circle cx="0" cy="34" r="32" fill="${cor}"/><rect x="-42" y="70" width="84" height="130" rx="36" fill="${cor}"/>
    <rect x="-30" y="180" width="24" height="100" rx="12" fill="${cor}"/><rect x="6" y="180" width="24" height="100" rx="12" fill="${cor}"/></svg>`;
}

// ---------- títulos (máx. 6 palavras por entrada) ----------
function titulo(id, texto, o = {}) {
  const cor = o.cor || COR.verde, top = o.top ?? 250, tam = o.tam ?? 92;
  return `<div class="abs titulo-h" id="${id}" style="left:80px;right:80px;top:${top}px;text-align:center;font-family:'Sans';font-weight:900;
    font-size:${tam}px;line-height:1.02;letter-spacing:-.01em;color:${cor};text-transform:uppercase;text-wrap:balance">${texto.split(' ').map(w => `<span class="w" style="display:inline-block">${w}</span>`).join(' ')}</div>`;
}
function animaTitulo(id, t, tin, tout = 1e9) {
  const el = document.getElementById(id);
  if (!el) return;
  el.style.opacity = 1 - E.inOut(prog(t, tout, tout + 0.3));
  el.style.visibility = t < tin || t > tout + 0.3 ? 'hidden' : 'visible';
  [...el.querySelectorAll('.w')].forEach((w, i) => entra(w, t, tin + i * 0.09, 1e9, { dy: 50, s0: 0.6, dur: 0.38, ease: E.back, base: '' }));
}
// selo pequeno (chip) que entra com mola
function chip(id, texto, x, y, o = {}) {
  return `<div class="abs" id="${id}" style="left:${x}px;top:${y}px;font-family:'Sans';font-weight:900;font-size:${o.tam || 44}px;letter-spacing:.02em;
    padding:14px 28px;border-radius:999px;background:${o.fundo || COR.cta};color:${o.cor || COR.papel};white-space:nowrap;text-transform:uppercase;
    box-shadow:0 12px 26px rgba(15,38,25,.22)">${texto}</div>`;
}

// ---------- cenários ----------
function cenaSala(id, extra = '') {
  return `<div class="cena" id="${id}" style="background:${COR.creme}"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <div class="abs" style="left:0;right:0;top:1180px;height:740px;background:${COR.p100}"></div>
    <svg class="abs par-f" viewBox="0 0 1080 1920" style="left:0;top:0;width:1080px;height:1920px">
      <rect x="110" y="640" width="300" height="360" rx="14" fill="#E3EFEE" stroke="${COR.linha}" stroke-width="14"/>
      <line x1="260" y1="640" x2="260" y2="1000" stroke="${COR.linha}" stroke-width="10"/><line x1="110" y1="820" x2="410" y2="820" stroke="${COR.linha}" stroke-width="10"/>
      <g id="${id}-cal"><rect x="700" y="660" width="210" height="230" rx="14" fill="#fff" stroke="${COR.linha}" stroke-width="6"/>
        <rect x="700" y="660" width="210" height="64" rx="14" fill="${COR.cta}"/><rect x="700" y="700" width="210" height="24" fill="${COR.cta}"/>
        <text x="805" y="705" text-anchor="middle" font-family="Sans" font-weight="900" font-size="34" fill="#fff">NOV</text>
        <text x="805" y="845" text-anchor="middle" font-family="Sans" font-weight="900" font-size="110" fill="${COR.verde}">23</text></g>
      <path d="M930 1180 L930 760 M890 760 L970 760 L950 700 L910 700Z" stroke="${COR.ouro}" stroke-width="10" fill="${COR.ouroSuave}"/>
    </svg>
    <svg class="abs" viewBox="0 0 1080 1920" style="left:0;top:0;width:1080px;height:1920px;z-index:1">
      <rect x="150" y="1000" width="780" height="300" rx="70" fill="${COR.verde}"/></svg>
    ${extra}
    <svg class="abs" viewBox="0 0 1080 1920" style="left:0;top:0;width:1080px;height:1920px;z-index:3">
      <rect x="110" y="1030" width="150" height="330" rx="60" fill="#235a3d"/><rect x="820" y="1030" width="150" height="330" rx="60" fill="#235a3d"/>
      <rect x="200" y="1200" width="680" height="150" rx="44" fill="#2b6a48"/>
      <rect x="190" y="1370" width="40" height="60" rx="10" fill="${COR.tinta}"/><rect x="850" y="1370" width="40" height="60" rx="10" fill="${COR.tinta}"/>
    </svg>
  </div></div>`;
}

function cenaMercado(id, extra = '') {
  const prods = [];
  const cores = [COR.cta, COR.ouro, '#7fae8c', COR.pessego, COR.teal, '#d77a4f'];
  for (let f = 0; f < 3; f++) for (let i = 0; i < 9; i++) {
    const vazio = (f === 1 && i > 3 && i < 8) || (f === 2 && (i === 1 || i === 2 || i === 6));
    if (!vazio) prods.push(`<rect x="${70 + i * 104}" y="${690 + f * 170 - 96}" width="78" height="96" rx="8" fill="${cores[(i * 7 + f * 3) % 6]}"/>`);
  }
  return `<div class="cena" id="${id}" style="background:#f3e6cf"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <svg class="abs par-f" viewBox="0 0 1080 1920" style="left:0;top:0;width:1080px;height:1920px">
      <rect x="40" y="560" width="1000" height="560" rx="18" fill="#fff8ec" stroke="${COR.linha}" stroke-width="8"/>
      ${[0, 1, 2].map(f => `<rect x="50" y="${690 + f * 170}" width="980" height="16" fill="${COR.linha}"/>`).join('')}
      ${prods.join('')}
      <rect x="90" y="1135" width="280" height="64" rx="14" fill="${COR.verde}"/>
      <text x="230" y="1180" text-anchor="middle" font-family="Sans" font-weight="900" font-size="38" fill="#fff">CAIXA</text>
      <g id="${id}-tag"><rect x="760" y="1140" width="260" height="96" rx="16" fill="${COR.cta}"/>
      <text x="890" y="1206" text-anchor="middle" font-family="Sans" font-weight="900" font-size="54" fill="#fff">23 DEZ</text></g>
    </svg>
    <div class="abs" id="${id}-fila" style="left:0;top:0;width:1080px;height:1920px;z-index:2">
      ${figura(40, 1170, 1.0, '#cdb893')}${figura(170, 1190, 0.95, '#bfa980')}${figura(560, 1180, 1.0, '#cdb893')}${figura(690, 1200, 0.95, '#c4ad85')}${figura(820, 1185, 1.0, '#b9a37b')}
    </div>${extra}
  </div></div>`;
}

// lista enorme que desenrola
function cenaLista(id, fundo = COR.creme, extra = '') {
  const linhas = Array.from({ length: 18 }, (_, i) => `<div style="display:flex;align-items:center;gap:18px;height:52px">
    <span style="width:30px;height:30px;border:4px solid ${COR.verde};border-radius:6px;flex:none"></span>
    <span style="height:14px;border-radius:7px;background:${COR.linha};width:${180 + (i * 97) % 260}px"></span></div>`).join('');
  return `<div class="cena" id="${id}" style="background:${fundo}"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <div class="abs" id="${id}-papel" style="left:470px;top:620px;width:500px;height:0;overflow:hidden;background:#fff;border-radius:14px;
      box-shadow:0 26px 60px rgba(15,38,25,.18);padding:30px 34px">${linhas}</div>
    <div class="abs mao" id="${id}-q1" style="left:120px;top:640px;font-size:150px;color:${COR.cta}">?</div>
    <div class="abs mao" id="${id}-q2" style="left:300px;top:590px;font-size:110px;color:${COR.ouro}">?</div>
    <div class="abs mao" id="${id}-q3" style="left:70px;top:930px;font-size:120px;color:${COR.cta}">?</div>
    <svg class="abs" id="${id}-rel" viewBox="-60 -60 120 120" style="left:880px;top:560px;width:150px;height:150px;z-index:4">
      <circle r="54" fill="#fff" stroke="${COR.verde}" stroke-width="8"/><line id="${id}-pm" x1="0" y1="0" x2="0" y2="-40" stroke="${COR.cta}" stroke-width="7" stroke-linecap="round"/>
      <line id="${id}-ph" x1="0" y1="0" x2="0" y2="-26" stroke="${COR.verde}" stroke-width="8" stroke-linecap="round"/></svg>
  ${extra}</div></div>`;
}
function relogioPonteiros(id, horas) {
  const m = document.getElementById(id + '-pm'), h = document.getElementById(id + '-ph');
  if (m) m.setAttribute('transform', `rotate(${(horas % 1) * 360})`);
  if (h) h.setAttribute('transform', `rotate(${(horas % 12) * 30})`);
}

// calendário 17 a 25 com tarefas (planejamento pronto)
const DIAS = [[17, 'cardapio', 'Cardápio'], [18, 'lista', 'Lista'], [19, '', ''], [20, '', ''], [21, 'peru', 'Geladeira'],
  [22, '', ''], [23, 'pratos', 'Adiantar'], [24, 'relogio', 'Hora a hora'], [25, 'pote', 'Sobras']];
function icone(nome, w = 70) {
  const s = (c) => `<svg viewBox="0 0 100 100" width="${w}" height="${w}">${c}</svg>`;
  switch (nome) {
    case 'cardapio': return s(`<rect x="22" y="10" width="56" height="80" rx="8" fill="#fff" stroke="${COR.verde}" stroke-width="6"/><line x1="34" y1="32" x2="66" y2="32" stroke="${COR.cta}" stroke-width="7" stroke-linecap="round"/><line x1="34" y1="50" x2="66" y2="50" stroke="${COR.linha}" stroke-width="6" stroke-linecap="round"/><line x1="34" y1="66" x2="58" y2="66" stroke="${COR.linha}" stroke-width="6" stroke-linecap="round"/>`);
    case 'lista': return s(`<rect x="20" y="10" width="60" height="80" rx="8" fill="#fff" stroke="${COR.verde}" stroke-width="6"/><path d="M30 34 l6 6 l10 -12 M30 58 l6 6 l10 -12" stroke="${COR.cta}" stroke-width="6" fill="none" stroke-linecap="round"/><line x1="52" y1="36" x2="70" y2="36" stroke="${COR.linha}" stroke-width="6"/><line x1="52" y1="60" x2="70" y2="60" stroke="${COR.linha}" stroke-width="6"/>`);
    case 'peru': return s(`<ellipse cx="50" cy="58" rx="36" ry="26" fill="#c9773f"/><ellipse cx="50" cy="52" rx="26" ry="14" fill="#e09a5f"/><path d="M18 62 L6 48 M82 62 L94 48" stroke="#c9773f" stroke-width="12" stroke-linecap="round"/><circle cx="5" cy="46" r="7" fill="#fff"/><circle cx="95" cy="46" r="7" fill="#fff"/><rect x="18" y="80" width="64" height="8" rx="4" fill="${COR.linha}"/>`);
    case 'pratos': return s(`<ellipse cx="50" cy="70" rx="42" ry="14" fill="#fff" stroke="${COR.verde}" stroke-width="5"/><path d="M22 66 Q50 30 78 66Z" fill="${COR.ouro}"/>`);
    case 'relogio': return s(`<circle cx="50" cy="50" r="38" fill="#fff" stroke="${COR.verde}" stroke-width="7"/><path d="M50 50 V26 M50 50 L66 60" stroke="${COR.cta}" stroke-width="7" stroke-linecap="round"/>`);
    case 'pote': return s(`<rect x="20" y="40" width="60" height="44" rx="10" fill="#E3EFEE" stroke="${COR.verde}" stroke-width="6"/><rect x="16" y="30" width="68" height="14" rx="6" fill="${COR.cta}"/>`);
    case 'pao': return s(`<path d="M14 64 Q14 30 50 30 Q86 30 86 64 Z" fill="#d9a35e"/><rect x="14" y="60" width="72" height="16" rx="6" fill="#c08646"/><path d="M34 40 l6 14 M50 38 l6 14 M66 40 l6 14" stroke="#f5d29b" stroke-width="5" stroke-linecap="round"/>`);
    case 'gelo': return s(`<rect x="12" y="40" width="34" height="34" rx="7" fill="#d7eef3" stroke="${COR.teal}" stroke-width="5"/><rect x="52" y="28" width="34" height="34" rx="7" fill="#d7eef3" stroke="${COR.teal}" stroke-width="5"/><rect x="36" y="58" width="34" height="34" rx="7" fill="#d7eef3" stroke="${COR.teal}" stroke-width="5"/>`);
    case 'frutas': return s(`<circle cx="36" cy="58" r="22" fill="${COR.cta}"/><circle cx="64" cy="62" r="20" fill="${COR.pessego}"/><circle cx="52" cy="38" r="14" fill="#7fae8c"/><path d="M52 24 q4 -10 12 -12" stroke="${COR.verde}" stroke-width="5" fill="none"/>`);
    case 'sobremesa': return s(`<path d="M22 20 L78 20 L66 88 L34 88Z" fill="#fff" stroke="${COR.verde}" stroke-width="5"/><path d="M26 40 L74 40 L71 56 L29 56Z" fill="${COR.pessego}"/><path d="M29 56 L71 56 L68 72 L32 72Z" fill="${COR.ouroSuave}"/><circle cx="50" cy="28" r="7" fill="${COR.cta}"/>`);
    case 'farofa': return s(`<path d="M8 46 Q50 100 92 46Z" fill="#fff" stroke="${COR.verde}" stroke-width="5"/><ellipse cx="50" cy="46" rx="42" ry="12" fill="#e0b465"/><circle cx="36" cy="44" r="3" fill="#8a5a2b"/><circle cx="58" cy="42" r="3" fill="#8a5a2b"/><circle cx="66" cy="48" r="3" fill="#7fae8c"/>`);
    case 'salpicao': return s(`<path d="M8 46 Q50 100 92 46Z" fill="#fff" stroke="${COR.verde}" stroke-width="5"/><ellipse cx="50" cy="46" rx="42" ry="12" fill="#f6efd8"/><path d="M30 42 l10 -4 M52 40 l12 2 M44 48 l8 2" stroke="${COR.cta}" stroke-width="4" stroke-linecap="round"/><circle cx="62" cy="47" r="3" fill="#7fae8c"/>`);
    case 'check': return s(`<circle cx="50" cy="50" r="44" fill="${COR.verde}"/><path d="M28 52 l14 14 l30 -32" stroke="#fff" stroke-width="10" fill="none" stroke-linecap="round" stroke-linejoin="round"/>`);
    case 'jogo': return s(`<rect x="14" y="30" width="72" height="46" rx="22" fill="${COR.teal}"/><path d="M32 46 v16 M24 54 h16" stroke="#fff" stroke-width="6" stroke-linecap="round"/><circle cx="64" cy="48" r="5" fill="#fff"/><circle cx="72" cy="58" r="5" fill="#fff"/>`);
    case 'moeda': return s(`<circle cx="50" cy="50" r="38" fill="${COR.ouro}"/><circle cx="50" cy="50" r="28" fill="none" stroke="#fff" stroke-width="5"/>`);
    default: return '';
  }
}
function cenaCalendario(id, fundo = COR.creme, extra = '') {
  const cel = DIAS.map(([d, ic, rot], i) => `<div class="abs dia" id="${id}-d${d}" style="left:${100 + (i % 3) * 300}px;top:${640 + Math.floor(i / 3) * 255}px;width:280px;height:235px;
     background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(15,38,25,.12);text-align:center">
     <div style="font-family:'Sans';font-weight:900;font-size:56px;color:${COR.verde};margin-top:14px">${d}</div>
     <div style="height:80px;display:flex;justify-content:center">${icone(ic, 80)}</div>
     <div style="font-family:'Sans';font-weight:800;font-size:34px;color:${COR.cta}">${rot}</div>
     <div class="abs ok" id="${id}-ok${d}" style="right:-14px;top:-14px">${ic ? icone('check', 64) : ''}</div></div>`).join('');
  return `<div class="cena" id="${id}" style="background:${fundo}"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <div class="abs" style="left:80px;top:610px;width:920px;height:830px;border-radius:30px;background:${COR.p100}"></div>${cel}${extra}</div></div>`;
}
function animaCalendario(id, t, t0, passo = 0.12) {
  DIAS.forEach(([d, ic], i) => {
    entra(`#${id}-d${d}`, t, t0 + i * passo, 1e9, { dy: 60, s0: 0.7, dur: 0.4, ease: E.back });
    if (ic) entra(`#${id}-ok${d}`, t, t0 + 0.5 + i * passo, 1e9, { dy: 0, s0: 0.2, dur: 0.3, ease: E.back });
  });
}

// PDF em camadas: capa + páginas reais do guia
const PAGINAS = [['guia-p031', '30 receitas'], ['guia-p008', '3 cardápios, 8 a 10 pessoas'], ['guia-p012', 'Lista por seção'], ['guia-p022', 'Dia 17 ao 25']];
function cenaPDF(id, fundo = COR.creme, extra = '', paginas = PAGINAS, ultimo = 'Dia 24 hora a hora') {
  return `<div class="cena" id="${id}" style="background:${fundo}"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <img class="abs" id="${id}-capa" src="../../assets/site/capa-ceia.webp" style="left:310px;top:650px;width:460px;border-radius:10px;box-shadow:0 30px 70px rgba(15,38,25,.35);z-index:1">
    ${paginas.map(([p, r], i) => `<div class="abs" id="${id}-p${i}" style="left:${150 + i * (450 / Math.max(1, paginas.length - 1))}px;top:${700 + (i % 2) * 40}px;width:330px;z-index:${2 + i}">
      <div style="background:#fff;border-radius:8px;overflow:hidden;box-shadow:0 24px 50px rgba(15,38,25,.28)"><img src="../../assets/site/${p}.webp" style="display:block;width:100%"></div></div>`).join('')}
    ${paginas.map(([p, r], i) => chip(`${id}-c${i}`, r, 0, 0, { tam: 46 })).join('')}
    ${ultimo ? chip(`${id}-c${paginas.length}`, ultimo, 0, 0, { tam: 46, fundo: COR.verde }) : ''}
  ${extra}</div></div>`;
}
// cada página entra num instante; o chip correspondente aparece centralizado acima da pilha
function animaPDF(id, t, tempos, tCapa) {
  entra(`#${id}-capa`, t, tCapa, 1e9, { dy: 120, s0: 0.85, dur: 0.6 });
  const rot = [-8, 5, -4, 7];
  tempos.forEach((ti, i) => {
    if (!document.getElementById(`${id}-p${i}`)) return;
    entra(`#${id}-p${i}`, t, ti, 1e9, { dy: 260, s0: 0.8, dur: 0.55, ease: E.back, rot: rot[i] });
  });
  tempos.forEach((ti, i) => {
    const fim = tempos[i + 1] ?? 1e9;
    const el = document.getElementById(`${id}-c${i}`);
    if (!el) return;
    el.style.left = '50%'; el.style.top = '1340px';
    entra(el, t, ti + 0.15, fim, { dy: 40, s0: 0.6, dur: 0.35, ease: E.back, base: 'translateX(-50%)', dyOut: -20, outDur: 0.2 });
  });
}

// celular grande com o PDF entrando e o aviso "salvo"
function cenaCelular(id, fundo = COR.creme, extra = '') {
  return `<div class="cena" id="${id}" style="background:${fundo}"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <div class="abs" id="${id}-tel" style="left:360px;top:640px;width:420px;height:780px;border-radius:56px;background:${COR.noite};box-shadow:0 30px 70px rgba(15,38,25,.35)">
      <div style="position:absolute;left:22px;right:22px;top:22px;bottom:22px;border-radius:38px;background:#E3EFEE;overflow:hidden">
        <div style="font-family:'Sans';font-weight:900;font-size:30px;color:${COR.verde};padding:34px 0 0 30px">Arquivos</div>
        <img id="${id}-pdf" src="../../assets/site/capa-ceia.webp" style="position:absolute;left:60px;top:110px;width:256px;border-radius:6px;box-shadow:0 12px 24px rgba(0,0,0,.2)">
        <div id="${id}-toast" style="position:absolute;left:24px;right:24px;bottom:40px;padding:18px;border-radius:20px;background:${COR.verde};color:#fff;
          font-family:'Sans';font-weight:900;font-size:30px;text-align:center">✓ Salvo</div>
      </div></div>
    <div class="abs" id="${id}-dia" style="left:800px;top:700px;width:190px;height:210px;border-radius:20px;background:#fff;box-shadow:0 16px 34px rgba(15,38,25,.18);text-align:center;overflow:hidden">
      <div style="background:${COR.cta};color:#fff;font-family:'Sans';font-weight:900;font-size:32px;padding:10px 0">DEZ</div>
      <div style="font-family:'Sans';font-weight:900;font-size:100px;color:${COR.verde};line-height:1.4">17</div></div>
  ${extra}</div></div>`;
}

// cartão de oferta: preço em duas entradas, garantia e botão pulsando
function cenaOferta(id, botao) {
  return `<div class="cena" id="${id}"><div class="cheio noite"></div><canvas class="luz" id="${id}-luz"></canvas><div class="vinheta"></div>
    <img class="abs" id="${id}-capa" src="../../assets/site/capa-ceia.webp" style="left:50%;top:250px;width:380px;margin-left:-190px;border-radius:8px;box-shadow:0 34px 70px rgba(0,0,0,.5);z-index:5">
    <div class="abs" id="${id}-p1" style="left:60px;right:60px;top:780px;text-align:center;font-family:'Sans';font-weight:900;font-size:96px;line-height:1;color:${COR.pessego};z-index:5">DEZENOVE E NOVENTA</div>
    <div class="abs" id="${id}-p2" style="left:60px;right:60px;top:${780 + 210}px;text-align:center;font-family:'Sans';font-weight:900;font-size:66px;line-height:1.05;color:${COR.papel};z-index:5">ATÉ TRINTA DE NOVEMBRO</div>
    <div class="abs" id="${id}-g" style="left:60px;right:60px;top:1150px;text-align:center;font-family:'Sans';font-weight:800;font-size:48px;color:${COR.ouroSuave};z-index:5">7 dias de garantia</div>
    <div class="abs" id="${id}-bt" style="left:50%;top:1260px;z-index:5;font-family:'Sans';font-weight:900;font-size:56px;padding:22px 64px;border-radius:999px;
      background:${COR.cta};color:#fff;white-space:nowrap;box-shadow:0 16px 36px rgba(0,0,0,.35)">${botao}</div>
  </div>`;
}
function animaOferta(id, t, a, tp1, tp2, tg, tbt) {
  cena(`#${id}`, t, a, 1e9, 0.01);
  if (t >= a - 0.05) luz(document.getElementById(`${id}-luz`), { semente: 9, n: 34, min: 16, max: 100, alfa: .2, brilhos: [[0.5, 0.9, 560, .3]] }, t);
  entra(`#${id}-capa`, t, a + 0.05, 1e9, { dy: 80, s0: 0.9, dur: 0.6 });
  entra(`#${id}-p1`, t, tp1, 1e9, { dy: 40, s0: 0.7, dur: 0.45, ease: E.back });
  entra(`#${id}-p2`, t, tp2, 1e9, { dy: 40, s0: 0.8, dur: 0.45, ease: E.back });
  entra(`#${id}-g`, t, tg, 1e9, { dy: 30 });
  const pulso = t > tbt + 0.5 ? 1 + 0.045 * Math.sin((t - tbt) * 2 * Math.PI / 1.1) : 1;
  entra(`#${id}-bt`, t, tbt, 1e9, { dy: 0, s0: 0.5, dur: 0.5, ease: E.back, base: `translateX(-50%) scale(${pulso})` });
}

// transição: faixa diagonal que varre a tela (cobre o corte)
function faixa(t, at, cor = COR.pessego, id = 'faixa') {
  let el = document.getElementById(id);
  if (!el) { el = document.createElement('div'); el.id = id; el.style.cssText = 'position:absolute;left:-400px;width:1880px;height:2600px;top:-340px;z-index:50;'; document.body.appendChild(el); }
  el.style.background = cor;
  const p = prog(t, at - 0.22, at + 0.22);
  el.style.visibility = p > 0 && p < 1 ? 'visible' : 'hidden';
  el.style.transform = `rotate(-12deg) translateY(${(1 - E.inOut(p) * 2) * 2700}px)`;
}
// câmera: zoom lento + parallax dos fundos durante a cena
function camera(id, t, a, b, s0 = 1, s1 = 1.08, dx = 0, dy = 0) {
  const c = document.getElementById(id + '-cam');
  if (!c) return;
  const p = E.inOut(prog(t, a, b));
  c.style.transform = `translate(${dx * p}px, ${dy * p}px) scale(${s0 + (s1 - s0) * p})`;
  c.style.transformOrigin = '50% 60%';
  c.querySelectorAll('.par-f').forEach(f => { f.style.transform = `translateX(${-dx * 0.6 * p - 30 * p}px)`; });
}

// ---------- peças do C34 (calendário de 7 dias) ----------
// calendário de parede gigante (dezembro) com uma folha de novembro que vira
function cenaParede(id, fundo = COR.creme, extra = '', marcados = [17, 21, 23, 24]) {
  const dias = [];
  // dezembro de 2026 começa numa terça (col 2, com domingo = 0)
  for (let d = 1; d <= 31; d++) {
    const i = d + 1, col = i % 7, lin = Math.floor(i / 7);
    const marca = marcados.includes(d);
    dias.push(`<div class="abs" id="${id}-n${d}" style="left:${28 + col * 100}px;top:${190 + lin * 100}px;width:88px;height:88px;border-radius:44px;
      display:flex;align-items:center;justify-content:center;font-family:'Sans';font-weight:900;font-size:40px;
      color:${marca ? '#fff' : COR.verde};background:${marca ? COR.cta : 'transparent'}">${d}</div>`);
  }
  return `<div class="cena" id="${id}" style="background:${fundo}"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <div class="abs" id="${id}-cal" style="left:150px;top:640px;width:760px;height:800px;background:#fff;border-radius:26px;box-shadow:0 30px 70px rgba(15,38,25,.2);perspective:1800px">
      <div style="position:absolute;left:0;right:0;top:0;height:150px;border-radius:26px 26px 0 0;background:${COR.verde};color:#fff;
        font-family:'Sans';font-weight:900;font-size:64px;text-align:center;line-height:160px;letter-spacing:.06em">DEZEMBRO</div>
      ${dias.join('')}
      <div id="${id}-folha" style="position:absolute;left:0;top:0;width:760px;height:800px;border-radius:26px;background:${COR.p100};
        transform-origin:50% 0;backface-visibility:hidden;box-shadow:0 10px 30px rgba(0,0,0,.12)">
        <div style="height:150px;border-radius:26px 26px 0 0;background:${COR.cta};color:#fff;font-family:'Sans';font-weight:900;font-size:64px;text-align:center;line-height:160px;letter-spacing:.06em">NOVEMBRO</div></div>
      ${[0, 1, 2, 3].map(k => `<div style="position:absolute;top:-22px;left:${150 + k * 150}px;width:22px;height:54px;border-radius:11px;background:${COR.tinta}"></div>`).join('')}
    </div>${extra}</div></div>`;
}
function animaParede(id, t, tVira) {
  const p = E.inOut(prog(t, tVira, tVira + 0.7));
  const f = document.getElementById(`${id}-folha`);
  f.style.transform = `rotateX(${p * 175}deg)`;
  f.style.opacity = p > 0.95 ? 0 : 1;
}
function cenaGeladeira(id, fundo = COR.creme, extra = '') {
  return `<div class="cena" id="${id}" style="background:${fundo}"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <div class="abs" style="left:0;right:0;top:1340px;height:600px;background:${COR.p100}"></div>
    <div class="abs" style="left:240px;top:620px;width:420px;height:800px;border-radius:40px;background:#eef3f1;border:10px solid ${COR.verde}">
      <div style="position:absolute;left:0;right:0;top:250px;height:10px;background:${COR.verde}"></div>
      <div style="position:absolute;right:26px;top:90px;width:16px;height:110px;border-radius:8px;background:${COR.verde}"></div>
      <div style="position:absolute;right:26px;top:310px;width:16px;height:160px;border-radius:8px;background:${COR.verde}"></div>
      <div style="position:absolute;left:30px;top:24px;font-family:'Sans';font-weight:900;font-size:40px;color:${COR.teal}">CONGELADOR</div>
      <div style="position:absolute;left:30px;top:284px;font-family:'Sans';font-weight:900;font-size:40px;color:${COR.verde}">GELADEIRA</div>
    </div>
    <div class="abs" id="${id}-peru" style="left:330px;top:700px;width:200px;height:200px;z-index:4">${icone('peru', 200)}</div>
    ${extra}</div></div>`;
}
function cenaBancada(id, itens, fundo = COR.creme, extra = '') {
  return `<div class="cena" id="${id}" style="background:${fundo}"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <div class="abs" style="left:40px;right:40px;top:1180px;height:90px;border-radius:20px;background:${COR.verde}"></div>
    <div class="abs" style="left:80px;right:80px;top:1270px;height:180px;background:#235a3d;border-radius:0 0 20px 20px"></div>
    ${itens.map(([ic, rot], i) => `<div class="abs" id="${id}-i${i}" style="left:${70 + i * 320}px;top:${790}px;width:300px;text-align:center">
      <div style="display:flex;justify-content:center">${icone(ic, 250)}</div>
      <div style="font-family:'Sans';font-weight:900;font-size:48px;color:${COR.cta};margin-top:10px">${rot}</div></div>`).join('')}
    ${extra}</div></div>`;
}
function cenaCozinha(id, fundo = COR.creme, extra = '') {
  return `<div class="cena" id="${id}" style="background:${fundo}"><div class="cam" id="${id}-cam" style="position:absolute;inset:0">
    <div class="abs" style="left:0;right:0;top:1340px;height:600px;background:${COR.p100}"></div>
    <div class="abs" style="left:90px;top:820px;width:440px;height:540px;border-radius:30px;background:${COR.tinta}">
      <div style="position:absolute;left:30px;right:30px;top:24px;height:50px;display:flex;gap:26px;justify-content:center">
        ${[0, 1, 2, 3].map(() => `<span style="width:44px;height:44px;border-radius:22px;background:#4a423c"></span>`).join('')}</div>
      <div id="${id}-vidro" style="position:absolute;left:40px;right:40px;top:110px;height:300px;border-radius:24px;background:#3a2a20;overflow:hidden">
        <div id="${id}-brilho" style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 70%, #f29a4a 0%, rgba(242,154,74,0) 70%)"></div>
        <div style="position:absolute;left:80px;top:70px">${icone('peru', 200)}</div></div>
      <div style="position:absolute;left:60px;right:60px;top:440px;height:22px;border-radius:11px;background:#6b625b"></div>
    </div>
    <svg class="abs" id="${id}-rel" viewBox="-60 -60 120 120" style="left:640px;top:640px;width:300px;height:300px">
      <circle r="56" fill="#fff" stroke="${COR.verde}" stroke-width="7"/>
      ${Array.from({ length: 12 }, (_, k) => `<line x1="0" y1="-48" x2="0" y2="-42" stroke="${COR.verde}" stroke-width="3" transform="rotate(${k * 30})"/>`).join('')}
      <line id="${id}-ph" x1="0" y1="0" x2="0" y2="-26" stroke="${COR.verde}" stroke-width="7" stroke-linecap="round"/>
      <line id="${id}-pm" x1="0" y1="0" x2="0" y2="-40" stroke="${COR.cta}" stroke-width="5" stroke-linecap="round"/><circle r="5" fill="${COR.verde}"/></svg>
    <div class="abs" style="left:640px;top:1180px;width:380px;height:40px;border-radius:12px;background:${COR.ouro}"></div>
    <div class="abs" style="left:670px;top:1220px;width:24px;height:200px;background:#a8853f"></div><div class="abs" style="left:966px;top:1220px;width:24px;height:200px;background:#a8853f"></div>
    ${extra}</div></div>`;
}
