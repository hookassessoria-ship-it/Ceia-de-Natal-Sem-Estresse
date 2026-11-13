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

# ---------------------------------------------------------------------------------------------
# Série de objeções (C21 a C32). Texto principal = coluna texto_medio. Todos com CTA "Saiba mais".
# Cada afirmação foi conferida contra FATOS.md.
# ---------------------------------------------------------------------------------------------
B = [
    dict(id='C21', nome='Eu de novembro', objecao='OBJ1 Ainda é novembro', angulo='OBJ1a o eu do dia 24 agradece o eu de novembro', nivel='b', formato='imagem',
         gatilho='Autocontinuidade (o eu do futuro) + estado final',
         gancho='Um bilhete do seu dia 24: valeu, novembro.',
         curto='Um bilhete do seu dia 24 para você, hoje: valeu. Às 18h30, o peru assa e você toma banho com calma.',
         medio='Um bilhete do seu dia 24 para você, hoje: valeu.\n18h30, o peru assando e você no banho, com calma. Esse horário está no cronograma do guia.\nPlanejar em novembro costuma deixar o dia 24 mais leve.\n3 cardápios para 8 a 10 pessoas, lista de compras e o dia 24 hora a hora, por R$ 19,90.',
         lista='Um bilhete do seu dia 24: valeu, novembro.\n• Cardápio escolhido com antecedência (3 opções, para 8 a 10 pessoas)\n• Lista de compras por seção do mercado\n• Cronograma do dia 17 ao 25\n• Dia 24 hora a hora, com o seu momento às 18h30\nR$ 19,90, acesso imediato por e-mail.',
         t1='Um bilhete do seu dia 24', t2='Planeje em novembro, respire no dia 24', t3='18h30 do dia 24: você no banho', desc='Guia em PDF · R$ 19,90',
         alt=['Seu dia 24 mandou um recado.', 'O favor que novembro faz pro dia 24.', '18h30 do dia 24: peru no forno, você no banho.'],
         ref='P3 cena do dia 24 (R02, R04); oportunidade 1 (cronograma)'),
    dict(id='C22', nome='Aos poucos', objecao='OBJ1 Ainda é novembro', angulo='OBJ1b comprar aos poucos pesa menos', nivel='b', formato='imagem',
         gatilho='Aversão à perda (o aperto de comprar tudo de uma vez) + especificidade das datas',
         gancho='Aos poucos, a ceia pode pesar menos.',
         curto='Aos poucos, a ceia pode pesar menos no bolso: a carne na oferta, com antecedência; os secos no dia 17; pão e gelo no dia 24.',
         medio='Aos poucos, a ceia pode pesar menos no bolso.\nComprar tudo de uma vez, na semana do Natal, costuma apertar. O guia sugere comprar o chester ou o lombo com antecedência, quando aparecer uma boa oferta, e congelar.\nE a lista separa o que comprar antes e o que deixar para a véspera.\n3 cardápios para 8 a 10 pessoas, por R$ 19,90.',
         lista='Aos poucos, a ceia pode pesar menos.\n• Com antecedência: o chester ou o lombo, quando aparecer uma boa oferta, direto pro congelador\n• 17 ou 18/12: o que não estraga\n• 24/12, 10h: pão, gelo e frutas\nTudo com a lista de compras por seção do guia. R$ 19,90.',
         t1='Aos poucos pode pesar menos', t2='A carne na oferta, o resto no dia certo', t3='Compre a ceia aos poucos, com lista', desc='Lista do que comprar antes',
         alt=['A ceia não precisa caber numa compra só.', 'Novembro: a carne. Dezembro: o resto.', 'Comprar aos poucos também é planejar.'],
         ref='P7 economia sem prometer valor (R03, R07)'),
    dict(id='C23', nome='Ainda é novembro', objecao='OBJ1 Ainda é novembro', angulo='OBJ1c o que o cronograma marca, desde já', nivel='b', formato='imagem',
         gatilho='Reenquadramento da objeção + especificidade (datas reais do cronograma)',
         gancho='Ainda é novembro? Ótimo.',
         curto='Ainda é novembro? Ótimo. Escolha o cardápio agora e chegue a dezembro com cada dia marcado.',
         medio='Ainda é novembro? Ótimo: dá tempo de fazer do jeito tranquilo.\nO cronograma do guia marca cada etapa: compras na semana do dia 17, o peru indo do congelador para a geladeira no dia 21, sobremesas, farofa e salpicão prontos no dia 23.\nNo dia 24, é seguir a hora a hora.\nEscolha o cardápio agora. R$ 19,90, acesso imediato por e-mail.',
         lista='Ainda é novembro? Ótimo. O que o cronograma do guia marca:\n• 17 ou 18/12: compras do que não estraga\n• 21/12: peru do congelador para a geladeira\n• 23/12: sobremesas, farofa e salpicão prontos\n• 24/12: hora a hora, com a ceia às 22h\nR$ 19,90.',
         t1='Ainda é novembro. Ótimo.', t2='Seu dezembro, com cada dia marcado', t3='Escolha hoje, siga o cronograma depois', desc='Cronograma do dia 17 ao 25',
         alt=['Dá tempo. E é agora que dá.', 'Faltam semanas. Perfeito pra planejar.', 'Dezembro com cada coisa no seu dia.'],
         ref='P5 urgência real e antecipação (R16, R17)'),
    dict(id='C24', nome='Mercado no dia 24', objecao='OBJ1 Ainda é novembro', angulo='OBJ1d dia 24 no mercado x dia 24 tranquilo', nivel='b', formato='vídeo',
         gatilho='Contraste vivido (correria x calma) + aversão à perda (a manhã perdida no mercado)',
         gancho='24/12, 10h. Fila do mercado.',
         curto='24/12, 10h: fila do mercado ou só pão, gelo e frutas? A diferença é o plano.',
         medio='24 de dezembro, 10h, fila do mercado.\nOu: 24 de dezembro, 10h, só pão, gelo e frutas, porque o resto já foi comprado antes.\nA diferença é o plano: lista de compras por seção e cronograma do dia 17 ao 25.\nNo guia, por R$ 19,90.',
         lista='24/12, 10h: só pão, gelo e frutas. Porque antes vieram:\n• A lista de compras por seção do mercado\n• As compras do que não estraga, na semana do dia 17\n• O dia 24 hora a hora, das 9h às 23h30\nGuia Ceia de Natal Sem Estresse, R$ 19,90.',
         t1='Dia 24: só pão, gelo e frutas', t2='O mercado fica pra antes do dia 24', t3='10h do dia 24: fila ou café?', desc='Lista e cronograma prontos',
         alt=['Dia 24, 10h: fila ou café?', 'O que fica pra véspera: pão, gelo e frutas.', '24/12, 10h. Onde você quer estar?'],
         ref='P3 cena do dia 24; contraste (C12 era imagem, este é vídeo com horário)'),
    dict(id='C25', nome='Ceia de sempre', objecao='OBJ2 Eu já sei fazer', angulo='OBJ2a mesma ceia de sempre, sem a correria', nivel='a', formato='imagem',
         gatilho='Estado final + preservação de identidade (você continua quem cozinha)',
         gancho='A ceia de sempre. Sem a correria.',
         curto='A ceia de sempre, sem a correria de sempre. Você cozinha; o guia organiza o dia.',
         medio='A ceia de sempre, sem a correria de sempre.\nVocê já sabe cozinhar. O que costuma apertar é a ordem: o que comprar antes, o que adiantar no dia 23, o que vai ao forno e a que horas.\nO guia organiza isso em 3 cardápios prontos para 8 a 10 pessoas, com cronograma do dia 17 ao 25 e lista de compras por seção.\nR$ 19,90.',
         lista='A ceia de sempre. Sem a correria.\n• Cronograma do dia 17 ao 25\n• Dia 24 hora a hora, das 9h às 23h30\n• Lista de compras por seção, com quantidades\n• Checklist de última hora com 14 itens\nR$ 19,90, acesso imediato por e-mail.',
         t1='A ceia de sempre, sem correria', t2='Você cozinha, o guia organiza', t3='O dia 24 em ordem, das 9h às 23h30', desc='Cronograma e lista prontos',
         alt=['Você já sabe fazer. Falta o dia 24 tranquilo.', 'Não é receita que falta. É hora marcada.', 'A mesma noite, sem correr.'],
         ref='P3 cena; oportunidade 1'),
    dict(id='C26', nome='Também senta à mesa', objecao='OBJ2 Eu já sei fazer', angulo='OBJ2b quem cozinha também quer sentar à mesa', nivel='a', formato='imagem',
         gatilho='Identidade (quem cozinha também é convidado) + aversão à perda (a conversa à mesa)',
         gancho='Quem cozinha também senta à mesa.',
         curto='Quem cozinha também senta à mesa. Com o dia 24 hora a hora, às 18h30 o momento é seu.',
         medio='Quem faz a ceia também é convidado.\nEm muita casa, a conversa acontece na sala e quem cozinha só escuta de longe. Com o dia 24 hora a hora, às 18h30 o peru assa e o momento é seu.\nNo checklist do guia tem até “lugar de cada convidado definido”. O seu também.\nR$ 19,90, acesso imediato.',
         lista='Quem cozinha também senta à mesa.\n• 18h30: banho e arrumação, enquanto o peru assa\n• 21h40: velas acesas, travessas na mesa\n• 22h: ceia servida\n• No checklist: lugar de cada convidado definido\nR$ 19,90.',
         t1='Quem cozinha também senta à mesa', t2='Um lugar reservado pra quem cozinhou', t3='Este ano, a conversa é com você', desc='Dia 24 hora a hora',
         alt=['Quem fez a ceia também é convidado.', 'A conversa é na sala. E quem cozinha?', 'Lugar marcado pra quem cozinhou.'],
         ref='P3 cena (R04); C01 tratava a dor, este trata identidade'),
    dict(id='C27', nome='O que dá errado', objecao='OBJ2 Eu já sei fazer', angulo='OBJ2c o que dá errado até pra quem sabe', nivel='a', formato='vídeo',
         gatilho='Especificidade (dado real do guia) + reconhecimento + aversão à perda',
         gancho='Você sabe fazer o peru. Mas sabe quando tirar do congelador?',
         curto='Você sabe fazer o peru. Mas sabia que um de 5 kg leva de 2 a 3 dias para descongelar na geladeira?',
         medio='Você sabe fazer o peru. Mas sabe quando tirar do congelador?\nUm peru de 5 kg leva de 2 a 3 dias para descongelar na geladeira. E no dia 24, às 21h, o forno é um só para tudo.\nO que costuma dar errado não é a receita. É a ordem.\nO guia traz o cronograma do dia 17 ao 25, com o dia 24 hora a hora. R$ 19,90.',
         lista='Até quem sabe fazer tropeça na ordem:\n• Peru de 5 kg: de 2 a 3 dias descongelando na geladeira\n• 21/12: hora de passar o peru do congelador para a geladeira\n• 23/12: sobremesas, farofa e salpicão prontos\n• 24/12: o forno com hora marcada\nTudo no cronograma do guia. R$ 19,90.',
         t1='Saber fazer não é o problema', t2='Peru de 5 kg: 2 a 3 dias pra descongelar', t3='O que dá errado até pra quem sabe', desc='Cronograma do dia 17 ao 25',
         alt=['Quando tirar o peru do congelador?', 'Quem sabe fazer também corre no dia 24.', 'A receita você sabe. E o horário?'],
         ref='P4 erro comum (R03); oportunidade 4 (educar com o guia)'),
    dict(id='C28', nome='Falta o plano', objecao='OBJ2 Eu já sei fazer', angulo='OBJ2d reconhecimento: faz tudo certo, falta organizar', nivel='a', formato='imagem',
         gatilho='Reconhecimento (validação de quem já sabe) + especificidade (18 horários)',
         gancho='Você sabe fazer tudo. Falta o plano.',
         curto='Você sabe fazer tudo. Falta só o plano: o dia 24 em 18 horários, das 9h às 23h30.',
         medio='Você sabe fazer tudo. Falta só o plano.\nNão é falta de prática: é tudo no mesmo dia, ao mesmo tempo. O guia distribui a ceia do dia 17 ao 25 e põe o dia 24 em ordem, em 18 horários, das 9h às 23h30.\nCom lista de compras por seção e quantidades para 8 a 10 pessoas.\nR$ 19,90, acesso imediato por e-mail.',
         lista='Você sabe fazer tudo. O guia entra com o plano:\n• Dia 24 em 18 horários, das 9h às 23h30\n• Cronograma do dia 17 ao 25\n• Lista de compras por seção, com quantidades\n• Checklist de última hora\nR$ 19,90.',
         t1='Você sabe fazer. Falta o plano.', t2='O dia 24 em 18 horários', t3='Prática você tem. Falta a ordem.', desc='Dia 24 hora a hora',
         alt=['Prática não falta. Falta a ordem.', 'Você faz tudo certo. Só que tudo junto.', 'O que falta não é receita.'],
         ref='P6 mostrar por dentro (página real do cronograma)'),
    dict(id='C29', nome='Mesa pra poucos', objecao='OBJ3 Ceia pequena', angulo='OBJ3a mesa posta para poucos, luz quente', nivel='a', formato='imagem',
         gatilho='Estado final + orgulho de caprichar (100% emocional na arte)',
         gancho='Mesa pra poucos. Capricho inteiro.',
         curto='Mesa pra poucos, capricho inteiro. Ceia pequena também merece vela acesa e música escolhida.',
         medio='Mesa pra poucos, capricho inteiro.\nVelas testadas, música escolhida, cada lugar pensado. Ceia pequena também merece esse cuidado.\nO guia traz cardápio, lista e cronograma pensados para 8 a 10 pessoas; para menos gente, é só dividir as receitas e a lista na mesma proporção.\nR$ 19,90.',
         lista='Mesa pra poucos. Capricho inteiro.\n• Velas testadas e música escolhida (está no checklist)\n• Lugar de cada um pensado\n• Cardápios para 8 a 10 pessoas: para menos gente, divida receitas e lista\n• Cronograma do dia 17 ao 25\nR$ 19,90.',
         t1='Mesa pra poucos, capricho inteiro', t2='Ceia pequena também é ceia', t3='O cuidado não depende do tamanho', desc='Dá pra dividir as receitas',
         alt=['Poucos à mesa. Nenhum detalhe a menos.', 'Ceia pequena também acende vela.', 'Pra quem importa, a mesa posta.'],
         ref='Oportunidade 7 (prova honesta); checklist real'),
    dict(id='C30', nome='Primeiro prato', objecao='OBJ3 Ceia pequena', angulo='OBJ3b o instante do primeiro prato', nivel='a', formato='vídeo',
         gatilho='Momento sensorial (antecipação do estado final) + pertencimento (100% emocional até o cartão final)',
         gancho='O primeiro prato na mesa.',
         curto='O primeiro prato na mesa. Um silêncio bom. Ceia pequena também tem esse instante.',
         medio='O primeiro prato chega à mesa. Um silêncio bom.\nCeia pequena também tem esse instante, quando o capricho aparece.\nO guia ajuda a chegar nele com calma: cardápio, lista de compras e cronograma, pensados para 8 a 10 pessoas. Para menos gente, é só dividir as receitas e a lista.\nR$ 19,90.',
         lista='Pra chegar ao primeiro prato com calma:\n• Cardápio escolhido (3 opções)\n• Lista de compras por seção\n• Cronograma do dia 17 ao 25\n• Receitas para 8 a 10 pessoas, que dá pra dividir para menos gente\nR$ 19,90.',
         t1='O primeiro prato, com calma', t2='Ceia pequena, momento grande', t3='Quando a mesa fica pronta', desc='Dá pra dividir as receitas',
         alt=['Aquele silêncio bom do primeiro prato.', 'Quando a mesa fica pronta e ninguém fala.', 'Ceia pequena. Momento grande.'],
         ref='P8 vídeo vertical; tom emocional sem prova inventada'),
    dict(id='C31', nome='Capricho é presente', objecao='OBJ3 Ceia pequena', angulo='OBJ3c a gratidão de quem recebe o cuidado', nivel='a', formato='imagem',
         gatilho='Reciprocidade afetiva (quem recebe sente) + especificidade (checklist real)',
         gancho='Pra quem está à mesa, o capricho é presente.',
         curto='Pra quem está à mesa, o capricho é presente: lugar pensado, música escolhida, velas testadas.',
         medio='Pra quem está à mesa, o capricho é presente.\nO lugar de cada um pensado, a música escolhida, as velas testadas. Quem recebe esse cuidado sente.\nEsses detalhes estão no checklist de última hora do guia, junto com cardápios, lista e cronograma para 8 a 10 pessoas (para menos gente, é só dividir).\nR$ 19,90.',
         lista='Pra quem está à mesa, o capricho é presente. Do checklist do guia:\n• Velas, fósforo e pisca-pisca testados\n• Lugar de cada convidado definido\n• Música escolhida\n• Um tempinho para respirar antes de abrir a porta\nR$ 19,90.',
         t1='O capricho também é presente', t2='Pra quem está à mesa, o detalhe', t3='14 detalhes de última hora, numa lista', desc='Checklist de última hora',
         alt=['O detalhe que quem senta à mesa nota.', 'Lugar pensado pra cada um.', 'Pra quem você ama, a mesa posta.'],
         ref='P6 mostrar por dentro (página real do checklist)'),
    dict(id='C32', nome='Fim da noite', objecao='OBJ3 Ceia pequena', angulo='OBJ3d fim da noite, louça na pia e coração cheio', nivel='a', formato='vídeo',
         gatilho='Estado final (a memória da noite) + pertencimento (100% emocional até o cartão final)',
         gancho='23h30. A louça pode esperar.',
         curto='23h30. A louça pode esperar, as sobras já têm pote e o coração está cheio.',
         medio='Fim da noite: louça na pia, coração cheio.\nAs sobras já têm pote e espaço na geladeira, porque estava no checklist. E no dia 25 viram sanduíche ou rabanada de panetone.\nCeia pequena também termina assim.\nO guia traz cardápio, lista e cronograma para 8 a 10 pessoas (para menos gente, é só dividir). R$ 19,90.',
         lista='23h30, fim da noite:\n• Sobras na geladeira em até 2 horas depois de servir\n• Potes e papel-alumínio já à mão (está no checklist)\n• No dia 25: sanduíche de peru, risoto ou rabanada de panetone\nO guia traz isso e o plano da ceia inteira. R$ 19,90.',
         t1='Louça na pia, coração cheio', t2='O fim de noite que vale a ceia', t3='Ceia pequena, noite cheia', desc='Dá pra dividir as receitas',
         alt=['23h30: a louça pode esperar.', 'Quando a noite acaba e o coração não.', 'Fim da noite, coração cheio.'],
         ref='Oportunidade 2 (sobras); tom emocional'),
]

