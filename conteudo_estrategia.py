# Carrosséis ESTRATÉGICOS (3 por dia) e RESERVA (entram no lugar de notícia que faltar).
# Mecanismo dos perfis modelados: gancho de problema, valor real, virada, CTA simples. Texto próprio.
# Nunca citar Tem Encaixe/SeparaGo, agenda, horário ou salão. Sem hashtag. Sem número inventado.
EU = "@gustavobaroni.ai"


def L(txt):
    return f"{txt}\n\n{EU}"


ESTRATEGIA = [
("b", [
 "Seu negócio perde dinheiro todo dia em um lugar que você nem olha.",
 "Não é o preço. Não é o concorrente.",
 "É a tarefa repetida que alguém da sua equipe faz de novo toda manhã.",
 "Copiar dado de um lugar para outro.\nResponder a mesma pergunta.\nConferir uma planilha.",
 "Cada uma parece pequena. Somadas, comem a semana inteira de uma pessoa.",
 "O primeiro passo é só anotar o que se repete.\nO resto a automação resolve.",
 "Salva para fazer essa lista hoje 📌",
], L("Antes de comprar qualquer ferramenta, descubra onde o tempo da sua equipe está indo embora.\n\nSalva e faz a lista hoje.")),

("p", [
 "3 sinais de que sua empresa já passou da hora de automatizar:",
 "1. Você ouve “eu sempre fiz assim” e ninguém sabe explicar por quê.",
 "2. Uma pessoa sumiu um dia e o processo parou.",
 "3. Você confere duas vezes porque não confia no resultado.",
 "Automatizar não é trocar gente por robô.\nÉ tirar o trabalho chato de quem pensa.",
 "Reconheceu algum? Me conta nos comentários 👇",
], L("Três sinais simples de que o trabalho repetido já está custando caro.\n\nQual deles aparece aí?")),

("b", [
 "O maior mito sobre IA nos negócios:",
 "“Preciso entender de tecnologia para usar.”",
 "Não precisa.\nPrecisa entender o seu próprio processo.",
 "Quem sabe explicar o que faz, passo a passo, já sabe pedir para a IA.",
 "A tecnologia é a parte fácil.\nDifícil é saber o que vale a pena automatizar.",
 "Por isso quem conhece o próprio negócio sai na frente 💡",
], L("A IA premia quem entende o próprio processo, não quem decora ferramenta.\n\nManda para alguém que acha que isso é só para programador.")),

("p", [
 "O erro que eu mais vejo empresário cometer com IA:",
 "Começar pela ferramenta.",
 "Abre o app da moda, testa 15 minutos e abandona.",
 "O caminho que funciona é o contrário:",
 "1. Escolha UMA dor.\n2. Descreva como você resolve hoje.\n3. Peça para a IA fazer só essa parte.",
 "Uma dor resolvida vale mais que dez ferramentas instaladas ✅",
], L("Começar pela dor, não pela ferramenta, é o que separa teste de resultado.\n\nSalva e escolhe sua primeira dor.")),

("b", [
 "Como eu penso antes de construir qualquer sistema:",
 "1. Quem vai usar isso?",
 "2. O que essa pessoa faz hoje, passo a passo?",
 "3. Qual passo dói mais?",
 "4. Dá para resolver sem código?",
 "5. Se não dá, qual o menor sistema que resolve?",
 "Quase todo projeto bom nasce nessas cinco perguntas 🧠",
], L("Cinco perguntas que eu faço antes de escrever uma linha de código.\n\nSalva para usar no seu próximo projeto.")),

("p", [
 "Você não precisa de mais conteúdo.",
 "Precisa de um sistema que publique por você.",
 "Quem posta quando tem tempo some quando a semana aperta.",
 "Quem tem rotina automática aparece todo dia, mesmo na semana ruim.",
 "Consistência é a parte que quase ninguém aguenta fazer na mão.",
 "Por isso eu automatizei a minha.",
 "Segue para ver como eu faço 👉",
], L("Consistência de verdade só vem com sistema. A minha roda sozinha.\n\nSegue para acompanhar como eu construo.")),

("b", [
 "Seu Instagram não cresce por causa de uma coisa:",
 "Você posta o que quer falar, não o que o outro precisa ouvir.",
 "Teste simples: leia seu último post e pergunte “e eu com isso?” do ponto de vista do cliente.",
 "Se a resposta não vem em 3 segundos, o post não é para ele. É para você.",
 "Primeiro slide: o problema da pessoa.\nÚltimo slide: o próximo passo dela.",
 "Salva esse teste 📌",
], L("Um teste de 3 segundos para saber se seu post é para o cliente ou para você.\n\nSalva e aplica no próximo.")),

("p", [
 "Por que o seu carrossel não é salvo:",
 "1. O primeiro slide não promete nada.",
 "2. Tem muito texto e pouca ideia.",
 "3. Termina sem dizer o que fazer.",
 "Carrossel bom ensina uma coisa só, do começo ao fim.",
 "E fecha dizendo: salva, manda ou segue.",
 "Quer mais dicas assim? Segue 👉",
], L("Três motivos para um carrossel ser ignorado, e como corrigir cada um.\n\nSegue para mais dicas de conteúdo.")),

("b", [
 "A automação mais barata que existe:",
 "Escrever um passo a passo.",
 "Se você explica uma tarefa em 7 linhas, qualquer pessoa ou IA consegue repetir.",
 "Se não consegue explicar, o problema não é falta de tecnologia.",
 "É um processo que ainda mora só na sua cabeça.",
 "Tirar da cabeça e colocar no papel já resolve metade 📝",
], L("Antes de automatizar, escreva o processo. Metade do trabalho já está feita ali.\n\nSalva e tenta com uma tarefa hoje.")),

("p", [
 "Pergunta que todo dono de negócio deveria se fazer:",
 "“Se eu ficar 30 dias fora, o que para?”",
 "O que parar é o que depende só de você.",
 "E é exatamente o que dá para transformar em sistema.",
 "Não para ficar de férias.\nPara ter a cabeça livre para crescer.",
 "Responde aqui: o que para na sua empresa? 👇",
], L("O que para quando você some mostra o que precisa virar sistema.\n\nResponde nos comentários, eu leio todos.")),

("b", [
 "Quanto custa uma resposta que demora?",
 "Quem pergunta preço e espera horas já está olhando o concorrente.",
 "Velocidade de resposta é parte do produto, não detalhe.",
 "Isso dá para resolver com resposta automática bem feita, que parece gente e passa a informação certa.",
 "Mas só funciona se você souber o que o cliente mais pergunta.",
 "Comece listando as 10 perguntas mais frequentes 📋",
], L("Responder rápido e bem vende mais do que qualquer anúncio. Dá para automatizar boa parte disso.\n\nSalva a ideia das 10 perguntas.")),

("p", [
 "O que eu faria se estivesse começando com IA hoje:",
 "1. Escolheria uma tarefa chata da semana.",
 "2. Pediria para a IA fazer só ela.",
 "3. Conferiria o resultado antes de confiar.",
 "4. Repetiria até ficar bom.",
 "5. Só então iria para a próxima.",
 "Devagar, mas todo dia. É assim que vira habilidade 🔁",
], L("Um caminho realista para começar com IA sem se perder em ferramenta.\n\nSalva e começa pela tarefa mais chata.")),

("b", [
 "Dado sem uso é só custo de armazenamento.",
 "Muita empresa guarda tudo e não olha nada.",
 "Três perguntas que transformam dado em decisão:",
 "1. O que mudou desde o mês passado?\n2. O que se repete?\n3. O que me surpreendeu?",
 "A IA ajuda a responder as três em minutos.",
 "Mas só se o dado estiver organizado em um lugar 🗂️",
], L("Organizar o dado é o primeiro passo para qualquer IA ser útil de verdade.\n\nManda para quem guarda tudo e não usa nada.")),

("p", [
 "Não existe sistema perfeito.",
 "Existe sistema que roda hoje e melhora amanhã.",
 "Quem espera ficar perfeito para lançar nunca lança.",
 "Eu lanço pequeno, vejo o que quebra e conserto.",
 "Cada erro encontrado cedo é um erro barato.",
 "Construir é isso: corrigir rápido ⚡",
], L("Lançar pequeno e corrigir rápido é a forma mais barata de aprender.\n\nSegue para ver o que eu construo, inclusive o que dá errado.")),

("b", [
 "Três perguntas para saber se vale automatizar uma tarefa:",
 "1. Ela se repete toda semana?",
 "2. Tem sempre os mesmos passos?",
 "3. Um erro nela custa caro?",
 "Três “sim”? Automatize.\nUm ou dois? Anote e volte depois.\nNenhum? Deixa quieto.",
 "Nem tudo precisa virar robô 😉",
], L("Um filtro simples para não perder tempo automatizando o que não vale.\n\nSalva para a próxima decisão.")),

("p", [
 "Quem usa IA bem não pede mais rápido.",
 "Pede melhor.",
 "Dê contexto: quem é o público, qual o objetivo, qual o formato.",
 "Mostre um exemplo do que você considera bom.",
 "Peça para a IA fazer perguntas antes de responder.",
 "Mesma ferramenta, resultado completamente diferente ✨",
], L("A diferença entre uma resposta genérica e uma boa está no que você entrega no pedido.\n\nSalva e testa hoje.")),

("b", [
 "Seu cliente não quer saber de tecnologia.",
 "Quer saber se o problema dele acaba.",
 "Quando você mostra a ferramenta, ele vê complicação.",
 "Quando você mostra o antes e o depois, ele vê solução.",
 "Fale do resultado na vida dele, não do recurso na tela.",
 "Isso vale para vender, para postar e para explicar 🎯",
], L("Mostre o antes e o depois, não a ferramenta.\n\nSegue para mais ideias de como comunicar melhor.")),
]

