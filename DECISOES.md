# DECISOES.md · série de objeções (C21 a C32)

Registro das escolhas feitas sem consulta, como pedido. Fatos de produto: ver [`FATOS.md`](FATOS.md). Resultado e checagens: ver [`RELATORIO.md`](RELATORIO.md).

## 1. Fontes de verdade

- **O PDF completo não está disponível** (nem no repositório, nem público). Li a página de vendas inteira, com o FAQ aberto, e as 6 páginas reais publicadas nela (8, 12, 22, 31, 57, 62). Tudo o que os criativos afirmam está em `FATOS.md`, com a fonte de cada linha.
- A página de vendas mudou desde a rodada anterior. Entraram um contador até a ceia ("Dá tempo de planejar tudo. Comece hoje.") e as respostas do FAQ, entre elas: "Para mais convidados, é só multiplicar as receitas e a lista de compras na mesma proporção; **para menos, divida**."
- **Não existe versão para ceia pequena.** A OBJ 3 é tratada só de forma emocional na arte. A copy diz a verdade: cardápios para 8 a 10 pessoas e, para menos gente, dividir receitas e lista (frase do FAQ).
- **Os 2 order bumps não foram citados.** Não aparecem na página de vendas e não consegui abrir o checkout para confirmar.
- **Números específicos usados**, todos contados nas páginas reais: o dia 24 tem **18 horários** (pág. 22), o checklist tem **14 itens** (pág. 62) e um peru de 5 kg leva **de 2 a 3 dias** para descongelar na geladeira (pág. 31). A lista do Econômico tem 40 itens em 5 seções (pág. 12); confirmei, mas não usei nesta série.

## 2. Imagens e fotos

| Decisão | Motivo |
|---|---|
| **Nenhuma foto nova** | Não há chave do Pixabay no ambiente. Liberei o Unsplash na rede do ambiente, mas a busca é protegida por um desafio anti-robô (Anubis) e **não contornei a proteção**. Os endereços `unsplash.com` e `images.unsplash.com` ficaram na lista do ambiente "Ceia-de-Natal-Sem-Estresse" sem uso; podem ser removidos nas configurações do ambiente |
| **Nenhuma imagem gerada por IA** | Gastaria créditos seus sem autorização, e no briefing anterior você pediu para descartar imagens com cara de IA |
| **Fotos com rosto excluídas** | `hero-familia` e `mesa-servida` mostram rostos identificáveis, o que esta rodada proíbe |
| **Foto das meias com o rosto desfocado** | Na original, o rosto já aparecia fora de foco atrás da caneca. Gerei `assets/derivados/meias-sem-rosto.jpg` com desfoque forte só nessa região: virou silhueta irreconhecível |
| **Foto da louça com cor aquecida** | `assets/derivados/louca-quente.jpg`, usada desfocada no fundo do C32 (fim da noite) |
| **Luz quente gerada por código** | Bokeh de velas e pisca-pisca, determinístico (`producao/luz.js`), com granulação editorial. Cria a "luz quente" da OBJ 3 sem foto falsa, sem clipart e sem bonequinho |
| **Páginas reais do PDF como prova** | Cronograma (pág. 22) atrás do bilhete do C21 e no C28; lista (pág. 12) no C22; checklist (pág. 62) no C31, com as linhas citadas marcadas em pêssego |

## 3. Identidade visual

- **Paleta da página de vendas** (lida no CSS dela): verde profundo `#1D4A32`, creme `#FFF4E3` / `#FFFAF2`, pêssego `#F2B880` (e tons claros), terracota `#C4532B`, ouro `#C9A45C`. Os C01 a C20 usam o vermelho e o dourado da capa; a série nova segue o seu pedido (verde, creme, pêssego).
- **Serifa com palavra em itálico:** DM Serif Display, a mesma dos C01 a C20. Em fundo escuro, o itálico vai em pêssego. Em fundo claro, pêssego sobre creme não tem contraste, então o itálico vai em verde com marca-texto pêssego.
- Títulos com `text-wrap: balance`, para não sobrar palavra sozinha na última linha.
- Mesmo pipeline dos C01 a C20 (HTML → Playwright → PNG/MP4), com dois acréscimos compatíveis em `producao/render.js`: a versão 9:16 das imagens (`<meta name="formatos">`) e vídeos sem faixa de áudio (`window.SEM_AUDIO`). Os criativos antigos continuam saindo iguais.

## 4. Formatos, nomes e zonas seguras

- **8 imagens** em 1080x1350 (`Cxx.png`) e **todas também em 1080x1920** (`Cxx_9x16.png`), porque todas funcionam em Stories e Reels.
- **4 vídeos** em 1080x1920, H.264, 30 fps, 12,5 a 14,5 s, **sem faixa de áudio** e com legenda em tela.
- **Zona segura do 9:16:** nada importante nos 250 px do topo nem nos 340 px da base. Conferido por script (`producao/zonas.js`), que mede cada elemento.
- **Nome do anúncio** no padrão `C21 | Nome curto | Imagem` (coluna `nome` do CSV). Os arquivos continuam `C21.png` / `C21_9x16.png` / `C24.mp4`, porque "|" quebra nome de arquivo no Windows.
- **Os C01 a C20 também ganharam um nome nesse padrão** no CSV. Esses nomes foram **inferidos**; se no Gerenciador eles têm outro nome, vale o do Gerenciador.

