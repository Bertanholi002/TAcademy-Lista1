import math

tamanho_arquivo = float(input('Qual é o tamanho do arquivo em MB? '))
velocidade_internet = float(input('Qual é a velocidade da internet, em Mbp/s? '))
tempo_de_download = math.ceil((tamanho_arquivo / (velocidade_internet / 10)) / 60)

print(f'O tempo de download do arquivo com tamanho {tamanho_arquivo}MB em uma velocidade {velocidade_internet}Mbp/s é de aproximadamente {tempo_de_download} minutos.')