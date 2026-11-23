# Roteiros com voz · vídeos da ceia

Os vídeos originais (mudos) continuam em `criativos/videos/`. As versões com voz, efeitos, música e legenda queimada estão aqui, com o sufixo `_voz`.

## Voz e áudio

| Item | Escolha |
|---|---|
| Voz | **Prister** (ElevenLabs, `YINKDXIRM4VvqAmVRusk`): feminina, pt-BR, adulta, calma e conversacional |
| Teste | 3 candidatas com a frase "Ninguém tá pensando na ceia agora... e tá tudo bem.": Prister, Sofia e Christine. A Prister foi escolhida pela descrição (pt-BR nativa, tom calmo e caloroso, sem cara de locução comercial) e pela duração natural da frase. **Não consegui ouvir as amostras; vale você ouvir e confirmar.** |
| Modelo | `eleven_v3`, o mais expressivo para pt-BR. O conector MCP não expõe stability, style, speaker boost nem velocidade, então ficaram no padrão do modelo. |
| Geração | Uma frase por arquivo (`producao/audio/vozes/`), números por extenso, respiro de 150 a 250 ms entre frases. No C34 a fala foi acelerada para 1,15x (o briefing permite isso se passar de 30 s). |
| Tratamento | Corte abaixo de 80 Hz, de-esser, compressão suave (2,5:1), sem reverb |
| Efeitos | ElevenLabs `eleven_text_to_sound_v2`: mercado, bipe do caixa, página, forno, relógio, panela, faca, cadeira, sala. Whoosh, pop, encaixe e confirmação são sintetizados no `mixar.py`. |
| Música | Original, sintetizada no `producao/audio/trilha.py`: violão dedilhado, pad, sino e escovinha, em Fá maior, 84 BPM, sem melodia conhecida e sem samples de terceiros. |
| Mixagem | Voz em −16 LUFS antes da mix. Música de 20 a 22 dB abaixo da voz (medida integrada), com *ducking* de 6 dB durante a fala; no C33 e no C33b ela cresce na parte do guia. Resultado: −14 LUFS integrados, pico ≤ −1 dBTP (loudnorm em 2 passos). MP4 H.264 + AAC 48 kHz estéreo, 1080x1920. |
| Legenda | Queimada, palavra por palavra (a palavra falada acende em pêssego), em blocos curtos, na faixa entre y≈1510 e 1600 |

Para refazer: `python3 producao/audio/mixar.py C15 C33 ...`. Os tempos, efeitos e legendas de cada vídeo estão em `producao/audio/roteiro.py`.

## Conferência com o guia

O PDF completo (63 páginas) **não está no repositório** nem é público. Conferi pelas 6 páginas reais publicadas na página de vendas (8, 12, 22, 31, 57 e 62, em `assets/site/`) e pelo texto da página, em 23/11/2026:

| Fala | Fonte | Situação |
|---|---|---|
| Dia 17: escolher o cardápio | Página: "17 ou 18/12, uma semana antes: escolher o cardápio, imprimir a lista e comprar o que não estraga" | confere |
| Dia 21: peru do congelador para a geladeira | Página: "21/12, três dias antes: passar o peru do congelador para a geladeira" | confere |
| Dia 23: sobremesa gelada, farofa e salpicão prontos | Página: "23/12: sobremesas geladas, farofa e salpicão prontos" | confere |
| Dia 24: só falta pão, gelo e frutas | Pág. 22: "10h compras de última hora: pão, gelo, frutas do ponche e da salada" | confere |
| 18h30: o peru já está assando | Pág. 22: "17h30 peru no forno · 18h30 seu momento: banho e arrumação, enquanto o peru assa" | confere |
| 15 receitas de aproveitamento | Página: bônus "Receitas com as Sobras da Ceia: **11 receitas** e um guia de conservação" + 4 receitas de sobras no guia (dado do briefing) | 11 confere na página; as 4 do guia não consegui ver no PDF |
| "Tabela de quanto tempo guardar cada coisa" | A página fala em "**guia de conservação**"; a pág. 57 diz "consuma em até 3 dias". Não achei a palavra "tabela" e não sei em que página ela fica. | **ajustado:** a fala virou "e tem um guia de quanto tempo guardar cada coisa" |