## 5. CSV

- Mesmo arquivo `textos-anuncios.csv`, as **mesmas 16 colunas** de antes e **9 colunas novas no fim**: `nome`, `url`, `titulo_3`, `objecao`, `gatilho`, `gancho_alt_1` a `gancho_alt_3` e `arquivo_9x16`. Para C01 a C20, `nome` e `url` também foram preenchidos.
- **Texto principal = coluna `texto_medio`** (3 a 5 linhas, 1ª linha é o gancho, sem emoji). `texto_curto` e `texto_lista` são opções extras para o recurso de múltiplos textos da Meta; o `texto_lista` usa "•", não ✔.
- **Título = `titulo_1`; alternativos = `titulo_2` e `titulo_3`.** Todos com até 40 caracteres; descrição com até 30.
- **CTA "Saiba mais" em todos os 12.** É o botão da maioria dos C01 a C20 e o que a regra deles usa para quem ainda tem objeção ou baixa consciência.
- **URL:** o mesmo padrão do README, `?utm_source=meta&utm_medium=paid&utm_campaign=ceia2026&utm_content=C21`.
- **`onda` = 3**, para separar esta série das ondas 1 e 2.

## 6. Copy: regras aplicadas

- **Linguagem neutra.** Sem "anfitriã", sem "obrigada" (o bilhete diz "Valeu"), sem estado civil, sem "sozinha", sem "triste". Usado: "quem cozinha", "quem está à mesa", "quem você ama".
- **OBJ 2 com cuidado:** o guia **tem** 30 receitas com passo a passo, então nenhum texto diz que ele "não ensina a cozinhar". Dizemos "você cozinha, o guia organiza" e mencionamos os 3 cardápios prontos, para não sugerir que a lista e o cronograma servem para qualquer cardápio.
- **Promessa só com "pode" ou "costuma":** "pode pesar menos no bolso", "costuma deixar o dia 24 mais leve". Nenhum valor em reais além de R$ 19,90.
- **Dramatização, não depoimento:** "Depois, um *que lindo* baixinho" (C30) é cena narrada, sem nome, sem aspas de cliente e sem "disse".
- **Urgência só a real:** "Ainda é novembro", "dá tempo", datas do cronograma. Nenhum contador; os dias que faltam não aparecem porque mudam a cada dia.
- **Sem Papai Noel, sem apelo religioso, sem alegação de saúde, sem marca de terceiros.**

## 7. Gatilho de cada criativo

| Criativo | Objeção | Ângulo | Gatilho principal |
|---|---|---|---|
| C21 · Eu de novembro · Imagem | OBJ 1 | (a) o eu do dia 24 agradece | **Autocontinuidade** (o eu do futuro) + estado final |
| C22 · Aos poucos · Imagem | OBJ 1 | (b) comprar aos poucos pesa menos | **Aversão à perda** (o aperto de uma compra só) + datas reais |
| C23 · Ainda é novembro · Imagem | OBJ 1 | (c) o que o cronograma marca | **Reenquadramento** da objeção ("Ótimo.") + especificidade |
| C24 · Mercado no dia 24 · Vídeo | OBJ 1 | (d) mercado x dia tranquilo | **Contraste vivido** + aversão à perda (a manhã no mercado) |
| C25 · Ceia de sempre · Imagem | OBJ 2 | (a) mesma ceia, sem correria | **Estado final** + preservação de identidade |
| C26 · Também senta à mesa · Imagem | OBJ 2 | (b) quem cozinha também senta | **Identidade** + aversão à perda (a conversa à mesa) |
| C27 · O que dá errado · Vídeo | OBJ 2 | (c) o que dá errado pra quem sabe | **Especificidade** (2 a 3 dias de descongelamento) + reconhecimento |
| C28 · Falta o plano · Imagem | OBJ 2 | (d) "você faz tudo certo" | **Reconhecimento** + especificidade (18 horários) |
| C29 · Mesa pra poucos · Imagem | OBJ 3 | (a) mesa posta para poucos | **Orgulho de caprichar** + estado final (**100% emocional**) |
| C30 · Primeiro prato · Vídeo | OBJ 3 | (b) o primeiro prato | **Momento sensorial** + pertencimento (**100% emocional**) |
| C31 · Capricho é presente · Imagem | OBJ 3 | (c) gratidão de quem recebe | **Reciprocidade afetiva** + checklist real |
| C32 · Fim da noite · Vídeo | OBJ 3 | (d) fim da noite, coração cheio | **Memória do estado final** + pertencimento (**100% emocional**) |

## 8. Diferença em relação aos C01 a C20

- O C12 (improvisada x planejada) era uma imagem; o C24 é um vídeo com horário e cena concreta.
- O C01 tratava a dor de passar a noite na cozinha; o C26 trata a identidade de quem cozinha.
- O C16 ensinava o que adiantar; o C23 reenquadra a objeção do mês.
- O C05 e o C14 vendiam o cronograma como recurso; o C21 e o C28 usam a página real como prova de outro argumento.
- A ceia pequena, o descongelamento do peru, o checklist como afeto e o mês de novembro são ângulos novos.
