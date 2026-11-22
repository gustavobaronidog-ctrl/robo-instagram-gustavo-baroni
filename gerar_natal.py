#!/usr/bin/env python3
"""Natal/fim de ano do perfil pessoal (@gustavobaroni.ai): 5 carrosseis educativos no estilo do perfil.
Perfil separado das empresas: nada de Tem Encaixe, SeparaGo, agenda, horario ou salao.
Insere na fila.json por POSICAO (depois de 'proximo'). Uso: python3 gerar_natal.py"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gerar as G
EU = "@gustavobaroni.ai"
CTA = "Quer ver isso rodando na sua empresa? Me chama no direct e segue para mais."
POSTS = [
(301, 90, "b", [
 "Dezembro: sua empresa vende mais e erra mais. Por quê? 🎄",
 "Pico de pedido, equipe cansada e tudo no WhatsApp. É receita para erro. 📱",
 "O buraco: o pedido é anotado em um lugar e conferido em outro. 🕳️",
 "Faça a conta, com números de exemplo: 10 pedidos errados por semana x R$ 80 = R$ 800 que somem. 🧮",
 "Não é preguiça da equipe. É processo manual em semana de pico. 🧠",
 "Um sistema que guarda o pedido uma única vez e confere na saída corta o erro pela raiz. ✅",
 "Você já sabe onde está o buraco de dezembro da sua empresa? 👇"],
 "O erro de dezembro quase nunca é falta de esforço. É processo manual em semana de pico."),
(302, 106, "p", [
 "3 erros que fazem o cliente comprar do concorrente no Natal:",
 "1. Responder o pedido horas depois. ⏰",
 "2. Prometer um prazo que a equipe não consegue cumprir. 📅",
 "3. Não saber o que ainda tem em estoque. 📦",
 "Os três nascem do mesmo lugar: tudo depende de alguém lembrar. 🧠",
 "Salva para conferir na sua empresa 📌"],
 "Três erros de fim de ano que custam cliente, e o que eles têm em comum."),
(303, 118, "b", [
 "COMANDOS PARA O NATAL DA SUA EMPRESA\nCLAUDE | PICO DE VENDAS",
 "1. \"Liste os 5 pedidos que mais dão retrabalho na minha operação.\"",
 "2. \"Para cada um, monte uma checklist de conferência em 3 passos.\"",
 "3. \"Escreva a mensagem que confirma o prazo ao cliente de forma clara.\"",
 "4. \"Monte o plano dos 7 dias de pico: quem faz o quê em cada dia.\"",
 "Salva para a semana das festas 📌"],
 "Quatro comandos para organizar a semana mais cheia do ano antes dela começar."),
(304, 130, "p", [
 "O presente mais caro do Natal: o funcionário que chega esgotado em janeiro. 🎁",
 "Quem passa dezembro apagando incêndio não tem energia para melhorar nada. 🔥",
 "Boa parte do incêndio é tarefa repetida que ninguém tirou da mão da equipe. 🔁",
 "Antes do dia 31, liste 3 tarefas repetidas da sua semana. 📝",
 "Cada uma é candidata a ser trocada por um sistema simples. ⚙️",
 "Comece por uma. O ano que vem agradece. 🎄"],
 "Tarefa repetida cansa a equipe e atrasa a empresa. Dezembro é o melhor momento para listar o que automatizar."),
(305, 138, "b", [
 "Feliz Natal 🎄",
 "Hoje a empresa pode descansar. O sistema que você construiu, não.",
 "O melhor Natal de dono de empresa é o que passa sem o celular na mesa. 📵",
 "Isso não vem de sorte. Vem de processo que funciona sem você. ⚙️",
 "Que o ano que vem tenha mais sistema e menos urgência. 🙏"],
 "Um Natal tranquilo é consequência de uma empresa que funciona sem depender de uma pessoa só."),
]
FP = "fila.json"; fila = json.load(open(FP, encoding="utf-8")); prox = json.load(open("estado.json"))["proximo"]
assert min(p[1] for p in POSTS) > prox
ids = {x["carrossel"] for x in fila}
os.makedirs("imagens", exist_ok=True)
for cid, pos, bg, sl, leg in sorted(POSTS, key=lambda p: p[1]):
    assert cid not in ids
    nomes = []
    for k, t in enumerate(sl, 1):
        nome = f"g{cid}_s{k}.jpg"; assert not os.path.exists("imagens/" + nome)
        G.slide(t, bg == "p", os.path.join("imagens", nome), k == len(sl), cid); nomes.append(nome)
    fila.insert(pos, {"carrossel": cid, "tipo": "educativo", "slides": nomes, "legenda": f"{leg}\n\nSalva.\n\n{CTA}\n\n{EU}"})
json.dump(fila, open(FP, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(fila))
