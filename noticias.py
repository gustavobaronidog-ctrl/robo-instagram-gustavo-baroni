#!/usr/bin/env python3
"""Robô de notícias do perfil pessoal (@gustavobaroni.ai). Roda no GitHub Actions, sem depender do Claude.
1) lê fontes de IA (RSS + Hacker News), 2) escolhe as 3 notícias mais quentes/polêmicas e relevantes para quem empreende,
3) escreve a análise na voz do Gustavo (modelo gratuito do GitHub Models), 4) gera o post em formato de jornal (5 slides),
5) coloca na fila_noticias.json; o maestro publica às 10h30, 14h30 e 17h.
Uso: python3 noticias.py            (fluxo completo, automático)
     python3 noticias.py --de-json arquivo.json   (renderiza e enfileira posts já escritos, ex.: pelo Claude)"""
import datetime, json, os, re, sys, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont

W, H, M = 1080, 1350, 80
SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SERIF_I = "/usr/share/fonts/truetype/liberation/LiberationSerif-Italic.ttf"
SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
PAPEL, TINTA, CINZA, AZUL = (243, 238, 227), (17, 17, 17), (95, 90, 80), (29, 78, 216)
HANDLE = "@gustavobaroni.ai"
POR_DIA = 3
MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
DIAS = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
FONTES_RSS = [
    ("TechCrunch", "https://techcrunch.com/category/artificial-intelligence/feed/"),
    ("The Verge", "https://www.theverge.com/rss/ai-artificial-intelligence/index.xml"),
    ("VentureBeat", "https://venturebeat.com/category/ai/feed/"),
    ("MIT Technology Review", "https://www.technologyreview.com/topic/artificial-intelligence/feed"),
    ("OpenAI", "https://openai.com/news/rss.xml"),
    ("Google AI", "https://blog.google/technology/ai/rss/"),
    ("Ars Technica", "https://feeds.arstechnica.com/arstechnica/technology-lab"),
    ("Wired", "https://www.wired.com/feed/tag/ai/latest/rss"),
]


def agora_brt():
    return datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=3)


