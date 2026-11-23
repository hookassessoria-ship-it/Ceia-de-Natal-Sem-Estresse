"""Roteiro falado, efeitos e tempos de cada vídeo com áudio.

'em'   = início mínimo da fala (s, no vídeo final); a fala nunca começa antes do fim da anterior + respiro (200 ms).
'cena' = instante do vídeo ORIGINAL em que começa a cena dessa fala (o vídeo é re-renderizado esticado para
         que a cena entre junto com a fala). Sem 'cena', vale 'em'.
'legenda' = texto queimado; '|' separa os blocos que aparecem juntos na tela.
Os textos falados exatos estão em criativos/videos/com-audio/roteiros.md.
"""

CTA_SAIBA = 'R$ 19,90 | até 30 de novembro, | com 7 dias de garantia. | Toca em Saiba mais.'
CTA_COMPRAR = 'R$ 19,90 | até 30 de novembro, | com 7 dias de garantia. | Toca em Comprar agora.'

ROTEIRO = {
    # D1 (tema: quanto comprar e o que fazer em cada dia)
    'C15': dict(video='criativos/videos/C15.mp4', semente=2, falas=[
        dict(clip='d1_1', em=0.25, legenda='Quanto comprar | e o que fazer em cada dia?'),
        dict(clip='d1_2', em=3.4, cena=3.6, legenda='O guia traz três cardápios | pra 8 a 10 pessoas, | lista de compras por seção | e cronograma | do dia 17 ao 25.'),
        dict(clip='cta_saiba', em=12.0, cena=15.0, legenda=CTA_SAIBA),
    ], sfx=[
        dict(nome='whoosh', cena=3.45), dict(nome='pop', cena=4.4), dict(nome='pop', cena=6.6), dict(nome='pop', cena=8.8),
        dict(nome='whoosh', cena=11.25), dict(nome='whoosh', cena=14.85), dict(nome='pop2', cena=16.0),
    ]),
    # roteiro novo no molde (tema: adiantar, cada coisa no seu dia)
    'C16': dict(video='criativos/videos/C16.mp4', semente=3, falas=[
        dict(clip='v16_1', em=0.25, legenda='O erro número 1 da ceia? | Deixar tudo pra véspera... | aí o forno não dá conta.'),
        dict(clip='v16_2', em=4.6, legenda='Dá pra adiantar. | Uma semana antes, escolhe o cardápio. | Dia 21, o peru vai pra geladeira. | Dia 23, sobremesa, | farofa e salpicão prontos.'),
        dict(clip='v16_3', em=13.4, legenda='Aí o forno chega livre | no dia 24.'),
        dict(clip='cta_saiba', em=17.0, cena=16.8, legenda=CTA_SAIBA),
    ], sfx=[
        dict(nome='panela', em=0.3, ganho=-4), dict(nome='folha', cena=4.45), dict(nome='pop', cena=5.6), dict(nome='pop', cena=8.0),
        dict(nome='pop', cena=10.4), dict(nome='whoosh', cena=13.25), dict(nome='forno', cena=13.6, ganho=-3), dict(nome='whoosh', cena=16.65),
    ]),
    # D2 (tema: sobras)
    'C19': dict(video='criativos/videos/C19.mp4', semente=8, falas=[
        dict(clip='d2_1', em=0.25, legenda='Sobrou ceia? | Calma, ainda tem | o que fazer com ela.'),
        dict(clip='d2_2', em=4.0, cena=3.0, legenda='São 15 receitas | de aproveitamento... | e tem um guia de quanto tempo | guardar cada coisa.'),
        dict(clip='cta_comprar', em=9.8, cena=14.6, legenda=CTA_COMPRAR),
    ], sfx=[
        dict(nome='panela', em=0.2, ganho=-8), dict(nome='whoosh', cena=2.85), dict(nome='pop', cena=3.8), dict(nome='pop', cena=6.2),
        dict(nome='pop', cena=8.6), dict(nome='whoosh', cena=11.45), dict(nome='whoosh', cena=14.45), dict(nome='pop2', cena=15.6),
    ]),
    # roteiro novo no molde (tema: o dia 24 com e sem plano)
    'C24': dict(video='criativos/videos/C24.mp4', semente=4, falas=[
        dict(clip='v24_1', em=0.2, legenda='Dia 24, 10 da manhã... | fila do mercado. | Faltou o creme de leite. | E às 9 da noite, | o forno lotado.'),
        dict(clip='v24_2', em=6.4, cena=6.3, legenda='Com o plano? | Só pão, gelo e frutas. | E às 6 e meia, | o peru assa | e você vai tomar banho.'),
        dict(clip='cta_saiba', em=12.0, cena=10.2, legenda=CTA_SAIBA),
    ], sfx=[
        dict(nome='mercado', em=0.0, loop_ate=8.4, ganho=-10), dict(nome='relogio', em=0.0, ganho=-6), dict(nome='bip', em=1.6, ganho=-4),
        dict(nome='bip', em=3.6, ganho=-4), dict(nome='panela', em=6.2, ganho=-6), dict(nome='whoosh', cena=6.15),
        dict(nome='forno', cena=9.0, ganho=-4), dict(nome='whoosh', cena=10.05), dict(nome='pop2', cena=11.2),
    ]),
    # roteiro novo no molde (tema: descongelar o peru, a ordem)
    'C27': dict(video='criativos/videos/C27.mp4', semente=5, falas=[
        dict(clip='v27_1', em=0.2, legenda='Você sabe fazer o peru. | Mas sabe quando tirar ele | do congelador?'),
        dict(clip='v27_2', em=4.4, cena=4.3, legenda='Um peru de 5 quilos | leva de 2 a 3 dias | pra descongelar na geladeira.'),
        dict(clip='v27_3', em=7.4, cena=7.2, legenda='E às 9 da noite... | o forno é um só.'),
        dict(clip='v27_4', em=9.5, cena=9.4, legenda='Saber fazer não é o problema. | É a ordem.'),
        dict(clip='cta_saiba', em=11.6, cena=11.5, legenda=CTA_SAIBA),
    ], sfx=[
        dict(nome='faca', em=0.3, ganho=-6), dict(nome='whoosh', cena=4.15), dict(nome='pop', cena=4.7), dict(nome='relogio', cena=4.8, ganho=-8),
        dict(nome='forno', cena=7.2, ganho=-4), dict(nome='whoosh', cena=9.25), dict(nome='whoosh', cena=11.35), dict(nome='pop2', cena=12.4),
    ]),
    # roteiro novo no molde: sem a fala "ceia pequena" (regra: não prometer nada para ceia pequena)
    'C30': dict(video='criativos/videos/C30.mp4', semente=6, falas=[
        dict(clip='v30_1', em=0.3, legenda='O primeiro prato | chega na mesa.'),
        dict(clip='v30_2', em=2.7, legenda='Um silêncio bom.'),
        dict(clip='v30_3', em=5.1, legenda='Depois, um "que lindo" | baixinho.'),
        dict(clip='g30', em=8.2, cena=9.4, legenda='Cardápio, lista e cronograma | prontos.'),
        dict(clip='cta_saiba', em=11.0, cena=9.4, legenda=CTA_SAIBA),
    ], sfx=[
        dict(nome='sala', em=0.0, loop_ate=8.2, ganho=-14), dict(nome='cadeira', em=0.1, dur=2.5, ganho=-6), dict(nome='whoosh', cena=9.25), dict(nome='pop2', cena=10.4, ganho=-4),
    ]),
    'C32': dict(video='criativos/videos/C32.mp4', semente=7, falas=[
        dict(clip='v32_1', em=0.25, legenda='Onze e meia da noite. | A louça pode esperar.'),
        dict(clip='v32_2', em=2.7, legenda='As sobras já têm pote.'),
        dict(clip='v32_3', em=4.9, legenda='E o coração... | cheio.'),
        dict(clip='g32', em=7.6, cena=9.8, legenda='O plano da ceia | tá pronto no guia.'),
        dict(clip='cta_saiba', em=10.0, cena=9.8, legenda=CTA_SAIBA),
    ], sfx=[
        dict(nome='sala', em=0.0, loop_ate=7.6, ganho=-14), dict(nome='panela', em=0.4, ganho=-8), dict(nome='whoosh', cena=9.65), dict(nome='pop2', cena=10.7, ganho=-4),
    ]),
}

