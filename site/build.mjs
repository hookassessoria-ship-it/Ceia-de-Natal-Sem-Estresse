// Build do site Cantinho do Lar: lê site.config.json, valida, injeta valores e gera dist/.
// Uso: node build.mjs   (sem dependências)
import fs from 'node:fs';
import crypto from 'node:crypto';
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
  for (const b of ['brincadeiras', 'sobras', 'economica', 'ceia_medida']) {
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
const somaSeparados = brl(num(cfg.REGULAR_PRICE) + ['brincadeiras', 'sobras', 'economica', 'ceia_medida'].reduce((t, b) => t + num(cfg.BONUS_VALUES?.[b] || '0'), 0));

const pixel = `<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];
/* fila do fbq criada já no início (PageView entra na fila agora); o arquivo do Meta baixa
   logo depois do carregamento da página, para não disputar com a primeira dobra */
var carregar=function(){t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)};
if(b.readyState==='complete')carregar();else f.addEventListener('load',carregar,{once:true})}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', '${cfg.PIXEL_ID}');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=${cfg.PIXEL_ID}&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->`;

const pixelNoscript = `<noscript><img height="1" width="1" style="display:none" alt=""
src="https://www.facebook.com/tr?id=${cfg.PIXEL_ID}&ev=PageView&noscript=1"
/></noscript>`;

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
  VAL_MEDIDA: cfg.BONUS_VALUES?.ceia_medida || '',
  VAL_TOTAL_SEPARADOS: somaSeparados,
};

// ---------- 3. gera dist/ ----------
fs.rmSync(DIST, { recursive: true, force: true });
// ---------- fontes próprias (sem CSS externo bloqueando a renderização) + versão nos arquivos estáticos ----------
const versoes = new Map();
const versao = (rel) => {
  if (!versoes.has(rel)) {
    const f = path.join(SRC, rel);
    versoes.set(rel, fs.existsSync(f) ? crypto.createHash('md5').update(fs.readFileSync(f)).digest('hex').slice(0, 8) : null);
  }
  return versoes.get(rel);
};
const comVersao = (rel) => { const v = versao(rel); return v ? `${rel}?v=${v}` : rel; };
const FONTES = `<link rel="preload" href="fontes/nunito.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fontes/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<style>
@font-face{font-family:"Fraunces";font-style:normal;font-weight:500 700;font-display:swap;src:url(fontes/fraunces.woff2) format("woff2")}
@font-face{font-family:"Fraunces";font-style:italic;font-weight:500 600;font-display:swap;src:url(fontes/fraunces-italico.woff2) format("woff2")}
@font-face{font-family:"Nunito";font-style:normal;font-weight:400 800;font-display:swap;src:url(fontes/nunito.woff2) format("woff2")}
</style>`;
const otimizar = (h) => {
  h = h.replace(/<link rel="preconnect" href="https:\/\/fonts\.(googleapis|gstatic)\.com"[^>]*>\s*/g, '');
  h = h.replace(/<link href="https:\/\/fonts\.googleapis\.com\/css2[^"]*" rel="stylesheet">/g, FONTES);
  h = h.replace(/((?:src|href|poster|data-src)=")((?:imagens|videos|fontes)\/[^"?#]+)"/g, (_, at, rel) => `${at}${comVersao(rel)}"`);
  h = h.replace(/(srcset=")([^"]+)"/g, (_, at, lista) => at + lista.replace(/((?:imagens|videos)\/[^\s,?]+)/g, (r) => comVersao(r)) + '"');
  h = h.replace(/url\(((?:imagens|videos|fontes)\/[^)?]+)\)/g, (_, rel) => `url(${comVersao(rel)})`);
  return h;
};

const copiar = (de, para) => {
  for (const nome of fs.readdirSync(de)) {
    const a = path.join(de, nome), b = path.join(para, nome);
    if (fs.statSync(a).isDirectory()) { fs.mkdirSync(b, { recursive: true }); copiar(a, b); continue; }
    if (!a.endsWith('.html')) { fs.copyFileSync(a, b); continue; }
    let h = fs.readFileSync(a, 'utf8');
    h = h.replace('<!--@PIXEL_NOSCRIPT@-->', pixelNoscript)
    h = h.replace('<!--@PIXEL@-->', pixel).replace('<!--@SITE@-->', siteJs);
    // blocos que só existem com SHOW_BONUS_VALUES=true
    h = h.replace(/<!--@SE_VALORES@-->([\s\S]*?)<!--@FIM_SE_VALORES@-->/g, (_, bloco) => (cfg.SHOW_BONUS_VALUES ? bloco : ''));
    // parcelamento só aparece se houver texto
    h = h.replace(/<!--@SE_PARCELAS@-->([\s\S]*?)<!--@FIM_SE_PARCELAS@-->/g, (_, bloco) => (cfg.INSTALLMENTS_TEXT ? bloco : ''));
    h = h.replace(/\{\{([A-Z_]+)\}\}/g, (m, k) => (k in tokens ? tokens[k] : m));
    h = otimizar(h);
    fs.writeFileSync(b, h);
  }
};
fs.mkdirSync(DIST, { recursive: true });
copiar(SRC, DIST);

// ---------- 4. controle de qualidade do que foi publicado ----------
const PROIBIDOS = [/(?<![0-9])3 bônus|três bônus/i, /PREENCHER/i, /lorem/i, /XXX/, /TODO/, /1152510153974851/, /álcool/i, /alcool/i, /alcoólica/i, /\{\{[A-Z_]+\}\}/, /<!--@[A-Z_]+@-->/, /fonts\.googleapis\.com/, /ViewContent|InitiateCheckout|'Purchase'|AddToCart/];
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
for (const nome of fs.readdirSync(DIST).filter((n) => n.endsWith('.html'))) {
  const h = fs.readFileSync(path.join(DIST, nome), 'utf8');
  if (h.includes('x_f=atob') && h.includes("fbq('init'")) achados.push(`${nome}: Meta Pixel do site junto com o Pixel da Utmify (duplicado)`);
}
if (achados.length) falhar(achados);

console.log(`✔ Build ok → dist/ (Pixel ${cfg.PIXEL_ID}, promoção até ${fimLabel}, valores dos bônus ${cfg.SHOW_BONUS_VALUES ? 'visíveis' : 'ocultos'})`);
