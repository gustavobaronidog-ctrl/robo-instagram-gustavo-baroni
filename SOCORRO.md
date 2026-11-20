# SOCORRO: robô do Instagram pessoal (@gustavobaroni.ai) sem o Claude

Tudo aqui roda no GitHub, mesmo com o limite do Claude acabado.
Repositório: https://github.com/gustavobaronidog-ctrl/robo-instagram-gustavo-baroni

## Como apertar um botão
1. Abra o repositório e clique na aba **Actions**.
2. Clique em **Maestro dos posts** (menu da esquerda) ou em **Vigia**.
3. Clique em **Run workflow** e depois no botão verde **Run workflow**. Clique só 1 vez: o robô publica só o que estiver atrasado.

## Como o robô trabalha
O **Maestro** fica de plantão: confere a cada 5 minutos o que já devia ter saído hoje (carrosséis 08h, 12h e 15h, horário de Brasília), compara com o que o Instagram já mostra e publica só o que faltar, no máximo 1 por conferência, entre 7h e 22h. Cada rodada dura uns 50 minutos e liga a próxima sozinha. Se o GitHub atrasar ou pular, o agendamento de reserva (minutos 17 e 47) religa. Cada post publicado é gravado na hora no GitHub.

O **Vigia** roda 5 vezes por dia e confere: token válido e conta certa, posts atrasados, estoque da fila e arquivos das próximas postagens. Se algo estiver errado, o job fica vermelho e o GitHub manda e-mail com o problema e a solução.

## Chegou e-mail "Run failed". O que fazer
| Problema | Sem o Claude | Com o Claude |
|---|---|---|
| post atrasado | Actions > Maestro dos posts > Run workflow (1 vez) | "o robô do Instagram pessoal atrasou, destrave" |
| token vencido ou na conta errada | gerar outro (passo a passo abaixo) e trocar em Settings > Secrets and variables > Actions > IG_TOKEN | "o token do Instagram pessoal venceu, troque" |
| estoque acabando | trocar "proximo" por 0 em estado.json e Commit changes (a fila recomeça) | "criar mais carrosséis para o Instagram pessoal" |
| arquivo não abre | em estado.json somar 1 ao "proximo" (pula o post) e Commit changes | "uma imagem não abre, restaure" |

## Gerar um token novo (só se o antigo parar de funcionar)
1. Abra https://developers.facebook.com/apps/29857447583889035/use_cases/customize/?use_case_enum=INSTAGRAM_BUSINESS&selected_tab=Unified-Login-API-Setup&product_route=instagram-business
2. Abra a caixa **2. Gerar tokens de acesso**, na linha do **gustavobaroni.ai** clique em **Gerar token**.
3. Na janelinha, escolha **Continue with Instagram** e entre no **@gustavobaroni.ai** (confira o nome).
4. Marque "Estou ciente", clique em **Copiar**.
5. Em Settings > Secrets and variables > Actions, clique no lápis de **IG_TOKEN**, cole e salve.

## Só o Claude resolve
Código novo, criar conteúdo novo, Reels e vídeos. Nada aqui é compartilhado com o Tem Encaixe nem com o SeparaGo.

## Notícias de IA (3 por dia, formato jornal)
O workflow **Noticias de IA** roda às 6h40 (Brasília): lê as fontes de IA e o Hacker News, escolhe as 3 mais quentes, escreve a análise na sua voz (modelo gratuito do GitHub Models) e coloca na fila; o Maestro publica às 10h30, 14h30 e 17h. Se não gerar, o Vigia avisa por e-mail: Actions > Noticias de IA > Run workflow (1 vez).
