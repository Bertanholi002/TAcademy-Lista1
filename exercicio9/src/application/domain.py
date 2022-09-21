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
     