#!/usr/bin/env python3
# Robô do perfil pessoal @gustavobaroni.ai: publica carrosséis pela API oficial da Meta.
# Roda no GitHub Actions (maestro). Não depende do computador do Gustavo nem do Claude.
# Nada aqui é compartilhado com as empresas (conta, app, chaves e fila são só deste perfil).
import json, os, re, subprocess, sys, time, datetime, urllib.error, urllib.parse, urllib.request

APP_ID = os.environ.get("IG_APP_ID", "").strip()
REDIRECT = os.environ.get("IG_REDIRECT", "").strip()
SEGREDO = os.environ.get("IG_APP_SECRET", "").strip()
BRUTO = os.environ.get("IG_TOKEN", "").strip()


def _openssl(args, dado):
    return subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-a", "-A", *args, "-pass", "env:IG_APP_SECRET"],
                          input=dado.encode(), capture_output=True, check=True).stdout.decode().strip()


def obter_token():
    if os.path.exists("token.enc") and SEGREDO:  # token já guardado, cifrado com a chave secreta do app
        return _openssl(["-d"], open("token.enc").read().strip())
    m = re.search(r"long_lived_token=([^&#\s]+)", BRUTO) or re.search(r"access_token=([^&#\s]+)", BRUTO)
    if m:
        return urllib.parse.unquote(m.group(1))
    c = re.search(r"[?&#]code=([^&#\s]+)", BRUTO)
    if c:  # troca o código do login pelo token definitivo, uma vez só
        q = urllib.parse.urlencode({"client_id": APP_ID, "client_secret": SEGREDO, "redirect_uri": REDIRECT,
                                    "code": urllib.parse.unquote(c.group(1))})
        with urllib.request.urlopen(f"https://graph.facebook.com/v21.0/oauth/access_token?{q}", timeout=60) as r:
            tok = json.load(r)["access_token"]
        open("token.enc", "w").write(_openssl([], tok) + "\n")
        print("Token obtido e guardado cifrado.", flush=True)
        return tok
    return BRUTO


TOKEN = obter_token()
REPO = os.environ.get("GITHUB_REPOSITORY", "")
BRANCH = os.environ.get("GITHUB_REF_NAME", "main")
BASE = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/imagens/"


def agora_brt():
    return datetime.datetime.utcnow() - datetime.timedelta(hours=3)


def _get(url):
    with urllib.request.urlopen(url, timeout=60) as r:
        return json.load(r)


def descobrir_conta():
    q = urllib.parse.quote(TOKEN)
    try:  # token do login do Instagram
        eu = _get(f"https://graph.instagram.com/v21.0/me?fields=user_id,username&access_token={q}")
        return "https://graph.instagram.com/v21.0", str(eu["user_id"]), eu.get("username")
    except Exception:
        pass
    pags = _get(f"https://graph.facebook.com/v21.0/me/accounts?fields=instagram_business_account{{id,username}}&access_token={q}")
    for p in pags.get("data", []):
        ig = p.get("instagram_business_account")
        if ig and (not os.environ.get("IG_USERNAME") or ig.get("username") == os.environ["IG_USERNAME"]):
            return "https://graph.facebook.com/v21.0", ig["id"], ig.get("username")
    ig = os.environ.get("IG_USER_ID", "").strip()
    eu = _get(f"https://graph.facebook.com/v21.0/{ig}?fields=id,username&access_token={q}")
    return "https://graph.facebook.com/v21.0", eu["id"], eu.get("username")


API, IG, NOME = descobrir_conta()
print("Conta:", NOME, flush=True)
if os.environ.get("IG_USERNAME") and NOME != os.environ["IG_USERNAME"]:
    sys.exit(f"PARADO: o token é da conta {NOME}, não de {os.environ['IG_USERNAME']}. Nada foi publicado.")


def chamar(caminho, dados):
    corpo = urllib.parse.urlencode(dict(dados, access_token=TOKEN)).encode()
    try:
        with urllib.request.urlopen(urllib.request.Request(f"{API}/{caminho}", data=corpo), timeout=120) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        print("ERRO da Meta:", e.read().decode()[:600], flush=True)
        raise


def esperar_pronto(cid, tentativas=20):
    for _ in range(tentativas):
        with urllib.request.urlopen(f"{API}/{cid}?fields=status_code&access_token={urllib.parse.quote(TOKEN)}", timeout=60) as r:
            st = json.load(r).get("status_code")
        if st == "FINISHED":
            return True
        if st == "ERROR":
            raise RuntimeError(f"container {cid} deu ERROR")
        time.sleep(15)
    raise RuntimeError(f"container {cid} não ficou pronto")


def publicar(fila_arq, estado_arq):
    """Publica o próximo carrossel da fila. Devolve True se publicou."""
    fila = json.load(open(fila_arq, encoding="utf-8"))
    estado = json.load(open(estado_arq))
    i = estado["proximo"]
    if i >= len(fila):
        print(f"Fila {fila_arq} terminada: nada a publicar. AVISO: criar mais conteúdo.", flush=True)
        return False
    item = fila[i]
    print(f"Publicando {fila_arq} #{item['carrossel']} (posição {i+1}/{len(fila)})", flush=True)
    filhos = [chamar(f"{IG}/media", {"image_url": BASE + n, "is_carousel_item": "true"})["id"] for n in item["slides"]]
    for c in filhos:
        esperar_pronto(c)
    pai = chamar(f"{IG}/media", {"media_type": "CAROUSEL", "children": ",".join(filhos), "caption": item["legenda"]})["id"]
    esperar_pronto(pai)
    pub = chamar(f"{IG}/media_publish", {"creation_id": pai})
    print("PUBLICADO:", pub, flush=True)
    hoje = agora_brt().strftime("%Y-%m-%d")
    estado["proximo"] = i + 1
    estado["ultimo_post_id"] = pub.get("id")
    estado.setdefault("por_dia", {})
    estado["por_dia"] = {hoje: estado["por_dia"].get(hoje, 0) + 1}  # só guarda o dia de hoje
    json.dump(estado, open(estado_arq, "w"), indent=1)
    return True


if __name__ == "__main__":
    publicar(*(sys.argv[1:3] or ["fila.json", "estado.json"]))