def baixar(url, headers=None, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (noticias-gustavo)", **(headers or {})})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


# ---------- coleta ----------
def coletar():
    corte = time.time() - 36 * 3600
    itens = []
    for nome, url in FONTES_RSS:
        try:
            raiz = ET.fromstring(baixar(url))
        except Exception as e:
            print(f"fonte falhou ({nome}): {e}")
            continue
        n = 0
        for it in list(raiz.iter("item")) + list(raiz.iter("{http://www.w3.org/2005/Atom}entry")):
            def pega(*tags):
                for t in tags:
                    el = it.find(t)
                    if el is not None and (el.text or el.get("href")):
                        return (el.text or el.get("href") or "").strip()
                return ""
            titulo = pega("title", "{http://www.w3.org/2005/Atom}title")
            link = pega("link", "{http://www.w3.org/2005/Atom}link")
            resumo = re.sub(r"<[^>]+>", " ", pega("description", "{http://www.w3.org/2005/Atom}summary"))
            resumo = re.sub(r"\s+", " ", resumo)[:500]
            data = pega("pubDate", "{http://www.w3.org/2005/Atom}updated", "{http://www.w3.org/2005/Atom}published")
            try:
                from email.utils import parsedate_to_datetime
                ts = parsedate_to_datetime(data).timestamp()
            except Exception:
                try:
                    ts = datetime.datetime.fromisoformat(data.replace("Z", "+00:00")).timestamp()
                except Exception:
                    ts = time.time()
            if titulo and ts >= corte:
                itens.append({"fonte": nome, "titulo": titulo, "url": link, "resumo": resumo, "quente": 0, "ts": ts})
                n += 1
        print(f"{nome}: {n} itens recentes")
    # termômetro do que está em alta: Hacker News (pontos e comentários)
    try:
        q = urllib.parse.urlencode({"tags": "story", "query": "AI", "numericFilters": f"created_at_i>{int(corte)},points>120", "hitsPerPage": 30})
        for h in json.loads(baixar("https://hn.algolia.com/api/v1/search_by_date?" + q)).get("hits", []):
            if h.get("title"):
                itens.append({"fonte": "Hacker News", "titulo": h["title"], "url": h.get("url") or f"https://news.ycombinator.com/item?id={h['objectID']}",
                              "resumo": "", "quente": (h.get("points") or 0) + 2 * (h.get("num_comments") or 0), "ts": h.get("created_at_i") or time.time()})
        print("Hacker News ok")
    except Exception as e:
        print(f"Hacker News falhou: {e}")
    vistos, saida = set(), []
    for i in sorted(itens, key=lambda x: (-x["quente"], -x["ts"])):
        k = re.sub(r"\W+", "", i["titulo"].lower())[:50]
        if k not in vistos:
            vistos.add(k)
            saida.append(i)
    return saida


# ---------- redação (modelo gratuito do GitHub Models) ----------
PROMPT = """Você é o Gustavo Baroni, um construtor de sistemas, IA e automação para empresários brasileiros. Escreva em português do Brasil, primeira pessoa, direto, concreto, sem exagero e sem jargão.
Abaixo estão notícias de IA das últimas 36 horas (com o "quente" = termômetro de repercussão). Escolha exatamente {n} notícias DIFERENTES entre si: priorize o que está bombando AGORA, as polêmicas e o que muda a vida de quem empreende ou constrói com IA. Evite notícia fraca, repetida ou só de produto menor.
Para cada uma escreva um post em formato de jornal. REGRAS: use só fatos presentes no título/resumo dado; não invente números, nomes nem citações; se não souber, diga o que está em aberto. Não cite empresas ou produtos do Gustavo e não fale de agenda, horário ou salão. Não copie frases da fonte. Sem hashtag.
Campos (JSON): manchete (até 90 caracteres, estilo manchete de jornal, forte e clara), subtitulo (até 140), contexto (até 330 caracteres: o que aconteceu, objetivo), importa (até 330: por que isso importa para quem empreende), leitura (até 380: a SUA leitura/conclusão como Gustavo, com opinião e um ponto que pouca gente está vendo), acao (até 300: o que o empresário pode fazer com isso esta semana), pergunta (até 110: pergunta aberta que gere comentário, tomando um lado), fonte (nome da fonte), url (link exato dado), legenda (2 a 3 frases curtas que prendem, terminando com a pergunta; sem hashtag).
Responda SOMENTE um JSON no formato {{"posts":[{{...}},{{...}},{{...}}]}}.

NOTÍCIAS:
{lista}"""


def redigir(cands, n):
    lista = "\n".join(f"{i+1}. [{c['fonte']}] (quente={c['quente']}) {c['titulo']} | {c['resumo'][:260]} | {c['url']}" for i, c in enumerate(cands[:40]))
    token = os.environ.get("GITHUB_TOKEN", "")
    ultimo = None
    for modelo in ["openai/gpt-4.1", "openai/gpt-4o", "openai/gpt-4.1-mini"]:
        try:
            corpo = json.dumps({"model": modelo, "temperature": 0.7, "max_tokens": 4000,
                                "messages": [{"role": "user", "content": PROMPT.format(n=n, lista=lista)}]}).encode()
            req = urllib.request.Request("https://models.github.ai/inference/chat/completions", data=corpo,
                                         headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json",
                                                  "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28",
                                                  "User-Agent": "noticias-gustavo-baroni"})
            with urllib.request.urlopen(req, timeout=120) as r:
                bruto = r.read().decode("utf-8", "replace")
            if '"choices"' not in bruto:  # segunda tentativa com curl (mesmo pedido, outra pilha de rede)
                import subprocess
                bruto = subprocess.run(["curl", "-sL", "-X", "POST", "https://models.github.ai/inference/chat/completions",
                                        "-H", "Accept: application/vnd.github+json", "-H", f"Authorization: Bearer {token}",
                                        "-H", "X-GitHub-Api-Version: 2022-11-28", "-H", "Content-Type: application/json",
                                        "-d", corpo.decode()], capture_output=True, text=True, timeout=150).stdout
            try:
                txt = json.loads(bruto)["choices"][0]["message"]["content"] or ""
            except Exception:
                print(f"resposta bruta de {modelo}: {bruto[:400]!r}")
                raise
            txt = re.sub(r"^```(?:json)?|```$", "", txt.strip(), flags=re.M).strip()
            ini, fim = txt.find("{"), txt.rfind("}")
            try:
                posts = json.loads(txt[ini:fim + 1])["posts"]
            except Exception:
                print(f"texto do modelo {modelo}: {txt[:400]!r}")
                raise
            posts = [p for p in posts if all(p.get(k) for k in ("manchete", "subtitulo", "contexto", "importa", "leitura", "acao", "pergunta", "fonte", "legenda"))]
            if len(posts) >= 1:
                print(f"redigido com {modelo}: {len(posts)} posts")
                return posts[:n]
        except Exception as e:
            ultimo = e
            print(f"modelo {modelo} falhou: {e}")
    raise SystemExit(f"nenhum modelo respondeu: {ultimo}")


