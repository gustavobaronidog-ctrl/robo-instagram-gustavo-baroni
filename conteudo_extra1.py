# Lote 1: listas salváveis (comandos, prompts, checklists). Posicionamento: quem constrói sistemas e automações com IA.
# Sem citar empresas, sem agenda/horário/salão.
EU = "@gustavobaroni.ai"


def L(txt):
    return f"{txt}\n\n{EU}"


POSTS = [
("p", [
 "COMANDOS SECRETOS\nCLAUDE | ANTES DE LANÇAR",
 "1. \"Finja que é um usuário que nunca viu esse sistema e tente quebrá-lo.\"",
 "2. \"Liste os 10 erros mais prováveis e o que o usuário veria em cada um.\"",
 "3. \"Me diga o que acontece se a internet cair no meio do processo.\"",
 "4. \"O que eu esqueci de perguntar antes de colocar isso no ar?\"",
 "Salva. Esse teste evita vergonha em produção 📌",
], L("Teste antes de lançar. Esses 4 comandos pegam o que você não viu.\n\nSalva para a próxima vez.")),

("b", [
 "5 prompts que eu uso toda semana para construir com IA:",
 "1. \"Explica isso como se eu tivesse 12 anos, depois como engenheiro sênior.\"",
 "2. \"Qual o jeito mais simples de fazer isso funcionar? Não me dê o mais elegante.\"",
 "3. \"Quais decisões minhas aqui vão me custar caro daqui a 6 meses?\"",
 "4. \"Revisa o que você acabou de escrever e aponta onde pode estar errado.\"",
 "5. \"Resume o que ficou decidido para eu colar na minha documentação.\"",
 "Manda para quem está começando a usar IA para criar 📲",
], L("5 prompts simples que mudaram o jeito que eu construo.\n\nManda para alguém que está começando.")),

("p", [
 "COMANDOS SECRETOS\nCLAUDE | ENTENDER UM CÓDIGO",
 "1. \"Me explique esse código linha por linha, sem termos técnicos.\"",
 "2. \"O que esse código faz de errado e ainda parece funcionar?\"",
 "3. \"Qual a parte mais frágil dele? Se quebrar, quebra onde?\"",
 "4. \"Reescreva só a parte mais frágil, sem mexer no resto.\"",
 "Você não precisa programar para entender o que foi feito 💡",
], L("Você não precisa saber programar para conferir o que a IA fez.\n\nSalva esses comandos.")),

("b", [
 "Quem constrói automações gostaria que você soubesse essas 5 coisas:",
 "1. Automação boa é chata: roda todo dia e ninguém percebe.",
 "2. O erro mais caro é o que ninguém vê acontecendo.",
 "3. Todo robô precisa de um aviso quando falha, com o que fazer.",
 "4. Automatizar o que está bagunçado só bagunça mais rápido.",
 "5. O melhor momento para automatizar é quando você cansou de repetir 🤖",
], L("Automação não é mágica. É disciplina.\n\nSegue para ver como eu monto as minhas.")),

("p", [
 "Conselho:\n\nnunca peça para a IA \"fazer um sistema\". Peça para ela te entrevistar primeiro.",
 "\"Faz um app pra mim\" gera um app genérico que ninguém usa.",
 "\"Me entrevista antes de construir\" gera algo que resolve o seu problema.",
 "As melhores perguntas que a IA faz são as que você não tinha pensado.",
 "Responda cada uma com calma. É aí que o projeto nasce 🧠",
], L("A melhor primeira mensagem para a IA é pedir que ela te faça perguntas.\n\nTesta e me conta.")),

("b", [
 "5 erros que fazem a IA te entregar um código ruim:",
 "1. Pedir tudo de uma vez em vez de por partes.",
 "2. Não explicar para quem o sistema é.",
 "3. Aceitar a primeira resposta sem revisar.",
 "4. Não pedir para testar o que ela mesma escreveu.",
 "5. Misturar vários assuntos na mesma conversa.",
 "Salva para conferir antes do próximo pedido 📌",
], L("Esses 5 erros pioram qualquer resposta da IA.\n\nSalva e confere antes de pedir.")),

("p", [
 "COMANDOS SECRETOS\nCLAUDE | DOCUMENTAR SEM SOFRER",
 "1. \"Documente o que você acabou de construir para eu entender daqui a um ano.\"",
 "2. \"Liste as decisões que tomamos e o motivo de cada uma.\"",
 "3. \"Escreva um passo a passo para eu consertar se quebrar e você não estiver.\"",
 "4. \"Quais senhas, chaves e acessos esse projeto usa? Onde cada um fica guardado?\"",
 "Sistema sem documentação vira refém de quem fez 🔒",
], L("Documentar é o que separa projeto de bagunça.\n\nSalva esses comandos.")),

("b", [
 "Como eu escolho o que automatizar primeiro:",
 "1. Algo que eu faço toda semana do mesmo jeito.",
 "2. Algo que, se eu esquecer, dá problema.",
 "3. Algo que não precisa de julgamento, só de regra.",
 "4. Algo que eu consigo explicar em 3 frases.",
 "Se passa nos 4, é candidato. Começa por ele ⚙️",
], L("Critério simples para saber por onde começar a automatizar.\n\nSalva e aplica hoje.")),

("p", [
 "A IA vai te dar uma resposta confiante mesmo quando estiver errada.",
 "Ela não tem vergonha de errar. Quem tem que ter é você, antes de usar.",
 "Peça sempre: \"Qual a chance disso estar errado e por quê?\"",
 "Peça fonte. Peça teste. Peça o contrário da resposta.",
 "Quem desconfia com método usa a IA melhor que quem confia 🔎",
], L("Confiar cego na IA custa caro. Desconfiar com método custa pouco.\n\nSalva.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | SEGURANÇA",
 "1. \"Revise esse projeto procurando senhas ou chaves que ficaram expostas.\"",
 "2. \"Quem consegue acessar o quê aqui? Alguém acessa mais do que deveria?\"",
 "3. \"Se um dado vazar, qual seria o pior caso e como eu limito o dano?\"",
 "4. \"Onde um invasor tentaria entrar primeiro?\"",
 "Segurança se pensa antes. Depois é remendo 🔐",
], L("Segurança não se coloca no final. Nasce junto com o projeto.\n\nSalva esses comandos.")),

("p", [
 "3 coisas que eu nunca faço com IA:",
 "1. Colar senha ou chave no chat.",
 "2. Publicar algo que eu não li.",
 "3. Deixar sem backup o que levou semanas para construir.",
 "Essas 3 regras evitam 90% dos desastres que eu vejo por aí ⚠️",
], L("3 regras que me salvam de dor de cabeça.\n\nManda para quem usa IA no trabalho.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | PENSAR UM PRODUTO",
 "1. \"Quem é a pessoa que mais sofre com esse problema? Descreva o dia dela.\"",
 "2. \"Qual a menor versão disso que já ajudaria alguém de verdade?\"",
 "3. \"O que eu estou construindo que ninguém pediu?\"",
 "4. \"Como eu saberia, em uma semana, se isso funciona?\"",
 "Quem pergunta antes constrói menos e acerta mais 🎯",
], L("Antes de construir, pergunte. Esses 4 comandos poupam meses.\n\nSalva.")),

("p", [
 "O que mudou na minha rotina desde que eu uso IA para construir:",
 "Eu parei de começar do zero. Eu começo de uma conversa.",
 "Eu parei de adiar o que eu não sabia fazer. Eu pergunto.",
 "Eu parei de achar que precisava de uma equipe para tirar uma ideia do papel.",
 "O limite agora não é saber programar. É saber o que construir 🚀",
], L("A ferramenta mudou. A pergunta agora é o que vale a pena construir.\n\nSegue para ver o que eu estou fazendo.")),

("b", [
 "Mito: \"IA vai fazer tudo sozinha.\"",
 "Realidade: ela faz o que você descreve bem.",
 "Quem descreve mal recebe uma coisa que parece certa e não é.",
 "A habilidade que mais vale hoje é explicar com clareza o que você quer.",
 "Escrever bem virou superpoder técnico ✍️",
], L("A habilidade que mais cresce é saber explicar o que você quer.\n\nSalva para lembrar.")),

("p", [
 "COMANDOS SECRETOS\nCLAUDE | AUTOMATIZAR ROTINA",
 "1. \"Me ajude a listar tudo que eu repito toda semana.\"",
 "2. \"Qual dessas tarefas é a mais fácil de automatizar de graça?\"",
 "3. \"Monte um passo a passo usando só ferramentas gratuitas.\"",
 "4. \"O que pode dar errado nessa automação e como eu fico sabendo?\"",
 "Começa pequeno. Uma tarefa por vez ⚙️",
], L("Automatizar de graça é possível. Começa com uma tarefa.\n\nSalva esse roteiro.")),

("b", [
 "Eu tenho um robô que posta por mim.",
 "Ele roda num servidor gratuito, sem eu ligar o computador.",
 "Se eu estiver dormindo, de férias ou sem tempo, ele posta igual.",
 "Eu só precisei pensar uma vez no que ele deveria fazer.",
 "Pensar uma vez e rodar mil: essa é a vantagem de construir 🤖",
], L("Um robô que trabalha enquanto você vive. Dá para construir, e de graça.\n\nSegue para ver como.")),

("p", [
 "5 perguntas que eu faço antes de confiar em um sistema:",
 "1. Se parar de funcionar hoje, eu fico sabendo como?",
 "2. Onde ficam as minhas senhas e chaves?",
 "3. Existe backup? Já testei restaurar?",
 "4. Quem mais tem acesso?",
 "5. Eu consigo consertar sozinho, ou dependo de alguém?",
 "Salva e aplica no que você usa 🔍",
], L("5 perguntas que mostram se um sistema é confiável de verdade.\n\nSalva.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | ESTUDAR RÁPIDO",
 "1. \"Me ensine isso em 5 níveis: criança, adolescente, graduação, mestrado, especialista.\"",
 "2. \"Quais os 3 erros mais comuns de quem está começando nisso?\"",
 "3. \"Me teste com 5 perguntas e me diga onde eu errei.\"",
 "4. \"Monte um plano de 7 dias para eu sair do zero.\"",
 "Aprender com IA é ter um professor que nunca cansa 📚",
], L("Comandos para aprender qualquer assunto em muito menos tempo.\n\nSalva.")),

("p", [
 "Dica de quem constrói com IA:",
 "Guarde tudo que funciona.",
 "Um prompt bom é um ativo. Uma resposta boa é um ativo.",
 "Eu guardo em um caderno digital organizado por assunto.",
 "Em um mês você tem uma biblioteca que ninguém mais tem 📓",
], L("O que funcionou uma vez funciona de novo. Guarde.\n\nSalva e começa a sua biblioteca.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | MELHORAR TEXTOS",
 "1. \"Reescreva isso mais curto, sem perder o sentido.\"",
 "2. \"Qual a frase mais fraca desse texto? Troque.\"",
 "3. \"Faça soar como uma pessoa conversando, não como um robô.\"",
 "4. \"Me dê 3 versões com tons diferentes.\"",
 "Texto bom é o que a pessoa lê até o fim ✍️",
], L("Comandos para deixar qualquer texto melhor.\n\nSalva.")),

("p", [
 "O erro de quem começa a usar IA:",
 "Achar que a primeira resposta é a resposta.",
 "A primeira resposta é um rascunho.",
 "A boa vem na terceira ou quarta troca, quando você corrige, pede mais e aponta o que faltou.",
 "Conversa é o método. Não é desperdício 💬",
], L("A IA melhora a cada troca. Continue a conversa.\n\nSalva.")),

("b", [
 "Quem constrói produtos com IA gostaria que você entendesse essas 5 coisas:",
 "1. Construir ficou barato. Acertar o que construir continua caro.",
 "2. Falar com cliente vale mais que mais um recurso.",
 "3. Simples que funciona vence completo que ninguém usa.",
 "4. Todo produto precisa de um jeito de ser consertado sem você.",
 "5. Começar pequeno é estratégia, não preguiça 🧱",
], L("Construir ficou fácil. Construir certo continua sendo o diferencial.\n\nSegue.")),

("p", [
 "COMANDOS SECRETOS\nCLAUDE | PEDIR UM APP",
 "1. \"Descreva o que o usuário vê na tela, passo a passo, antes de programar.\"",
 "2. \"Quais telas são essenciais e quais eu posso deixar para depois?\"",
 "3. \"Monte uma versão que eu consiga testar hoje, mesmo incompleta.\"",
 "4. \"Me diga o que depende de mim: contas, chaves, decisões.\"",
 "Começar pelo que o usuário vê evita retrabalho 📱",
], L("Como pedir um app para a IA sem se arrepender.\n\nSalva.")),

("b", [
 "Eu não confio em nada que não tem aviso de falha.",
 "Todo sistema que eu construo avisa quando algo dá errado.",
 "E o aviso já vem dizendo o que fazer, não só o que quebrou.",
 "\"Deu erro\" é inútil. \"Deu erro, faça isso\" é solução.",
 "Aviso bom é metade do conserto 🔔",
], L("Alerta sem solução é só barulho.\n\nSalva para aplicar nos seus sistemas.")),

("p", [
 "3 sinais de que você usa IA do jeito certo:",
 "1. Você revisa o que ela entrega antes de usar.",
 "2. Você guarda o que funcionou.",
 "3. Você sabe explicar o que foi feito, mesmo sem ter digitado.",
 "Se você tem os 3, já está na frente da maioria 🏁",
], L("Faça o teste. Quantos desses você já faz?\n\nComenta quantos.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | DECIDIR MELHOR",
 "1. \"Liste os prós e contras como se você fosse contra a minha ideia.\"",
 "2. \"Qual a pior consequência possível e como eu evito?\"",
 "3. \"Se eu estiver errado, onde eu estou errando?\"",
 "4. \"Me diga o que alguém experiente nesse assunto me perguntaria.\"",
 "A IA é um ótimo advogado do diabo 😈",
], L("Use a IA para discordar de você. É aí que ela mais ajuda.\n\nSalva.")),

("p", [
 "Por que eu construo as minhas próprias ferramentas:",
 "Porque ferramenta pronta faz o que a maioria precisa.",
 "A minha faz exatamente o que eu preciso.",
 "Antes eu precisava contratar. Hoje eu converso com a IA e testo no mesmo dia.",
 "Quem aprende a construir não depende de ninguém para começar 🛠️",
], L("Construir a própria ferramenta ficou acessível. Pouca gente percebeu.\n\nSegue para ver o que eu faço.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | ORGANIZAR A VIDA",
 "1. \"Me ajude a separar o que é urgente, importante e só barulho.\"",
 "2. \"Monte um plano da semana com no máximo 3 prioridades por dia.\"",
 "3. \"O que eu estou fazendo que poderia ser eliminado?\"",
 "4. \"Faça um resumo do que ficou decidido hoje.\"",
 "Não é produtividade. É clareza 🧭",
], L("Clareza vale mais que produtividade. Esses comandos ajudam.\n\nSalva.")),
]
