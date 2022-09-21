import math
def calcula_tempo_download(tamanho_arquivo: float, velocidade_internet: float)->float:
    return math.ceil((tamanho_arquivo / (velocidade_internet / 10)) / 60)
