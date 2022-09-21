from typing import List

class Atleta:
    def __init__(self, nome):
        self.nome = nome
        self.saltos:List[float] = []
        self.media:int = 0
 
    while pedir_nome(self) == True:  # type: ignore
        
        def maior_salto(self) -> int:
            nova_lista = self.saltos.copy()
            max_value  = max(nova_lista)
            return max_value  # type: ignore

        def menor_salto(self) -> int:
            nova_lista = self.saltos.copy()
            min_value  = min(nova_lista)
            return min_value  # type: ignore

        def media_final(self)->float:
            resultado = sum(self.saltos) // len(self.saltos)
            self.media = resultado  # type: ignore
            return self.media

        def mostrar_resultado(self):
            return f"O nome do atleta é {self.nome} e os seus saltos são  {self.saltos} e a média é de {self.media} "        

        def pedir_salto(self):
            for el in range(7):
                el = float(input("Qual é a nota para esse atleta? "))
                self.saltos.append(el)
                print(self.saltos)
            
        def pedir_nome(self):
            nome = input("Qual o nome do atleta? ")
            return nome
           
    else:   
        variavel = Atleta()  # type: ignore
        print(variavel.pedir_salto())
        print(variavel.maior_salto())
        print(variavel.menor_salto())
        print(variavel.media_final())   
        print(variavel.mostrar_resultado())    


