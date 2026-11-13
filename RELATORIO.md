# RELATORIO.md · série de objeções (C21 a C32)

Nada foi publicado e nada foi mexido no Gerenciador de Anúncios. Só arquivos.
Escolhas e gatilhos: [`DECISOES.md`](DECISOES.md). Fatos do produto: [`FATOS.md`](FATOS.md).

## Os 12 criativos

| Nome (coluna `nome`) | Objeção | Ângulo | Gatilho | Formato | Arquivos |
|---|---|---|---|---|---|
| C21 \| Eu de novembro \| Imagem | 1 · Ainda é novembro | Bilhete do eu do dia 24 ("Valeu, eu de novembro. Peru assando. Eu, no banho.") sobre a página real do cronograma | Autocontinuidade + estado final | Imagem 4:5 e 9:16 | `criativos/imagens/C21.png`, `C21_9x16.png` |
| C22 \| Aos poucos \| Imagem | 1 | "Aos poucos, pode pesar menos": novembro (carne na oferta), 17/12 (secos), 24/12 (pão e gelo) | Aversão à perda + datas reais | Imagem 4:5 e 9:16 | `C22.png`, `C22_9x16.png` |
| C23 \| Ainda é novembro \| Imagem | 1 | "Ainda é novembro. Ótimo." + 17, 21, 23 e 24/12 do cronograma | Reenquadramento + especificidade | Imagem 4:5 e 9:16 | `C23.png`, `C23_9x16.png` |
| C24 \| Mercado no dia 24 \| Vídeo | 1 | 24/12, 10h: fila do mercado x só pão, gelo e frutas | Contraste vivido + aversão à perda | Vídeo 13,5 s | `criativos/videos/C24.mp4` |
| C25 \| Ceia de sempre \| Imagem | 2 · Eu já sei fazer | "A ceia de sempre. Sem a correria. Você cozinha. O guia organiza." | Estado final + identidade preservada | Imagem 4:5 e 9:16 | `C25.png`, `C25_9x16.png` |
| C26 \| Também senta à mesa \| Imagem | 2 | Cartão "Reservado pra quem fez a ceia" | Identidade + aversão à perda | Imagem 4:5 e 9:16 | `C26.png`, `C26_9x16.png` |
| C27 \| O que dá errado \| Vídeo | 2 | "Você sabe fazer o peru. Mas sabe quando tirar do congelador?" → 2 a 3 dias (pág. 31) → "É a ordem." | Especificidade + reconhecimento | Vídeo 14,5 s | `C27.mp4` |
| C28 \| Falta o plano \| Imagem | 2 | "Você sabe fazer tudo. Falta o plano." + página real do dia 24 | Reconhecimento + especificidade | Imagem 4:5 e 9:16 | `C28.png`, `C28_9x16.png` |
| C29 \| Mesa pra poucos \| Imagem | 3 · Ceia pequena | "Mesa pra poucos. Capricho inteiro." Luz quente, 100% emocional | Orgulho de caprichar + estado final | Imagem 4:5 e 9:16 | `C29.png`, `C29_9x16.png` |
| C30 \| Primeiro prato \| Vídeo | 3 | O primeiro prato, o silêncio bom, "Ceia pequena. Momento grande." 100% emocional | Momento sensorial + pertencimento | Vídeo 12,5 s | `C30.mp4` |
| C31 \| Capricho é presente \| Imagem | 3 | "Pra quem está à mesa, o capricho é presente" + checklist real marcado | Reciprocidade afetiva + prova | Imagem 4:5 e 9:16 | `C31.png`, `C31_9x16.png` |
| C32 \| Fim da noite \| Vídeo | 3 | 23h30: louça na pia, sobras no pote, coração cheio. 100% emocional | Memória do estado final + pertencimento | Vídeo 13 s | `C32.mp4` |

Distribuição: **8 imagens + 4 vídeos**; pelo menos 1 vídeo por objeção (C24, C27, C30, C32); **3 criativos 100% emocionais** na OBJ 3 (C29, C30, C32). Copy completa, 3 títulos, descrição, CTA, URL com UTM e 3 ganchos alternativos de cada um estão nas linhas C21 a C32 de [`textos-anuncios.csv`](textos-anuncios.csv).

## O que foi checado

