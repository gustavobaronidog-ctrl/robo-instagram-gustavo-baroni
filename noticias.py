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
POR_DIA = 4
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
    ("Airbnb Engineering", "https://medium.com/feed/airbnb-engineering"),
    ("Anthropic (Hacker News)", "https://hnrss.org/newest?q=anthropic&points=50"),
    ("Perplexity (Hacker News)", "https://hnrss.org/newest?q=perplexity&points=50"),
    ("Notion", "https://www.notion.com/blog/rss.xml"),
    ("Shopify Engineering", "https://shopify.engineering/blog.atom"),
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
Abaixo estão notícias de IA das últimas 36 horas (com o "quente" = termômetro de repercussão). Escolha exatamente {n} notícias DIFERENTES entre si: priorize o que está bombando AGORA, as polêmicas e o que muda a vida de quem empreende ou constrói com IA. Varie os ângulos entre as {n}: (a) lançamento de laboratório (OpenAI, Anthropic, Google, ElevenLabs, Perplexity), (b) empresa grande ou conhecida usando IA no negócio (Airbnb, Gamma, Notion, Shopify, Klarna etc.: o que lançou e o que a IA passou a fazer), (c) polêmica ou regra. Evite notícia fraca, repetida ou só de produto menor.
Para cada uma escreva um post em formato de jornal. REGRAS: use só fatos presentes no título/resumo dado; não invente números, nomes nem citações; se não souber, diga o que está em aberto. Não cite empresas ou produtos do Gustavo e não fale de agenda, horário ou salão. Não copie frases da fonte. Sem hashtag.
Campos (JSON): manchete (até 90 caracteres, estilo manchete de jornal, forte e clara), subtitulo (até 140), contexto (até 330 caracteres: o que aconteceu, objetivo), importa (até 330: por que isso importa para quem empreende), leitura (até 380: a SUA leitura/conclusão como Gustavo, com opinião e um ponto que pouca gente está vendo), acao (até 300: o que o empresário pode fazer com isso esta semana), pergunta (até 110: pergunta aberta que gere comentário, tomando um lado), numeros (lista de 0 a 3 objetos {{\"n\": número ou dado curto com unidade, ex. \"US$ 22 bi\", \"r\": o que o número mede, até 70 caracteres}} usando SOMENTE números que aparecem no título/resumo; se não houver, lista vazia), fonte (nome da fonte), url (link exato dado), legenda (2 a 3 frases curtas que prendem, terminando com a pergunta; sem hashtag).
Responda SOMENTE um JSON no formato {{"posts":[{{...}},{{...}},{{...}}]}}.

NOTÍCIAS:
{lista}"""


def chamar_modelo(url, modelo, token, corpo_msgs):
    """Chama um endpoint de chat/completions com curl -i e devolve (status, corpo)."""
    import subprocess
    corpo = json.dumps({"model": modelo, "temperature": 0.7, "max_tokens": 4000, "messages": corpo_msgs})
    r = subprocess.run(["curl", "-sS", "-i", "-L", "-X", "POST", url, "-H", f"Authorization: Bearer {token}",
                        "-H", "Content-Type: application/json", "-H", "Accept: application/json",
                        "-H", "User-Agent: noticias-gustavo-baroni", "-d", corpo], capture_output=True, text=True, timeout=170)
    saida = r.stdout.replace("\r\n", "\n")
    cab, _, resto = saida.rpartition("\n\n")
    status = cab.split("\n")[0] if cab else "sem status"
    return status, (resto or saida), r.stderr[:200]


def chamar_gemini(modelo, chave, prompt):
    import subprocess
    corpo = json.dumps({"contents": [{"parts": [{"text": prompt}]}],
                        "generationConfig": {"temperature": 0.7, "responseMimeType": "application/json", "maxOutputTokens": 6000}})
    r = subprocess.run(["curl", "-sS", "-i", "-X", "POST", f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent",
                        "-H", f"x-goog-api-key: {chave}", "-H", "Content-Type: application/json", "-d", corpo],
                       capture_output=True, text=True, timeout=40)
    saida = r.stdout.replace("\r\n", "\n")
    cab, _, resto = saida.rpartition("\n\n")
    status = cab.split("\n")[0] if cab else "sem status"
    try:
        txt = json.loads(resto)["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        txt = ""
    return status, txt, (resto[:300] if not txt else ""), r.stderr[:150]


def modelos_gemini(chave):
    """Modelos flash que a chave pode usar (a lista do Google muda; o robô descobre sozinho)."""
    import subprocess
    achados = []
    try:
        r = subprocess.run(["curl", "-sS", "https://generativelanguage.googleapis.com/v1beta/models?pageSize=200", "-H", f"x-goog-api-key: {chave}"],
                           capture_output=True, text=True, timeout=60)
        for m in json.loads(r.stdout).get("models", []):
            nome = m["name"].split("/")[-1]
            if "flash" in nome and "lite" not in nome and "generateContent" in m.get("supportedGenerationMethods", []) \
                    and not any(x in nome for x in ("image", "tts", "audio", "live", "thinking", "preview-0", "exp")):
                achados.append(nome)
    except Exception as e:
        print(f"  não consegui listar os modelos: {e}")
    achados.sort(key=lambda n: [int(x) if x.isdigit() else 0 for x in re.findall(r"\d+", n)], reverse=True)
    print("modelos flash disponíveis:", achados[:4])
    # Quatro modelos diferentes, para manter o tempo de recuperação dentro do limite do Actions.
    return achados[:4]


def validar(txt, n):
    txt = re.sub(r"^```(?:json)?|```$", "", txt.strip(), flags=re.M).strip()
    ini, fim = txt.find("{"), txt.rfind("}")
    posts = json.loads(txt[ini:fim + 1])["posts"]
    return [p for p in posts if all(p.get(k) for k in ("manchete", "subtitulo", "contexto", "importa", "leitura", "acao", "pergunta", "fonte", "legenda"))][:n]


def redigir(cands, n):
    lista = "\n".join(f"{i+1}. [{c['fonte']}] (quente={c['quente']}) {c['titulo']} | {c['resumo'][:260]} | {c['url']}" for i, c in enumerate(cands[:40]))
    token = os.environ.get("GITHUB_TOKEN", "")
    prompt = PROMPT.format(n=n, lista=lista)
    msgs = [{"role": "user", "content": prompt}]
    chave = os.environ.get("GEMINI_API_KEY", "").strip()
    if chave:
        modelos = dict.fromkeys(["gemini-3.8-flash"] + modelos_gemini(chave) + ["gemini-flash-latest", "gemini-2.5-flash"])
        for modelo in modelos:
            for tentativa in range(2):
                try:
                    status, txt, corpo, err = chamar_gemini(modelo, chave, prompt)
                    print(f"{modelo} @ gemini (tentativa {tentativa + 1}/3): {status} {err}")
                    if txt:
                        posts = validar(txt, n)
                        if posts:
                            print(f"redigido com {modelo}: {len(posts)} posts")
                            return posts
                        print(f"  sem posts válidos: {txt[:200]!r}")
                        break
                    print(f"  corpo: {corpo!r}")
                    # 429/5xx são falhas transitórias; tenta novamente antes de trocar de modelo.
                    if not any(codigo in status for codigo in ("429", "500", "502", "503", "504")):
                        break
                    if tentativa < 1:
                        espera = 15
                        print(f"  serviço indisponível; nova tentativa em {espera}s")
                        time.sleep(espera)
                except Exception as e:
                    print(f"  erro com {modelo}: {e}")
                    if tentativa < 1:
                        time.sleep(15)
    tentativas = [("https://models.github.ai/inference/chat/completions", m) for m in ("openai/gpt-4.1", "openai/gpt-4o", "openai/gpt-4.1-mini")] + \
                 [("https://models.inference.ai.azure.com/chat/completions", m) for m in ("gpt-4o", "gpt-4o-mini")]
    for url, modelo in tentativas:
        try:
            status, bruto, err = chamar_modelo(url, modelo, token, msgs)
            print(f"{modelo} @ {url.split('/')[2]}: {status} {err}")
            if '"choices"' not in bruto:
                print(f"  corpo: {bruto[:300]!r}")
                continue
            txt = json.loads(bruto)["choices"][0]["message"]["content"] or ""
            txt = re.sub(r"^```(?:json)?|```$", "", txt.strip(), flags=re.M).strip()
            ini, fim = txt.find("{"), txt.rfind("}")
            posts = json.loads(txt[ini:fim + 1])["posts"]
            posts = [p for p in posts if all(p.get(k) for k in ("manchete", "subtitulo", "contexto", "importa", "leitura", "acao", "pergunta", "fonte", "legenda"))]
            if posts:
                print(f"redigido com {modelo}: {len(posts)} posts")
                return posts[:n]
            print(f"  texto sem posts válidos: {txt[:200]!r}")
        except Exception as e:
            print(f"  erro com {modelo}: {e}")
    raise SystemExit("nenhum modelo respondeu")


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


VERM, PRETO, BRANCO = (214, 32, 39), (14, 14, 14), (255, 255, 255)
PAPEL = (250, 247, 240)


def arte_fundo(seed, forte=True):
    """Fundo diagramado escuro (rede de nós, grade e brilho vermelho), sem depender de imagens externas."""
    import random
    from PIL import ImageFilter
    rnd = random.Random(seed)
    base = Image.new("RGB", (W, H), (9, 9, 13))
    g = ImageDraw.Draw(base)
    for y in range(H):
        t = y / H
        g.line((0, y, W, y), fill=(int(10 + 26 * t), int(10 + 4 * t), int(14 + 6 * t)))
    brilho = Image.new("RGB", (W, H), (0, 0, 0))
    bd = ImageDraw.Draw(brilho)
    for _ in range(3):
        cx, cy, r = rnd.randint(150, 930), rnd.randint(150, 1200), rnd.randint(260, 420)
        bd.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(150, 20, 28))
    brilho = brilho.filter(ImageFilter.GaussianBlur(150))
    base = Image.blend(base, Image.composite(brilho, base, brilho.convert("L")), 0.55)
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    o = ImageDraw.Draw(ov)
    for x in range(0, W, 90):
        o.line((x, 0, x, H), fill=(255, 255, 255, 14))
    for y in range(0, H, 90):
        o.line((0, y, W, y), fill=(255, 255, 255, 14))
    nos = [(rnd.randint(40, W - 40), rnd.randint(140, H - 140)) for _ in range(26 if forte else 16)]
    for i, p1 in enumerate(nos):
        for p2 in sorted(nos, key=lambda q: (q[0] - p1[0]) ** 2 + (q[1] - p1[1]) ** 2)[1:3]:
            o.line((p1, p2), fill=(255, 255, 255, 46), width=2)
    for (x, y) in nos:
        r = rnd.choice([5, 7, 10])
        cor = (232, 52, 58, 230) if rnd.random() < 0.3 else (255, 255, 255, 170)
        o.ellipse((x - r, y - r, x + r, y + r), fill=cor)
    base.paste(ov, (0, 0), ov)
    pel = Image.new("RGBA", (W, H), (0, 0, 0, 95 if forte else 140))
    base.paste(pel, (0, 0), pel)
    return base


def bloco(im, box, cor=(0, 0, 0), alpha=255, raio=28):
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    ImageDraw.Draw(ov).rounded_rectangle(box, radius=raio, fill=cor + (alpha,))
    im.paste(ov, (0, 0), ov)


def moldura(n, total, data_txt, escuro=False, seed=0):
    if escuro:
        im = arte_fundo(seed, forte=(n == 1))
        fg, mut = BRANCO, (200, 200, 205)
    else:
        im = Image.new("RGB", (W, H), PAPEL)
        fg, mut = TINTA, CINZA
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 14), fill=VERM)
    d.text((M, 54), "GUSTAVO BARONI · IA & AUTOMAÇÃO", font=f(SANS_B, 25), fill=fg)
    tw = d.textlength(data_txt, font=f(SANS, 25))
    d.text((W - M - tw, 54), data_txt, font=f(SANS, 25), fill=mut)
    d.rectangle((M, 104, W - M, 110), fill=fg)
    d.rectangle((M, 118, W - M, 120), fill=fg)
    d.rectangle((M, H - 118, W - M, H - 116), fill=fg)
    d.text((M, H - 92), f"{n}/{total}", font=f(SANS_B, 28), fill=fg)
    tw = d.textlength(HANDLE, font=f(SANS_B, 28))
    d.text((W - M - tw, H - 92), HANDLE, font=f(SANS_B, 28), fill=fg)
    return im, d


def faixa(d, txt, y, cor=VERM, tcor=BRANCO, x=M):
    fnt = f(SANS_B, 32)
    w = d.textlength(txt, font=fnt) + 56
    d.rectangle((x, y, x + w, y + 64), fill=cor)
    d.text((x + 28, y + 14), txt, font=fnt, fill=tcor)
    return x + w


def rotulo(d, txt, y=156, fg=TINTA):
    d.rectangle((M, y, M + 12, y + 46), fill=VERM)
    d.text((M + 30, y + 4), txt, font=f(SANS_B, 34), fill=fg)
    d.rectangle((M, y + 66, W - M, y + 68), fill=fg)


def painel_numero(im, d, y, h, numero, legenda, escuro=False):
    if escuro:
        bloco(im, (M, y, W - M, y + h), (0, 0, 0), 190)
    else:
        d.rounded_rectangle((M, y, W - M, y + h), radius=28, fill=PRETO)
    d.rectangle((M, y + 36, M + 14, y + h - 36), fill=VERM)
    fnt = None
    for tam in range(min(190, int(h * 0.52)), 60, -6):
        fnt = f(SERIF_B, tam)
        if d.textlength(numero, font=fnt) <= W - 2 * M - 90:
            break
    d.text((M + 52, y + 30), numero, font=fnt, fill=BRANCO)
    caixa(d, legenda, SANS_B, M + 52, y + 24 + fnt.size * 1.2, W - 2 * M - 100, h - fnt.size * 1.2 - 40, 32, 22, esp=1.2, cor=(235, 235, 235))


def altura_texto(d, texto, path, maxw, ini, minimo, maxh, esp):
    for tam in range(ini, minimo - 1, -2):
        linhas = quebrar(d, texto, f(path, tam), maxw)
        if len(linhas) * tam * esp <= maxh or tam <= minimo:
            break
    return tam, len(linhas) * tam * esp


def renderizar(p, pasta, prefixo, data_txt, escuro=False):
    nomes, total = [], 5
    numeros = p.get("numeros") or []
    seed = sum(ord(c) for c in p["manchete"])
    fg = BRANCO if escuro else TINTA
    mut = (200, 200, 205) if escuro else CINZA
    # 1 capa
    im, d = moldura(1, total, data_txt, escuro, seed)
    faixa(d, "● ÚLTIMA HORA", 156)
    y = caixa(d, p["manchete"], SERIF_B, M, 252, W - 2 * M, 520, 100, 58, esp=1.08, cor=fg)
    d.rectangle((M, y + 14, M + 170, y + 22), fill=VERM)
    py = max(y + 52, 800)
    if numeros:
        painel_numero(im, d, py, 1130 - py, numeros[0]["n"], numeros[0]["r"], escuro)
    else:
        if escuro:
            bloco(im, (M, py, W - M, 1130), (0, 0, 0), 190)
        else:
            d.rounded_rectangle((M, py, W - M, 1130), radius=28, fill=PRETO)
        d.rectangle((M, py + 36, M + 14, 1130 - 36), fill=VERM)
        av = avatar(140)
        im.paste(av, (int(M + 52), int(py + 36)), av)
        d.text((M + 222, py + 52), "Minha análise", font=f(SANS_B, 40), fill=BRANCO)
        d.text((M + 222, py + 106), "Gustavo Baroni · deslize para ler", font=f(SANS, 30), fill=(210, 210, 210))
        caixa(d, p["subtitulo"], SERIF_I, M + 52, py + 200, W - 2 * M - 100, 1130 - py - 230, 36, 26, esp=1.22, cor=(235, 235, 235))
    d.text((M, H - 190), f"Fonte: {p['fonte']}", font=f(SANS, 28), fill=mut)
    tw = d.textlength("deslize →", font=f(SANS_B, 32))
    d.text((W - M - tw, H - 192), "deslize →", font=f(SANS_B, 32), fill=(240, 70, 76) if escuro else VERM)
    im.save(os.path.join(pasta, f"{prefixo}_s1.jpg"), quality=92); nomes.append(f"{prefixo}_s1.jpg")
    # 2 o que aconteceu (+ números)
    im, d = moldura(2, total, data_txt, escuro, seed + 1)
    rotulo(d, "O QUE ACONTECEU", fg=fg)
    ty = 262
    if len(numeros) > 1:
        for k, nm in enumerate(numeros[1:3]):
            painel_numero(im, d, 262 + k * 270, 240, nm["n"], nm["r"], escuro)
        ty = 262 + len(numeros[1:3]) * 270 + 10
        caixa(d, p["contexto"], SERIF, M, ty, W - 2 * M, H - 140 - ty, 44, 30, esp=1.28, cor=fg)
    else:
        caixa(d, p["contexto"], SERIF, M, ty, W - 2 * M, H - 160 - ty, 58, 36, esp=1.32, cor=fg)
    im.save(os.path.join(pasta, f"{prefixo}_s2.jpg"), quality=92); nomes.append(f"{prefixo}_s2.jpg")
    # 3 por que importa (bloco destacado)
    im, d = moldura(3, total, data_txt, escuro, seed + 2)
    rotulo(d, "POR QUE IMPORTA", fg=fg)
    if escuro:
        bloco(im, (M, 262, W - M, H - 170), (0, 0, 0), 175)
        d.rectangle((M, 300, M + 12, H - 208), fill=VERM)
    else:
        d.rounded_rectangle((M, 262, W - M, H - 170), radius=28, fill=PRETO)
    d.text((M + 44, 280), "\u201c", font=f(SERIF_B, 220), fill=VERM)
    caixa(d, p["importa"], SERIF_B, M + 52, 470, W - 2 * M - 104, H - 170 - 470 - 40, 64, 34, esp=1.28, cor=BRANCO)
    im.save(os.path.join(pasta, f"{prefixo}_s3.jpg"), quality=92); nomes.append(f"{prefixo}_s3.jpg")
    # 4 minha leitura
    im, d = moldura(4, total, data_txt, escuro, seed + 3)
    rotulo(d, "MINHA LEITURA", fg=fg)
    av = avatar(190)
    im.paste(av, (M, 262), av)
    d.ellipse((M - 6, 256, M + 196, 458), outline=VERM, width=6)
    d.text((M + 230, 300), "Gustavo Baroni", font=f(SANS_B, 46), fill=fg)
    d.text((M + 230, 360), HANDLE, font=f(SANS, 30), fill=mut)
    faixa(d, "ANÁLISE", 408 - 12, x=M + 230)
    caixa(d, p["leitura"], SERIF, M, 500, W - 2 * M, H - 160 - 500, 52, 34, esp=1.3, cor=fg)
    im.save(os.path.join(pasta, f"{prefixo}_s4.jpg"), quality=92); nomes.append(f"{prefixo}_s4.jpg")
    # 5 ação + pergunta (caixa vermelha ajustada ao texto, sem espaço vazio)
    im, d = moldura(5, total, data_txt, escuro, seed + 4)
    rotulo(d, "O QUE FAZER ESTA SEMANA", fg=fg)
    y = caixa(d, p["acao"], SERIF, M, 262, W - 2 * M, 430, 54, 34, esp=1.3, cor=fg)
    larg = W - 2 * M - 88
    tam, alt = altura_texto(d, p["pergunta"], SERIF_B, larg, 76, 40, 380, 1.16)
    by = int(y + 44)
    bh = int(alt + 88)
    d.rounded_rectangle((M, by, W - M, by + bh), radius=28, fill=VERM)
    caixa(d, p["pergunta"], SERIF_B, M + 44, by + 44, larg, alt + 4, tam, tam, esp=1.16, cor=BRANCO)
    cy = by + bh + 36
    d.text((M, cy), "Responde nos comentários. Eu leio todos.", font=f(SANS_B, 32), fill=(240, 70, 76) if escuro else VERM)
    d.text((M, cy + 50), "Segue para ver o que muda antes de virar tendência.", font=f(SANS, 29), fill=mut)
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
        slides = renderizar(p, "imagens", prefixo, data_txt, escuro=(num % 2 == 0))
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
    teste = os.environ.get("TESTE") == "true"
    if teste:
        cands = coletar()
        for p in redigir(cands, 2):
            print("TESTE OK:", p["manchete"], "|", p["fonte"])
        return
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
