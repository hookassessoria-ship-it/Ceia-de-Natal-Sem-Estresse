# Ceia de Natal Sem Estresse · criativos para Meta Ads

Pacote de criativos do guia **Ceia de Natal Sem Estresse** (Cantinho do Lar, R$ 19,90), feito a partir de uma pesquisa real na Biblioteca de Anúncios da Meta.

## O que tem aqui

| Arquivo | O que é |
|---|---|
| [`pesquisa-biblioteca.md`](pesquisa-biblioteca.md) | Fase 0: método, 25 referências com sinais de vencedor, 8 padrões, oportunidades e como cada padrão foi adaptado |
| [`referencias/biblioteca/`](referencias/biblioteca/) | Prints das 25 referências e `coleta-completa.csv` com os 247 anúncios coletados |
| [`estrategia.md`](estrategia.md) | Fase 1: posicionamento, matriz de 11 ângulos, 30 ganchos, princípios de copy, mudanças no briefing, ondas e bloqueios antes de subir |
| [`criativos/imagens/`](criativos/imagens/) | C01 a C12 e C21, C22, C23, C25, C26, C28, C29, C31 · PNG 1080x1350 (4:5); da série de objeções também `_9x16.png` (1080x1920) |
| [`criativos/videos/`](criativos/videos/) | C13 a C20 · MP4 1080x1920 (9:16), H.264, 30 fps, 17 a 22 s, com faixa de áudio silenciosa · C24, C27, C30, C32 · 12,5 a 14,5 s, sem faixa de áudio |
| [`textos-anuncios.csv`](textos-anuncios.csv) | Fase 3: 3 textos, 2 títulos, descrição, CTA e `utm_content` de cada criativo |
| [`assets/site/`](assets/site/) | Capa, 6 páginas do PDF e 4 fotos, baixadas da página de vendas (os originais não estavam no repositório) |
| [`FATOS.md`](FATOS.md) · [`DECISOES.md`](DECISOES.md) · [`RELATORIO.md`](RELATORIO.md) | Série de objeções C21 a C32: o que o guia realmente traz, as escolhas feitas e o QA com a ordem de entrada |
| [`producao/`](producao/) | Fontes, HTMLs e scripts que geram as artes, os vídeos e o CSV (`zonas.js` e `qa_artes.js` fazem o QA da série de objeções) |

## Como subir no Gerenciador de Anúncios

1. Para cada linha do CSV, crie um anúncio com o arquivo da coluna `arquivo`.
2. Em **Texto principal**, use "Adicionar opções de texto" e cole `texto_curto`, `texto_medio` e `texto_lista`.
3. Em **Título**, cole `titulo_1` e `titulo_2` como opções; em **Descrição**, `descricao`.
4. Botão: a coluna `cta`.
5. URL do site: `https://cantinho-ceia.vercel.app/?utm_source=meta&utm_medium=paid&utm_campaign=ceia2026&utm_content=C01` (troque `C01` pelo ID).
6. Vídeos: são mudos e foram feitos para ser entendidos sem som. Vale adicionar uma música da biblioteca de sons da Meta no próprio Gerenciador.
7. Comece pela **onda 1** (12 criativos). A onda 2 entra a partir de 01/12 ou quando a onda 1 cansar (ver `estrategia.md`).

## Como regerar

```bash
node producao/render.js imagens          # todas as imagens (ou: imagens C01 C05)
node producao/render.js videos           # todos os vídeos (ou: videos C14)
python3 producao/textos.py               # CSV, com validação de limites e termos proibidos
```

Precisa de Node com Playwright (Chromium) e ffmpeg. As fontes (DM Serif Display, Nunito e Caveat, licença OFL) estão em `producao/fonts`.
