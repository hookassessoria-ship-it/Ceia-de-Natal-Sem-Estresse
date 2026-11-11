# Pesquisa na Biblioteca de Anúncios da Meta

**Produto:** Ceia de Natal Sem Estresse (Cantinho do Lar) · R$ 19,90
**Coleta:** 11/11/2026, Biblioteca de Anúncios, país Brasil, todos os anúncios (`active_status=all`)
**Arquivos:** prints das 25 referências em [`referencias/biblioteca/`](referencias/biblioteca/) e a coleta inteira (247 anúncios) em [`referencias/biblioteca/coleta-completa.csv`](referencias/biblioteca/coleta-completa.csv), com o link de cada anúncio na Biblioteca.

---

## 1. Como a pesquisa foi feita

- **14 buscas** com navegador automatizado (Playwright): ceia de natal, cardápio de natal, receitas de natal, ceia econômica, ebook receitas, receitas pdf, cardápio da semana, planejamento de ceia, natal sem estresse, ceia de natal pdf, receitas natalinas, ceia de natal receitas, apostila receitas, cardápio semanal, ceia de natal econômica.
- **247 anúncios únicos** coletados; **150** com cara de infoproduto (PDF, e-book, apostila, receitas, página de vendas); **98** deles são infoprodutos de Natal ou ceia.
- **A ordem dos resultados é por impressões.** A própria Meta redireciona a busca para `sort_data[mode]=total_impressions&sort_data[direction]=desc`. Por isso, a coluna "posição" abaixo funciona como sinal de entrega: quem aparece em 1º a 10º lugar numa busca está entre os anúncios mais exibidos daquele termo.

### Limitações (leia antes de usar os dados)

1. **Os vencedores do Natal de 2025 não estão mais visíveis.** No Brasil, a Biblioteca só guarda anúncios comuns *inativos* se eles também rodaram na União Europeia (selo "Transparência da UE"). Uma busca filtrada por anúncios de outubro a dezembro de 2025 voltou praticamente vazia (só anunciantes portugueses). Os anúncios brasileiros de ceia que pararam em dezembro sumiram.
2. **A temporada de 2026 começou há poucas semanas.** O anúncio de Natal mais antigo ainda ativo começou em 27/09. Por isso, o critério "30 dias ou mais no ar" foi adaptado (próxima seção).
3. **O número de anúncios por anunciante foi contado dentro da coleta**, não na página do anunciante. A visão por página da Biblioteca não abriu com os IDs disponíveis. O número real pode ser maior.
4. **Vídeos:** o navegador automatizado não carrega o arquivo de vídeo, só a capa. Para vídeos, o gancho registrado é a 1ª linha do texto e o quadro de capa visível no print, não os primeiros 3 segundos assistidos.
5. **Não há dados de vendas.** Tempo no ar, número de versões e posição por impressões indicam que o anunciante continua investindo, não quanto vende.

### Critério de "vencedor" adaptado

| Tipo de anúncio | Sinal usado |
|---|---|
| Natal 2026 (sazonal) | Ativo há 25 dias ou mais; **ou** várias versões do mesmo criativo; **ou** anunciante com 5 ou mais anúncios na coleta; **e**, de preferência, entre as 10 primeiras posições por impressões |
| Infoproduto de receitas o ano todo | Ativo há 44 dias ou mais (alguns passam de 400 dias) |
| Lançados há 1 ou 2 dias | Entram só como **mapa da concorrência** (oferta, preço, promessa), não como prova de que funciona |

---

## 2. As 25 referências

Legenda de ângulo: **D** dor · **De** desejo/cena · **E** economia · **P** praticidade/plano · **V** volume de receitas · **R** renda extra · **Ed** erro comum/educativo · **U** urgência da data · **Pr** prova (mostrar por dentro).

