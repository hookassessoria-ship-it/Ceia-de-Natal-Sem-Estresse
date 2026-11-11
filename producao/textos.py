"""Gera textos-anuncios.csv e valida os limites e as regras de honestidade.

    python3 producao/textos.py
"""
import csv
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
NIVEL = {'a': 'a) não sabe que tem o problema', 'b': 'b) sente o problema', 'c': 'c) quer uma solução'}

A = [
    dict(id='C01', onda=1, formato='imagem', angulo='A4 cena do dia 24', nivel='b', cta='Saiba mais',
         gancho='Passou a ceia inteira na cozinha?',
         curto='Passou a ceia inteira na cozinha? Este ano, sente à mesa. Cardápio, lista de compras e cronograma prontos por R$ 19,90.',
         medio='Passou a ceia inteira na cozinha?\nÀs nove da noite, a casa cheia, todo mundo conversando na sala, e a ceia ainda no fogão.\nO guia traz o plano pronto: 3 cardápios para 8 a 10 pessoas, a lista de compras por seção do mercado e o dia 24 hora a hora.\nÀs 18h30, enquanto o peru assa, o momento é seu. R$ 19,90, acesso imediato. 👉 Toque em Saiba mais.',
         lista='Passou a ceia inteira na cozinha? Este ano, sente à mesa. 🎄\n✔ 3 cardápios prontos para 8 a 10 pessoas\n✔ Lista de compras por seção do mercado\n✔ Cronograma do dia 17 ao 25, com o dia 24 hora a hora\n✔ 30 receitas com tempo e rendimento\n✔ Bônus: receitas com as sobras\nR$ 19,90 · PDF de 63 páginas · acesso imediato por e-mail · garantia de 7 dias',
         t1='Este ano, sente à mesa', t2='A ceia planejada por R$ 19,90', desc='Guia em PDF · acesso imediato',
         ref='P3 cena do dia 24 (R02, R04); P1 estrutura com lista'),
    dict(id='C02', onda=1, formato='imagem', angulo='A8 planejar em uma tarde', nivel='c', cta='Comprar agora',
         gancho='Planeje a ceia inteira em uma tarde.',
         curto='Planeje a ceia inteira em uma tarde: escolha o cardápio, imprima a lista e siga o cronograma. Guia em PDF por R$ 19,90.',
         medio='Planeje a ceia inteira em uma tarde.\nUma ceia tranquila não depende de cozinhar mais rápido. Depende de decidir antes.\nNo guia, você escolhe 1 dos 3 cardápios (um teste de 2 minutos ajuda), imprime a lista por seção do mercado e cola o cronograma na geladeira. No dia 24, é só seguir a hora a hora.\nR$ 19,90, acesso imediato por e-mail.',
         lista='Planeje a ceia inteira em uma tarde, em 4 passos:\n✔ Escolha 1 dos 3 cardápios (8 a 10 pessoas)\n✔ Imprima a lista de compras por seção do mercado\n✔ Cole o cronograma do dia 17 ao 25 na geladeira\n✔ No dia 24, siga a hora a hora\n+ 30 receitas, checklist de última hora e bônus das sobras.\nR$ 19,90 · acesso imediato · garantia de 7 dias',
         t1='Planeje a ceia em uma tarde', t2='3 cardápios + lista + cronograma', desc='PDF de 63 páginas',
         ref='P5 antecipação (R16, R17); P6 páginas por dentro'),
    dict(id='C03', onda=1, formato='imagem', angulo='A5 quanto comprar / lista', nivel='c', cta='Comprar agora',
         gancho='Lista de compras pronta, por seção do mercado.',
         curto='Lista de compras da ceia pronta, separada por seção do mercado e com as quantidades para 8 a 10 pessoas. R$ 19,90.',
         medio='Lista de compras pronta, por seção do mercado.\nNada de lista feita de cabeça.\nCada um dos 3 cardápios tem a sua lista: hortifrúti, açougue, frios e laticínios, mercearia e temperos, com as quantidades para 8 a 10 pessoas e caixinhas pra marcar. E o guia separa o que comprar antes e o que deixar pra véspera.\nR$ 19,90, acesso imediato.',
         lista='Lista de compras pronta, por seção do mercado. 🛒\n✔ Hortifrúti, açougue, frios e laticínios, mercearia e temperos\n✔ Quantidades para 8 a 10 pessoas\n✔ Uma lista para cada um dos 3 cardápios\n✔ O que comprar antes e o que deixar pra véspera\n✔ + cronograma, 30 receitas e checklist de última hora\nR$ 19,90 · PDF · acesso imediato por e-mail',
         t1='Lista da ceia pronta, por seção', t2='Imprima e risque no mercado', desc='Para 8 a 10 pessoas',
         ref='P6 mostrar por dentro (R04, R05, R06)'),
    dict(id='C04', onda=1, formato='imagem', angulo='A10 produto por dentro + preço', nivel='c', cta='Comprar agora',
         gancho='3 cardápios prontos para 8 a 10 pessoas.',
         curto='3 cardápios de ceia prontos para 8 a 10 pessoas, com lista de compras e cronograma. 30 receitas por R$ 19,90.',
         medio='3 cardápios prontos para 8 a 10 pessoas: Econômico, Tradicional e Fartura.\nCada um vem com a lista de compras por seção do mercado e o cronograma do dia 17 ao dia 25.\nSão 30 receitas com ingredientes, preparo, tempo, rendimento e uma dica.\nTudo num PDF de 63 páginas por R$ 19,90: menos de R$ 1 por receita. Acesso imediato por e-mail.',
         lista='3 cardápios prontos para 8 a 10 pessoas. 🎄\n✔ Econômico, Tradicional e Fartura\n✔ Lista de compras por seção para cada cardápio\n✔ Cronograma do dia 17 ao 25, com o dia 24 hora a hora\n✔ 30 receitas: 5 entradas, 6 principais, 8 acompanhamentos, 8 sobremesas e 3 bebidas\n✔ Checklist de última hora + bônus das sobras\nR$ 19,90 · menos de R$ 1 por receita · garantia de 7 dias',
         t1='3 cardápios prontos pra ceia', t2='30 receitas + 3 cardápios: R$ 19,90', desc='Acesso imediato por e-mail',
         ref='P1 lista do que vem (R11); P6 mockup + preço (R08, R10)'),
    dict(id='C05', onda=1, formato='imagem', angulo='A7 plano hora a hora', nivel='b', cta='Saiba mais',
         gancho='Dia 24, hora a hora.',
         curto='Dia 24, hora a hora: do café da manhã às 9h até a ceia servida às 22h. Está tudo no guia, por R$ 19,90.',
         medio='Dia 24, hora a hora.\n17h30: peru no forno. 18h30: seu momento, banho e arrumação, enquanto o peru assa. 22h: ceia servida.\nO guia traz o cronograma completo, do dia 17 ao dia 25, para cada tarefa cair no seu dia e o forno chegar livre ao dia 24.\nCom 3 cardápios, lista de compras e 30 receitas. R$ 19,90.',
         lista='Dia 24, hora a hora. Um trecho do guia:\n✔ 09h café da manhã tranquilo; releia o cardápio\n✔ 14h montar a mesa e gelar as bebidas\n✔ 17h30 peru (ou chester) no forno\n✔ 18h30 seu momento: banho e arrumação\n✔ 22h ceia servida\nO cronograma vai do dia 17 ao 25. + 3 cardápios, lista de compras e 30 receitas por R$ 19,90.',
         t1='Dia 24, hora a hora', t2='Ceia servida às 22h, com plano', desc='Cronograma do dia 17 ao 25',
         ref='Oportunidade 1: ninguém mostra o cronograma (R02, R04, R06 só citam)'),
    dict(id='C06', onda=2, formato='imagem', angulo='A3 dia 25 / sobras', nivel='a', cta='Saiba mais',
         gancho='E as sobras? Tem receita pra isso.',
         curto='E as sobras da ceia? O guia tem 4 receitas pro dia 25, do sanduíche de peru à rabanada de panetone.',
         medio='E as sobras? Tem receita pra isso.\nA ceia sempre rende. No dia 25, o que sobrou vira sanduíche de peru ou chester (15 min), risoto (25 min), torta salgada (55 min) ou rabanada de panetone (25 min).\nO bônus também ensina a guardar e requentar farofa, arroz e carnes com segurança.\nVem junto com o guia completo da ceia, por R$ 19,90.',
         lista='E as sobras? Tem receita pra isso. 🎄\n✔ Sanduíche de peru ou chester · 15 min\n✔ Risoto de aproveitamento · 25 min\n✔ Torta salgada de sobras · 55 min\n✔ Rabanada de panetone · 25 min\n✔ Como guardar e requentar com segurança\nBônus do guia Ceia de Natal Sem Estresse, com 3 cardápios, lista e cronograma. R$ 19,90.',
         t1='O dia 25 também resolvido', t2='4 receitas com as sobras da ceia', desc='Bônus do guia da ceia',
         ref='Oportunidade 2: ninguém fala das sobras'),
    dict(id='C07', onda=2, formato='imagem', angulo='A5 quanto comprar', nivel='b', cta='Saiba mais',
         gancho='Quanto comprar pra 10 pessoas?',
         curto='Quanto comprar pra 10 pessoas? O guia da ceia já traz as quantidades, item por item. R$ 19,90.',
         medio='Quanto comprar pra 10 pessoas?\nNo guia, cada cardápio tem a lista com as quantidades para 8 a 10 pessoas. No Econômico, por exemplo: 1 chester de cerca de 3,5 kg, 1,5 kg de batata e 1 kg de arroz.\nVai receber mais gente? É só multiplicar as receitas.\nR$ 19,90, com cronograma e 30 receitas. Acesso imediato.',
         lista='Quanto comprar pra 10 pessoas? Um trecho da lista do cardápio Econômico:\n✔ Chester: 1, de cerca de 3,5 kg\n✔ Batata: 1,5 kg\n✔ Arroz: 1 pacote (1 kg)\n✔ Farinha de mandioca torrada: 500 g\n✔ Creme de leite: 4 caixinhas\nSão 3 cardápios, cada um com sua lista por seção do mercado. R$ 19,90.',
         t1='Quanto comprar pra 10 pessoas', t2='A lista da ceia com quantidades', desc='Para 8 a 10 pessoas',
         ref='P6 página de quantidades (R04); dor da página de vendas'),
    dict(id='C08', onda=1, formato='imagem', angulo='A2 carga mental de decidir', nivel='a', cta='Saiba mais',
         gancho='Já decidiu o cardápio da ceia?',
         curto='Já decidiu o cardápio da ceia? Se ainda não, tem 3 prontos aqui, para 8 a 10 pessoas.',
         medio='Já decidiu o cardápio da ceia?\nO que servir, quanto comprar, o que fazer antes: é muita decisão pra uma noite só.\nO guia traz 3 cardápios fechados (Econômico, Tradicional e Fartura), cada um com lista de compras e cronograma. Um teste de 2 minutos ajuda a escolher.\nR$ 19,90, acesso imediato por e-mail.',
         lista='Já decidiu o cardápio da ceia? Se não, escolha um destes:\n✔ Econômico: simples e cabe no bolso\n✔ Tradicional: os clássicos da ceia\n✔ Fartura: mesa farta\nTodos para 8 a 10 pessoas, com lista de compras por seção e cronograma do dia 17 ao 25.\n+ 30 receitas · R$ 19,90 · garantia de 7 dias',
         t1='Já decidiu o cardápio da ceia?', t2='3 cardápios prontos pra escolher', desc='Com teste pra escolher',
         ref='P4 carga mental (R07, R23); formato nativo de texto (R16, R22, R23)'),
    dict(id='C09', onda=1, formato='imagem', angulo='A6 economia sem promessa de valor', nivel='b', cta='Saiba mais',
         gancho='Tem cardápio econômico pra ceia.',
         curto='Tem cardápio econômico pra ceia: pratos que rendem e ingredientes fáceis de achar, para 8 a 10 pessoas.',
         medio='Tem cardápio econômico pra ceia.\nChester assado com ervas (ou lombo com mostarda e mel), arroz de forno cremoso, farofa de bacon, salada de maionese, canapés, mousse de maracujá e suco natalino.\nDica do guia: compre o chester com antecedência, quando aparecer uma boa oferta, e congele.\nCom lista de compras e cronograma. R$ 19,90.',
         lista='Tem cardápio econômico pra ceia. 🎄\n✔ Pratos que rendem e ingredientes fáceis de achar\n✔ Para 8 a 10 pessoas, com lista de compras própria\n✔ Cerca de 3 horas de cozinha no dia 24\n✔ Dica de quando comprar o chester\n✔ + cardápios Tradicional e Fartura no mesmo guia\nR$ 19,90 · PDF de 63 páginas · acesso imediato',
         t1='Cardápio econômico pra ceia', t2='Ceia para 10 com lista pronta', desc='+ Tradicional e Fartura',
         ref='P7 economia (R03, R07, R09)'),
    dict(id='C10', onda=2, formato='imagem', angulo='A11 garantia', nivel='c', cta='Comprar agora',
         gancho='Teste por 7 dias. Se não gostar, devolvemos.',
         curto='Teste o guia da ceia por 7 dias. Se não for pra você, peça o reembolso pelo e-mail e devolvemos o valor integral.',
         medio='Teste por 7 dias. Se não gostar, devolvemos.\nVocê recebe o PDF por e-mail logo depois da compra. Se achar que não é pra você, peça o reembolso pelo e-mail em até 7 dias e devolvemos o valor integral.\nDentro: 3 cardápios para 8 a 10 pessoas, lista de compras, cronograma e 30 receitas.\nR$ 19,90, pagamento único.',
         lista='Teste por 7 dias. Se não gostar, devolvemos.\n✔ Acesso imediato por e-mail\n✔ 3 cardápios para 8 a 10 pessoas\n✔ Lista de compras por seção e cronograma do dia 17 ao 25\n✔ 30 receitas + bônus das sobras\n✔ Garantia de 7 dias, conforme o Código de Defesa do Consumidor\nR$ 19,90 · pagamento único',
         t1='7 dias de garantia', t2='Teste o guia da ceia por 7 dias', desc='Reembolso integral pelo e-mail',
         ref='Oportunidade 6: garantia só no rodapé (R04, R10, R11)'),
    dict(id='C11', onda=2, formato='imagem', angulo='A10 formato', nivel='c', cta='Comprar agora',
         gancho='Seu guia da ceia no celular.',
         curto='Seu guia da ceia no celular, ou impresso na porta da geladeira. PDF de 63 páginas, acesso imediato. R$ 19,90.',
         medio='Seu guia da ceia no celular. Ou impresso na porta da geladeira.\nÉ um PDF de 63 páginas que chega por e-mail logo depois da compra. Dá pra consultar no mercado, riscar a lista impressa e deixar o cronograma à vista na cozinha.\n3 cardápios para 8 a 10 pessoas, 30 receitas e o dia 24 hora a hora.\nR$ 19,90.',
         lista='Seu guia da ceia no celular. 📲\n✔ PDF de 63 páginas, por e-mail na hora\n✔ Leia no celular ou imprima\n✔ 3 cardápios e listas de compras com caixinhas\n✔ Cronograma pra deixar na porta da geladeira\n✔ 30 receitas com tempo e rendimento\nR$ 19,90 · garantia de 7 dias',
         t1='O guia da ceia no seu celular', t2='PDF com acesso imediato', desc='Ou impresso na geladeira',
         ref='P6 mostrar o produto; "passo a passo no seu celular" (R02, R07)'),
    dict(id='C12', onda=2, formato='imagem', angulo='A4 contraste', nivel='b', cta='Saiba mais',
         gancho='Ceia improvisada x ceia planejada.',
         curto='Ceia improvisada: tudo no dia 24. Ceia planejada: cada coisa no seu dia. O plano está pronto no guia.',
         medio='Ceia improvisada x ceia planejada.\nNa improvisada, o cardápio é decidido de cabeça, a volta ao mercado acontece na véspera e tudo precisa ficar pronto na mesma hora.\nNa planejada, a lista já está pronta, as sobremesas geladas saem no dia 23 e às 18h30 o momento é seu.\nO plano vem pronto no guia. R$ 19,90.',
         lista='Ceia improvisada x ceia planejada. O guia traz o plano:\n✔ 3 cardápios fechados para 8 a 10 pessoas\n✔ Lista de compras por seção do mercado\n✔ O que adiantar 1 semana antes, 3 dias antes e no dia 23\n✔ Dia 24 hora a hora\n✔ 30 receitas e checklist de última hora\nR$ 19,90 · acesso imediato',
         t1='Cada coisa no seu dia', t2='A ceia planejada, por R$ 19,90', desc='Cronograma do dia 17 ao 25',
         ref='P3 cena (R04); contraste de categoria (R20, R22)'),
    dict(id='C13', onda=1, formato='vídeo', angulo='A1 erro comum / educativo', nivel='a', cta='Saiba mais',
         gancho='3 mudanças pra sair da cozinha na ceia.',
         curto='3 mudanças pra sair da cozinha na ceia. A 3ª é a melhor: às 18h30, enquanto o peru assa, o momento é seu.',
         medio='3 mudanças pra sair da cozinha na ceia:\n1. Decida o cardápio uma semana antes e já compre o que não estraga.\n2. No dia 23, deixe prontas as sobremesas geladas, a farofa e o salpicão.\n3. No dia 24, siga um cronograma hora a hora.\nEsse plano vem pronto no guia Ceia de Natal Sem Estresse, por R$ 19,90.',
         lista='3 mudanças pra sair da cozinha na ceia. O guia já traz:\n✔ Cardápio escolhido uma semana antes (3 opções)\n✔ Lista de compras por seção do mercado\n✔ O que adiantar no dia 23\n✔ Dia 24 hora a hora, com a ceia às 22h\n✔ 30 receitas para 8 a 10 pessoas\nR$ 19,90 · acesso imediato por e-mail',
         t1='3 mudanças pra sair da cozinha', t2='O plano da ceia, pronto', desc='Do dia 17 ao dia 25',
         ref='P4 erro comum/educativo (R03: 7 primeiras posições)'),
    dict(id='C14', onda=1, formato='vídeo', angulo='A7 plano hora a hora', nivel='b', cta='Saiba mais',
         gancho='Dia 24, hora a hora.',
         curto='18h30: banho e arrumação, enquanto o peru assa. 22h: ceia servida. O dia 24 hora a hora está no guia.',
         medio='Dia 24, hora a hora, com a ceia servida às 22h.\n9h café tranquilo. 14h mesa montada e bebidas gelando. 17h30 peru no forno. 18h30 seu momento: banho e arrumação. 21h40 velas acesas.\nO guia traz esse cronograma completo e o plano do dia 17 ao 25, com 3 cardápios, lista de compras e 30 receitas.\nR$ 19,90.',
         lista='Dia 24, hora a hora. Trecho real do guia:\n✔ 09h café da manhã tranquilo\n✔ 12h almoço leve (cozinhar com fome não dá certo!)\n✔ 17h30 peru no forno, coberto com papel-alumínio\n✔ 18h30 seu momento: banho e arrumação\n✔ 22h ceia servida\n+ 3 cardápios, lista de compras e 30 receitas. R$ 19,90.',
         t1='Dia 24, hora a hora', t2='18h30: o seu momento', desc='Ceia servida às 22h',
         ref='Oportunidade 1 (cronograma como protagonista); P8 vídeo vertical'),
    dict(id='C15', onda=1, formato='vídeo', angulo='A9 clareza em vez de volume', nivel='c', cta='Comprar agora',
         gancho='Você não precisa de 300 receitas.',
         curto='Você não precisa de 300 receitas. Precisa de um cardápio fechado, com lista e cronograma. São 3, por R$ 19,90.',
         medio='Você não precisa de 300 receitas. Precisa de um cardápio fechado.\nNo guia são 3: Econômico (cerca de 3 horas de cozinha no dia 24), Tradicional (cerca de 5) e Fartura (cerca de 7), todos para 8 a 10 pessoas.\nCada um com lista de compras e cronograma. São 30 receitas no total.\nR$ 19,90: menos de R$ 1 por receita.',
         lista='Você não precisa de 300 receitas. Precisa de um plano:\n✔ 3 cardápios fechados para 8 a 10 pessoas\n✔ 30 receitas com tempo e rendimento\n✔ Lista de compras por seção para cada cardápio\n✔ Cronograma do dia 17 ao 25\n✔ Teste de 2 minutos para escolher o seu\nR$ 19,90 · menos de R$ 1 por receita',
         t1='Não precisa de 300 receitas', t2='3 cardápios fechados: R$ 19,90', desc='Menos de R$ 1 por receita',
         ref='Oportunidade 3: contraste com P2 (volume em R01, R02, R05, R09)'),
    dict(id='C16', onda=1, formato='vídeo', angulo='A1 erro comum / educativo', nivel='a', cta='Saiba mais',
         gancho='O erro nº 1 da ceia: deixar tudo pra véspera.',
         curto='O erro nº 1 da ceia é deixar tudo pra véspera: o forno não dá conta de tudo na mesma hora. Veja o que dá pra adiantar.',
         medio='O erro nº 1 da ceia: deixar tudo pra véspera.\nO que dá pra adiantar: uma semana antes, escolher o cardápio e comprar o que não estraga. No dia 21, passar o peru do congelador pra geladeira. No dia 23, sobremesas geladas, farofa e salpicão prontos.\nAssim o forno chega livre ao dia 24.\nEsse cronograma está no guia, por R$ 19,90.',
         lista='O erro nº 1 da ceia: deixar tudo pra véspera. O guia divide assim:\n✔ 17 ou 18/12: cardápio escolhido e compras do que não estraga\n✔ 21/12: peru do congelador pra geladeira, gelo extra\n✔ 23/12: sobremesas geladas, farofa e salpicão\n✔ 24/12: hora a hora, com a ceia às 22h\n✔ 25/12: sobras guardadas e reaproveitadas\nR$ 19,90 · 3 cardápios · 30 receitas',
         t1='O que adiantar antes da ceia', t2='O forno livre no dia 24', desc='Cronograma do dia 17 ao 25',
         ref='P4 erro comum (R03); P5 antecipação (R16, R17)'),
    dict(id='C17', onda=2, formato='vídeo', angulo='A5 lista / quanto comprar', nivel='b', cta='Saiba mais',
         gancho='Esqueceu o creme de leite?',
         curto='Esqueceu o creme de leite e voltou ao mercado na véspera? Com a lista por seção, cada item tem o seu lugar.',
         medio='Esqueceu o creme de leite?\nLista feita de cabeça costuma deixar alguma coisa pra trás.\nNo guia, cada cardápio tem a lista separada por seção do mercado (hortifrúti, açougue, frios e laticínios, mercearia e temperos), com as quantidades para 8 a 10 pessoas e caixinhas pra marcar.\nR$ 19,90, com cronograma e 30 receitas.',
         lista='Esqueceu o creme de leite? A lista do guia separa tudo por seção:\n✔ Hortifrúti\n✔ Açougue e peixaria\n✔ Frios e laticínios (o creme de leite está aqui: 4 caixinhas)\n✔ Mercearia\n✔ Temperos e extras\nCom as quantidades para 8 a 10 pessoas. R$ 19,90 · acesso imediato',
         t1='A lista da ceia por seção', t2='Lista pronta, com quantidades', desc='Para 8 a 10 pessoas',
         ref='P3 cena específica (dor da página de vendas); P6 lista por dentro (R04)'),
    dict(id='C18', onda=1, formato='vídeo', angulo='A10 produto por dentro', nivel='c', cta='Comprar agora',
         gancho='O que vem dentro do guia.',
         curto='Veja por dentro: 3 cardápios, lista de compras, cronograma, 30 receitas, bônus das sobras e checklist. R$ 19,90.',
         medio='O que vem dentro do guia Ceia de Natal Sem Estresse:\n3 cardápios para 8 a 10 pessoas, uma lista de compras por seção para cada um, o cronograma do dia 17 ao 25 com o dia 24 hora a hora, 30 receitas com tempo e rendimento, o checklist de última hora e o bônus das sobras.\n63 páginas, R$ 19,90, acesso imediato por e-mail.',
         lista='O que vem dentro do guia: 🎄\n✔ 3 cardápios: Econômico, Tradicional e Fartura\n✔ Listas de compras por seção do mercado\n✔ Cronograma do dia 17 ao 25, com o dia 24 hora a hora\n✔ 30 receitas com ingredientes, preparo, tempo, rendimento e dica\n✔ Checklist de última hora\n✔ Bônus: receitas com as sobras\n63 páginas · R$ 19,90 · garantia de 7 dias',
         t1='Veja o guia da ceia por dentro', t2='63 páginas por R$ 19,90', desc='Acesso imediato por e-mail',
         ref='P1 lista do que vem (R11); P6 páginas por dentro (R05, R06)'),
    dict(id='C19', onda=2, formato='vídeo', angulo='A3 dia 25 / sobras', nivel='a', cta='Saiba mais',
         gancho='3 ideias com as sobras da ceia.',
         curto='3 ideias com as sobras da ceia: sanduíche de peru (15 min), risoto (25 min) e rabanada de panetone (25 min).',
         medio='3 ideias com as sobras da ceia:\n1. Sanduíche de peru ou chester, em 15 minutos.\n2. Risoto de aproveitamento, em 25.\n3. Rabanada de panetone, em 25.\nImportante: sobras na geladeira em até 2 horas depois da ceia.\nAs receitas estão no bônus do guia, junto com os 3 cardápios. R$ 19,90.',
         lista='3 ideias com as sobras da ceia (e uma quarta no guia):\n✔ Sanduíche de peru ou chester · 15 min\n✔ Risoto de aproveitamento · 25 min\n✔ Rabanada de panetone · 25 min\n✔ Torta salgada de sobras · 55 min\n✔ Como guardar e requentar com segurança\nBônus do guia completo da ceia · R$ 19,90',
         t1='O que fazer com as sobras', t2='O dia 25 também resolvido', desc='Bônus do guia da ceia',
         ref='Oportunidade 2 (sobras); P4 educativo'),
    dict(id='C20', onda=2, formato='vídeo', angulo='A8 planejar em uma tarde', nivel='c', cta='Comprar agora',
         gancho='Planeje a ceia em uma tarde: 4 passos.',
         curto='Planeje a ceia em uma tarde: escolha o cardápio, imprima a lista, cole o cronograma e siga a hora a hora.',
         medio='Planeje a ceia em uma tarde, em 4 passos:\n1. Escolha um dos 3 cardápios.\n2. Imprima a lista de compras por seção.\n3. Cole o cronograma na geladeira.\n4. No dia 24, siga a hora a hora.\nTudo isso vem pronto no guia, por R$ 19,90.',
         lista='Planeje a ceia em uma tarde. O guia traz:\n✔ 3 cardápios para 8 a 10 pessoas (+ teste de 2 minutos)\n✔ Listas de compras por seção do mercado\n✔ Cronograma do dia 17 ao 25\n✔ Dia 24 hora a hora\n✔ 30 receitas + bônus das sobras\nR$ 19,90 · acesso imediato · garantia de 7 dias',
         t1='A ceia planejada em 4 passos', t2='Planeje hoje, sente à mesa dia 24', desc='PDF com acesso imediato',
         ref='P5 antecipação (R16, R17); P1 estrutura'),
]

