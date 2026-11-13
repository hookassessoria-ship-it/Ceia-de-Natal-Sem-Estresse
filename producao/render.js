// Renderiza os criativos a partir dos HTMLs em producao/imagens e producao/videos.
//   node producao/render.js imagens [C01 C02 ...]   -> criativos/imagens/Cxx.png (1080x1350)
//   node producao/render.js videos  [C13 ...]       -> criativos/videos/Cxx.mp4 (1080x1920, H.264, 30 fps)
// Cada HTML de vídeo expõe window.DURACAO (s) e window.render(t), que desenha o quadro do instante t.
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..');
const FPS = 30;

async function renderImagens(browser, ids) {
  const dir = path.join(__dirname, 'imagens');
  const out = path.join(ROOT, 'criativos', 'imagens');
  fs.mkdirSync(out, { recursive: true });
  const files = fs.readdirSync(dir).filter(f => f.endsWith('.html') && (!ids.length || ids.includes(f.slice(0, 3))));
  // <meta name="formatos" content="45,916"> gera também a versão vertical (Cxx_9x16.png). Sem a meta, só 4:5.
  const TAM = { '45': [1080, 1350, ''], '916': [1080, 1920, '_9x16'] };
  for (const f of files.sort()) {
    const sonda = await browser.newPage();
    await sonda.goto('file://' + path.join(dir, f));
    const fmts = (await sonda.evaluate(() => (document.querySelector('meta[name=formatos]') || {}).content || '45')).split(',');
    await sonda.close();
    for (const fm of fmts) {
      const [w, h, suf] = TAM[fm.trim()];
      const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
      await page.goto('file://' + path.join(dir, f) + '#' + fm.trim());
      await page.evaluate(() => document.fonts.ready);
      await page.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; }))));
      await page.waitForTimeout(300);
      const dest = path.join(out, f.replace('.html', suf + '.png'));
      await page.screenshot({ path: dest, type: 'png' });
      await page.close();
      console.log('ok', path.relative(ROOT, dest));
    }
  }
}

async function renderVideo(browser, file) {
  const dir = path.join(__dirname, 'videos');
  const out = path.join(ROOT, 'criativos', 'videos');
  fs.mkdirSync(out, { recursive: true });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 });
  await page.goto('file://' + path.join(dir, file));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 1 : new Promise(r => { i.onload = i.onerror = r; }))));
  await page.waitForTimeout(400);
  const dur = await page.evaluate(() => window.DURACAO);
  const frames = Math.round(dur * FPS);
  const dest = path.join(out, file.replace('.html', '.mp4'));
  // window.SEM_AUDIO = true gera o MP4 sem nenhuma faixa de áudio (C21 em diante); os antigos têm faixa silenciosa.
  const semAudio = await page.evaluate(() => !!window.SEM_AUDIO);
  const entradaAudio = semAudio ? [] : ['-f', 'lavfi', '-i', 'anullsrc=channel_layout=stereo:sample_rate=48000'];
  const mapa = semAudio ? ['-an'] : ['-map', '0:v', '-map', '1:a', '-shortest', '-c:a', 'aac', '-b:a', '128k'];
  const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error',
    '-f', 'image2pipe', '-framerate', String(FPS), '-i', '-',
    ...entradaAudio, ...mapa,
    '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-preset', 'medium', '-crf', '19', '-r', String(FPS),
    '-movflags', '+faststart', dest]);
  ff.stderr.on('data', d => process.stderr.write(d));
  const done = new Promise((res, rej) => ff.on('close', c => c === 0 ? res() : rej(new Error('ffmpeg ' + c))));
  for (let i = 0; i < frames; i++) {
    await page.evaluate(t => window.render(t), i / FPS);
    const buf = await page.screenshot({ type: 'jpeg', quality: 93 });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  }
  ff.stdin.end();
  await done;
  await page.close();
  console.log('ok', path.relative(ROOT, dest), `${dur}s`, frames, 'quadros');
}

(async () => {
  const [, , kind, ...ids] = process.argv;
  const browser = await chromium.launch();
  if (kind === 'imagens') await renderImagens(browser, ids);
  else if (kind === 'videos') {
    const dir = path.join(__dirname, 'videos');
    const files = fs.readdirSync(dir).filter(f => /^C\d\d.*\.html$/.test(f) && (!ids.length || ids.includes(f.slice(0, 3)))).sort();
    for (const f of files) await renderVideo(browser, f);
  } else if (kind === 'quadro') {
    // node producao/render.js quadro C13 4.5 saida.jpg  -> um quadro para conferência
    const [id, t, outFile] = ids;
    const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
    const f = fs.readdirSync(path.join(__dirname, 'videos')).find(x => x.startsWith(id));
    await page.goto('file://' + path.join(__dirname, 'videos', f));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForTimeout(300);
    for (const tt of t.split(',')) {
      await page.evaluate(x => window.render(x), Number(tt));
      await page.screenshot({ path: outFile.replace('.jpg', `-${tt}.jpg`), type: 'jpeg', quality: 80 });
    }
  }
  await browser.close();
})();