| Ref | Anunciante | Início · tempo no ar | Versões · anúncios na coleta | Posição (impressões) | Formato | Gancho (1ª linha) | Ângulo | Estrutura do texto | Oferta e preço | CTA | Destino | Print |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | Chef Miguel Ramos | 11/10/2026 · 31 dias, ativo | 1 · **7 anúncios** iguais desde 10/10 | 2º em "receitas de natal" | Vídeo (1:16) | "Transforme sua ceia de Natal em um momento ainda mais especial!" | V, De | Promessa → "200 receitas" → "práticas e fáceis" → CTA | 200 receitas, preço só na página | Saiba mais | Página única (netlify) | [R01](referencias/biblioteca/R01_chef-miguel-ramos_1423432709858828.png) |
| R02 | Maria Alice | 02/11/2026 · 9 dias | 1 · **5 anúncios** | 11º em "receitas de natal" | Vídeo (0:51) | "A ceia de Natal inteira planejada, sem passar o dia 24 na cozinha!" | De, P, V | Cena → número → **lista ✅** (cardápio por tamanho e orçamento, lista, o que adiantar no dia 23) → preço → CTA | +300 receitas, "a partir de R$ 10" | Saiba mais | Página única | [R02](referencias/biblioteca/R02_maria-alice_2514654549027438.png) |
| R03 | Wanda Oliveira | 09/11/2026 · 2 dias | **Várias versões** · **7 anúncios** | **1º a 7º** em "ceia econômica" | Imagem e vídeo (0:19) | "Se você começa a planejar sua ceia de Natal escolhendo as receitas, provavelmente já está cometendo o primeiro erro!" | Ed, E | **Erro comum** → por quê → "o certo é o contrário" → produto → CTA | Cardápios, listas e receitas; preço na página | Saiba mais | Página única (vercel) | [R03](referencias/biblioteca/R03_wanda-oliveira_969204722539764.png) |
| R04 | Herança de Vó | 10/11/2026 · 1 dia | 1 · 1 | 8º em "natal sem estresse" | Imagem (página do produto: "Quanto comprar para 10 pessoas?") | "Este ano a ceia vai estar pronta às 21 h, e você vai estar sentada à mesa com a família." | De, P, Pr | Cena do dia 24 → o que vem (emojis por item) → preço → acesso imediato | 3 cardápios, quantidades, lista por seção, cronograma hora a hora, 18 receitas · **R$ 27** · garantia de 7 dias | Saiba mais | Página única (pages.dev) | [R04](referencias/biblioteca/R04_heranca-de-vo_3537352049767928.png) |
| R05 | Natal em Família | 09/11/2026 · 2 dias | **Várias versões** · 1 | 3º em "natal sem estresse" | Vídeo (0:28) | "Quer uma ceia de Natal sem estresse este ano?" | De, Pr, V | Pergunta → produto → **como é por dentro** (rendimento, tempo, passo a passo) → preço → CTA | 200 receitas · **R$ 15,90** | Saiba mais | Página única (netlify) | [R05](referencias/biblioteca/R05_natal-em-familia_1519522543331097.png) |
| R06 | Dona Cida (Natal à Mesa) | 10/11/2026 · 1 dia | 1 · **14 anúncios** em 1 dia (teste em massa) | 11º a 24º em "natal sem estresse" | Carrossel, imagem e vídeo | "Ceia de Natal sem estresse e sem pensar no que fazer." | P, V, Pr | Promessa → produto + bônus (lista, cronograma, cardápios) → preço | 50 receitas + 3 bônus · **R$ 22,90** | Saiba mais | Página única (vercel) | [R06](referencias/biblioteca/R06_dona-cida_1753709022392510.png) |
| R07 | Nutri Juliana Marques | 15/10/2026 · 27 dias | 1 · 2 | 15º em "ceia de natal receitas" | Vídeo (0:55) | "Você ainda não sabe o que vai fazer na ceia de Natal?" | D, E | Pergunta → agitação (tudo caro, não sabe o que preparar) → criação do produto → **lista ✅** → acesso imediato → CTA | 80 ceias econômicas; preço na página | **Baixar** | Página única (netlify) | [R07](referencias/biblioteca/R07_nutri-juliana-marques_1879321436385000.png) |
| R08 | Receitas Ilimitadas | 17/10/2026 · 25 dias | **Várias versões** · 1 | 2º em "cardápio de natal" | Imagem (mockup + selo de preço) | "Natal está chegando!" | U, R, V | Data → o que aprende → exemplos → bônus → preço | 30 sobremesas de travessa · **R$ 3,99** | (ver detalhes) | Página única | [R08](referencias/biblioteca/R08_receitas-ilimitadas_1337240071686381.png) |
| R09 | Karinadicas | 10/11/2026 · 1 dia | 1 · 3 | 6º e 7º em "natal sem estresse" | Imagem (mulher + "Sua ceia começa aqui" + selo R$ 5,90) | "ATENÇÃO! O NATAL ESTÁ CHEGANDO E VOCÊ NÃO PODE FICAR SEM ESSAS RECEITAS!" | U, V | Alerta em caixa alta → número → CTA | 100 receitas + 5 bônus · **R$ 5,90** | Saiba mais | Página única (lovable) | [R09](referencias/biblioteca/R09_karinadicas_2238056390430126.png) |
| R10 | Natal Prático | 10/11/2026 · 1 dia | 1 · 1 | 8º em "ceia econômica" | Imagem (mockups de capas + preço) | "Seu Natal inteiro resolvido" | P | Promessa → itens → **✅ acesso, pagamento, garantia** → CTA | 6 guias em PDF · **a partir de R$ 9,90** · garantia de 7 dias | Saiba mais | Página única | [R10](referencias/biblioteca/R10_natal-pratico_2336695483796099.png) |
| R11 | BIFIT Doces Fit | 27/09/2026 · 45 dias | 1 · 2 | 2º em "receitas natalinas" | Vídeo (1:40) | "Tudo o que você leva no A Magia do Natal Saudável:" | Pr, R | **Começa pela lista do que vem** → preço ancorado → garantia | Curso · "de R$ 597 por R$ 197" · garantia de 7 dias | **Comprar agora** | Site próprio | [R11](referencias/biblioteca/R11_bifit-doces-fit_1780121646591413.png) |
| R12 | Receitas Sem Culpa 3.0 | 30/10/2026 · 12 dias | **2 versões** · 2 | 14º em "receitas de natal" | Vídeo (0:52) | "Esse Natal dá pra comer a sobremesa sem medo do açúcar!" | De, V | Desejo → número → bônus em lista ✅ (inclui "cardápio + lista + cronograma") → CTA | 40 receitas; pagamento depois, via WhatsApp | Enviar mensagem | WhatsApp | [R12](referencias/biblioteca/R12_receitas-sem-culpa-3-0_40187755710808574.png) |
| R13 | Lorena Rosa | 04/11/2026 · 7 dias | 1 · 1 | 6º em "ceia de natal pdf" | Vídeo (1:16) | "Imagine servir um panetone lindo no Natal e dizer com orgulho: 'Fui eu que fiz!'" | De | Cena de orgulho → preço → o que vem → usos → CTA | 50 receitas · **R$ 10,90** | Enviar mensagem | WhatsApp | [R13](referencias/biblioteca/R13_lorena-rosa_4440260446287270.png) |
| R14 | Doceria Smart | 16/10/2026 · 24 dias (inativo, rodou na UE) | 1 · 2 | 25º em "receitas de natal" | Imagem (pessoa + guia na mão + preço) | "Em dezembro todo mundo quer sobremesa pronta, pra ceia, pro amigo secreto…" | R, U | Cenário de demanda → oferta | 11 receitas + 3 bônus · **R$ 47** | Saiba mais | Site próprio | [R14](referencias/biblioteca/R14_doceria-smart_1605080988082868.png) |
| R15 | mundo_da_dona_elvira | 07/12/2023 · **1.070 dias**, ativo | 1 · 1 | **1º** em "receitas natalinas" | Imagem | "Maravilhosas receitas natalinas da Vó." | De (afeto, vó) | 1 frase + hashtags | Não informa | Saiba mais | Instagram | [R15](referencias/biblioteca/R15_mundo-da-dona-elvira_731240272249269.png) |
| R16 | PedagoKits | 01/10/2026 · 41 dias | **2 anúncios usam esse criativo** · 1 | 3º em "ceia de natal pdf" | Imagem (foto da ceia + "A ceia acabou. Cada um foi pro celular?") | "As brincadeiras do Natal não precisam ficar para a última hora." | U (antecipação), De | Antecipação → benefício → o que vem → PDF, imprime → CTA | Até 40 jogos · **a partir de R$ 10** | (ver resumo) | Página única (netlify) | [R16](referencias/biblioteca/R16_pedagokits_2641207342996420.png) |
| R17 | Missão Pequeno Explorador | 30/10/2026 · 12 dias | 1 · 1 | **1º** em "ceia de natal pdf" | Carrossel | "Mamãe, vovó, professora... dezembro chega voando!" | U (antecipação) | Chamado ao público → "quem se prepara antes curte com calma" → lista com emojis → PDF na hora | Material para colorir; preço no WhatsApp | Enviar mensagem | WhatsApp | [R17](referencias/biblioteca/R17_missao-pequeno-explorador_2550112025476286.png) |
| R18 | Marina Duarte | 04/11/2026 · 7 dias | 1 · 1 | 9º em "ceia de natal pdf" | Vídeo | "A melhor parte do Natal são as histórias que a família vai contar depois." | De (família) | Afeto → produto → CTA | +250 gincanas · **R$ 17,90** | Saiba mais | Página única | [R18](referencias/biblioteca/R18_marina-duarte_2281120369952767.png) |
| R19 | Leidy Cakes | 27/06/2025 · **502 dias**, ativo | 1 · 1 | 7º em "ebook receitas" | Imagem (fotos de doces + selo de preço) | "Chegou o e-book que vai transformar suas sobremesas em renda extra!" | R | 3 linhas: promessa → o que aprende → preço → CTA | E-book · **R$ 10** | Saiba mais | Página única | [R19](referencias/biblioteca/R19_leidy-cakes_1057966452978335.png) |
| R20 | Bombons RG | 19/09/2025 · **418 dias**, ativo | 1 · 1 | 5º em "ebook receitas" | Imagem | "Tem gente se matando em CLT pra ganhar R$1.400… enquanto tem gente faturando R$3.000…" | R (contraste) | 1 frase de contraste | E-book; "somente hoje esse valor" | **Comprar agora** | Página única (Canva) | [R20](referencias/biblioteca/R20_bombons-rg_1485797339429194.png) |
| R21 | Matheus Carvalho | 15/09/2025 · **422 dias**, ativo | 1 · 2 | 2º em "ebook receitas" | Vídeo | "Aprenda Receitas e Lucre com sua Paixão por Brigadeiros!" | R | Promessa curta → CTA | Curso; preço na página | Saiba mais | Site próprio | [R21](referencias/biblioteca/R21_matheus-carvalho_1580639392914561.png) |
| R22 | Crocheteca | 28/09/2026 · 44 dias | 1 · 3 | 12º em "receitas pdf" | Imagem ("comprou receitas e recebeu drive?") | "comprou receitas e recebeu uma pasta de links?" | D (desorganização), Pr | Objeção da categoria → como é diferente → números → preço único | App de receitas · **R$ 13,90 uma vez** | (ver detalhes) | Quiz | [R22](referencias/biblioteca/R22_crocheteca_2177397992846759.png) |
| R23 | Raízs | 19/08/2026 · 84 dias | **Várias versões** · 1 | 3º em "cardápio da semana" | Imagem ("cansada de pensar no que comer?") | "decidir o cardápio da semana não precisa ser um peso." | D (carga mental de decidir) | 2 frases em minúsculas, tom de conversa | Assinatura de orgânicos | Saiba mais | Site próprio | [R23](referencias/biblioteca/R23_raizs_1783414636123195.png) |
| R24 | Renata Brugnera (nutrição) | 29/05/2026 · 166 dias | 1 · 1 | **1º** em "cardápio da semana" | Vídeo | "O link do nosso app com + de 150 receitas fáceis, saudáveis e realmente gostosas" | P, V | Frase curta, nativa → link | App de receitas | (ver detalhes) | Página de vendas | [R24](referencias/biblioteca/R24_renata-brugnera-nutricao_1473903903955667.png) |
| R25 | Chef Isadora Leblanc | 06/08/2026 · 97 dias | 1 · 1 | 20º em "ebook receitas" | Imagem | "Sobremesas incríveis SEM açúcar? Sim, é possível!" | De | Pergunta → resposta → benefício → "oferta só hoje" | "De R$ 67 por R$ 10" | Saiba mais | Página única (vercel) | [R25](referencias/biblioteca/R25_chef-isadora-leblanc_1781872672825505.png) |

