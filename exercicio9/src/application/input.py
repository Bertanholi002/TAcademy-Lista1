




def recebe_nome_atleta():
    return input("Qual o nome do atleta? ")

def recebe_saltos(atleta: Atleta):
    for i in range(5):
        salto = int(input(f"Qual o valor do {i+1}o. salto do atleta? "))
        atleta.adiciona_salto(salto)