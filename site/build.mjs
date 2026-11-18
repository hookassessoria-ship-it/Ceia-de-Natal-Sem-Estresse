// Build do site Cantinho do Lar: lê site.config.json, valida, injeta valores e gera dist/.
// Uso: node build.mjs   (sem dependências)
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const RAIZ = path.dirname(fileURLToPath(import.meta.url));
const SRC = path.join(RAIZ, 'src');
const DIST = path.join(RAIZ, 'dist');

const falhar = (msgs) => {
  console.error('\n✖ BUILD FALHOU\n' + msgs.map((m) => '  - ' + m).join('\n') + '\n');
  process.exit(1);
};

// ---------- 1. configuração ----------
let cfg;
try { cfg = JSON.parse(fs.readFileSync(path.join(RAIZ, 'site.config.json'), 'utf8')); }
catch (e) { falhar(['Não consegui ler site.config.json: ' + e.message]); }

const OBRIGATORIOS = ['CHECKOUT_URL', 'PIXEL_ID', 'PROMO_END', 'PROMO_PRICE', 'REGULAR_PRICE', 'GUARANTEE_DAYS', 'BONUS_RELEASE_DAY', 'SUPPORT_EMAIL', 'SITE_URL'];
const vazio = (v) => v === undefined || v === null || String(v).trim() === '';
const erros = [];
for (const k of OBRIGATORIOS) if (vazio(cfg[k])) erros.push(`Campo obrigatório vazio em site.config.json: ${k}`);
if (typeof cfg.SHOW_BONUS_VALUES !== 'boolean') erros.push('SHOW_BONUS_VALUES precisa ser true ou false');
if (cfg.SHOW_BONUS_VALUES) {
  for (const b of ['brincadeiras', 'sobras', 'economica']) {
    if (vazio(cfg.BONUS_VALUES?.[b])) erros.push(`SHOW_BONUS_VALUES está true, mas falta BONUS_VALUES.${b}`);
  }
}
if (!vazio(cfg.PROMO_END) && isNaN(Date.parse(cfg.PROMO_END))) erros.push('PROMO_END inválido. Use o formato 2026-11-30T23:59:59-03:00');
if (!vazio(cfg.CHECKOUT_URL) && !/^https:\/\//.test(cfg.CHECKOUT_URL)) erros.push('CHECKOUT_URL precisa começar com https://');
if (!vazio(cfg.PIXEL_ID) && !/^\d{10,20}$/.test(cfg.PIXEL_ID)) erros.push('PIXEL_ID precisa ter só números');
for (const k of ['PROMO_PRICE', 'REGULAR_PRICE']) if (!vazio(cfg[k]) && !/^\d+,\d{2}$/.test(cfg[k])) erros.push(`${k} precisa estar no formato 19,90`);
if (erros.length) falhar(erros);

// ---------- 2. valores derivados ----------
const num = (s) => Number(String(s).replace('.', '').replace(',', '.'));
const brl = (n) => n.toFixed(2).replace('.', ',');
const fim = new Date(cfg.PROMO_END);
const fimLabel = new Intl.DateTimeFormat('pt-BR', { day: '2-digit', month: '2-digit', timeZone: 'America/Sao_Paulo' }).format(fim);
const somaSeparados = brl(num(cfg.REGULAR_PRICE) + ['brincadeiras', 'sobras', 'economica'].reduce((t, b) => t + num(cfg.BONUS_VALUES?.[b] || '0'), 0));

const pixel = `<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '${cfg.PIXEL_ID}');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=${cfg.PIXEL_ID}&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->`;

const siteJs = `<script>window.SITE=${JSON.stringify({
  checkoutUrl: cfg.CHECKOUT_URL,
  promoEnd: cfg.PROMO_END,
  promoPrice: cfg.PROMO_PRICE,
  regularPrice: cfg.REGULAR_PRICE,
  installments: cfg.INSTALLMENTS_TEXT || '',
})};</script>`;

const tokens = {
  CHECKOUT_URL: cfg.CHECKOUT_URL,
  PROMO_PRICE: cfg.PROMO_PRICE,
  REGULAR_PRICE: cfg.REGULAR_PRICE,
  PROMO_END_LABEL: fimLabel,
  GUARANTEE_DAYS: cfg.GUARANTEE_DAYS,
  BONUS_RELEASE_DAY: cfg.BONUS_RELEASE_DAY,
  SUPPORT_EMAIL: cfg.SUPPORT_EMAIL,
  SITE_URL: cfg.SITE_URL,
  INSTALLMENTS_TEXT: cfg.INSTALLMENTS_TEXT || '',
  VAL_BRINCADEIRAS: cfg.BONUS_VALUES?.brincadeiras || '',
  VAL_SOBRAS: cfg.BONUS_VALUES?.sobras || '',
  VAL_ECONOMICA: cfg.BONUS_VALUES?.economica || '',
  VAL_TOTAL_SEPARADOS: somaSeparados,
};

// ---------- 3. gera dist/ ----------
fs.rmSync(DIST, { recursive: true, force: true });
const copiar = (de, para) => {
  for (const nome of fs.readdirSync(de)) {
    const a = path.join(de, nome), b = path.join(para, nome);
    if (fs.statSync(a).isDirectory()) { fs.mkdirSync(b, { recursive: true }); copiar(a, b); continue; }
    if (!a.endsWith('.html')) { fs.copyFileSync(a, b); continue; }
    let h = fs.readFileSync(a, 'utf8');
    h = h.replace('<!--@PIXEL@-->', pixel).replace('<!--@SITE@-->', siteJs);
    // blocos que só existem com SHOW_BONUS_VALUES=true
    h = h.replace(/<!--@SE_VALORES@-->([\s\S]*?)<!--@FIM_SE_VALORES@-->/g, (_, bloco) => (cfg.SHOW_BONUS_VALUES ? bloco : ''));
    // parcelamento só aparece se houver texto
    h = h.replace(/<!--@SE_PARCELAS@-->([\s\S]*?)<!--@FIM_SE_PARCELAS@-->/g, (_, bloco) => (cfg.INSTALLMENTS_TEXT ? bloco : ''));
    h = h.replace(/\{\{([A-Z_]+)\}\}/g, (m, k) => (k in tokens ? tokens[k] : m));
    fs.writeFileSync(b, h);
  }
};
fs.mkdirSync(DIST, { recursive: true });
copiar(SRC, DIST);

// ---------- 4. controle de qualidade do que foi publicado ----------
const PROIBIDOS = [/PREENCHER/i, /lorem/i, /XXX/, /TODO/, /1152510153974851/, /álcool/i, /alcool/i, /alcoólica/i, /\{\{[A-Z_]+\}\}/, /<!--@[A-Z_]+@-->/];
const achados = [];
const varrer = (dir) => {
  for (const nome of fs.readdirSync(dir)) {
    const f = path.join(dir, nome);
    if (fs.statSync(f).isDirectory()) { varrer(f); continue; }
    if (!/\.(html|css|js|json|txt|xml|svg)$/.test(f)) continue;
    const t = fs.readFileSync(f, 'utf8');
    for (const re of PROIBIDOS) if (re.test(t)) achados.push(`${path.relative(DIST, f)} contém ${re}`);
  }
};
varrer(DIST);
if (achados.length) falhar(achados);

console.log(`✔ Build ok → dist/ (Pixel ${cfg.PIXEL_ID}, promoção até ${fimLabel}, valores dos bônus ${cfg.SHOW_BONUS_VALUES ? 'visíveis' : 'ocultos'})`);
