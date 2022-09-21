
from typing import List


class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.notas : List[float] = []

    def receber_nota(self, nota):
        self.notas.append(nota)  

    def maior_nota(self)->float:
        nova_lista = self.notas.copy()
        max_value  = max(nova_lista)
        nova_lista.remove(max_value)

        return max(nova_lista)
    
    def menor_nota(self):
        nova_lista = self.notas.copy()
        min_value  = min(nova_lista)
        nova_lista.remove(min_value)

    def media_final(self, notas):
        resultado = sum(notas) / len(notas)
        return resultado
