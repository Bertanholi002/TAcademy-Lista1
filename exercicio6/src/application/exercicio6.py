#mostrar o total de votos para candidato, voto em branco e nulo.
#porcentagem de voto nulo sobre o total de votos
# votos em branco sobre total de votos

jose = []
joao = []
maria = []
carlos = []
nulo = []
branco = []

def votacao():
    voto = int(input(f"Para votar, jose (1)joao(2)maria(3)carlos(4)nulo(5)branco(6)"))
    while voto == True:
        if voto == 1:
            jose.append(voto)
        elif voto == 2:
            joao.append(voto)
        elif voto == 3:
            maria.append(voto)
        elif voto == 4:
            carlos.append(voto)
        elif voto == 5:
            nulo.append(voto)
        else:
            branco.append(voto)

total_de_votos = len(jose) + len(joao) + len(maria) + len(carlos) + len(nulo) + len(branco)
porcentagem_nulo_sobre_voto = total_de_votos * len(nulo) 
porcentagem_branco_sobre_voto = total_de_votos * len(branco)

def mostrar_resultado_geral():
    print(jose, joao, maria, carlos, nulo, branco, porcentagem_branco_sobre_voto, porcentagem_nulo_sobre_voto)





