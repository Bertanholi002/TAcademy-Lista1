from multiprocessing.sharedctypes import Value
from optparse import Values
from re import S


def pegar_resposta():
    gabarito = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"e",7:"d",8:"c",9:"b",10:"a"}
   
    while True:   
        lista_geral = {}
        pontos = 0
        nome = input("Qual o seu nome? ")
        start = int(input("Deseja fazer a prova? (1)Sim (2)Não ")) 
        if (start == 2):
            break

        for chave in gabarito.keys():
            resposta = input(f"Qual a resposta da questão {chave} ")
            if resposta in gabarito[chave]:
                pontos += 1
                print(f"Você acertou a {chave} ") 
                lista_geral[nome] = pontos 
            else:
                print(f"Você errou a questão {chave}")
        
    print(lista_geral)

pegar_resposta()


       