# Nomes no padrão "Cxx | Nome curto | Formato" para os criativos antigos (inferidos; os do Gerenciador prevalecem)
NOMES_ANTIGOS = {
    'C01': 'Cozinha inteira', 'C02': 'Planeje em uma tarde', 'C03': 'Lista por seção', 'C04': '3 cardápios', 'C05': 'Dia 24 hora a hora',
    'C06': 'Sobras', 'C07': 'Quanto comprar', 'C08': 'Já decidiu o cardápio', 'C09': 'Cardápio econômico', 'C10': 'Garantia 7 dias',
    'C11': 'Guia no celular', 'C12': 'Improvisada x planejada', 'C13': '3 mudanças', 'C14': 'Dia 24 hora a hora', 'C15': '300 receitas',
    'C16': 'Erro da véspera', 'C17': 'Creme de leite', 'C18': 'Por dentro do guia', 'C19': 'Ideias com sobras', 'C20': 'Ceia em 4 passos',
}
URL = 'https://cantinho-ceia.vercel.app/?utm_source=meta&utm_medium=paid&utm_campaign=ceia2026&utm_content={}'


def nome_anuncio(id_, nome, formato):
    return f"{id_} | {nome} | {'Imagem' if formato == 'imagem' else 'Vídeo'}"


# Regras extras da série de objeções: atributos pessoais, depoimento, promessa, estatística, clique-isca, escassez falsa.
PROIBIDO_B = PROIBIDO + [r'\bcasad', r'marido', r'esposa', r'solteir', r'sozinh', r'trist', r'solid', r'viúv', r'\bpena\b', r'anfitriã',
                         r'cliente', r'disse que', r'aluna', r'\d+ ?%', r'nunca mais', r'você não vai acreditar', r'corre[!,]', r'acaba (hoje|logo)',
                         r'vagas', r'garant(?!ia)', r'Papai Noel', r'\bDeus\b', r'Jesus', r'saúde', r'emagre', r'Sadia|Perdigão|Seara']