---

## Vídeos existentes

O texto de tela de cada vídeo foi comparado com os temas D1, D2 e D3:

| Vídeo | Tema da tela | Locução usada |
|---|---|---|
| C15 | 3 cardápios, lista e cronograma | **D1** (exata) |
| C19 | 3 ideias com as sobras | **D2** (exata, com o ajuste "guia" no lugar de "tabela") |
| C16 | o que dá para adiantar, dia a dia | **nova, no molde** (frases já gravadas + CTA de D1) |
| C24 | dia 24 com e sem plano | **nova, no molde** |
| C27 | descongelar o peru, a ordem | **nova, no molde** |
| C30 | o primeiro prato na mesa | **nova, no molde**, sem a fala "ceia pequena" |
| C32 | 23h30, as sobras já têm pote | **nova, no molde**, sem a fala "ceia pequena" |
| D3 (orçamento) | nenhum vídeo existente tem esse tema | não usada |

Os botões foram alinhados à fala no `textos-anuncios.csv`: **C15 passou para Saiba mais** (D1 diz "Toca em Saiba mais") e **C19 passou para Comprar agora** (D2 diz "Toca em Comprar agora").

### C15_voz · D1 (19 s) · botão Saiba mais
1. Quanto comprar e o que fazer em cada dia?
2. O guia traz três cardápios pra oito a dez pessoas, lista de compras por seção e cronograma do dia dezessete ao vinte e cinco.
3. Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Saiba mais.

### C19_voz · D2 (18 s) · botão Comprar agora
1. Sobrou ceia? Calma, ainda tem o que fazer com ela.
2. São quinze receitas de aproveitamento... e tem um guia de quanto tempo guardar cada coisa.
3. Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Comprar agora.

O cartão final do C19 dizia "Bônus: 4 receitas com as sobras", o que contradiz as 15 da fala. Na versão com voz ele diz "15 receitas de aproveitamento". **O C19.mp4 mudo antigo continua com o texto velho.**

### C16_voz · locução nova (27 s) · botão Saiba mais · *para você revisar*
1. O erro número um da ceia? Deixar tudo pra véspera... aí o forno não dá conta.
2. Dá pra adiantar. Uma semana antes, escolhe o cardápio. Dia vinte e um, o peru vai pra geladeira. Dia vinte e três, sobremesa, farofa e salpicão prontos.
3. Aí o forno chega livre no dia vinte e quatro.
4. Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Saiba mais.

### C24_voz · locução nova (23 s) · botão Saiba mais · *para você revisar*
1. Dia vinte e quatro, dez da manhã... fila do mercado. Faltou o creme de leite. E às nove da noite, o forno lotado.
2. Com o plano? Só pão, gelo e frutas. E às seis e meia, o peru assa e você vai tomar banho.
3. Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Saiba mais.

### C27_voz · locução nova (24 s) · botão Saiba mais · *para você revisar*
1. Você sabe fazer o peru. Mas sabe quando tirar ele do congelador?
2. Um peru de cinco quilos leva de dois a três dias pra descongelar na geladeira.
3. E às nove da noite... o forno é um só.
4. Saber fazer não é o problema. É a ordem.
5. Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Saiba mais.

### C30_voz · locução nova (18 s) · botão Saiba mais · *para você revisar*
1. O primeiro prato chega na mesa.
2. Um silêncio bom.
3. Depois, um "que lindo" baixinho.
4. Cardápio, lista e cronograma prontos.
5. Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Saiba mais.

A tela original do C30 ainda mostra "Ceia pequena. Momento grande." (sem fala por cima). Pela regra nova (não prometer nada para ceia pequena), vale decidir se esse vídeo continua no ar.

### C32_voz · locução nova (17 s) · botão Saiba mais · *para você revisar*
1. Onze e meia da noite. A louça pode esperar.
2. As sobras já têm pote.
3. E o coração... cheio.
4. O plano da ceia tá pronto no guia.
5. Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Saiba mais.

A tela original do C32 mostra "Ceia pequena. Noite cheia." (sem fala por cima). Mesma observação do C30.