# ---------- vídeos novos (C33, C34, C33b): o HTML já foi animado nos tempos destas falas, sem re-render esticado ----------
def _f(clip, em, legenda, tempo=1.0):
    return dict(clip=clip, em=em, legenda=legenda, tempo=tempo, respiro=0.05)


def _s(nome, em, **k):
    return dict(nome=nome, em=em, **k)


ROTEIRO['C33'] = dict(video='criativos/videos/C33.mp4', semente=11, warp=False, cauda=0.6,
    musica_env=[[0, -2], [12.6, -2], [24.8, 1.5], [28.6, 0], [36, 0]], falas=[
    _f('n33_1', 0.20, 'Hoje você tá no sofá. | Dia 23, pode estar | numa fila de mercado.'),
    _f('n33_2', 5.15, 'Chega dezembro | e começam as dúvidas: | quanto comprar, | o que preparar, | quando fazer?'),
    _f('n33_3', 10.55, 'E se o plano | já estivesse pronto?'),
    _f('n33_4', 12.67, 'São 30 receitas, | três cardápios | pra 8 a 10 pessoas, | lista de compras por seção | e cronograma | do dia 17 ao 25, | com o dia 24 | hora a hora.'),
    _f('n33_5', 24.92, 'Garante agora, | guarda no celular | e abre dia 17.'),
    _f('cta_comprar', 28.72, CTA_COMPRAR),
], sfx=[
    _s('sala', 0.0, loop_ate=1.75, ganho=-12), _s('pop', 0.2), _s('whoosh', 1.5), _s('mercado', 1.75, loop_ate=3.25, ganho=-8),
    _s('pop', 1.8), _s('bip', 2.4, ganho=-4), _s('pop2', 2.9), _s('bip', 3.6, ganho=-4),
    _s('whoosh', 4.78), _s('folha', 5.2), _s('relogio', 5.5, ganho=-8), _s('pop', 6.75), _s('pop', 8.39), _s('pop', 9.41),
    _s('whoosh', 10.23), _s('encaixe', 11.15), _s('encaixe', 11.59), _s('encaixe', 11.92),
    _s('whoosh', 12.38), _s('folha', 13.0), _s('folha', 14.14), _s('folha', 16.87), _s('folha', 18.88), _s('pop', 22.57),
    _s('whoosh', 24.58), _s('pop', 25.89), _s('pop2', 26.5), _s('pop', 27.15),
    _s('whoosh', 28.38), _s('pop', 28.72), _s('pop', 29.93), _s('confirma', 33.47),
])

