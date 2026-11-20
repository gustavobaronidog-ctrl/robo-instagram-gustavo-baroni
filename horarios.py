# Horarios de Brasilia (minutos desde 00:00) de cada tipo de post. Usado pelo maestro e pelo vigia.
# Ate 20/11/2026 (inclusive): 6 posts/dia (3 educativos + 3 noticias). A partir de 21/11: 12 posts/dia.
SLOTS_ANTIGOS = {"educativo": [8 * 60, 12 * 60, 15 * 60], "noticia": [10 * 60 + 30, 14 * 60 + 30, 17 * 60]}
SLOTS_NOVOS = {
    "educativo": [8 * 60, 12 * 60, 15 * 60, 18 * 60],              # 4: passo a passo / ensinando
    "noticia": [10 * 60 + 30, 14 * 60 + 30, 17 * 60, 19 * 60 + 30],  # 4: noticias de IA
    "estrategia": [9 * 60 + 15, 13 * 60, 16 * 60],                  # 3: estrategia (modelagem dos perfis)
    "reflexao": [11 * 60 + 30],                                      # 1: estatico de reflexao
}
DATA_NOVA = "2026-11-21"
# Horarios extras so para um dia especifico (ex.: dia de 12 posts). Formato: {"AAAA-MM-DD": {"tipo": [minutos, ...]}}
EXTRAS = {
    "2026-11-20": {"educativo": [17 * 60 + 30, 19 * 60, 20 * 60 + 30], "noticia": [18 * 60 + 30, 20 * 60, 21 * 60 + 30]},
}


def slots_do_dia(nome, hoje):
    base = SLOTS_NOVOS if hoje >= DATA_NOVA else SLOTS_ANTIGOS
    return base.get(nome, []) + EXTRAS.get(hoje, {}).get(nome, [])