erros = []
for b in B:
    linhas = [l for l in b['medio'].split('\n') if l.strip()]
    if not 3 <= len(linhas) <= 5:
        erros.append(f"{b['id']} texto principal com {len(linhas)} linhas (3 a 5)")
    for campo in ('curto', 'medio', 'lista', 'gancho', 't1', 't2', 't3', 'desc'):
        txt = b[campo]
        if campo in ('curto', 'medio', 'lista') and len(txt.split('\n')[0]) > 125:
            erros.append(f"{b['id']} {campo}: 1ª linha com mais de 125 caracteres")
        if len(EMOJI.findall(txt)) > 1:
            erros.append(f"{b['id']} {campo}: mais de 1 emoji")
        for p in PROIBIDO_B:
            if re.search(p, txt, re.I):
                erros.append(f"{b['id']} {campo}: termo proibido '{p}'")
        for preco in re.findall(r'R\$ ?\d+(?:,\d{2})?', txt):
            if preco.replace(' ', '') != 'R$19,90':
                erros.append(f"{b['id']} {campo}: valor não permitido {preco}")
    for campo, lim in (('t1', 40), ('t2', 40), ('t3', 40), ('desc', 30)):
        if len(b[campo]) > lim:
            erros.append(f"{b['id']} {campo}: {len(b[campo])} caracteres (máx. {lim})")
    if len(b['alt']) != 3:
        erros.append(f"{b['id']}: precisa de 3 ganchos alternativos")
    for g in b['alt']:
        for p in PROIBIDO_B:
            if re.search(p, g, re.I):
                erros.append(f"{b['id']} gancho alternativo: termo proibido '{p}'")
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