# ---------- imagens (formato jornal) ----------
def f(path, tam):
    return ImageFont.truetype(path, tam)


def quebrar(d, texto, fnt, maxw):
    linhas = []
    for par in texto.split("\n"):
        atual = ""
        for pal in par.split():
            t = (atual + " " + pal).strip()
            if d.textlength(t, font=fnt) <= maxw:
                atual = t
            else:
                linhas.append(atual)
                atual = pal
        linhas.append(atual)
    return linhas


def caixa(d, texto, path, x, y, maxw, maxh, ini, minimo, esp=1.25, cor=TINTA):
    for tam in range(ini, minimo - 1, -2):
        fnt = f(path, tam)
        linhas = quebrar(d, texto, fnt, maxw)
        if len(linhas) * tam * esp <= maxh or tam <= minimo:
            break
    for i, l in enumerate(linhas):
        d.text((x, y + i * tam * esp), l, font=fnt, fill=cor)
    return y + len(linhas) * tam * esp


def avatar(tam):
    a = Image.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "avatar.jpg")).convert("RGB").resize((tam * 2, tam * 2), Image.LANCZOS)
    m = Image.new("L", (tam * 2, tam * 2), 0)
    ImageDraw.Draw(m).ellipse((0, 0, tam * 2 - 1, tam * 2 - 1), fill=255)
    a.putalpha(m)
    return a.resize((tam, tam), Image.LANCZOS)


def moldura(n, total, data_txt):
    im = Image.new("RGB", (W, H), PAPEL)
    d = ImageDraw.Draw(im)
    d.text((M, 62), "GUSTAVO BARONI · IA & AUTOMAÇÃO", font=f(SANS_B, 25), fill=TINTA)
    tw = d.textlength(data_txt, font=f(SANS, 25))
    d.text((W - M - tw, 62), data_txt, font=f(SANS, 25), fill=CINZA)
    d.rectangle((M, 112, W - M, 118), fill=TINTA)
    d.rectangle((M, 126, W - M, 128), fill=TINTA)
    d.rectangle((M, H - 118, W - M, H - 116), fill=TINTA)
    d.text((M, H - 92), f"{n}/{total}", font=f(SANS_B, 28), fill=TINTA)
    tw = d.textlength(HANDLE, font=f(SANS_B, 28))
    d.text((W - M - tw, H - 92), HANDLE, font=f(SANS_B, 28), fill=TINTA)
    return im, d


def etiqueta(d, txt, x, y, preenchida=True):
    fnt = f(SANS_B, 30)
    w = d.textlength(txt, font=fnt) + 44
    if preenchida:
        d.rectangle((x, y, x + w, y + 58), fill=AZUL)
        d.text((x + 22, y + 11), txt, font=fnt, fill=(255, 255, 255))
    else:
        d.text((x, y + 11), txt, font=fnt, fill=AZUL)