---

## 3. Os 8 padrões que se repetem

### P1. Estrutura do texto: gancho → o que é → lista ✅ → preço + "acesso imediato" → "Toque em Saiba mais"
Aparece em R02, R04, R05, R06, R07, R10, R11 e R12. A 1ª linha é uma cena, pergunta ou alerta; depois vem o nome do produto com um número; depois uma lista com ✅ ou emojis por item; e fecha com preço, "pagamento único", "acesso imediato" e a instrução do clique. R11 (45 dias no ar) começa direto pela lista.

### P2. Âncora de volume: "+300", "200", "100", "80", "50 receitas" por preço baixo
R01, R02, R05, R06, R07, R08, R09, R13 e R14. A categoria disputa quem tem mais receitas. Faixa de preço observada: **R$ 3,99 a R$ 27** (R$ 3,99 · 5,90 · 9,90 · 10 · 10,90 · 15,90 · 17,90 · 22,90 · 27), com R$ 47 e R$ 197 para cursos e renda extra. **Os R$ 19,90 ficam no meio da faixa.**

### P3. A cena do dia 24 e a promessa de sentar à mesa
R02 ("sem passar o dia 24 na cozinha"), R04 ("ceia pronta às 21 h, e você sentada à mesa"), R05/R06/R09 ("ceia de Natal sem estresse", "sem pensar no que fazer"). É o ângulo emocional dominante dos concorrentes diretos e coincide com a sua página de vendas.

