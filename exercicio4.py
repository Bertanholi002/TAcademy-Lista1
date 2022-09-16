lista = []
def ligacao():
    jose = 0
    joao = 0
    marcia = 0
    douglas = 0
    branco = 0
    nulo = 0

    for el in range(5):
        el = int(input("Digite seu codigo de votacao "))    
        if el == 1: 
            jose += 1 
        elif el == 2:
            joao += 1
        elif el == 3:
            marcia += 1
        elif el == 4:
            douglas += 1
        elif el == 5:
            branco += 1
        elif el == 6:
            nulo += 1
        
        soma = jose +  marcia + douglas + joao + branco + nulo
        porcentagem = nulo /soma *100
        porcentagem2 = branco/soma*100
        
        print(f"O numero de votações sobre o Candidato Jose é de {jose}")
        print(f"O numero de votações sobre o Candidato Joao é de {joao}")
        print(f"O numero de votações sobre o Candidato Douglas é de {douglas}")
        print(f"O numero de votações sobre o Candidato Marcia é de {marcia}")
        print(f"O numero de votações sobre o Voto Nulo é de {nulo}")
        print(f"O numero de votações sobre o branco é de {branco}")    
        print(f'Média de votos nulos foi de  {porcentagem}%. ')   
        print(f'Média de votos nulos foi de  {porcentagem2}%. ')  
ligacao()    

    

             
                
    
      

        
