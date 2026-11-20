# Robô do Instagram pessoal: @gustavobaroni.ai

Perfil pessoal. NÃO é de nenhuma empresa: não compartilha conta, app da Meta, chaves, repositório nem conteúdo com Tem Encaixe ou SeparaGo.

- `fila.json` / `estado.json`: carrosséis educativos (3 por dia: 08h, 12h, 15h)
- `fila_noticias.json` / `estado_noticias.json`: carrosséis de notícias de IA (3 por dia: 10h30, 14h30, 17h)
- `maestro.py` + `.github/workflows/maestro.yml`: plantão que confere a cada 5 min o que já devia ter saído e publica
- `gerar.py` + `conteudo_educativo.py`: geram as imagens 1080x1350 e a fila (só o Claude usa, para criar conteúdo)
- Segredos (Settings > Secrets and variables > Actions): `IG_TOKEN`, `IG_APP_SECRET`; variáveis: `IG_APP_ID`, `IG_REDIRECT`
- Para pausar: Actions > Maestro dos posts > Disable workflow
