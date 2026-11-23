"""Trilha original sintetizada (sem samples de terceiros, sem melodia conhecida).

Violão dedilhado (síntese aditiva), pad suave, sino leve e escovinha, em Fá maior, 84 BPM,
progressão I-vi-IV-V. Uso: python3 producao/audio/trilha.py <segundos> <saida.wav> [semente]
"""
import sys
import wave
import numpy as np

SR = 48000
BPM = 84
BEAT = 60 / BPM


def nota(m):
    return 440.0 * 2 ** ((m - 69) / 12)


# acordes em MIDI: F, Dm, Bb, C
ACORDES = [[53, 57, 60], [50, 53, 57], [46, 50, 53], [48, 52, 55]]


def env(n, ataque, decaimento):
    t = np.arange(n) / SR
    a = np.minimum(1, t / max(ataque, 1e-3))
    return a * np.exp(-t / decaimento)


def corda(freq, dur, vel):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.zeros(n)
    for k in range(1, 9):
        s += (1 / k ** 1.3) * np.sin(2 * np.pi * freq * k * t) * np.exp(-t * (1.6 + 1.1 * k))
    return vel * s * np.minimum(1, t / 0.004)


def pad(freqs, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.zeros((n, 2))
    for f in freqs:
        for lado, det in ((0, -0.15), (1, 0.15)):
            s[:, lado] += np.sin(2 * np.pi * (f + det) * t) + 0.25 * np.sin(2 * np.pi * 2 * (f + det) * t)
    a = np.minimum(1, t / 0.9) * np.minimum(1, (dur - t) / 0.9)
    return s * a[:, None] * 0.05


def sino(freq, dur):
    n = int(dur * SR)
    t = np.arange(n) / SR
    s = np.sin(2 * np.pi * freq * t) + 0.35 * np.sin(2 * np.pi * freq * 2.76 * t) * np.exp(-t * 3)
    return s * np.exp(-t * 2.2) * 0.12


def gerar(dur, semente=1):
    rng = np.random.default_rng(semente)
    n = int((dur + 2) * SR)
    mix = np.zeros((n, 2))
    compasso = 4 * BEAT
    padrao = [0, 2, 1, 2, 0, 2, 1, 2]  # índices do acorde em colcheias
    c = 0
    t0 = 0.0
    while t0 < dur + 1:
        ac = ACORDES[c % 4]
        i0 = int(t0 * SR)
        p = pad([nota(m) for m in ac], compasso + 0.6)
        mix[i0:i0 + len(p)] += p[: n - i0]
        for j, idx in enumerate(padrao):
            tt = t0 + j * BEAT / 2 + rng.uniform(-0.008, 0.008)
            m = ac[idx] + 12 + (12 if j in (3, 7) else 0)
            s = corda(nota(m), 1.6, rng.uniform(0.10, 0.16) * (1.2 if j == 0 else 1))
            k = max(0, int(tt * SR))
            pan = 0.35 + 0.3 * (j % 2)
            seg = s[: max(0, n - k)]
            mix[k:k + len(seg), 0] += seg * (1 - pan)
            mix[k:k + len(seg), 1] += seg * pan
        # baixo
        b = corda(nota(ac[0] - 12), 2.2, 0.22)
        mix[i0:i0 + len(b), 0] += b[: n - i0] * 0.5
        mix[i0:i0 + len(b), 1] += b[: n - i0] * 0.5
        # escovinha nos tempos 2 e 4
        for bt in (1, 3):
            k = int((t0 + bt * BEAT) * SR)
            ln = int(0.18 * SR)
            ru = rng.standard_normal(ln) * np.exp(-np.arange(ln) / SR / 0.05) * 0.018
            ru = np.diff(np.concatenate([[0], ru]))  # tira graves
            mix[k:k + ln] += ru[: max(0, n - k), None]
        # sino a cada 2 compassos
        if c % 2 == 1:
            s = sino(nota(ac[2] + 36), 2.5)
            k = int((t0 + 2 * BEAT) * SR)
            mix[k:k + len(s), 0] += s[: max(0, n - k)] * 0.6
            mix[k:k + len(s), 1] += s[: max(0, n - k)] * 0.4
        c += 1
        t0 += compasso
    mix = mix[: int(dur * SR)]
    # filtro passa-baixa suave (média móvel) para aquecer
    k = 5
    ker = np.ones(k) / k
    for ch in range(2):
        mix[:, ch] = np.convolve(mix[:, ch], ker, mode='same')
    fi, fo = int(0.6 * SR), int(1.5 * SR)
    mix[:fi] *= np.linspace(0, 1, fi)[:, None]
    mix[-fo:] *= np.linspace(1, 0, fo)[:, None]
    mix /= max(1e-9, np.abs(mix).max()) / 0.7
    return mix


def salvar(mix, caminho):
    d = (np.clip(mix, -1, 1) * 32767).astype('<i2')
    with wave.open(caminho, 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(d.tobytes())


if __name__ == '__main__':
    salvar(gerar(float(sys.argv[1]), int(sys.argv[3]) if len(sys.argv) > 3 else 1), sys.argv[2])