| Checagem | Como | Resultado |
|---|---|---|
| **Visual das imagens** | Revisei as 16 artes (8 em 4:5 e 8 em 9:16) em pranchas e ampliei a 100% os pontos de risco: nitidez da foto ampliada no C25, legibilidade da página no C31, marcações nas linhas certas | Corrigido: legendas emendadas no C22; capa e preço invadindo a base no 9:16 do C28 e do C31; pautas do bilhete no C21; palavras sozinhas na última linha (títulos balanceados) |
| **Zonas seguras do 9:16** | Script `producao/zonas.js` mede cada elemento: nada entre y=0–250 nem y=1580–1920 | 8 de 8 ok |
| **Vídeos** | Quadros extraídos dos MP4 finais aos 0,8 s, 2 s, no meio e no cartão final, e `ffprobe` | Ganchos legíveis antes de 1 s; corrigidos "2 a 3 dias" quebrando sobre o texto (C27), frases encostadas (C32) e última palavra sozinha nos cartões finais. Especificação: 1080x1920, H.264, 30 fps, só faixa de vídeo (sem áudio), 12,5 a 14,5 s |
| **Palavras na arte** | Script `producao/qa_artes.js` | Sem contar o preço: C29 9, C25/C26/C28 12, C31 13, C21 e C23 14, C22 16. Tirando também as datas (24/12, 18h30…): de 9 a 13. Para chegar lá, cortei os sobretítulos do C21 e do C22 e encurtei o apoio do C25. O C22 é o mais carregado, porque a linha do tempo precisa das 3 datas |
| **Política (textos)** | `producao/textos.py` varre texto curto, principal, lista, títulos, descrição e os 3 ganchos alternativos: atributos pessoais (casada, marido, solteira, sozinha, triste…), depoimento (cliente, "disse que"), promessa ("garanto"), porcentagem, clique-isca, escassez falsa, Papai Noel, apelo religioso, saúde, marcas, qualquer valor em R$ diferente de R$ 19,90 | 0 ocorrência. Antes, testei o validador com 9 frases ruins de propósito: pegou as 9 |
| **Política (artes)** | `producao/qa_artes.js` extrai o texto visível das 12 artes e passa a mesma lista | 0 ocorrência |
| **Rostos** | Fotos com rosto excluídas; na foto das meias, o rosto (que já estava fora de foco) foi desfocado até virar silhueta | Nenhum rosto identificável |
| **Fatos** | Cada afirmação conferida contra `FATOS.md` (tabela abaixo) | Reescritos antes de entregar: "o guia não ensina a cozinhar" (falso: tem 30 receitas), "versão para 2" (não existe) e "anfitriã" (atributo de gênero) |
| **Português** | Revisão de concordância, crase e pontuação; tom de conversa ("pra", "dá pra") mantido de propósito, como nos C01 a C20 | Ok |
| **Limites da Meta** | Títulos até 40, descrição até 30, 1ª linha até 125 caracteres, texto principal de 3 a 5 linhas | Ok (maior título: 40 caracteres) |

### Afirmações e fonte

| Afirmação usada | Onde | Fonte |
|---|---|---|
| 18h30: banho e arrumação, enquanto o peru assa | C21, C24, C26 | pág. 22 |
| Dia 24 em 18 horários, das 9h às 23h30 | C24, C25, C28 | pág. 22 (contados) |
| 10h: pão, gelo e frutas | C22, C24 | pág. 22 |
| 21h40 velas acesas; 22h ceia servida; 23h30 sobras na geladeira | C23, C26, C32 | pág. 22 |
| 17 ou 18/12 compras; 21/12 peru do congelador para a geladeira; 23/12 sobremesas, farofa e salpicão | C22, C23, C27 | página de vendas |
| Comprar o chester ou o lombo com antecedência, na oferta, e congelar | C22 | pág. 8 |
| A lista separa o que comprar antes e o que deixar para a véspera | C22 | página de vendas |
| Peru de 5 kg: 2 a 3 dias para descongelar na geladeira | C27 | pág. 31 |
| No dia 24 o forno não dá conta de tudo na mesma hora | C27 | página de vendas |
| Checklist de 14 itens: velas testadas, música escolhida, lugar de cada convidado definido, potes à mão, espaço na geladeira | C25, C26, C29, C31, C32 | pág. 62 |
| Cardápios para 8 a 10 pessoas; para menos, divida | C29 a C32 | página de vendas (FAQ) |
| Dia 25: sanduíche, risoto, rabanada de panetone | C32 | página de vendas |
| R$ 19,90, PDF, acesso imediato por e-mail | todos | página de vendas |

## O que ficou de fora por falta de confirmação

- **Os 2 order bumps:** não aparecem na página de vendas e não consegui abrir o checkout.
- **Pratos completos do Tradicional e do Fartura:** só aparecem indiretamente na pág. 22.
- **Qualquer ideia de "versão para 2 a 4 pessoas":** não existe; usei só o "para menos, divida" do FAQ.
- **Fotos reais de mesa para poucos, mãos e talheres:** não há fonte disponível; o Unsplash tem proteção anti-robô e não foi contornada. Se você tiver fotos próprias (mesa posta, mãos servindo, sem rosto), elas podem substituir a luz gerada por código no C29 e no C30 sem mudar o resto.
- **Imagens geradas por IA:** não usadas.
- **O número de dias até o Natal:** muda todo dia.
- **Os depoimentos da página de vendas:** continuam falando de organizar a casa, não da ceia.

## Ordem sugerida de entrada (3 por dia)

Cada dia leva um criativo de cada objeção, para a comparação ser justa. A OBJ 1 ("ainda é novembro") perde força conforme dezembro chega, então os 4 dela entram até o 4º dia.

| Dia | Criativos | Por quê |
|---|---|---|
| 1 | **C23** Ainda é novembro · **C27** O que dá errado (vídeo) · **C29** Mesa pra poucos | O gancho mais direto de cada objeção: reenquadra a objeção, traz um fato específico e o emocional mais limpo |
| 2 | **C24** Mercado no dia 24 (vídeo) · **C28** Falta o plano · **C30** Primeiro prato (vídeo) | Os contrastes: correria x calma, prática x plano, e o vídeo emocional |
| 3 | **C21** Eu de novembro · **C25** Ceia de sempre · **C31** Capricho é presente | Identidade e reciprocidade, com prova real (cronograma e checklist) |
| 4 | **C22** Aos poucos · **C26** Também senta à mesa · **C32** Fim da noite (vídeo) | Fecham os ângulos restantes de cada objeção |

Sugestão de datas: dia 1 em 14/11, dia 4 em 17/11.

## Atenção antes de publicar

1. **Depoimentos fora do tema na página de vendas:** risco de reprovação por página enganosa, já apontado na rodada anterior.
2. **Confirme no PDF final:** a numeração da pág. 31 (citada no C27); os 18 horários do dia 24; os 14 itens do checklist; e a dica do chester na oferta, que aparece no cardápio Econômico.
3. **OBJ 3:** os textos deixam claro que os cardápios são para 8 a 10 pessoas e que, para menos gente, divide-se receitas e lista. Se não quiser essa frase nos anúncios, troque o texto principal pelo `texto_curto`.
