#criar atleta
#receber 7 notas 
#retirar o maior e o menor e fazer a media dos restantes

from typing import List

class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.notas : List[float] = []

    def receber_nota(self, nota):
        self.notas.append(nota)  

    def maior_nota(self, notas):
       maior_nota = max.remove(notas)
       return maior_nota
    
    def menor_nota(self,notas):
       menor_nota = min.remove(notas)
       return menor_nota 

def pedir_nota(nota):
    for el in range(7):
        nota = float(input("Qual é a nota para esse atleta? "))
        return nota

def media_final(resultado, notas):
   resultado = sum(notas) / len(notas)
   return resultado

def mostrar_resultado():
     

