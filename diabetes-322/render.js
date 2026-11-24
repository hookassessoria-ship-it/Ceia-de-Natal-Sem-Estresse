// Renderiza a capa provisória e os criativos D01-D05 (1080x1350).
//   node diabetes-322/render.js
// Se existir capa/capa-original.png (a capa real), ela é usada e os arquivos saem como D0x.png.
// Sem ela, usa a capa provisória e os arquivos saem como D0x_capa-provisoria.png.
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const D = __dirname;
(async () => {
  const b = await chromium.launch();
  const shot = async (html, w, h, out) => {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    await p.goto('file://' + path.join(D, 'html', html));
    await p.evaluate(() => document.fonts.ready);
    await p.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; }))));
    await p.waitForTimeout(300);
    await p.screenshot({ path: out, type: 'png' });
    await p.close();
  };
  await shot('capa-provisoria.html', 900, 1260, path.join(D, 'capa', 'capa-provisoria.png'));
  const original = path.join(D, 'capa', 'capa-original.png');
  const usaOriginal = fs.existsSync(original);
  fs.copyFileSync(usaOriginal ? original : path.join(D, 'capa', 'capa-provisoria.png'), path.join(D, 'capa', 'capa-atual.png'));
  for (const id of ['D01', 'D02', 'D03', 'D04', 'D05', 'D06']) {
    const out = path.join(D, 'criativos', id + (usaOriginal ? '' : '_capa-provisoria') + '.png');
    await shot(id + '.html', 1080, 1350, out);
    console.log('ok', path.relative(D, out));
  }
  await b.close();
})();
