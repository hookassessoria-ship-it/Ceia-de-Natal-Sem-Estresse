// QA: confere se os elementos importantes das versões 9:16 ficam entre y=250 e y=1580 (zonas seguras de Stories e Reels).
//   node producao/zonas.js C21 C22 ...
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const ids = process.argv.slice(2);
  const browser = await chromium.launch();
  let falhas = 0;
  for (const id of ids) {
    const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
    await page.goto('file://' + path.join(__dirname, 'imagens', id + '.html') + '#916');
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(200);
    const r = await page.evaluate(() => [...document.querySelectorAll('.zona .titulo, .zona .apoio, .zona .olho, .ponte, .zona .bilhete, .zona .grade, .zona .trilha, .zona .detalhe, .zona .cartao, .tag')]
      .map(e => { const b = e.getBoundingClientRect(); return { el: e.className.split(' ')[0], top: Math.round(b.top), bottom: Math.round(b.bottom) }; }));
    const ruins = r.filter(x => x.top < 250 || x.bottom > 1580);
    console.log(id, ruins.length ? 'FORA: ' + JSON.stringify(ruins) : 'ok (' + r.length + ' elementos)');
    falhas += ruins.length;
    await page.close();
  }
  await browser.close();
  process.exit(falhas ? 1 : 0);
})();
