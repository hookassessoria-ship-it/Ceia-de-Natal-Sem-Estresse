# QA técnico dos vídeos com voz

Gerado por `producao/audio/qa.py`.

| Arquivo | Vídeo | Áudio | Duração v/a (s) | LUFS | Pico (dBTP) | Tamanho |
|---|---|---|---|---|---|---|
| criativos/videos/com-audio/C15_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 19.00 / 19.00 | -14.0 | -1.5 | 1.8 MB |
| criativos/videos/com-audio/C16_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 27.10 / 27.09 | -14.0 | -1.5 | 2.2 MB |
| criativos/videos/com-audio/C19_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 18.00 / 18.00 | -14.0 | -1.5 | 2.7 MB |
| criativos/videos/com-audio/C24_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 22.93 / 22.93 | -14.0 | -1.7 | 2.7 MB |
| criativos/videos/com-audio/C27_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 24.30 / 24.29 | -13.9 | -1.8 | 2.8 MB |
| criativos/videos/com-audio/C30_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 18.07 / 18.08 | -13.9 | -1.5 | 5.3 MB |
| criativos/videos/com-audio/C32_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 16.90 / 16.90 | -14.0 | -1.5 | 3.8 MB |
| criativos/videos/com-audio/C33_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 35.90 / 35.90 | -14.0 | -1.5 | 7.7 MB |
| criativos/videos/com-audio/C33b_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 28.30 / 28.30 | -14.0 | -1.8 | 5.7 MB |
| criativos/videos/com-audio/C34_voz.mp4 | h264 1080x1920 | aac 48000 Hz 2 ch | 30.30 / 30.30 | -14.0 | -1.5 | 3.7 MB |
| criativos/videos/vsl/vsl-ceia-720p.mp4 | h264 720x1280 | aac 48000 Hz 2 ch | 85.58 / 85.61 | -14.0 | -1.4 | 3.0 MB |

**Erros:** nenhum

**Termos da lista de bloqueio encontrados (conferir contexto):**
- textos-anuncios.csv:39 [bebida] ✔ 30 receitas: 5 entradas, 6 principais, 8 acompanhamentos, 8 sobremesas e 3 bebidas
- textos-anuncios.csv:47 [bebida] ✔ 14h montar a mesa e gelar as bebidas
- textos-anuncios.csv:133 [bebida] 9h café tranquilo. 14h mesa montada e bebidas gelando. 17h30 peru no forno. 18h30 seu momento: banho e arrumaç

## Transcrição (ElevenLabs Scribe) das falas com preço, data e número

O conector não envia arquivo local, então transcrevi as falas geradas (a fonte de todo número dito nos vídeos). As 15 batem palavra por palavra com o roteiro:

| Fala | Transcrição |
|---|---|
| CTA Saiba mais (C15, C16, C24, C27, C30, C32) | Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Saiba mais. |
| CTA Comprar agora (C19, C33) | Dezenove e noventa até trinta de novembro, com sete dias de garantia. Toca em Comprar agora. |
| C34 fala 8 | Dezenove e noventa até trinta de novembro, sete dias de garantia. Toca em Saiba mais. |
| C33b fala 6 | Dezenove e noventa até trinta de novembro, sete dias de garantia. Toca em Comprar agora. |
| VSL fala 12 | Dezenove e noventa até trinta de novembro. Garante agora, guarda no celular e abre dia dezessete. |
| C15 fala 2 | O guia traz três cardápios pra oito a dez pessoas, lista de compras por seção e cronograma do dia dezessete ao vinte e cinco. |
| C19 fala 2 | São quinze receitas de aproveitamento... e tem um guia de quanto tempo guardar cada coisa. |
| C33 fala 4 | São trinta receitas, três cardápios pra oito a dez pessoas, lista de compras por seção e cronograma do dia dezessete ao vinte e cinco, com o dia vinte e quatro hora a hora. |
| C34 fala 6 | O guia traz o dia hora a hora... às dezoito e trinta, o peru já tá assando. |
| C34 fala 3 | Dia vinte e um: passar peru do congelador pra geladeira. |
| C33b fala 4 | Três cardápios pra oito a dez pessoas, lista por seção e cronograma até dia vinte e cinco. |
| VSL fala 7 | E um cronograma do dia dezessete ao vinte e cinco. Dia dezessete, escolhe o cardápio. Dia vinte e um, o peru vai do congelador pra geladeira. Dia vinte e três, sobremesa, farofa e salpicão prontos. |
| VSL fala 8 | No dia vinte e quatro, o guia vai hora a hora... e às dezoito e trinta, o peru já tá assando. |
| VSL fala 10 | É um PDF de sessenta e três páginas. Dá pra ler no celular, no computador ou imprimir. |
| VSL fala 11 | E você tem sete dias de garantia: se não for pra você, pede o reembolso. |

**Voz x música:** a voz fica de 20 a 22 dB acima da música (medido no arquivo inteiro), e cerca de 6 dB a mais durante a fala, por causa do *ducking*. O briefing pedia 22 a 26 dB na mixagem e 15 a 20 dB no QA; ficou no meio.

**"bebida" no CSV:** são textos antigos dos anúncios ("3 bebidas" entre as receitas e "gelar as bebidas", da pág. 22). Nada indica álcool, e nenhum vídeo com voz fala disso.
