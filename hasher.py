import hashlib

from config import TAMANHO_BLOCO


def calcular_hash(caminho):
    
    sha256 = hashlib.sha256()

    with open(caminho, "rb") as arquivo:
        while True:
            bloco = arquivo.read(TAMANHO_BLOCO)
            if not bloco:
                break
            sha256.update(bloco)

    return sha256.hexdigest()