# CHECKLIST · Site Black Friday (Ceia de Natal Sem Estresse)

Branch: `site-black-friday` (criada a partir do `main`). Sem PR e sem deploy em produção: só preview.

## Como rodar

```bash
cd site
node build.mjs        # gera dist/ a partir de src/ + site.config.json
```

A Vercel roda o mesmo comando (`vercel.json`). Se um campo obrigatório estiver vazio, o build falha e diz qual.

## O que foi feito

- [x] Página reorganizada na ordem pedida: hero, dor, o que vem no guia, 3 bônus, card de oferta (#oferta), como funciona, perguntas frequentes, CTA final e rodapé.
- [x] Faixa e selo de Black Friday (selo pulsando de leve). Somem sozinhos depois de `PROMO_END`.
- [x] Todos os botões "Quero o guia" rolam até `#oferta`. Só o botão de dentro do card leva ao checkout da Kirvano.
- [x] Barra fixa no celular: rola até `#oferta` e some quando o card está na tela.
- [x] Card de oferta ("ticket"): guia + 3 bônus com selo GRÁTIS, "de R$ 39,90 por R$ 19,90", preço grande, contagem regressiva real até `PROMO_END`, botão para o checkout, selos (acesso por e-mail, pagamento seguro pela Kirvano) e garantia de 7 dias com o selo recortado em fundo transparente e efeito 3D.
- [x] Depois de `PROMO_END` (testado simulando 01/12/2026): preço vira R$ 39,90; faixa, "de/por" e contagem somem.
- [x] `SHOW_BONUS_VALUES` (padrão `false`): com `true`, mostra os valores riscados (R$ 14,90 / 18,90 / 11,90) e a soma "Valor percebido · os 4 e-books" (R$ 85,60). Testado nos dois modos.
- [x] Parcelamento só aparece se `INSTALLMENTS_TEXT` for preenchido (hoje vazio).
- [x] 4 vídeos (C30 no hero, C24 na dor, C27 em "o que vem", C32 no final): mudos, em loop, com poster, carregados só perto da tela. Comprimidos para 540x960 sem áudio: 204 a 421 KB cada.
- [x] Pixel antigo removido de todas as páginas. Pixel novo `1205067451580311` com PageView em todas as páginas e ViewContent quando o card de oferta aparece. Nenhum InitiateCheckout ou Purchase no site.
- [x] Script de UTMs da Utmify no `<head>` (decodificado: carrega `cdn.utmify.com.br/scripts/utms/latest.js`).
- [x] Link do checkout preserva todos os parâmetros da URL de entrada, sem duplicar.
- [x] Rodapé sem nome, CNPJ e e-mail: "Cantinho do Lar · Material digital para imprimir. Nada é enviado pelo correio." (também em termos, privacidade e contato).
- [x] Termos e página de obrigado atualizados: 3 bônus liberados no 8º dia após a compra.
- [x] Animações leves (revelar ao rolar, capas flutuando, números subindo, brilho no botão, selo pulsando), desligadas com `prefers-reduced-motion`.

## Controle de qualidade (feito)

- [x] Grep no `dist/` por PREENCHER, lorem, XXX, TODO, 1152510153974851 e álcool: zero (o build também falha se aparecer).
- [x] Capturas página inteira em 390x844 e 1440x900, olhadas trecho a trecho. Corrigido: vídeos sumindo no desktop, cards de bônus estourando a largura, faixa quebrando em 2 linhas, vídeo cortando texto.
- [x] Sem rolagem lateral; sem erro no console.
- [x] Botão do topo rola até o card; botão do card leva ao checkout com UTMs; contagem anda; troca de preço após `PROMO_END`; barra fixa.
- [x] Peso inicial no celular: cerca de 1 MB (inclui o vídeo do hero, que carrega depois da página).

## Variáveis (`site/site.config.json`)

| Campo | Valor atual | Obrigatório |
|---|---|---|
| `CHECKOUT_URL` | link atual da Kirvano | sim |
| `PIXEL_ID` | 1205067451580311 | sim |
| `PROMO_END` | 2026-11-30T23:59:59-03:00 | sim |
| `PROMO_PRICE` / `REGULAR_PRICE` | 19,90 / 39,90 | sim |
| `INSTALLMENTS_TEXT` | vazio (não mostra parcelamento) | não |
| `GUARANTEE_DAYS` / `BONUS_RELEASE_DAY` | 7 / 8 | sim |
| `SHOW_BONUS_VALUES` | true (ligado em 18/11 a seu pedido) | sim (true/false) |
| `BONUS_VALUES` | 14,90 / 18,90 / 11,90 | só se `SHOW_BONUS_VALUES` for true |
| `SUPPORT_EMAIL`, `SITE_URL` | preenchidos | sim |

## Pendências e decisões suas

- [ ] **Preço âncora:** "de R$ 39,90 por R$ 19,90" foi mantido por decisão sua. O guia é vendido a R$ 19,90 desde 09/11 e ainda não foi vendido a R$ 39,90. Pelas regras de preço de referência (CDC e Procon), o risco dessa âncora é seu.
- [ ] **01/12:** o site passa sozinho a mostrar R$ 39,90, mas o checkout continua no mesmo link. Lembrar de mudar o preço da oferta na Kirvano.
- [ ] **Ordem dos valores dos bônus** (Brincadeiras R$ 14,90 / Sobras R$ 18,90 / Ceia Econômica R$ 11,90): confirmar antes de ligar `SHOW_BONUS_VALUES`.
- [ ] **Parcelamento:** o checkout mostrava "4x de R$ 5,75". Se quiser exibir, preencher `INSTALLMENTS_TEXT` com o texto exato da Kirvano.
- [ ] **Bônus:** confirmar que os 3 PDFs (13 brincadeiras, 11 receitas + guia de conservação, cardápio para 8 pessoas) existem e que a Kirvano libera no 8º dia. As frases da página vêm das capas.
- [ ] **Pixel novo:** conferir no Gerenciador de Eventos se o PageView do `1205067451580311` chega depois de publicar.
- [ ] **Produção:** quando aprovar o preview, publicar com `npx vercel --prod` dentro de `site/` (projeto `cantinho-ceia`).
