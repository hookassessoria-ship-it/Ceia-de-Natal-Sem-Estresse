"""QA dos vídeos com voz: faixas, durações, loudness, pico, tamanho e termos proibidos.

    python3 producao/audio/qa.py   -> imprime a tabela e grava criativos/videos/com-audio/qa.md
"""
import json
import re
import subprocess
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
PASTAS = [RAIZ / 'criativos/videos/com-audio', RAIZ / 'criativos/videos/vsl']
PROIBIDOS = [r'álcool', r'alcool', r'bebida', r'cerveja', r'vinho', r'estrela', r'só hoje', r'e-mail', r'email', r'cnpj',
             r'\bpresa\b', r'sozinha', r'\bmãe\b', r'50 ?%', r'desconto']


def probe(f):
    r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type,codec_name,width,height,sample_rate,channels,duration',
                        '-of', 'json', str(f)], capture_output=True, text=True)
    return json.loads(r.stdout)['streams']


def loud(f):
    r = subprocess.run(['ffmpeg', '-hide_banner', '-i', str(f), '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True)
    i = float(re.findall(r'I:\s+(-?[\d.]+) LUFS', r.stderr)[-1])
    tp = float(re.findall(r'Peak:\s+(-?[\d.]+) dBFS', r.stderr)[-1])
    return i, tp


linhas = ['| Arquivo | Vídeo | Áudio | Duração v/a (s) | LUFS | Pico (dBTP) | Tamanho |', '|---|---|---|---|---|---|---|']
erros = []
for pasta in PASTAS:
    for f in sorted(pasta.glob('*.mp4')):
        s = probe(f)
        v = next((x for x in s if x['codec_type'] == 'video'), None)
        a = next((x for x in s if x['codec_type'] == 'audio'), None)
        mb = f.stat().st_size / 1e6
        if not a:
            erros.append(f'{f.name}: sem áudio')
            continue
        dv, da = float(v['duration']), float(a['duration'])
        i, tp = loud(f)
        if abs(dv - da) > 0.1:
            erros.append(f'{f.name}: vídeo {dv:.2f}s x áudio {da:.2f}s')
        if tp > -1.0:
            erros.append(f'{f.name}: pico {tp} dBTP')
        if mb > 30:
            erros.append(f'{f.name}: {mb:.1f} MB')
        linhas.append(f"| {f.relative_to(RAIZ)} | {v['codec_name']} {v['width']}x{v['height']} | {a['codec_name']} {a['sample_rate']} Hz {a['channels']} ch | "
                      f"{dv:.2f} / {da:.2f} | {i:.1f} | {tp:.1f} | {mb:.1f} MB |")
# termos proibidos nos roteiros e textos
textos = [RAIZ / 'criativos/videos/com-audio/roteiros.md', RAIZ / 'producao/audio/roteiro.py', RAIZ / 'anuncios-novos-videos.md',
          RAIZ / 'textos-anuncios.csv', *sorted((RAIZ / 'producao/videos').glob('C3[34]*.html')), RAIZ / 'producao/videos/VSL.html']
achados = []
for t in textos:
    if not t.exists():
        continue
    for n, l in enumerate(t.read_text(encoding='utf-8').splitlines(), 1):
        for p in PROIBIDOS:
            if re.search(p, l, re.I):
                achados.append(f'{t.relative_to(RAIZ)}:{n} [{p}] {l.strip()[:110]}')
out = '\n'.join(linhas)
out += '\n\n**Erros:** ' + ('nenhum' if not erros else '; '.join(erros))
out += '\n\n**Termos da lista de bloqueio encontrados (conferir contexto):**\n' + ('\n'.join(f'- {a}' for a in achados) if achados else 'nenhum')
print(out)
(RAIZ / 'criativos/videos/com-audio/qa.md').write_text('# QA técnico dos vídeos com voz\n\nGerado por `producao/audio/qa.py`.\n\n' + out + '\n', encoding='utf-8')