def arquivo(id_, formato):
    return f"criativos/imagens/{id_}.png" if formato == 'imagem' else f"criativos/videos/{id_}.mp4"


saida = RAIZ / 'textos-anuncios.csv'
with open(saida, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    # As 16 primeiras colunas são as originais; as seguintes foram acrescentadas na série de objeções (C21+).
    w.writerow(['id', 'onda', 'formato', 'angulo', 'nivel_consciencia', 'gancho', 'texto_curto', 'texto_medio', 'texto_lista',
                'titulo_1', 'titulo_2', 'descricao', 'cta', 'arquivo', 'utm_content', 'referencia_da_pesquisa',
                'nome', 'url', 'titulo_3', 'objecao', 'gatilho', 'gancho_alt_1', 'gancho_alt_2', 'gancho_alt_3', 'arquivo_9x16'])
    for a in A:
        w.writerow([a['id'], a['onda'], a['formato'], a['angulo'], NIVEL[a['nivel']], a['gancho'], a['curto'], a['medio'], a['lista'],
                    a['t1'], a['t2'], a['desc'], a['cta'], arquivo(a['id'], a['formato']), a['id'], a['ref'],
                    nome_anuncio(a['id'], NOMES_ANTIGOS[a['id']], a['formato']), URL.format(a['id']), '', '', '', '', '', '', ''])
    for b in B:
        w.writerow([b['id'], 3, b['formato'], b['angulo'], NIVEL[b['nivel']], b['gancho'], b['curto'], b['medio'], b['lista'],
                    b['t1'], b['t2'], b['desc'], 'Saiba mais', arquivo(b['id'], b['formato']), b['id'], b['ref'],
                    nome_anuncio(b['id'], b['nome'], b['formato']), URL.format(b['id']), b['t3'], b['objecao'], b['gatilho'],
                    *b['alt'], f"criativos/imagens/{b['id']}_9x16.png" if b['formato'] == 'imagem' else ''])
print(f'ok: {len(A) + len(B)} anúncios em {saida.relative_to(RAIZ)}')
