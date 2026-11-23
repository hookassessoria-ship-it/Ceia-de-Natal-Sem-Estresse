"""Mixa voz + efeitos + trilha nos vídeos e queima legenda palavra por palavra.

    python3 producao/audio/mixar.py C15 C16 ...     (ou sem argumentos: todos do ROTEIRO)

Saída: criativos/videos/com-audio/Cxx_voz.mp4 (H.264 + AAC 48 kHz estéreo, -14 LUFS, pico -1 dBTP).
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
import trilha  # noqa: E402
from roteiro import ROTEIRO  # noqa: E402

SR = 48000
RAIZ = Path(__file__).resolve().parents[2]
VOZES = RAIZ / 'producao/audio/vozes'
SFX = RAIZ / 'producao/audio/sfx'
SAIDA = RAIZ / 'criativos/videos/com-audio'


def sh(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stderr[-2000:])
    return r


def ler(caminho, filtros=None):
    cmd = ['ffmpeg', '-v', 'error', '-i', str(caminho)]
    if filtros:
        cmd += ['-af', filtros]
    cmd += ['-f', 'f32le', '-ac', '2', '-ar', str(SR), '-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, dtype='<f4').reshape(-1, 2).copy()


def lufs(sinal):
    with tempfile.NamedTemporaryFile(suffix='.wav') as f:
        trilha.salvar(np.clip(sinal, -1, 1), f.name)
        r = sh(['ffmpeg', '-hide_banner', '-i', f.name, '-af', 'ebur128', '-f', 'null', '-'])
    m = re.findall(r'I:\s+(-?[\d.]+) LUFS', r.stderr)
    return float(m[-1]) if m else -70.0


def db(x):
    return 10 ** (x / 20)


# ---------- efeitos sintetizados (whoosh, pop) ----------
def whoosh(d=0.45):
    n = int(d * SR)
    t = np.arange(n) / SR
    ruido = np.random.default_rng(3).standard_normal(n)
    # varredura: filtra com média móvel de tamanho decrescente
    out = np.zeros(n)
    for i, k in enumerate(np.linspace(40, 4, 8).astype(int)):
        seg = slice(i * n // 8, (i + 1) * n // 8)
        out[seg] = np.convolve(ruido, np.ones(k) / k, mode='same')[seg]
    env = np.sin(np.pi * t / d) ** 2
    s = out * env * 0.5
    return np.stack([s * np.linspace(0.3, 1, n), s * np.linspace(1, 0.3, n)], 1)


def pop(f=880, d=0.12):
    n = int(d * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * f * t * (1 + 0.6 * np.exp(-t * 40))) * np.exp(-t * 35) * 0.5
    return np.stack([s, s], 1)


def carregar_sfx(nome, dur=None, loop_ate=None):
    if nome == 'whoosh':
        s = whoosh()
    elif nome == 'pop':
        s = pop()
    elif nome == 'pop2':
        s = pop(660)
    elif nome == 'encaixe':  # clique de encaixe: batida grave curta + estalo
        n = int(0.09 * SR); t = np.arange(n) / SR
        b = (np.sin(2 * np.pi * 140 * t) * np.exp(-t * 60) + 0.5 * np.sin(2 * np.pi * 2400 * t) * np.exp(-t * 160)) * 0.6
        s = np.stack([b, b], 1)
    elif nome == 'confirma':  # duas notas subindo (som de confirmação)
        a, b = pop(880, 0.18), pop(1320, 0.3)
        s = np.zeros((len(a) // 2 + len(b), 2)); s[:len(a)] += a; s[len(a) // 2:] += b
    else:
        s = ler(SFX / f'{nome}.mp3')
    if dur:
        s = s[: int(dur * SR)]
    if loop_ate:
        # repete com crossfade até cobrir loop_ate segundos
        alvo = int(loop_ate * SR)
        cf = int(0.25 * SR)
        out = s.copy()
        while len(out) < alvo:
            a = out[:-cf]
            b = out[-cf:] * np.linspace(1, 0, cf)[:, None] + s[:cf] * np.linspace(0, 1, cf)[:, None]
            out = np.concatenate([a, b, s[cf:]])
        s = out[:alvo]
    fade = min(len(s) // 4, int(0.08 * SR))
    if fade:
        s[:fade] *= np.linspace(0, 1, fade)[:, None]
        s[-fade:] *= np.linspace(1, 0, fade)[:, None]
    return s


def processar_voz(clip, tempo):
    filtros = ('silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.05,'
               'areverse,silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse,'
               'highpass=f=80,deesser=i=0.4,acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120:makeup=2')
    if abs(tempo - 1) > 1e-3:
        filtros += f',atempo={tempo}'
    return ler(VOZES / f'{clip}.mp3', filtros)


EXPANDE = {'R$': 'reais', '19,90': 'dezenove e noventa', '300': 'trezentas', '24': 'vinte e quatro', '23': 'vinte e três',
           '21': 'vinte e um', '17': 'dezessete', '25': 'vinte e cinco', '10': 'dez', '30': 'trinta', '9': 'nove', '6': 'seis',
           '5': 'cinco', '3': 'três', '2': 'dois', '8': 'oito', '1': 'um', '23h30': 'onze e meia', 'nº': 'número',
           '7': 'sete', '15': 'quinze', '18h30': 'dezoito e trinta', '22': 'vinte e dois'}


def tempos_palavras(texto, dur):
    """Divide a duração do clipe entre as palavras, proporcional ao tamanho falado, com respiros na pontuação."""
    toks, quebras = [], set()
    for t in texto.split():
        if t == '|':
            quebras.add(len(toks) - 1)
        else:
            toks.append(t)
    pesos = []
    for t in toks:
        base = re.sub(r'[^\wÀ-ÿ$,]', '', t).strip(',')
        pesos.append(len(EXPANDE.get(base, base)) + 2)
        pesos.append(7 if t.endswith('...') else 4 if t[-1] in '.?!:' else 2.5 if t.endswith(',') else 0)
    total = sum(pesos)
    out, acc = [], 0.0
    for i, t in enumerate(toks):
        ini = acc / total * dur
        acc += pesos[2 * i]
        fim = acc / total * dur
        acc += pesos[2 * i + 1]
        out.append((t, ini, fim, i in quebras or i == len(toks) - 1))
    return out


def ass_cabecalho():
    return """[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Leg,Inter,58,&H0080B8F2,&H00FFFFFF,&H00190F0A,&H00190F0A,-1,0,0,0,100,100,0,0,3,14,0,2,110,110,{mv},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ts(t):
    t = max(0, t)
    h, r = divmod(t, 3600)
    m, s = divmod(r, 60)
    return f'{int(h)}:{int(m):02d}:{s:05.2f}'


def legendas(eventos, mv):
    linhas = [ass_cabecalho().replace('{mv}', str(mv))]
    for palavras in eventos:
        # blocos de até 4 palavras, quebrando em pontuação
        bloco = []
        blocos = []
        manual = any(p[3] for p in palavras[:-1])
        for p in palavras:
            bloco.append(p)
            if (manual and p[3]) or (not manual and (len(bloco) >= 4 or p[0][-1] in '.?!:' or p[0].endswith('...'))):
                blocos.append(bloco)
                bloco = []
        if bloco:
            blocos.append(bloco)
        for i, b in enumerate(blocos):
            ini = b[0][1] - 0.05
            fim = (blocos[i + 1][0][1] - 0.02) if i + 1 < len(blocos) else b[-1][2] + 0.35
            txt = ''
            prev = ini
            for w, a, z, _q in b:
                cs = max(1, int(round((z - prev) * 100)))
                txt += f'{{\\k{cs}}}{w} '
                prev = z
            linhas.append(f'Dialogue: 0,{ts(ini)},{ts(fim)},Leg,,0,0,0,,{txt.strip()}')
    return '\n'.join(linhas) + '\n'


def inverso(mapa, t_orig):
    for (a0, b0), (a1, b1) in zip(mapa, mapa[1:]):
        if t_orig <= b1:
            return a0 + (a1 - a0) * (t_orig - b0) / max(1e-6, b1 - b0)
    return mapa[-1][0]


def mixar(vid):
    cfg = ROTEIRO[vid]
    video = RAIZ / cfg['video']
    dur_video = float(sh(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', str(video)]).stdout)
    # 1) voz
    faixas, fim_ant, eventos = [], 0.0, []
    for fala in cfg['falas']:
        s = processar_voz(fala['clip'], fala.get('tempo', 1.0))
        ini = max(fala['em'], fim_ant + fala.get('respiro', 0.2))
        faixas.append((ini, s))
        d = len(s) / SR
        eventos.append([(w, ini + a, ini + z, q) for w, a, z, q in tempos_palavras(fala['legenda'], d)])
        fim_ant = ini + d
    dur = max(dur_video, fim_ant + cfg.get('cauda', 0.9))
    # mapa de tempo: cada cena começa quando começa a fala dela (o vídeo é re-renderizado esticado)
    mapa = [[0.0, 0.0]]
    for fala, (ini, _s) in zip(cfg['falas'], faixas):
        o, sa = fala.get('cena', fala['em']), max(0.0, ini - 0.15)
        if o > mapa[-1][1] + 0.05 and sa > mapa[-1][0] + 0.05:
            mapa.append([max(sa, mapa[-1][0] + (o - mapa[-1][1]) * 0.6), o])
    resto = dur_video - mapa[-1][1]
    dur = max(dur, mapa[-1][0] + resto)
    mapa.append([dur, dur_video])
    n = int(dur * SR)
    voz = np.zeros((n, 2))
    for ini, s in faixas:
        k = int(ini * SR)
        voz[k:k + len(s)] += s[: n - k]
    voz *= db(-16 - lufs(voz))  # voz em ~ -16 LUFS antes da mix
    # 2) efeitos
    fx = np.zeros((n, 2))
    for e in cfg.get('sfx', []):
        s = carregar_sfx(e['nome'], e.get('dur'), e.get('loop_ate'))
        t_fx = inverso(mapa, e['cena']) if 'cena' in e else e['em']
        k = int(t_fx * SR)
        fx[k:k + len(s)] += s[: max(0, n - k)] * db(e.get('ganho', 0))
    if np.abs(fx).max() > 0:
        pico_fx = np.abs(fx).max()
        fx *= db(-14) / pico_fx  # pico dos efeitos 10 dB abaixo do fundo de escala, ajustado pelos ganhos relativos
    # 3) trilha com ducking
    mus = trilha.gerar(dur, cfg.get('semente', 1))[:n]
    mus *= db(lufs(voz) - cfg.get('musica_abaixo', 15.5) - lufs(mus))
    if cfg.get('musica_env'):  # curva de ganho da trilha em dB: [[t, dB], ...] (ex.: música crescente)
        pts = np.array(cfg['musica_env'], dtype=float)
        mus *= db(np.interp(np.arange(n) / SR, pts[:, 0], pts[:, 1]))[:, None]
    env = np.abs(voz).mean(1)
    win = int(0.05 * SR)
    env = np.convolve(env, np.ones(win) / win, mode='same')
    ativo = (env > db(-40)).astype(float)
    rel = int(0.35 * SR)
    ativo = np.convolve(ativo, np.ones(rel) / rel, mode='same')
    ganho_duck = 1 - (1 - db(-cfg.get('ducking', 6))) * np.clip(ativo * 3, 0, 1)
    mus *= ganho_duck[:, None]
    mix = voz + fx + mus
    tmp = Path(tempfile.mkdtemp())
    trilha.salvar(np.clip(mix / max(1, np.abs(mix).max() / 0.95), -1, 1), str(tmp / 'mix.wav'))
    trilha.salvar(np.clip(voz, -1, 1), str(tmp / 'voz.wav'))
    trilha.salvar(np.clip(mus, -1, 1), str(tmp / 'mus.wav'))
    # 4) loudnorm em dois passos: -14 LUFS, -1 dBTP
    r = sh(['ffmpeg', '-hide_banner', '-i', str(tmp / 'mix.wav'), '-af', 'loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json', '-f', 'null', '-'])
    m = json.loads(r.stderr[r.stderr.rfind('{'):])
    ln = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    sh(['ffmpeg', '-y', '-v', 'error', '-i', str(tmp / 'mix.wav'), '-af', ln + ',aresample=48000', '-ar', '48000', str(tmp / 'final.wav')])
    # 5) legenda e vídeo
    (tmp / 'leg.ass').write_text(legendas(eventos, cfg.get('margem_legenda', 320)), encoding='utf-8')
    if cfg.get('warp', True):
        sh(['node', str(RAIZ / 'producao/render.js'), 'warp', vid, json.dumps(mapa), str(tmp / 'video.mp4')])
        video = tmp / 'video.mp4'
        vf = f"subtitles={tmp / 'leg.ass'}"
    else:
        vf = f"tpad=stop_mode=clone:stop_duration={max(0, dur - dur_video):.3f},subtitles={tmp / 'leg.ass'}"
    saida = SAIDA / f'{vid}_voz.mp4'
    SAIDA.mkdir(parents=True, exist_ok=True)
    sh(['ffmpeg', '-y', '-v', 'error', '-i', str(video), '-i', str(tmp / 'final.wav'), '-map', '0:v', '-map', '1:a',
        '-vf', vf, '-t', f'{dur:.3f}', '-c:v', 'libx264', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'medium',
        '-r', '30', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', str(saida)])
    # relatório
    lv, lm = lufs(voz), lufs(mus)
    info = {'mapa': [[round(a, 2), round(b, 2)] for a, b in mapa], 'video': vid, 'duracao': round(dur, 2), 'voz_LUFS': round(lv, 1), 'musica_LUFS': round(lm, 1), 'voz_menos_musica_dB': round(lv - lm, 1)}
    (tmp / 'eventos.json').write_text(json.dumps(eventos, ensure_ascii=False))
    print(json.dumps(info, ensure_ascii=False))
    return info


if __name__ == '__main__':
    for v in (sys.argv[1:] or list(ROTEIRO)):
        mixar(v)
