import math

def receber_tamanho():
    return float(input("Qual a area a ser pintada? "))

def calculo_tinta_area(tamanho):
    return (tamanho / 6 )

def galao_necessario(quantidade):
    return (quantidade / 3.6)

def preco_final(galao):
    return  (math.ceil(galao) * 80)
    
def lata_necessaria(quantidade):
    return (quantidade / 18)

def preco_final_lata(galao):
    return  (math.ceil(galao) * 80)


def mostrar_ao_cliente(galao_necessario, preco_final):
    print(f"A quantidade de tinta necessaria sera de {math.ceil(galao_necessario)}, e o preço total é de {preco_final:.2f}")

tamanho = receber_tamanho()
qtdade_tinta = calculo_tinta_area(tamanho)
qtdade_galao = galao_necessario(qtdade_tinta)
preco = preco_final(qtdade_galao)
mostrar_ao_cliente(qtdade_galao, preco)