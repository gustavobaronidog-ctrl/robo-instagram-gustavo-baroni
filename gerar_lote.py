#!/usr/bin/env python3
"""Anexa o lote 5 ao FIM das filas do perfil pessoal (por posicao, depois de tudo que ja existe).
Nao mexe em estado*.json. Uso: python3 gerar_lote.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gerar as G, gerar2 as G2
import conteudo_lote5 as C
os.makedirs("imagens", exist_ok=True)
def ler(p): return json.load(open(p, encoding="utf-8"))
def gravar(p, d): json.dump(d, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
def carr(posts, pre, tipo, fila_arq, base):
    fila = ler(fila_arq); ids = {str(x.get("carrossel", x.get("reflexao"))) for x in fila}
    for i, (bg, sl, leg) in enumerate(posts, 1):
        cid = f"{pre}{i}"; assert cid not in ids
        nomes = []
        for k, t in enumerate(sl, 1):
            n = f"{pre}{i:03d}_s{k}.jpg"; assert not os.path.exists("imagens/" + n), n
            G.slide(t, bg == "p", "imagens/" + n, k == len(sl), base + i); nomes.append(n)
        cta = G.CTAS[(base + i) % len(G.CTAS)]
        if "me chama no direct" not in leg.lower(): leg = leg.replace(f"\n\n{G.HANDLE}", f"\n\n{cta[0]} {cta[1]}\n\n{G.HANDLE}")
        fila.append({"carrossel": cid, "tipo": tipo, "slides": nomes, "legenda": leg})
    gravar(fila_arq, fila); print(fila_arq, len(fila))
carr(C.EDU, "h", "educativo", "fila.json", 200)
carr(C.EST, "s", "estrategia", "fila_estrategia.json", 300)
fila = ler("fila_reflexao.json")
for i, (t, leg) in enumerate(C.REF, 1):
    n = f"fh{i:03d}_s1.jpg"; assert not os.path.exists("imagens/" + n)
    G2.slide_reflexao(t, "imagens/" + n, 100 + i)
    fila.append({"reflexao": f"h{i}", "tipo": "reflexao", "slides": [n], "legenda": leg})
gravar("fila_reflexao.json", fila); print("fila_reflexao.json", len(fila))
