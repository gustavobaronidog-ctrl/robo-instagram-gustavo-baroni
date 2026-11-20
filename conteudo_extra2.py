# Lote 2: opiniões fortes, conselhos curtos e "o que quem constrói gostaria que entendessem".
EU = "@gustavobaroni.ai"


def L(txt):
    return f"{txt}\n\n{EU}"


POSTS = [
("b", [
 "Quem trabalha com IA todo dia gostaria que você soubesse essas 5 coisas:",
 "1. Ela não pensa por você. Ela acelera o seu pensamento.",
 "2. Quem não sabe o que quer recebe qualquer coisa.",
 "3. Revisar dá mais trabalho que gerar, e é onde está o valor.",
 "4. Não existe prompt mágico. Existe contexto bom.",
 "5. O próximo passo é aprender a construir com ela, não só conversar 🧩",
], L("Cinco verdades de quem usa IA todo dia.\n\nManda para alguém que ainda acha que é só perguntar.")),

("p", [
 "AGORA:\n\nconstruir um sistema que antes levava meses já é possível em dias.",
 "Não porque ficou fácil. Porque ficou acessível.",
 "Quem tem uma ideia clara e paciência para testar chega longe.",
 "Quem espera ter certeza para começar fica olhando.",
 "A diferença está em quem começa 🚀",
], L("O que antes pedia uma equipe hoje começa numa conversa.\n\nSegue para acompanhar.")),

("b", [
 "Conselho:\n\naprenda a perguntar bem antes de aprender a programar.",
 "Programar você aprende em meses. Perguntar bem muda tudo em dias.",
 "Quem sabe o problema que quer resolver já está 80% do caminho.",
 "A IA escreve o código. Você escolhe o que vale escrever.",
 "Comece pelo problema, não pela ferramenta 🎯",
], L("O problema bem descrito vale mais que qualquer ferramenta.\n\nSalva.")),

("p", [
 "Opinião impopular:\n\nmuita gente vai ficar para trás não por falta de acesso à IA, mas por medo de testar.",
 "Todo mundo tem a ferramenta. Poucos usam para construir.",
 "O medo de errar é o maior concorrente.",
 "Errar com IA custa minutos. Não testar custa anos.",
 "Teste hoje. Algo pequeno ⏳",
], L("Testar custa minutos. Esperar custa anos.\n\nFaz um teste hoje.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | MEMÓRIA",
 "1. \"Resuma o que decidimos hoje em 5 linhas para eu salvar.\"",
 "2. \"Liste o que ficou pendente e quem precisa decidir.\"",
 "3. \"Crie um glossário com os termos que usamos nessa conversa.\"",
 "4. \"Escreva as instruções para eu retomar isso amanhã sem perder nada.\"",
 "Quem registra não recomeça do zero 📓",
], L("Como não perder o fio do trabalho com IA.\n\nSalva.")),

("p", [
 "Eu mantenho um caderno digital onde registro tudo que construo.",
 "Decisões, erros, o que funcionou e por quê.",
 "Quando eu começo algo novo, eu já tenho uma base.",
 "Aprender uma vez e reutilizar é a maior alavanca que eu conheço.",
 "Quem anota evolui mais rápido que quem só faz 📓",
], L("O segredo de evoluir rápido é registrar.\n\nSegue para ver como eu organizo.")),

("b", [
 "3 coisas que a IA não sabe sobre o seu trabalho:",
 "1. O que o seu cliente realmente quer.",
 "2. O que você já tentou e não deu certo.",
 "3. O que não pode dar errado de jeito nenhum.",
 "Conte tudo isso. Contexto é o que separa resposta genérica de resposta útil 🧠",
], L("Quanto mais contexto, melhor a resposta.\n\nSalva.")),

("p", [
 "Nunca foi tão barato testar uma ideia.",
 "Em um dia você monta uma versão, mostra para alguém e descobre se vale.",
 "Antes, o teste custava meses e dinheiro.",
 "Quem testa mais ideias por mês tem mais chances de acertar uma.",
 "Velocidade de teste é vantagem competitiva 🏎️",
], L("O custo de testar ideias despencou.\n\nSalva e testa uma hoje.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | PROJETOS",
 "1. \"Quebre esse projeto em etapas que eu consiga terminar em um dia cada.\"",
 "2. \"O que eu preciso decidir antes de começar a etapa 1?\"",
 "3. \"Qual etapa traz resultado visível mais rápido?\"",
 "4. \"Me diga quando eu estiver complicando demais.\"",
 "Projeto grande vira vários pequenos 🧱",
], L("Como tirar um projeto grande do papel sem travar.\n\nSalva.")),

("p", [
 "Dois tipos de pessoas com IA:",
 "As que pedem respostas.",
 "E as que constroem coisas.",
 "Quem pede respostas economiza tempo.",
 "Quem constrói coisas cria ativos que trabalham sozinhos.",
 "De que lado você quer estar? 🤔",
], L("Duas formas de usar IA, com resultados bem diferentes.\n\nComenta de que lado você está.")),

("b", [
 "O que eu faria se estivesse começando hoje:",
 "1. Escolheria um problema real, pequeno e meu.",
 "2. Pediria para a IA me ajudar a resolver só ele.",
 "3. Mostraria para uma pessoa e ouviria sem defender.",
 "4. Melhoraria e repetiria.",
 "Sem curso caro, sem esperar permissão 🧭",
], L("O caminho mais curto para começar a construir com IA.\n\nSalva.")),

("p", [
 "Sistema bom não depende de você estar acordado.",
 "Ele roda, avisa se falhar e diz como resolver.",
 "Quem constrói assim recupera o tempo que perdia apagando incêndio.",
 "O objetivo não é trabalhar mais. É trabalhar uma vez e colher várias.",
 "Automatize o que se repete 🔁",
], L("Um sistema bom trabalha sozinho e avisa quando precisa de você.\n\nSegue.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | CRIAR AUTOMAÇÕES",
 "1. \"Que partes desse processo seguem sempre as mesmas regras?\"",
 "2. \"Escreva um script simples que faça só isso, sem enfeites.\"",
 "3. \"Como eu rodo isso todo dia sem deixar o computador ligado?\"",
 "4. \"Me avise por e-mail se falhar, com o que fazer.\"",
 "Quatro perguntas, um robô trabalhando por você 🤖",
], L("Do processo repetitivo ao robô que roda sozinho.\n\nSalva esse caminho.")),

("p", [
 "Hot take:\n\no problema da maioria dos negócios não é falta de ferramenta.",
 "É falta de um processo claro para a ferramenta seguir.",
 "Sem processo, a melhor tecnologia só acelera a confusão.",
 "Primeiro entenda o fluxo. Depois automatize 🔥",
], L("Ferramenta nenhuma salva um processo confuso.\n\nSalva e manda para quem precisa ouvir.")),

("b", [
 "5 hábitos de quem constrói rápido:",
 "1. Começa pelo mais simples que funciona.",
 "2. Testa com uma pessoa antes de mostrar para todo mundo.",
 "3. Corrige hoje o que descobriu hoje.",
 "4. Registra o aprendizado.",
 "5. Descansa para pensar melhor amanhã 😴",
], L("Velocidade vem de hábito, não de pressa.\n\nSalva.")),

("p", [
 "Eu comecei a tratar a IA como um estagiário muito rápido.",
 "Ele faz o que eu peço, rápido, mas precisa de instrução clara.",
 "Se eu digo \"faz algo legal\", ele inventa. Se eu digo exatamente o que quero, ele acerta.",
 "E eu sempre confiro antes de entregar.",
 "Clareza é a minha função agora 🧑‍💻",
], L("A IA é o estagiário mais rápido que existe. Instrução clara é tudo.\n\nSegue.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | QUANDO O CÓDIGO QUEBRA",
 "1. \"Aqui está o erro exato. O que ele quer dizer em português simples?\"",
 "2. \"Quais as 3 causas mais prováveis, da mais para a menos provável?\"",
 "3. \"Como eu confirmo qual delas é, antes de mudar qualquer coisa?\"",
 "4. \"Conserte só o necessário e explique o que mudou.\"",
 "Diagnóstico antes de remédio 🩺",
], L("Quando algo quebra, diagnostique antes de consertar.\n\nSalva.")),

("p", [
 "A pergunta que mais me ajudou a construir:",
 "\"Qual a versão mais simples disso que já resolve?\"",
 "Quase tudo que eu complicava podia ser feito com metade do esforço.",
 "Simplicidade não é falta de ambição. É respeito pelo tempo.",
 "Tira um recurso hoje 🧹",
], L("Simples que funciona vence complexo que nunca termina.\n\nSalva.")),

("b", [
 "Sinais de que o seu projeto está complicado demais:",
 "1. Você não consegue explicar em 3 frases.",
 "2. Tem recurso que ninguém pediu.",
 "3. Cada mudança quebra outra coisa.",
 "4. Só você sabe como funciona.",
 "Se marcou 2, simplifique antes de crescer ✂️",
], L("Quatro sinais de que está na hora de simplificar.\n\nSalva e confere o seu projeto.")),

("p", [
 "Verdade desconfortável:\n\ntudo que você faz repetidamente hoje já pode ser feito por um robô.",
 "A pergunta é se você vai aprender a construir esse robô.",
 "Quem aprende ganha tempo. Quem não aprende paga alguém que aprendeu.",
 "Os dois caminhos são válidos. Só um é barato 🤷",
], L("O que você repete todo dia pode ser automatizado.\n\nSegue para ver como.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | PESQUISAR UM MERCADO",
 "1. \"Quem são os 5 principais concorrentes e o que cada um faz melhor?\"",
 "2. \"O que as pessoas mais reclamam nesse mercado?\"",
 "3. \"Onde existe espaço que ninguém está atendendo?\"",
 "4. \"Quais riscos eu estou ignorando?\"",
 "Pesquise antes de construir 🔍",
], L("Como pesquisar um mercado em uma tarde.\n\nSalva.")),

("p", [
 "A maior vantagem de quem constrói com IA:",
 "Você erra rápido, barato e sozinho.",
 "Antes, errar custava uma equipe e meses.",
 "Agora você testa uma ideia de manhã e descarta à tarde, sem drama.",
 "Quem erra mais cedo acerta mais cedo ⚡",
], L("Errar barato e cedo é uma vantagem enorme.\n\nSalva.")),

("b", [
 "Antes de usar qualquer ferramenta nova, eu pergunto:",
 "1. Ela resolve um problema que eu realmente tenho?",
 "2. Quanto custa se eu quiser sair dela?",
 "3. Meus dados ficam comigo?",
 "4. Eu consigo fazer a mesma coisa de um jeito mais simples?",
 "Moda passa. Problema fica 🧐",
], L("4 perguntas para não cair em toda ferramenta da moda.\n\nSalva.")),

("p", [
 "Gente que usa IA e gente que constrói com IA vão ter resultados bem diferentes nos próximos anos.",
 "Os primeiros economizam tempo.",
 "Os segundos criam coisas que crescem sozinhas.",
 "Eu escolhi construir.",
 "Segue para ver o que sai disso 🏗️",
], L("Usar e construir com IA são jogos diferentes.\n\nSegue para acompanhar o meu.")),

("b", [
 "COMANDOS SECRETOS\nCLAUDE | TOMAR DECISÃO DIFÍCIL",
 "1. \"Liste as minhas opções, inclusive as que eu não considerei.\"",
 "2. \"Qual delas eu me arrependeria menos daqui a 5 anos?\"",
 "3. \"O que uma pessoa muito experiente me aconselharia?\"",
 "4. \"Que informação falta para eu decidir com segurança?\"",
 "A IA não decide. Ela amplia o seu olhar 🔭",
], L("Use a IA para enxergar mais opções antes de decidir.\n\nSalva.")),

("p", [
 "Se você me perguntasse qual habilidade desenvolver hoje:",
 "Saber explicar o que você quer com clareza.",
 "Para a IA, para o cliente, para o time.",
 "Quem explica bem coordena máquinas e pessoas.",
 "É a habilidade mais subestimada do momento 🗣️",
], L("Comunicação clara virou a habilidade técnica mais valiosa.\n\nSalva.")),

("b", [
 "O que eu aprendi errando com IA:",
 "1. Confiar sem testar sempre dá problema.",
 "2. Pedir tudo de uma vez bagunça o resultado.",
 "3. Sem registro, eu refazia o mesmo trabalho.",
 "4. Segurança deixada para depois nunca chega.",
 "5. Simples funciona. Complicado quebra 🧱",
], L("Cinco lições que custaram tempo e não precisam custar o seu.\n\nSalva.")),

("p", [
 "Eu uso a IA para três coisas:",
 "Construir o que antes eu não sabia construir.",
 "Revisar o que eu mesmo construí.",
 "Aprender rápido o que eu preciso para o próximo passo.",
 "Todo o resto, eu decido sozinho ✅",
], L("Três usos que mudaram minha forma de trabalhar.\n\nComenta como você usa.")),
]
