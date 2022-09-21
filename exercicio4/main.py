from exercicio2.src.application.domain import calcula_tempo_download
from exercicio2.src.application.input import pega_tamanho_arquivo, pega_velocidade_internet
from exercicio2.src.application.output import mostra_mensagem


if __name__ == '__main__':
    tamanho_arquivo = pega_tamanho_arquivo()
    velocidade_internet = pega_velocidade_internet() 
    tempo_de_download = calcula_tempo_download(tamanho_arquivo=tamanho_arquivo, velocidade_internet=velocidade_internet)

    mostra_mensagem(mensagem=f'O tempo de download do arquivo com tamanho {tamanho_arquivo}MB em uma velocidade {velocidade_internet}Mbp/s é de aproximadamente {tempo_de_download} minutos.')