### P4. Erro comum e conteúdo educativo para quem ainda não sabe que tem o problema
R03 é o caso mais forte da pesquisa: 7 anúncios ocupando **as 7 primeiras posições por impressões** em "ceia econômica", com o gancho "provavelmente já está cometendo o primeiro erro" e uma explicação antes da oferta. R07 ("Você ainda não sabe o que vai fazer na ceia?") e R23 ("decidir o cardápio não precisa ser um peso", 84 dias) atacam a carga mental de decidir.

### P5. Urgência verdadeira da data e antecipação
"Natal está chegando!" (R08, R09), "dezembro chega voando… quem se prepara antes curte o Natal com calma" (R17, **1º lugar** em "ceia de natal pdf") e "não precisam ficar para a última hora" (R16, 41 dias e 2 versões). Nenhum dos que mais aparecem usa contador.

### P6. Mostrar o produto por dentro, com o preço na arte
Carrossel de páginas (R06: "Cada receita em uma página clara"), a página de quantidades como criativo (R04: "Quanto comprar para 10 pessoas?"), "cada receita vem em uma página, com rendimento, tempo…" (R05) e mockups com selo de preço (R08, R09, R10, R14, R19).

### P7. Economia como ângulo próprio
R03 (planejar pelo orçamento), R07 ("80 Ceias Econômicas… sem gastar uma fortuna"), R09 ("fáceis e econômicas") e R04 (cardápio econômico). Ninguém promete valor exato em reais nos anúncios de ceia.

