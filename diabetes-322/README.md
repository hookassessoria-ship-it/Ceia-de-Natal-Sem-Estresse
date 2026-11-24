# 322 Receitas para Quem Tem Diabetes · 5 criativos para Meta Ads

Produto: ebook **322 Receitas para Quem Tem Diabetes**, da marca **Cantinho do Lar**. Formato 4:5, 1080x1350 PNG, um arquivo por criativo, em `criativos/`.

> **Atenção: a capa original não veio junto com o pedido.** Os criativos foram montados com uma **capa provisória** (`capa/capa-provisoria.png`), desenhada a partir da descrição: verde, creme, marrom, nome, 322 receitas, marca e "do café da manhã à marmita". Por isso os arquivos saem com o sufixo `_capa-provisoria`. **Não publique com ela.**
>
> Para trocar: salve a capa real como `capa/capa-original.png` (de preferência vertical, perto de 900x1260) e rode `node diabetes-322/render.js`. Os arquivos saem como `D01.png` a `D05.png`, já com a capa real.

| Arquivo | Ângulo | Headline | CTA |
|---|---|---|---|
| `D01` | Identificação / repetição | Cansou de comer sempre a mesma coisa? | CONHEÇA O EBOOK |
| `D02` | Variedade / rotina (café, almoço, lanche, jantar) | Do café da manhã à marmita! | VEJA TODAS AS RECEITAS |
| `D03` | Diferencial: carboidratos por porção | Receitas com carboidratos por porção. | DESCUBRA O MATERIAL |
| `D04` | Oferta / 3 bônus (mockup em tablet) | 322 RECEITAS + 3 BÔNUS GRATUITOS | QUERO CONHECER |
| `D05` | Praticidade (cozinha real, ebook no tablet) | Mais ideias para o seu dia a dia. | CONHEÇA AS 322 RECEITAS |

## Campos editáveis

- **Bônus (D04):** em `html/D04.html`, troque `const BONUS = ['[BÔNUS 1]', '[BÔNUS 2]', '[BÔNUS 3]']` pelos nomes reais e rode o render de novo. Nada sobre os bônus foi inventado.
- **Carboidratos (D03):** a página é um **exemplo ilustrativo**, com selo na imagem e nota no rodapé. O campo mostra "__ g", sem número inventado. Para usar uma receita real do ebook, troque "Nome da receita" e o `__ g` em `html/D03.html` (`id="carbo"`).

## Regras seguidas

- Nenhuma promessa de cura, tratamento, controle de diabetes ou redução da glicose.
- Nada de medo, depoimento, avaliação, preço, desconto ou urgência.
- Nenhuma pessoa triste ou doente. Em D05 aparecem só as mãos de quem cozinha.
- Textos exatamente como no briefing, com acentuação revisada.
- Menor texto da arte: 24 px. Headlines entre 84 e 92 px. Tudo dentro de margens de 56 a 70 px.

## Fotos

Todas são fotos reais do Pixabay, sob a [Licença de Conteúdo Pixabay](https://pixabay.com/service/license-summary/): uso comercial livre, sem atribuição obrigatória. Escolhi de propósito fotos antigas, de 2016 a 2021, anteriores às imagens geradas por IA. Nenhuma foto mostra rosto, para não associar uma pessoa real a uma condição de saúde.

| Arquivo | Fonte | Autor |
|---|---|---|
| `salada-aspargos-ovo.jpg` | https://pixabay.com/photos/asparagus-salad-spring-green-5190463/ | Einladung_zum_Essen |
| `marmita-grao-de-bico.jpg` | https://pixabay.com/photos/salad-chickpeas-carrots-peppers-2724355/ | jereskok |
| `bandeja-cafe.jpg` | https://pixabay.com/photos/breakfast-orange-juice-loaf-1804436/ | Einladung_zum_Essen |
| `torrada-abacate-ovo.jpg` | https://pixabay.com/photos/avocado-breakfast-loaf-toast-egg-1821778/ | Einladung_zum_Essen |
| `frango-legumes.jpg` | https://pixabay.com/photos/chicken-vegetables-meal-food-dish-6484332/ | merakistudio |
| `iogurte-frutas.jpg` | https://pixabay.com/photos/strawberry-dessert-strawberries-2191973/ | RitaE |
| `salmao-legumes.jpg` | https://pixabay.com/photos/food-fish-salmon-meal-plate-3356315/ | pastel100 |
| `frango-arroz-brocolis.jpg` | https://pixabay.com/photos/meal-plate-chicken-rice-broccoli-932985/ | tookapic |
| `ingredientes-tabua.jpg` | https://pixabay.com/photos/avocado-chopping-board-ingredients-1838785/ | Pexels |
| `mesa-madeira.jpg` | https://pixabay.com/photos/background-food-delicious-olives-2068211/ | Daria-Yakovleva |
| `cozinha-pimentao.jpg` | https://pixabay.com/photos/bell-pepper-slicing-culinary-569070/ | JESHOOTS-com |
| `cozinha-maos.jpg` | https://pixabay.com/photos/woman-hands-cutting-vegetables-1207952/ | martinvorel_com |

## Como refazer

```bash
node diabetes-322/render.js      # capa provisória + D01-D05 (usa capa/capa-original.png se existir)
```

Layouts em HTML/CSS (`html/`), estilo em `estilo.css`, com as fontes DM Serif Display e Nunito (OFL) de `producao/fonts`.
