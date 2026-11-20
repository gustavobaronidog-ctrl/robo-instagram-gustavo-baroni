#!/usr/bin/env python3
# Gera os posts novos: estratégicos (fila_estrategia), reserva (fila_reserva) e reflexão estática (fila_reflexao).
# Não toca nos estados (estado_*.json só é criado se não existir). Uso: python3 gerar2.py
import json, os, random, sys
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gerar as G
from conteudo_estrategia import ESTRATEGIA, RESERVA
from conteudo_reflexao import REFLEXAO
from conteudo_meta import POSTS as META

W, H = G.W, G.H


def fundo_esfumacado(seed):
    rnd = random.Random(seed)
    base = Image.new("RGB", (W, H), (8, 8, 10))
    fumaca = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(fumaca)
    for _ in range(16):
        cx, cy, r = rnd.randint(-100, W + 100), rnd.randint(150, H + 100), rnd.randint(180, 420)
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=rnd.randint(35, 95))
    fumaca = fumaca.filter(ImageFilter.GaussianBlur(120))
    cinza = Image.new("RGB", (W, H), (120, 122, 130))
    base = Image.composite(cinza, base, fumaca)
    vig = Image.new("L", (W, H), 0)
    ImageDraw.Draw(vig).ellipse((-250, -150, W + 250, H + 150), fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(200))
    return Image.composite(base, Image.new("RGB", (W, H), (0, 0, 0)), vig)


def slide_reflexao(texto, destino, seed):
    img = fundo_esfumacado(seed)
    draw = ImageDraw.Draw(img)
    G.cabecalho(img, draw, True)
    maxw = W - 2 * G.PAD
    tam = 92
    while True:
        f = G.fonte(G.BOLD, tam)
        linhas = G.quebrar(draw, texto, f, tam, maxw)
        alt = len(linhas) * int(tam * 1.3)
        if alt <= H - 640 or tam <= 48:
            break
        tam -= 2
    y = 330 + max(0, (H - 330 - 200 - alt) // 2)
    for ln in linhas:
        draw.text((G.PAD, y), ln, font=f, fill=(255, 255, 255))
        y += int(tam * 1.3)
    draw.rectangle((G.PAD, y + 24, G.PAD + 150, y + 31), fill=(214, 32, 39))
    img.save(destino, "JPEG", quality=93, optimize=True)


def estado(arq):
    if not os.path.exists(arq):
        json.dump({"proximo": 0, "por_dia": {}}, open(arq, "w"), indent=1)


def carrosseis(posts, prefixo, tipo, fila_arq, chave, inicio_cta, gravar=True):
    fila = []
    for i, (bg, slides, legenda) in enumerate(posts, start=1):
        nomes = []
        for k, t in enumerate(slides, start=1):
            nome = f"{prefixo}{i:03d}_s{k}.jpg"
            G.slide(t, bg == "p", os.path.join("imagens", nome), k == len(slides), inicio_cta + i)
            nomes.append(nome)
        cta = G.CTAS[(inicio_cta + i) % len(G.CTAS)]
        legenda = legenda.replace(f"\n\n{G.HANDLE}", f"\n\n{cta[0]} {cta[1]}\n\n{G.HANDLE}")
        fila.append({chave: i, "tipo": tipo, "slides": nomes, "legenda": legenda})
    if gravar:
        json.dump(fila, open(fila_arq, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(fila_arq, len(fila))
    return fila


def main():
    os.makedirs("imagens", exist_ok=True)
    antigos = carrosseis(ESTRATEGIA, "e", "estrategia", "fila_estrategia.json", "carrossel", 0, gravar=False)
    novos = carrosseis(META, "m", "estrategia", "fila_estrategia.json", "carrossel", 7, gravar=False)
    # intercala: 1 do método Meta (diagnóstico), 1 do lote anterior, e assim por diante; o resto segue em ordem
    fila = []
    for k in range(max(len(antigos), len(novos))):
        if k < len(novos):
            fila.append(dict(novos[k], carrossel=f"m{k+1}"))
        if k < len(antigos):
            fila.append(antigos[k])
    json.dump(fila, open("fila_estrategia.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("fila_estrategia.json", len(fila))
    carrosseis(RESERVA, "r", "reserva", "fila_reserva.json", "carrossel", 40)
    fila = []
    for i, (texto, legenda) in enumerate(REFLEXAO, start=1):
        nome = f"f{i:03d}_s1.jpg"
        slide_reflexao(texto, os.path.join("imagens", nome), i)
        fila.append({"reflexao": i, "tipo": "reflexao", "slides": [nome], "legenda": legenda})
    json.dump(fila, open("fila_reflexao.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("fila_reflexao.json", len(fila))
    for e in ("estado_estrategia.json", "estado_reflexao.json", "estado_reserva.json"):
        estado(e)


if __name__ == "__main__":
    main()