ROTEIRO['C34'] = dict(video='criativos/videos/C34.mp4', semente=12, warp=False, cauda=0.3, falas=[
    _f('n34_1', 0.15, 'Olha esse calendário...', 1.15),
    _f('n34_2', 1.67, 'Dia 17: | escolher cardápio.', 1.15),
    _f('n34_3', 3.90, 'Dia 21: | passar peru do congelador | pra geladeira.', 1.15),
    _f('n34_4', 7.60, 'Dia 23: | sobremesa, farofa | e salpicão prontos.', 1.15),
    _f('n34_5', 11.51, 'Dia 24: | só faltam pão, | gelo e frutas.', 1.15),
    _f('n34_6', 15.49, 'O guia traz o dia | hora a hora... | às 18h30, | o peru já tá assando.', 1.15),
    _f('n34_7', 20.88, 'Garante agora, | guarda no celular, | abre dia 17.', 1.15),
    _f('n34_8', 24.30, 'R$ 19,90 | até 30 de novembro, | 7 dias de garantia. | Toca em Saiba mais.', 1.15),
], sfx=[
    _s('pop', 0.2), _s('folha', 0.45), _s('whoosh', 1.45), _s('pop', 1.72), _s('whoosh', 3.63), _s('pop', 3.95),
    _s('pop', 5.6), _s('pop2', 6.6), _s('whoosh', 7.28), _s('pop', 8.87), _s('pop', 9.56), _s('pop', 10.12),
    _s('whoosh', 11.18), _s('pop', 13.69), _s('pop', 14.10), _s('pop', 14.61),
    _s('whoosh', 15.18), _s('forno', 15.5, ganho=-4), _s('relogio', 16.0, loop_ate=4.5, ganho=-6), _s('pop2', 17.83),
    _s('whoosh', 20.58), _s('pop', 21.75), _s('pop2', 22.3), _s('pop', 22.86),
    _s('whoosh', 23.98), _s('pop', 24.3), _s('pop', 25.46), _s('confirma', 28.58),
])

ROTEIRO['C33b'] = dict(video='criativos/videos/C33b.mp4', semente=13, warp=False, cauda=0.6,
    musica_env=[[0, -2], [11.3, -2], [17.8, 1.5], [20.9, 0], [30, 0]], falas=[
    _f('nb_1', 0.20, 'Falta pouco mais de um mês | pro Natal. | Você já sabe | o que vai servir?'),
    _f('nb_2', 4.37, 'Dia 23, mercado cheio | e ainda falta decidir | o que comprar.'),
    _f('n33_3', 9.26, 'E se o plano | já estivesse pronto?'),
    _f('nb_4', 11.43, 'Três cardápios | pra 8 a 10 pessoas, | lista por seção | e cronograma | até dia 25.'),
    _f('nb_5', 18.00, 'Guarda no celular | e abre dia 17.'),
    _f('nb_6', 21.01, 'R$ 19,90 | até 30 de novembro, | 7 dias de garantia. | Toca em Comprar agora.'),
], sfx=[
    _s('pop', 0.3), _s('folha', 1.0), _s('pop', 1.75), _s('pop', 2.33), _s('pop2', 2.6),
    _s('whoosh', 4.03), _s('mercado', 4.25, loop_ate=4.9, ganho=-8), _s('pop2', 4.45), _s('bip', 5.0, ganho=-4), _s('pop', 5.55), _s('bip', 7.0, ganho=-4),
    _s('whoosh', 8.93), _s('encaixe', 9.85), _s('encaixe', 10.29), _s('encaixe', 10.62),
    _s('whoosh', 11.08), _s('folha', 11.43), _s('folha', 14.15), _s('folha', 15.41),
    _s('whoosh', 17.63), _s('pop', 18.0), _s('pop2', 18.66), _s('pop', 19.32),
    _s('whoosh', 20.68), _s('pop', 21.01), _s('pop', 22.29), _s('confirma', 25.75),
])