### P8. Formato e visual: vídeo vertical na maioria; "Saiba mais" como botão padrão
Entre os 98 infoprodutos de Natal/ceia, **59% são vídeo**, 37% imagem e 4% carrossel. Os vídeos mostram comida sendo preparada ou uma pessoa falando. As imagens usam mulher sorrindo com texto grande, mockup com selo de preço ou pergunta escrita sobre foto (R16, R22, R23). Paleta vermelho, verde e dourado. **"Saiba mais" é o botão em cerca de 2 de cada 3 infoprodutos** (65 de 100 com botão identificado), mesmo com preço no texto; "Comprar agora" aparece em ofertas diretas (R11, R20). O destino é quase sempre uma página única em vercel, netlify, lovable ou pages.dev, igual à sua.

### Alerta: prova social que não vamos copiar
**39 dos 98** anúncios de Natal/ceia têm "⭐⭐⭐⭐⭐ 4.9" no texto, no título ou na descrição do link (R01, R02, R06, R07, R08, R09…). Outros usam "Oferta única", "só hoje" e preço riscado sem referência ("de R$ 597 por R$ 197", "de R$ 67 por R$ 10"). Isso fere as suas regras e é risco real de reprovação e de denúncia. **A ausência de estrelas vira diferencial**: a nossa prova são as páginas reais do guia.

---

