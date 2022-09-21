from typing import List

class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.notas:List[float] = []
        self.media:int = 0
 
    def maior_nota(self) -> int:
        nova_lista = self.notas.copy()
        max_value  = max(nova_lista)
        return max_value  # type: ignore

    def menor_nota(self) -> int:
        nova_lista = self.notas.copy()
        min_value  = min(nova_lista)
        return min_value  # type: ignore

    def media_final(self):
        resultado = sum(self.notas) // len(self.notas)
        self.media = resultado  # type: ignore
        return self.media

    def mostrar_resultado(self):
        return f"O nome do atleta é {self.nome} e a suas notas são  {self.notas} e a média é de {self.media}  "        

    def pedir_nota(self):
        for el in range(7):
            el = float(input("Qual é a nota para esse atleta? "))
            self.notas.append(el)
            print(self.notas)
            
    def pedir_nome(self):
        nome = input("Qual o nome do atleta? ")
        return nome
        


variavel = Atleta()  # type: ignore
print(variavel.pedir_nome())
print(variavel.pedir_nota())
print(variavel.maior_nota())
print(variavel.menor_nota())
print(variavel.media_final())
print(variavel.mostrar_resultado())


    

 