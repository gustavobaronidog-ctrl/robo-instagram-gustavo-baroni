#!/usr/bin/env python3
"""Vigia do robô do Instagram pessoal (@gustavobaroni.ai). Roda no GitHub Actions, sem depender do Claude.
Se algo estiver errado o job FALHA e o próprio GitHub manda e-mail ao dono do repositório, já com a solução.
Confere: (1) token válido e conta certa, (2) posts atrasados, (3) estoque da fila, (4) arquivos das próximas postagens."""
import datetime, json, os, sys, urllib.parse, urllib.request

REPO = "https://github.com/gustavobaronidog-ctrl/robo-instagram-gustavo-baroni"
problemas, avisos = [], []


def prob(msg, sem, com):
    problemas.append((msg, sem, com))


def fmt(msg, sem, com):
    return f"{msg}%0A>> SEM O CLAUDE: {sem}%0A>> COM O CLAUDE: {com}%0A>> Guia completo: {REPO}/blob/main/SOCORRO.md"


agora = datetime.datetime.utcnow() - datetime.timedelta(hours=3)
hoje = agora.date().isoformat()

# 1) token e conta
tok, uid = os.environ.get("IG_TOKEN", "").strip(), os.environ.get("IG_USER_ID", "").strip()
if not tok:
    prob("o segredo IG_TOKEN está vazio no GitHub",
         f"abra {REPO}/settings/secrets/actions , clique no lápis de IG_TOKEN e cole o token novo (veja o passo a passo no SOCORRO).",
         "abra o Claude e escreva: o token do Instagram pessoal venceu, gere outro e coloque no GitHub.")
else:
    try:
        q = urllib.parse.quote(tok)
        with urllib.request.urlopen(f"https://graph.facebook.com/v21.0/{uid}?fields=username&access_token={q}", timeout=30) as r:
            nome = json.load(r).get("username")
        print("conta:", nome)
        if nome != "gustavobaroni.ai":
            prob(f"o token pertence a outra conta ({nome}), o robô não vai postar",
                 "gere o token de novo logado no @gustavobaroni.ai (veja SOCORRO) e troque em IG_TOKEN.",
                 "abra o Claude e escreva: o token do Instagram pessoal está na conta errada, corrija.")
    except Exception as e:
        prob(f"o token do Instagram pessoal não funciona ({e})",
             "gere outro no painel da Meta (veja o passo a passo no SOCORRO) e troque em Settings > Secrets and variables > Actions > IG_TOKEN.",
             "abra o Claude e escreva: o token do Instagram pessoal venceu, troque.")

# 2) filas, estoque, atrasos e arquivos de cada tipo de post
from horarios import slots_do_dia
TIPOS = {  # nome: (fila, estado, posts por dia a partir de 21/11)
    "educativo": ("fila.json", "estado.json", 4),
    "estrategia": ("fila_estrategia.json", "estado_estrategia.json", 3),
    "reflexao": ("fila_reflexao.json", "estado_reflexao.json", 1),
    "noticia": ("fila_noticias.json", "estado_noticias.json", 4),
}


def ler(arq):
    return json.load(open(arq, encoding="utf-8"))


try:
    reserva = len(ler("fila_reserva.json")) - ler("estado_reserva.json")["proximo"]
except Exception:
    reserva = 0
print(f"reserva: {reserva} carrosséis")
for nome, (fila_arq, est_arq, por_dia) in TIPOS.items():
    try:
        fila, est = ler(fila_arq), ler(est_arq)
        p = est["proximo"]
    except Exception as e:
        prob(f"não consegui ler {fila_arq}/{est_arq} ({e})",
             f"abra {REPO}/commits/main , clique no último commit que mexeu nesses arquivos e depois em 'Revert' e confirme.",
             f"abra o Claude e escreva: o vigia do Instagram pessoal não lê a fila de {nome}, conserte.")
        continue
    resta = len(fila) - p
    if nome == "noticia":
        # notícia sem item de hoje é coberta pela reserva; só avisa
        hoje_n = sum(1 for x in fila if x.get("data") == hoje)
        if (agora.hour, agora.minute) >= (9, 30) and hoje_n < 4 and hoje >= "2026-11-21":
            msg = f"as notícias de IA de hoje não foram todas geradas ({hoje_n} de 4); a reserva ({reserva}) cobre o que faltar"
            if reserva > 0:
                avisos.append(msg)
            else:
                prob(msg, f"abra {REPO}/actions/workflows/noticias.yml , clique em 'Run workflow' (1 vez).",
                     "abra o Claude e escreva: o robô de notícias do Instagram pessoal não gerou os posts, conserte e crie carrosséis de reserva.")
    else:
        dias = resta / por_dia
        print(f"{nome}: faltam {resta} = {dias:.0f} dias")
        sem = (f"abra {REPO}/blob/main/{est_arq} , clique no lápis, troque o número de \"proximo\" por 0 (a fila recomeça do início "
               "e reposta conteúdo antigo, sem parar o robô) e clique em Commit changes. Depois peça conteúdo novo com calma.")
        com = f"abra o Claude e escreva: criar mais posts de {nome} para o Instagram pessoal."
        if resta <= 0:
            prob(f"a fila de {nome} do Instagram pessoal ACABOU, nada desse tipo será postado", sem, com)
        elif dias < 2:
            prob(f"estoque de {nome} do Instagram pessoal para menos de 2 dias ({resta} posts)", sem, com)
        elif dias < 7:
            avisos.append(f"estoque de {nome} do Instagram pessoal baixo: {dias:.0f} dias")
    # atrasados (mais de 90 min depois do horário e ainda não saiu)
    saiu = est.get("por_dia", {}).get(hoje, 0)
    devia = sum(1 for m in slots_do_dia(nome, hoje) if (agora.hour * 60 + agora.minute) >= m + 90)
    if 7 <= agora.hour < 22 and saiu < devia and (resta > 0 or reserva > 0):
        prob(f"{devia - saiu} post(s) de {nome} atrasado(s) há mais de 90 min (saíram {saiu} de {devia} previstos até agora)",
             f"abra {REPO}/actions/workflows/maestro.yml , clique em 'Run workflow' (à direita) e no botão verde 'Run workflow'. Clique só 1 vez: o robô publica o que estiver atrasado.",
             "abra o Claude e escreva: o robô do Instagram pessoal atrasou os posts, destrave.")
    # arquivos das próximas postagens
    faltando = [os.path.join("imagens", x) for it in fila[p:p + 12] for x in it.get("slides", []) if not os.path.exists(os.path.join("imagens", x))]
    if faltando:
        prob(f"arquivos que faltam no GitHub ({nome}): {', '.join(faltando[:6])}",
             f"abra {REPO}/blob/main/{est_arq} , clique no lápis, some 1 ao número de 'proximo' (pula o post com defeito) e clique em Commit changes.",
             "abra o Claude e escreva: conferir as imagens que faltam no robô do Instagram pessoal e subir.")

for a in avisos:
    print(f"::warning::{a}")
if problemas:
    resumo = os.environ.get("GITHUB_STEP_SUMMARY")
    for m, sem, com in problemas:
        print(f"::error title=Robo Instagram pessoal::{fmt(m, sem, com)}")
        if resumo:
            with open(resumo, "a", encoding="utf-8") as f:
                f.write(f"### Problema: {m}\n- **Sem o Claude:** {sem}\n- **Com o Claude:** {com}\n\n")
    sys.exit(1)
print("Tudo certo.")
