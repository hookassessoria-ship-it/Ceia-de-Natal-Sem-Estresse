# VSL da página (opcional)

| Arquivo | O que é |
|---|---|
| `vsl-ceia-720p.mp4` | VSL de 85 s, 720x1280 (vertical), H.264 + AAC, abaixo de 3 MB, legenda queimada |
| `vsl-poster.jpg` | Poster (capa do guia + preço), mostrado antes do toque |

**O site não foi alterado.** Para usar, coloque o vídeo **abaixo da dobra** (nunca no topo), sem autoplay e carregando só quando a pessoa tocar:

```html
<video controls playsinline preload="none" poster="vsl-poster.jpg" width="360" style="max-width:100%;height:auto">
  <source src="vsl-ceia-720p.mp4" type="video/mp4">
</video>
```

`preload="none"` faz o navegador baixar só o poster; o MP4 só é baixado quando a pessoa toca no play.

## Roteiro (fatos da página de vendas e das páginas reais do guia)

1. Todo ano, a ceia de Natal chega do mesmo jeito: tudo pra decidir na última hora.
2. Quanto comprar, o que preparar... e o forno que não dá conta no dia vinte e quatro.
3. O problema não é você. É fazer tudo de cabeça, na última hora. *(frase da própria página)*
4. O guia Ceia de Natal Sem Estresse põe cada coisa no seu dia.
5. São trinta receitas de casa, com ingredientes de mercado, e três cardápios pra oito a dez pessoas: Econômico, Tradicional e Fartura.
6. Cada cardápio tem lista de compras por seção do mercado, com as quantidades.
7. E um cronograma do dia dezessete ao vinte e cinco. Dia dezessete, escolhe o cardápio. Dia vinte e um, o peru vai do congelador pra geladeira. Dia vinte e três, sobremesa, farofa e salpicão prontos.
8. No dia vinte e quatro, o guia vai hora a hora... e às dezoito e trinta, o peru já tá assando.
9. E ainda tem três bônus: Brincadeiras e Jogos para a Festa, Receitas com as Sobras da Ceia, e Ceia Econômica.
10. É um PDF de sessenta e três páginas. Dá pra ler no celular, no computador ou imprimir.
11. E você tem sete dias de garantia: se não for pra você, pede o reembolso.
12. Dezenove e noventa até trinta de novembro. Garante agora, guarda no celular e abre dia dezessete.

Esta locução foi escrita por mim, para você revisar. O botão desenhado no fim do vídeo diz "Quero o guia", o mesmo texto do botão da página. Depois de 30/11, a fala 12 fica desatualizada: tire o vídeo da página ou gere outra fala final.

Para refazer: `node producao/render.js warp VSL '[[0,0],[85.6,85.6]]' /tmp/claude-0/vsl/vsl_base.mp4`, depois `python3 producao/audio/mixar.py VSL` e `producao/audio/vsl_final.sh`. O caminho do vídeo-base está em `producao/audio/roteiro.py`.
