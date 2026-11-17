from pathlib import Path

from hasher import calcular_hash


def varrer_diretorio(diretorio):
    
    base = Path(diretorio)

    if not base.exists():
        raise FileNotFoundError(f"Diretório não encontrado: {base}")
    if not base.is_dir():
        raise NotADirectoryError(f"O caminho não é um diretório: {base}")

    hashes = {}
    erros = []

    for caminho in sorted(base.rglob("*")):
        if not caminho.is_file():
            continue

        relativo = caminho.relative_to(base).as_posix()

        try:
            hashes[relativo] = calcular_hash(caminho)
        except OSError as erro:
            erros.append((relativo, str(erro)))

    return hashes, erros