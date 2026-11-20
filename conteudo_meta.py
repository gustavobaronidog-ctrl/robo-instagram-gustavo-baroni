# Carrosséis "DIAGNÓSTICO" (dicas da Meta, 20/11/2026): o dono de empresa se vê no post e quer saber onde está o buraco.
# Moldura de 9 slides (níveis de consciência): 1 capa (dor+número+curiosidade), 2 agita a dor, 3 mostra o buraco,
# 4 custo (conta), 5 quebra a crença, 6 solução, 7 antes/depois, 8 o que muda na prática, 9 fecho.
# Regras deste perfil: nunca citar empresas do Gustavo, agenda, horário ou salão; números só como exemplo declarado;
# CTA sempre "me chama no direct" (nada de "comente PALAVRA" sem automação); sem hashtag.
EU = "@gustavobaroni.ai"


def L(txt):
    return f"{txt}\n\n{EU}"


POSTS = [
("b", [
 "Sua empresa está vazando dinheiro e você não vê.",
 "Todo dia acontece isso:\nUm cliente pergunta.\nVocê está ocupado.\nA resposta demora.",
 "O cliente não reclama.\nEle só some.",
 "Faz a conta, com números de exemplo:\n3 clientes perdidos por dia\nx R$ 150 cada",
 "= R$ 450 por dia.\n= R$ 13.500 por mês.\nTroque pelos seus números e veja.",
 "E não é culpa sua.\nNão dá para atender, cobrar, organizar e vender ao mesmo tempo.",
 "O problema não é trabalhar pouco.\nÉ trabalhar no manual.",
 "Um sistema simples responde rápido, organiza tudo e avisa você só do que importa.",
 "Quer descobrir onde a sua empresa está vazando?",
], L("O vazamento mais caro da empresa é o que ninguém vê: o cliente que não chegou a reclamar.\n\nSe você quer um diagnóstico do seu caso, me chama no direct.")),

("p", [
 "7 sinais de que sua empresa precisa de um sistema:",
 "1. Você controla tudo em planilha ou caderno.",
 "2. Demora mais de 10 minutos para responder um cliente.",
 "3. Esquece de cobrar ou de confirmar.",
 "4. Não sabe quantos clientes te chamaram ontem.",
 "5. Pedido ou serviço chega bagunçado e dá erro.",
 "6. Se uma pessoa falta, tudo para.",
 "7. Trabalha muito e no fim do mês não sobra.",
 "Marcou 3 ou mais? Sua empresa está vazando.",
], L("Sete sinais simples. Três ou mais e o problema não é venda, é processo.\n\nSalva e confere com a sua empresa.")),

("b", [
 "Seu cliente desiste em 10 minutos.",
 "Ele manda a mensagem às 9h.",
 "Você está atendendo e não vê.",
 "Ele chama o concorrente às 9h10.",
 "Você nunca soube que ele existiu.",
 "Quem responde primeiro quase sempre vende.",
 "Não é simpatia. É velocidade.",
 "Resposta automática bem feita passa a informação certa na hora e chama você só quando precisa.",
 "Quanto tempo o seu cliente espera hoje?",
], L("Velocidade de resposta é parte do produto. Quem demora entrega o cliente ao concorrente sem perceber.\n\nQuer ver como resolver no seu caso? Me chama no direct.")),

("p", [
 "3 erros que fazem uma loja perder dinheiro com pedido no WhatsApp:",
 "Erro 1: anotar o pedido no meio de uma conversa longa.",
 "Resultado: item errado, cliente bravo.",
 "Erro 2: não guardar o contato de quem comprou.",
 "Resultado: toda venda começa do zero.",
 "Erro 3: não saber o que mais vende.",
 "Resultado: estoque errado e promoção no escuro.",
 "Um sistema de pedidos organiza as três coisas sem esforço extra.",
 "Qual desses três acontece na sua loja?",
], L("Pedido bagunçado custa mais do que parece: retrabalho, cliente insatisfeito e venda que não se repete.\n\nConta aqui qual dos três você mais vê.")),

("b", [
 "Se uma pessoa falta, o que para na sua empresa?",
 "Se a resposta é “tudo”, você não tem equipe.",
 "Você tem uma pessoa e vários cargos.",
 "Isso é risco, não força.",
 "Uma doença, uma saída, uma férias, e a empresa trava.",
 "O que só uma pessoa sabe fazer precisa sair da cabeça dela.",
 "Escrever o passo a passo já é o primeiro sistema.",
 "O segundo é automatizar a parte que se repete.",
 "O que só uma pessoa sabe fazer aí?",
], L("Dependência de uma única pessoa é o risco mais ignorado em empresa pequena.\n\nSalva e anota o que só uma pessoa faz na sua.")),

("p", [
 "Quanto custa uma tarefa repetida?",
 "Exemplo: 1 hora por dia copiando dados de um lugar para outro.",
 "1 hora x 22 dias = 22 horas por mês.",
 "Se a hora da pessoa vale R$ 30:\nR$ 660 por mês.",
 "R$ 7.920 por ano para fazer o que uma automação faz em segundos.",
 "E isso é UMA tarefa.\nNa empresa existem dezenas.",
 "Não é preguiça da equipe.\nÉ ninguém ter olhado para isso ainda.",
 "O primeiro passo é listar o que se repete toda semana.",
 "Qual tarefa repetida você tem aí?",
], L("Troque os números do exemplo pelos seus. A conta quase sempre assusta.\n\nQuer ajuda para achar o que automatizar primeiro? Me chama no direct.")),

("b", [
 "Você paga taxa toda vez que vende?",
 "Plataforma de terceiros é ótima para começar.",
 "Mas ela fica com uma parte de cada venda.",
 "E fica com o contato do seu cliente.",
 "Exemplo: R$ 30 mil vendidos x 25% de taxa = R$ 7.500 por mês.",
 "Isso dá R$ 90 mil por ano que não ficam com você.",
 "Quem depende só da plataforma não tem cliente.\nTem aluguel de cliente.",
 "Canal próprio, bem feito, deixa a venda e o contato com você.",
 "Quanto do seu faturamento fica pelo caminho?",
], L("Plataforma ajuda a começar. Depender só dela custa caro e te deixa sem o contato do cliente.\n\nQuer calcular o seu caso? Me chama no direct.")),

("p", [
 "O dinheiro que sua empresa tem para receber e não recebe:",
 "Cobrança que ninguém lembrou.",
 "Boleto vencido sem aviso.",
 "Cliente que “ficou de pagar”.",
 "Exemplo: 10 cobranças esquecidas de R$ 200 = R$ 2.000 parados.",
 "Todo mês.",
 "Não é inadimplência.\nÉ falta de lembrete.",
 "Uma cobrança automática educada recupera boa parte sem constrangimento.",
 "Quanto está parado aí hoje?",
], L("Muita empresa não perde por falta de venda, perde por falta de cobrança.\n\nSalva e olhe seu contas a receber hoje.")),

("b", [
 "Orçamento demorado é venda perdida.",
 "O cliente pede o valor hoje.",
 "Você manda amanhã.",
 "Ele já fechou com quem mandou ontem.",
 "Quem manda proposta primeiro é lembrado.\nQuem manda melhor, fecha.",
 "O problema quase nunca é preço.\nÉ demora e bagunça.",
 "Orçamento padronizado sai em minutos e não esquece nada.",
 "Você responde rápido sem trabalhar a mais.",
 "Em quanto tempo sai o seu orçamento?",
], L("Rapidez e clareza no orçamento vendem mais do que desconto.\n\nQuer um modelo simples para o seu negócio? Me chama no direct.")),

("p", [
 "Você sabe quem comprou de você mês passado?",
 "Muita empresa sabe quanto vendeu.\nPoucas sabem para quem.",
 "Sem esse registro, toda venda começa do zero.",
 "Quem compra uma vez costuma comprar de novo, se for lembrado.",
 "Cadastro organizado permite chamar de volta no momento certo.",
 "Isso custa quase nada e vende mais do que anúncio.",
 "Cliente antigo é o caminho mais barato de crescer.",
 "Comece guardando nome, contato e o que a pessoa comprou.",
 "Hoje, onde ficam esses dados aí?",
], L("Vender de novo para quem já comprou é mais barato que conquistar cliente novo.\n\nSalva e comece o cadastro hoje.")),

("b", [
 "Antes e depois de uma empresa que saiu do manual:",
 "ANTES:\nTudo na cabeça de uma pessoa.",
 "DEPOIS:\nTudo escrito e rodando sozinho.",
 "ANTES:\nResposta quando dava tempo.",
 "DEPOIS:\nResposta na hora, todo dia.",
 "ANTES:\nCobrança que dependia de lembrar.",
 "DEPOIS:\nCobrança que sai sozinha.",
 "O dono saiu do operacional e foi para o crescimento.",
 "O que você quer mudar primeiro?",
], L("O contraste é sempre o mesmo: o que dependia de memória passa a depender de sistema.\n\nQuer sair do manual? Me chama no direct.")),

("p", [
 "O erro que custa caro:\nautomatizar uma bagunça.",
 "Se o processo está confuso, a automação só bagunça mais rápido.",
 "Primeiro: escreva o passo a passo.",
 "Segundo: corte o que não precisa.",
 "Terceiro: só então automatize o que sobrou.",
 "Parece lento, mas é o caminho mais rápido.",
 "Sistema bom nasce de processo simples.",
 "Ferramenta nenhuma conserta processo que ninguém entende.",
 "Seu processo cabe em 7 linhas?",
], L("Antes de automatizar, simplifique. Automação em cima de bagunça só acelera o erro.\n\nSalva os 3 passos.")),

("b", [
 "Retrabalho é o imposto invisível da sua empresa.",
 "Digitar duas vezes o mesmo dado.",
 "Corrigir pedido errado.",
 "Refazer orçamento porque faltou informação.",
 "Exemplo: 5 retrabalhos por semana x 30 minutos = 10 horas por mês.",
 "E o cliente ainda sente a demora.",
 "O retrabalho aparece onde o processo tem buraco.",
 "Achar o buraco e fechar costuma ser mais barato do que parece.",
 "Onde você mais refaz coisa hoje?",
], L("Retrabalho não aparece na conta, mas está em todo prejuízo escondido.\n\nConta aqui onde você mais refaz coisa.")),

("p", [
 "Você não tem problema de venda.",
 "Você tem problema de processo.",
 "O cliente chega.\nO que acontece depois?",
 "Demora na resposta.\nBagunça no pedido.\nEsquecimento na cobrança.",
 "Cada etapa mal feita derruba uma parte das vendas.",
 "Não adianta trazer mais cliente por um funil furado.",
 "Primeiro fecha o buraco. Depois enche o funil.",
 "É o investimento com o melhor retorno que existe.",
 "Qual etapa mais vaza aí?",
], L("Antes de gastar com anúncio, conserte o processo que atende quem já chegou.\n\nQuer ajuda para achar a etapa que mais vaza? Me chama no direct.")),

("b", [
 "5 perguntas para achar o buraco da sua empresa:",
 "1. Quanto tempo leva para responder um cliente?",
 "2. Quantos clientes te procuraram ontem?",
 "3. Quantos você respondeu?",
 "4. O que depende de uma única pessoa?",
 "5. Quanto tempo por semana vai em tarefa repetida?",
 "Se você não sabe responder alguma, achou o buraco.",
 "Medir é o primeiro passo. Sem número, é achismo.",
 "Quantas dessas você sabe responder?",
], L("Cinco perguntas, dez minutos. Quem não sabe responder já descobriu o buraco.\n\nSalva e responde hoje. Me chama no direct se quiser ajuda para ler o resultado.")),

("p", [
 "O que uma IA de atendimento faz bem, e o que não faz:",
 "FAZ BEM:\nResponder as dúvidas que se repetem.",
 "FAZ BEM:\nResponder na hora, a qualquer hora.",
 "FAZ BEM:\nOrganizar o que o cliente pediu.",
 "NÃO FAZ BEM:\nNegociar caso difícil.",
 "NÃO FAZ BEM:\nAcalmar cliente bravo.",
 "A regra: a IA cuida do repetitivo, você cuida do que exige gente.",
 "Quem promete que a IA faz tudo está vendendo ilusão.",
 "O que se repete no seu atendimento?",
], L("IA de atendimento funciona quando cada coisa fica no lugar certo: o repetitivo com ela, o delicado com você.\n\nQuer ver o que cabe no seu negócio? Me chama no direct.")),

("b", [
 "Empresa de 2026 com processo de 2015.",
 "Cliente que quer resposta na hora.",
 "Dono que ainda anota no caderno.",
 "Equipe que digita o mesmo dado três vezes.",
 "Isso funcionou por muito tempo.",
 "Mas hoje o concorrente que usa sistema entrega mais rápido.",
 "Não é moda. É vantagem de tempo.",
 "Quem ganha tempo, atende mais e erra menos.",
 "Seu processo ainda é de 2015?",
], L("A tecnologia deixou de ser luxo e virou a diferença de velocidade entre quem cresce e quem estaciona.\n\nQuer conversar sobre o seu processo? Me chama no direct.")),

("p", [
 "Diagnóstico de 10 minutos para fazer sozinho:",
 "Passo 1: liste tudo que a equipe faz toda semana.",
 "Passo 2: marque o que se repete igual.",
 "Passo 3: marque o que dá erro com frequência.",
 "Passo 4: marque o que só uma pessoa sabe fazer.",
 "Passo 5: o que tem as 3 marcas é a sua prioridade.",
 "Resolva uma por vez.",
 "Em um mês você sente a diferença.",
 "Qual é a sua prioridade número 1?",
], L("Um método simples, de caneta e papel, para achar por onde começar.\n\nSalva e faça hoje. Me chama no direct com o resultado se quiser uma segunda opinião.")),

("b", [
 "3 números que todo dono precisa ver toda semana:",
 "1. Quantos clientes chamaram.",
 "2. Quantos viraram venda.",
 "3. Quanto tempo levou para responder.",
 "Com esses três você enxerga onde está perdendo.",
 "Sem eles, você decide no escuro.",
 "Dá para juntar tudo em um painel simples que se atualiza sozinho.",
 "Aí a decisão deixa de ser palpite.",
 "Você acompanha esses três hoje?",
], L("Três números mudam a forma de decidir. E dá para ter eles sem esforço, com o sistema certo.\n\nQuer montar o seu painel? Me chama no direct.")),

("p", [
 "Por que sua empresa trabalha tanto e sobra tão pouco?",
 "Porque o dono virou o sistema.",
 "Responde, cobra, organiza, vende, corrige.",
 "Tudo passa por você.",
 "Isso limita a empresa ao tamanho do seu dia.",
 "Para crescer, o que você faz precisa funcionar sem você.",
 "Cada tarefa que vira sistema libera uma hora sua.",
 "Com as horas livres você faz o que só o dono faz: crescer.",
 "O que você tira das suas mãos primeiro?",
], L("Empresa que depende do dono para tudo não cresce: ela só repete o dia do dono.\n\nQuer tirar o primeiro peso das suas mãos? Me chama no direct.")),
]
