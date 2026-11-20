#!/usr/bin/env python3
# Maestro (plantão): fica ligado ~50 min e confere a cada 5 min o que JÁ DEVIA ter ido ao ar hoje e ainda não foi.
# Publica no máximo 1 de cada tipo por conferência. Cada post é gravado no GitHub na hora.
import json, subprocess, sys, time
import publicar as P

# Horários de Brasília (minutos desde 00:00). Todos antes das 18h.
# Reels de carrossel e vídeos dinâmicos entram aqui quando forem produzidos (fila própria cada um).
TIPOS = {
    "educativo": {"slots": [8 * 60, 12 * 60, 15 * 60], "fila": "fila.json", "estado": "estado.json"},
    "noticia": {"slots": [10 * 60 + 30, 14 * 60 + 30, 17 * 60], "fila": "fila_noticias.json", "estado": "estado_noticias.json"},
}
INICIO, LIMITE, DURACAO, INTERVALO = 7 * 60, 22 * 60, 50 * 60, 5 * 60


def sh(cmd):
    return subprocess.run(cmd, shell=True).returncode


def gravar():
    sh("git add estado*.json; git add token.enc 2>/dev/null || true")
    if sh("git diff --staged --quiet") != 0:
        sh('git commit -q -m "maestro: avança as filas"')
        for _ in range(3):
            if sh("git pull --rebase -q && git push -q") == 0:
                break
            time.sleep(3)


def conferir(minutos):
    hoje = P.agora_brt().strftime("%Y-%m-%d")
    atrasado = 0
    for nome, t in TIPOS.items():
        try:
            ja = json.load(open(t["estado"])).get("por_dia", {}).get(hoje, 0)
        except FileNotFoundError:
            continue
        devidos = [s for s in t["slots"] if s <= minutos]
        if len(devidos) - ja <= 0:
            continue
        print(f"{hoje} {minutos//60:02d}:{minutos%60:02d} DEVIDO e não publicado: {nome} (faltam {len(devidos)-ja}). Publicando 1.", flush=True)
        try:
            P.publicar(t["fila"], t["estado"])
        except Exception as e:
            print(f"ERRO ao publicar {nome}: {e}", flush=True)
            if minutos - devidos[-1] > 90:
                atrasado = 1
        gravar()
        time.sleep(20)
    return atrasado


def main():
    inicio, erro = time.time(), 0
    while True:
        agora = P.agora_brt()
        minutos = agora.hour * 60 + agora.minute
        if minutos < INICIO or minutos > LIMITE:
            print("Fora do horário (7h-22h): nada a fazer.", flush=True)
            break
        sh("git pull --rebase -q")
        try:
            import importlib; importlib.reload(P)  # pega correções novas sem esperar a próxima rodada
        except Exception as e:
            print(f"reload falhou: {e}", flush=True)
        try:
            erro = conferir(minutos)
        except Exception as e:
            print(f"ERRO na conferência: {e}", flush=True)
        if time.time() - inicio + INTERVALO > DURACAO:
            break
        time.sleep(INTERVALO)
    return erro


if __name__ == "__main__":
    sys.exit(main())