## 4. O que ninguém está fazendo (oportunidades)

1. **O cronograma hora a hora como protagonista.** Os concorrentes citam "cronograma" como um item da lista (R02, R04, R06, R12). Ninguém mostra o dia 24 de verdade. O guia tem a página inteira, das 9h às 23h30, e uma linha que vende sozinha: **"18h30: seu momento: banho e arrumação, enquanto o peru assa."**
2. **O dia 25 e as sobras.** Nenhum anúncio coletado fala do que fazer com o que sobrou. O bônus tem 4 receitas e como guardar e requentar com segurança.
3. **Clareza em vez de volume.** A categoria briga por "300 receitas", mas a dor é "não sei o que fazer". Ninguém diz: *você não precisa de 300 receitas, precisa de um plano*. Os 3 cardápios fechados com 30 receitas são exatamente isso.
4. **Educar com o próprio conteúdo do guia.** Só R03 ensina antes de vender, e ficou com as 7 primeiras posições do termo. Há conteúdo real para vídeos educativos: o que adiantar no dia 23, quando tirar o peru do congelador (dia 21), o que comprar uma semana antes.
5. **Quantidades exatas como prova.** Só R04 usa uma página de quantidades. A lista do guia traz "chester de cerca de 3,5 kg", "batata 1,5 kg" etc. para 8 a 10 pessoas.
6. **Garantia como argumento.** A garantia de 7 dias aparece só no rodapé (R04, R10, R11). Para quem tem medo de comprar PDF de anúncio, ela pode ser o gancho.
7. **Prova honesta.** Num mar de "4.9 estrelas", mostrar a página real (e dizer "veja por dentro antes de comprar") é mais crível.

### Atenção à concorrência pelo nome
R04 (Herança de Vó) vende um e-book chamado **"Ceia de Natal sem Estresse"**, com quase a mesma oferta (3 cardápios, quantidades, lista por seção, cronograma hora a hora, garantia de 7 dias) por R$ 27. R05, R06 e R09 também usam "ceia de Natal sem estresse" no texto, e existe uma página chamada "Natal Sem Estresse". O nome está virando termo genérico. Nos criativos, a marca **Cantinho do Lar**, a capa e as provas específicas (63 páginas, 30 receitas, dia 24 hora a hora, sobras) é que diferenciam.

---

## 5. Como cada padrão vira criativo nosso

| Padrão | Adaptação honesta | Onde entra |
|---|---|---|
| P1 Estrutura com lista ✅ | Mesma ordem, só com itens reais do guia; "pagamento único" e "acesso imediato por e-mail" são verdade | Texto "lista" de todos os anúncios; C04, C18 |
| P2 Âncora de volume | Não competimos por volume. Ancoramos em **plano + preço**: "30 receitas + 3 cardápios por R$ 19,90", "menos de R$ 1 por receita" (19,90 ÷ 30 = R$ 0,66) | C04, C15, textos médios |
| P3 Cena do dia 24 | A cena real do guia: "18h30: seu momento", "ceia servida às 22h", "sente à mesa" | C01, C05, C12, C14 |
| P4 Erro comum / educativo | Vídeos que ensinam algo útil de verdade, tirado do guia, e só no fim mostram o produto | C13, C16, C19, C08 |
| P5 Urgência verdadeira | "O Natal está chegando", "uma semana antes você já compra o que não estraga". Sem contador nem data inventada | Textos curtos, C16, C20 |
| P6 Mostrar por dentro | Páginas reais do PDF em todos os criativos de consciência alta; preço na arte | C03, C04, C05, C06, C09, C11, C14, C18 |
| P7 Economia | "Tem cardápio econômico", com a dica real do guia (comprar o chester na oferta e congelar). Nenhum valor prometido | C09, C07 |
| P8 Formato | 8 vídeos verticais (9:16) + 12 imagens 4:5; "Saiba mais" para consciência baixa, "Comprar agora" para alta | Todos |
| Oportunidade: garantia | Garantia como gancho principal, com o texto real da página | C10 |
| Oportunidade: sobras | Dia 25 resolvido | C06, C19 |
| Oportunidade: clareza vs. volume | "Você não precisa de 300 receitas. Precisa de um plano." (sem citar ninguém) | Banco de ganchos, C15 |