---

## Vídeos novos (locução oficial, sem reescrever)

### C33 · "Você hoje x você no dia 23" (36 s) · botão Comprar agora
| # | Tempo | Fala | Tela |
|---|---|---|---|
| 1 | 0,2 s | Hoje você tá no sofá. Dia vinte e três, pode estar numa fila de mercado. | HOJE ✕ DIA VINTE E TRÊS · sofá → corte → mercado lotado |
| 2 | 5,2 s | Chega dezembro e começam as dúvidas: quanto comprar, o que preparar, quando fazer? | QUANTO COMPRAR? · lista enorme, relógio rápido |
| 3 | 10,6 s | E se o plano já estivesse pronto? | E SE JÁ ESTIVESSE PRONTO? · calendário 17-25 se encaixa |
| 4 | 12,7 s | São trinta receitas, três cardápios pra oito a dez pessoas, lista de compras por seção e cronograma do dia dezessete ao vinte e cinco, com o dia vinte e quatro hora a hora. | A CEIA ORGANIZADA · PDF em camadas (páginas reais) |
| 5 | 24,9 s | Garante agora, guarda no celular e abre dia dezessete. | GUARDA NO CELULAR · o PDF entra no celular, "17 DEZ" |
| 6 | 28,7 s | Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Comprar agora. | DEZENOVE E NOVENTA / ATÉ TRINTA DE NOVEMBRO · botão |

O roteiro previa 35 s; com a fala natural ficou em 35,9 s.

### C34 · "O calendário de 7 dias" (30 s) · botão Saiba mais
Fala a 1,15x (ficava com 32,5 s), com pausa curta entre as datas.
| # | Tempo | Fala | Tela |
|---|---|---|---|
| 1 | 0,2 s | Olha esse calendário... | CADA COISA NO SEU DIA · a folha de novembro vira |
| 2 | 1,7 s | Dia dezessete: escolher cardápio. | DIA 17 · zoom no dia 17 |
| 3 | 3,9 s | Dia vinte e um: passar peru do congelador pra geladeira. | DIA 17 · DIA 21 · peru vai para a geladeira |
| 4 | 7,6 s | Dia vinte e três: sobremesa, farofa e salpicão prontos. | DIA 23: TUDO ADIANTADO · três pratos na bancada |
| 5 | 11,5 s | Dia vinte e quatro: só faltam pão, gelo e frutas. | DIA 24: · pão, gelo, frutas |
| 6 | 15,5 s | O guia traz o dia hora a hora... às dezoito e trinta, o peru já tá assando. | DIA 24: ÀS 18H30 · forno, relógio, tique-taque |
| 7 | 20,9 s | Garante agora, guarda no celular, abre dia dezessete. | o PDF entra no celular |
| 8 | 24,3 s | Dezenove e noventa até trinta de novembro, sete dias de garantia. Toca em Saiba mais. | DEZENOVE E NOVENTA / ATÉ TRINTA DE NOVEMBRO · botão |

### C33b · "Falta pouco mais de um mês" (28 s) · botão Comprar agora
| # | Tempo | Fala | Tela |
|---|---|---|---|
| 1 | 0,2 s | Falta pouco mais de um mês pro Natal. Você já sabe o que vai servir? | JÁ PENSOU NA CEIA? · calendário, 25 marcado |
| 2 | 4,4 s | Dia vinte e três, mercado cheio e ainda falta decidir o que comprar. | A CORRERIA COMEÇA · mercado cheio, "23 DEZ" |
| 3 | 9,3 s | E se o plano já estivesse pronto? | TUDO NO PLANEJAMENTO · calendário organizado |
| 4 | 11,4 s | Três cardápios pra oito a dez pessoas, lista por seção e cronograma até dia vinte e cinco. | CARDÁPIO, LISTA E CRONOGRAMA · páginas reais |
| 5 | 18,0 s | Guarda no celular e abre dia dezessete. | o PDF entra no celular |
| 6 | 21,0 s | Dezenove e noventa até trinta de novembro, sete dias de garantia. Toca em Comprar agora. | DEZENOVE E NOVENTA / ATÉ TRINTA DE NOVEMBRO · botão |