def renderizar(p, pasta, prefixo, data_txt):
    nomes = []
    total = 5
    # 1 capa
    im, d = moldura(1, total, data_txt)
    etiqueta(d, "ÚLTIMA HORA", M, 168)
    y = caixa(d, p["manchete"], SERIF_B, M, 262, W - 2 * M, 560, 112, 60, esp=1.1)
    d.rectangle((M, y + 22, M + 160, y + 28), fill=AZUL)
    caixa(d, p["subtitulo"], SERIF_I, M, y + 60, W - 2 * M, 1130 - (y + 60), 44, 30, esp=1.25, cor=CINZA)
    d.text((M, H - 190), f"Fonte: {p['fonte']}", font=f(SANS, 28), fill=CINZA)
    tw = d.textlength("deslize →", font=f(SANS_B, 30))
    d.text((W - M - tw, H - 190), "deslize →", font=f(SANS_B, 30), fill=AZUL)
    im.save(os.path.join(pasta, f"{prefixo}_s1.jpg"), quality=92); nomes.append(f"{prefixo}_s1.jpg")
    # 2-4 miolo
    miolo = [("O QUE ACONTECEU", p["contexto"]), ("POR QUE IMPORTA", p["importa"]), ("MINHA LEITURA", p["leitura"])]
    for k, (rot, txt) in enumerate(miolo, start=2):
        im, d = moldura(k, total, data_txt)
        etiqueta(d, rot, M, 168, preenchida=False)
        d.rectangle((M, 232, W - M, 234), fill=AZUL)
        topo = 280
        if rot == "MINHA LEITURA":
            im.paste(avatar(96), (M, 262), avatar(96))
            d.text((M + 118, 280), "Gustavo Baroni", font=f(SANS_B, 34), fill=TINTA)
            d.text((M + 118, 322), HANDLE, font=f(SANS, 26), fill=CINZA)
            topo = 400
        caixa(d, txt, SERIF, M, topo, W - 2 * M, H - 160 - topo, 58, 36, esp=1.32)
        im.save(os.path.join(pasta, f"{prefixo}_s{k}.jpg"), quality=92); nomes.append(f"{prefixo}_s{k}.jpg")
    # 5 ação + pergunta
    im, d = moldura(5, total, data_txt)
    etiqueta(d, "O QUE FAZER ESTA SEMANA", M, 168, preenchida=False)
    d.rectangle((M, 232, W - M, 234), fill=AZUL)
    y = caixa(d, p["acao"], SERIF, M, 280, W - 2 * M, 430, 50, 34, esp=1.3)
    d.rectangle((M, 770, W - M, 776), fill=TINTA)
    caixa(d, p["pergunta"], SERIF_B, M, 810, W - 2 * M, 300, 62, 38, esp=1.18)
    d.text((M, 1120), "Responde nos comentários. Eu leio todos.", font=f(SANS_B, 30), fill=AZUL)
    d.text((M, 1168), "Segue para ver o que muda antes de virar tendência.", font=f(SANS, 28), fill=CINZA)
    im.save(os.path.join(pasta, f"{prefixo}_s5.jpg"), quality=92); nomes.append(f"{prefixo}_s5.jpg")
    return nomes


def enfileirar(posts):
    agora = agora_brt()
    data_txt = f"{DIAS[agora.weekday()]}, {agora.day} de {MESES[agora.month - 1]} de {agora.year}"
    fila = json.load(open("fila_noticias.json", encoding="utf-8")) if os.path.exists("fila_noticias.json") else []
    usadas = json.load(open("noticias_usadas.json", encoding="utf-8")) if os.path.exists("noticias_usadas.json") else []
    os.makedirs("imagens", exist_ok=True)
    for p in posts:
        num = len(fila) + 1
        prefixo = f"n{agora.strftime('%Y%m%d')}_{num:03d}"
        slides = renderizar(p, "imagens", prefixo, data_txt)
        legenda = p["legenda"].strip() + f"\n\nFonte: {p['fonte']}\n\n{HANDLE}"
        fila.append({"noticia": num, "tipo": "noticia", "data": agora.date().isoformat(), "slides": slides, "legenda": legenda, "url": p.get("url", "")})
        usadas.append({"titulo": p["manchete"], "url": p.get("url", "")})
    json.dump(fila, open("fila_noticias.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(usadas[-300:], open("noticias_usadas.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"{len(posts)} posts de notícia enfileirados")


def main():
    if "--de-json" in sys.argv:
        enfileirar(json.load(open(sys.argv[sys.argv.index("--de-json") + 1], encoding="utf-8")))
        return
    hoje = agora_brt().date().isoformat()
    fila = json.load(open("fila_noticias.json", encoding="utf-8")) if os.path.exists("fila_noticias.json") else []
    ja = sum(1 for x in fila if x.get("data") == hoje)
    if ja >= POR_DIA:
        print(f"hoje já tem {ja} notícias na fila (talvez feitas pelo Claude): nada a fazer")
        return
    cands = coletar()
    usadas = json.load(open("noticias_usadas.json", encoding="utf-8")) if os.path.exists("noticias_usadas.json") else []
    urls = {u["url"] for u in usadas}
    cands = [c for c in cands if c["url"] not in urls]
    print(f"{len(cands)} candidatas")
    if len(cands) < 3:
        raise SystemExit("poucas notícias coletadas: fontes fora do ar?")
    enfileirar(redigir(cands, POR_DIA - ja))


if __name__ == "__main__":
    main()
