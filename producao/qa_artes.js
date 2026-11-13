// QA das artes C21+: extrai o texto visível (sem as páginas reais do PDF, que são imagens), conta palavras
// e procura termos proibidos. Uso: node producao/qa_artes.js
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const PROIBIDOS = [/\bcasad/i, /marido/i, /esposa/i, /solteir/i, /sozinh/i, /trist/i, /solid/i, /viúv/i, /\bpena\b/i, /anfitriã/i,
  /cliente/i, /disse que/i, /\d+ ?%/, /nunca mais/i, /garant(?!ia)/i, /últim[ao]s/i, /vagas/i, /só hoje/i, /papai noel/i,
  /estressad/i, /cansad/i, /você não vai acreditar/i, /⭐/, /estrela/i];
const PRECO_OK = /^R\$ ?19,90$/;

(async () => {
  const browser = await chromium.launch();
  const itens = [];
  for (const [pasta, ids] of [['imagens', ['C21', 'C22', 'C23', 'C25', 'C26', 'C28', 'C29', 'C31']], ['videos', ['C24', 'C27', 'C30', 'C32']]]) {
    for (const id of ids) {
      const page = await browser.newPage({ viewport: { width: 1080, height: pasta === 'imagens' ? 1350 : 1920 } });
      await page.goto('file://' + path.join(__dirname, pasta, id + '.html') + '#45');
      await page.evaluate(() => document.fonts.ready);
      // nos vídeos, o texto de todas as cenas existe no DOM; pega tudo
      const txt = await page.evaluate(() => {
        const out = [];
        const walk = n => { n.childNodes.forEach(c => { if (c.nodeType === 3 && c.textContent.trim()) out.push(c.textContent.trim()); else if (c.nodeType === 1 && !['SCRIPT', 'STYLE'].includes(c.tagName)) walk(c); }); };
        walk(document.body);
        return out.join(' ').replace(/\s+/g, ' ');
      });
      const palavras = txt.split(' ').filter(w => /[\p{L}\d]/u.test(w)).length;
      const ruins = PROIBIDOS.filter(r => r.test(txt)).map(String);
      const precos = (txt.match(/R\$ ?\d+(?:,\d{2})?/g) || []).filter(p => !PRECO_OK.test(p));
      itens.push({ id, formato: pasta, palavras, texto: txt, problemas: [...ruins, ...precos] });
      await page.close();
    }
  }
  await browser.close();
  let falhou = false;
  for (const i of itens) {
    console.log(`${i.id} [${i.formato}] ${i.palavras} palavras ${i.problemas.length ? 'PROBLEMA: ' + i.problemas.join(', ') : 'ok'}\n   "${i.texto}"`);
    if (i.problemas.length) falhou = true;
  }
  fs.writeFileSync(path.join(__dirname, 'qa_artes.json'), JSON.stringify(itens, null, 1));
  process.exit(falhou ? 1 : 0);
})();
