#!/usr/bin/env python3
# Gera os carrosséis (1080x1350) no estilo "post de pessoa": avatar redondo, nome com selo, texto grande em negrito.
# Uso: python3 gerar.py  -> escreve imagens/gNNN_sK.jpg e fila.json (sem tocar no estado.json).
import json, os, re, sys
from PIL import Image, ImageDraw, ImageFont

W, H = 1080, 1350
PAD = 84
BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"
NOME = "Gustavo Baroni"
HANDLE = "@gustavobaroni.ai"
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF☀-➿⬀-⯿⏩-⏿]️?")


def fonte(path, tam):
    return ImageFont.truetype(path, tam)


_avatar = None


def avatar(tam):
    global _avatar
    if _avatar is None:
        a = Image.open(os.path.join(os.path.dirname(__file__), "avatar.jpg")).convert("RGB")
        _avatar = a
    a = _avatar.resize((tam * 2, tam * 2), Image.LANCZOS)
    m = Image.new("L", (tam * 2, tam * 2), 0)
    ImageDraw.Draw(m).ellipse((0, 0, tam * 2 - 1, tam * 2 - 1), fill=255)
    a.putalpha(m)
    return a.resize((tam, tam), Image.LANCZOS)


def emoji_img(ch, tam):
    f = ImageFont.truetype(EMOJI, 109)
    im = Image.new("RGBA", (136, 128), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((0, 0), ch, font=f, embedded_color=True)
    bb = im.getbbox() or (0, 0, 136, 128)
    im = im.crop(bb)
    r = tam / max(im.size)
    return im.resize((max(1, int(im.width * r)), max(1, int(im.height * r))), Image.LANCZOS)


def medir(draw, trecho, f, tam):
    # largura de um trecho com emojis (cada emoji ocupa ~ tam)
    larg = 0
    pos = 0
    for m in EMOJI_RE.finditer(trecho):
        larg += draw.textlength(trecho[pos:m.start()], font=f)
        larg += tam * 1.0
        pos = m.end()
    larg += draw.textlength(trecho[pos:], font=f)
    return larg


def quebrar(draw, texto, f, tam, maxw):
    linhas = []
    for par in texto.split("\n"):
        if not par.strip():
            linhas.append("")
            continue
        atual = ""
        for palavra in par.split(" "):
            teste = (atual + " " + palavra).strip()
            if medir(draw, teste, f, tam) <= maxw:
                atual = teste
            else:
                linhas.append(atual)
                atual = palavra
        linhas.append(atual)
    return linhas


def escrever(img, draw, x, y, linha, f, tam, cor):
    pos = 0
    cx = x
    for m in EMOJI_RE.finditer(linha):
        trecho = linha[pos:m.start()]
        draw.text((cx, y), trecho, font=f, fill=cor)
        cx += draw.textlength(trecho, font=f)
        e = emoji_img(m.group(0), int(tam * 0.95))
        img.paste(e, (int(cx + tam * 0.05), int(y + tam * 0.12)), e)
        cx += tam * 1.0
        pos = m.end()
    draw.text((cx, y), linha[pos:], font=f, fill=cor)


def cabecalho(img, draw, escuro, y0=96):
    cor_nome = (255, 255, 255) if escuro else (15, 20, 25)
    cor_h = (113, 118, 123) if escuro else (83, 100, 113)
    av = avatar(132)
    img.paste(av, (PAD, y0), av)
    fn = fonte(BOLD, 46)
    draw.text((PAD + 132 + 28, y0 + 14), NOME, font=fn, fill=cor_nome)
    nw = draw.textlength(NOME, font=fn)
    # selo azul com check
    cx, cy, r = PAD + 132 + 28 + nw + 30, y0 + 38, 19
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(29, 155, 240))
    draw.line([(cx - 9, cy + 1), (cx - 3, cy + 8), (cx + 10, cy - 8)], fill=(255, 255, 255), width=5, joint="curve")
    draw.text((PAD + 132 + 28, y0 + 72), HANDLE, font=fonte(REG, 38), fill=cor_h)