# Reserva: entram no lugar de uma notícia que não foi escrita no dia (a quantidade de posts nunca diminui).
RESERVA = [
("p", [
 "Tem tarefa na sua semana que você faz há anos sem questionar?",
 "Aquele relatório que ninguém lê.\nAquela conferência que nunca acha erro.",
 "Pergunte: se eu parasse de fazer, alguém reclamaria?",
 "Se ninguém reclama, corte.\nSe reclamam, automatize.",
 "Em ambos os casos você ganha tempo ⏳",
], L("Cortar ou automatizar: toda tarefa antiga merece essa pergunta.\n\nSalva e revisa sua semana.")),

("b", [
 "Como pedir uma coisa para a IA e receber algo útil:",
 "1. Diga quem você é e para quem é o resultado.",
 "2. Diga o objetivo em uma frase.",
 "3. Diga o formato: lista, e-mail, tabela.",
 "4. Mostre um exemplo.",
 "5. Peça para ela perguntar o que faltou.",
 "Salva esse roteiro 📌",
], L("Cinco passos para pedidos melhores para qualquer IA.\n\nSalva e usa na próxima conversa.")),

("p", [
 "A pergunta que separa quem cresce de quem fica parado:",
 "“O que eu estou fazendo hoje que um sistema poderia fazer?”",
 "Quem se faz essa pergunta toda semana cria hábito de melhorar.",
 "Quem não se faz, só trabalha mais.",
 "Anota essa pergunta onde você vê todo dia 🗒️",
], L("Uma pergunta por semana que muda como você enxerga o seu trabalho.\n\nSegue para mais ideias assim.")),

("b", [
 "3 coisas que uma boa automação nunca faz:",
 "1. Esconder o que está fazendo.",
 "2. Quebrar sem avisar ninguém.",
 "3. Depender de uma única pessoa para funcionar.",
 "Se a sua faz alguma dessas, ela ainda é uma gambiarra.",
 "Dá para melhorar 🔧",
], L("Três sinais de que uma automação ainda não está pronta para confiar.\n\nManda para quem monta robô sozinho.")),

("p", [
 "Todo mundo quer o resultado.\nPoucos querem a rotina.",
 "Quem posta todo dia por 90 dias aparece.\nQuem posta quando dá, não.",
 "Foi por isso que eu automatizei a minha parte chata.",
 "Assim a disciplina vira sistema, não força de vontade 💪",
], L("A rotina vence o talento quando ela é automática.\n\nSegue para acompanhar a minha.")),

("b", [
 "Antes de contratar uma ferramenta nova, responda:",
 "1. Que problema exato ela resolve?",
 "2. Quanto tempo vou economizar por semana?",
 "3. Quem vai cuidar dela?",
 "Sem resposta para as três, não compre ainda.",
 "Ferramenta sem dono vira assinatura esquecida 💸",
], L("Três perguntas antes de assinar mais uma ferramenta.\n\nSalva para a próxima compra.")),
]