PROIBIDO = [r'estressad', r'cansad', r'sem dinheiro', r'só hoje', r'últim[ao]s? (vagas|unidades)', r'⭐', r'estrela',
            r'garantid[ao]', r'compraram', r'vendid', r'depoimento', r'antes e depois', r'economize R\$', r'(?<!menos )\bde R\$ ?\d+ por',
            r'order bump', r'upsell']
EMOJI = re.compile('[\U0001F300-\U0001FAFF\u2600-\u26FF]')

erros = []
for a in A:
    for campo in ('curto', 'medio', 'lista'):
        txt = a[campo]
        l1 = txt.split('\n')[0]
        if len(l1) > 125:
            erros.append(f"{a['id']} {campo}: 1ª linha com {len(l1)} caracteres (máx. 125)")
        if len(EMOJI.findall(txt)) > 3:
            erros.append(f"{a['id']} {campo}: mais de 3 emojis")
        for p in PROIBIDO:
            if re.search(p, txt, re.I):
                erros.append(f"{a['id']} {campo}: termo proibido '{p}'")
    for campo, lim in (('t1', 40), ('t2', 40), ('desc', 30)):
        if len(a[campo]) > lim:
            erros.append(f"{a['id']} {campo}: {len(a[campo])} caracteres (máx. {lim})")
    if a['cta'] not in ('Comprar agora', 'Saiba mais'):
        erros.append(f"{a['id']}: CTA inválido")

if erros:
    print('\n'.join(erros))
    sys.exit(1)

saida = RAIZ / 'textos-anuncios.csv'
with open(saida, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['id', 'onda', 'formato', 'angulo', 'nivel_consciencia', 'gancho', 'texto_curto', 'texto_medio', 'texto_lista',
                'titulo_1', 'titulo_2', 'descricao', 'cta', 'arquivo', 'utm_content', 'referencia_da_pesquisa'])
    for a in A:
        arq = f"criativos/imagens/{a['id']}.png" if a['formato'] == 'imagem' else f"criativos/videos/{a['id']}.mp4"
        w.writerow([a['id'], a['onda'], a['formato'], a['angulo'], NIVEL[a['nivel']], a['gancho'], a['curto'], a['medio'], a['lista'],
                    a['t1'], a['t2'], a['desc'], a['cta'], arq, a['id'], a['ref']])
print(f'ok: {len(A)} anúncios em {saida.relative_to(RAIZ)}')
