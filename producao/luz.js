// Luz quente gerada por código (bokeh de velas e pisca-pisca), determinística: mesmo resultado a cada render.
// formato(): lê o hash (#45 ou #916) e aplica a classe no body. luz(canvas, opções, t) desenha o quadro do instante t.
function formato() {
  const f = (location.hash || '#45').slice(1);
  document.body.classList.add(f === '916' ? 'f916' : 'f45');
  return f;
}
function semente(s) { return () => { s = (s * 16807) % 2147483647; return (s - 1) / 2147483646; }; }
function luz(cv, o = {}, t = 0) {
  const W = cv.width = document.body.clientWidth, H = cv.height = document.body.clientHeight;
  const c = cv.getContext('2d');
  c.clearRect(0, 0, W, H);
  c.globalCompositeOperation = 'lighter';
  const r = semente(o.semente || 7);
  const cores = o.cores || [[242, 184, 128], [232, 211, 162], [255, 214, 160], [201, 164, 92]];
  const n = o.n || 34;
  const faixa = o.faixa || [0, 1];
  // brilhos grandes e suaves (velas fora de foco)
  (o.brilhos || []).forEach(([x, y, raio, a]) => {
    const fl = 1 + 0.06 * Math.sin(t * 7.3 + x) + 0.04 * Math.sin(t * 13.1 + y);
    const g = c.createRadialGradient(x * W, y * H, 0, x * W, y * H, raio * fl);
    g.addColorStop(0, `rgba(255,196,128,${a})`);
    g.addColorStop(0.35, `rgba(242,160,90,${a * 0.45})`);
    g.addColorStop(1, 'rgba(242,160,90,0)');
    c.fillStyle = g; c.fillRect(0, 0, W, H);
  });
  for (let i = 0; i < n; i++) {
    const cor = cores[Math.floor(r() * cores.length)];
    const x = r() * W + Math.sin(t * 0.35 + i) * (o.deriva ?? 14);
    const y = (faixa[0] + r() * (faixa[1] - faixa[0])) * H + Math.cos(t * 0.28 + i * 1.7) * (o.deriva ?? 14);
    const raio = (o.min || 18) + r() * ((o.max || 90) - (o.min || 18));
    const a = (o.alfa || 0.22) * (0.45 + r() * 0.55) * (1 + 0.12 * Math.sin(t * (1.5 + r() * 2) + i));
    const g = c.createRadialGradient(x, y, 0, x, y, raio);
    g.addColorStop(0, `rgba(${cor},${a * 0.55})`);
    g.addColorStop(0.72, `rgba(${cor},${a * 0.7})`);
    g.addColorStop(0.9, `rgba(${cor},${a})`);
    g.addColorStop(1, `rgba(${cor},0)`);
    c.fillStyle = g;
    c.beginPath(); c.arc(x, y, raio, 0, Math.PI * 2); c.fill();
  }
  c.globalCompositeOperation = 'source-over';
}
