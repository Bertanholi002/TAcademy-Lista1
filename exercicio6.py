
from typing import List

class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.saltos: List[float] = []

    def adiciona_salto(self, salto: float):
        self.saltos.append(salto)

    def maior_salto(self):
        maior_salto = max(self.saltos)
        return maior_salto
    def menor_salto(self):
        menor_salto =  min(self.saltos)
        return menor_salto


    
def resultado_salto_final(saltos, maior_salto, menor_salto):
   saltos.remove(maior_salto)
   saltos.remove(menor_salto)

def media_de_saltos(saltos):
    resultado = sum(saltos) / len(saltos)
    







# pegar o nome
#criar um atleta
# pegar saltos e jogar no atleta
#maior_salto = atleta.maior_salto()