CTAS = [
    ("Quer um sistema assim no seu negócio?", "Me chama no direct."),
    ("Quer ver isso rodando na sua empresa?", "Me chama no direct e segue para mais."),
    ("Gostou? Segue para mais sistemas e IA", "que funcionam de verdade."),
    ("Se isso faz sentido para o seu negócio,", "me chama no direct."),
]


def slide(texto, escuro, destino, ultimo=False, idx=0):
    bg = (0, 0, 0) if escuro else (255, 255, 255)
    cor = (255, 255, 255) if escuro else (15, 20, 25)
    img = Image.new("RGB", (W, H), bg)
    draw = ImageDraw.Draw(img)
    # tamanho da fonte conforme o tamanho do texto (maior para frases curtas)
    n = len(texto)
    tam = 78 if n < 70 else 70 if n < 120 else 64 if n < 170 else 58
    maxw = W - 2 * PAD
    reserva_cta = 200 if ultimo else 0
    CAB, GAP = 132, 44  # altura do cabeçalho e espaço até o texto (como um post de Twitter)
    while True:
        f = fonte(BOLD, tam)
        linhas = quebrar(draw, texto, f, tam, maxw)
        alt = len(linhas) * int(tam * 1.3)
        if CAB + GAP + alt <= H - 150 - 110 - reserva_cta or tam <= 44:
            break
        tam -= 2
    area_top, area_bot = 70, H - 110 - reserva_cta
    y0 = area_top + max(0, (area_bot - area_top - (CAB + GAP + alt)) // 2)
    cabecalho(img, draw, escuro, y0)
    y = y0 + CAB + GAP
    for ln in linhas:
        escrever(img, draw, PAD, y, ln, f, tam, cor)
        y += int(tam * 1.3)
    if ultimo:
        l1, l2 = CTAS[idx % len(CTAS)]
        cor_div = (47, 51, 54) if escuro else (207, 217, 222)
        draw.rectangle((PAD, H - 280, W - PAD, H - 277), fill=cor_div)
        draw.text((PAD, H - 250), l1, font=fonte(BOLD, 40), fill=(29, 155, 240))
        draw.text((PAD, H - 196), l2, font=fonte(BOLD, 40), fill=cor)
    img.save(destino, "JPEG", quality=93, optimize=True)


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from conteudo_educativo import POSTS as OLD
    from conteudo_novo import POSTS as NEW
    # descarta 3 posts antigos genéricos e intercala: 1 novo (modelado), 1 antigo (bastidor/processo)
    cortar = {i for i, p in enumerate(OLD) if p[1][0].startswith(("Teste grátis", "Últimos 30", "Pare de pagar"))}
    antigos = [p for i, p in enumerate(OLD) if i not in cortar]
    POSTS = []
    for k in range(max(len(NEW), len(antigos))):
        if k < len(NEW):
            POSTS.append(NEW[k])
        if k < len(antigos):
            POSTS.append(antigos[k])
    os.makedirs("imagens", exist_ok=True)
    # Lotes novos entram DEPOIS dos já programados (a ordem da fila nunca muda para trás).
    from conteudo_extra1 import POSTS as E1
    from conteudo_extra2 import POSTS as E2
    from conteudo_extra3 import POSTS as E3
    from conteudo_extra4 import POSTS as E4
    for k in range(max(len(E1), len(E2), len(E3), len(E4))):
        for lote in (E1, E2, E3, E4):
            if k < len(lote):
                POSTS.append(lote[k])
    fila = []
    for i, (bg, slides, legenda) in enumerate(POSTS, start=1):
        nomes = []
        for k, t in enumerate(slides, start=1):
            nome = f"g{i:03d}_s{k}.jpg"
            slide(t, bg == "p", os.path.join("imagens", nome), k == len(slides), i)
            nomes.append(nome)
        cta = CTAS[i % len(CTAS)]
        legenda = legenda.replace(f"\n\n{HANDLE}", f"\n\n{cta[0]} {cta[1]}\n\n{HANDLE}")
        fila.append({"carrossel": i, "tipo": "educativo", "slides": nomes, "legenda": legenda})
        print("ok", i, len(nomes), "slides", flush=True)
    json.dump(fila, open("fila.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("fila.json:", len(fila), "carrosseis")


if __name__ == "__main__":
    main()