# ---------- VSL da página (85 s): o vídeo-base é renderizado de producao/videos/VSL.html (render.js warp VSL, mapa identidade) ----------
_vsl = [
    ('vsl_01', 'Todo ano, a ceia de Natal | chega do mesmo jeito: | tudo pra decidir | na última hora.'),
    ('vsl_02', 'Quanto comprar, | o que preparar... | e o forno que não dá conta | no dia 24.'),
    ('vsl_03', 'O problema não é você. | É fazer tudo de cabeça, | na última hora.'),
    ('vsl_04', 'O guia Ceia de Natal | Sem Estresse | põe cada coisa no seu dia.'),
    ('vsl_05', 'São 30 receitas de casa, | com ingredientes de mercado, | e três cardápios | pra 8 a 10 pessoas: | Econômico, Tradicional | e Fartura.'),
    ('vsl_06', 'Cada cardápio tem | lista de compras | por seção do mercado, | com as quantidades.'),
    ('vsl_07', 'E um cronograma | do dia 17 ao 25. | Dia 17, | escolhe o cardápio. | Dia 21, o peru vai | do congelador pra geladeira. | Dia 23, sobremesa, | farofa e salpicão prontos.'),
    ('vsl_08', 'No dia 24, | o guia vai hora a hora... | e às 18h30, | o peru já tá assando.'),
    ('vsl_09', 'E ainda tem três bônus: | Brincadeiras e Jogos | para a Festa, | Receitas com as Sobras da Ceia, | e Ceia Econômica.'),
    ('vsl_10', 'É um PDF de 63 páginas. | Dá pra ler no celular, | no computador | ou imprimir.'),
    ('vsl_11', 'E você tem 7 dias de garantia: | se não for pra você, | pede o reembolso.'),
    ('vsl_12', 'R$ 19,90 | até 30 de novembro. | Garante agora, | guarda no celular | e abre dia 17.'),
]
_em, _t = [], 0.3
for _c, _leg in _vsl:
    _em.append(_t)
    _t += {'vsl_01': 5.06, 'vsl_02': 5.68, 'vsl_03': 4.44, 'vsl_04': 4.32, 'vsl_05': 9.6, 'vsl_06': 4.93, 'vsl_07': 13.6,
           'vsl_08': 6.95, 'vsl_09': 8.32, 'vsl_10': 6.16, 'vsl_11': 4.4, 'vsl_12': 6.94}[_c] + 0.35
ROTEIRO['VSL'] = dict(video='/tmp/claude-0/vsl/vsl_base.mp4', semente=14, warp=False, cauda=0.5,
    musica_env=[[0, -1], [11.5, -1], [16.3, -3], [21, 0], [77, 1], [86, 0]],
    falas=[_f(c, em, leg) for (c, leg), em in zip(_vsl, _em)],
    sfx=[_s('mercado', 0.0, loop_ate=5.5, ganho=-10), _s('bip', 1.6, ganho=-4), _s('pop2', 1.2), _s('pop', 3.3)]
    + [_s('whoosh', t0 - 0.22) for t0 in (5.55, 11.55, 16.35, 21.0, 36.25, 42.2, 46.1, 50.2, 57.5, 66.2, 72.7, 77.45)]
    + [_s('folha', 5.75), _s('relogio', 6.0, ganho=-8), _s('pop', 8.38), _s('sala', 11.55, loop_ate=4.8, ganho=-14), _s('folha', 16.6),
       _s('folha', 21.5), _s('folha', 25.46), _s('folha', 32.24), _s('pop', 39.87), _s('pop', 44.2), _s('pop2', 45.3),
       _s('pop', 47.39), _s('pop', 48.14), _s('pop', 48.75), _s('forno', 50.4, ganho=-4), _s('relogio', 51.5, loop_ate=4.0, ganho=-8),
       _s('pop', 59.61), _s('pop', 62.17), _s('pop', 64.73), _s('pop', 66.74), _s('pop2', 69.95), _s('encaixe', 73.5),
       _s('pop', 77.61), _s('pop', 78.87), _s('confirma', 80.64)])
