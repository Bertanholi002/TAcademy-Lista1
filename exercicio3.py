gabarito = {1:"a",2:"b",3:"c",4:"d",5:"e",6:"e",7:"d",8:"c",9:"b",10:"a"}
pontos = 0

questao1 = input("Qual a resposta da primeira pergunta : ")
if questao1 == gabarito[1]:
    pontos += 1
    print("Correto")
else:
    pontos += 0
    print("Incorreto")

questao2 = input("Qual a resposta da segunda pergunta : ")
if questao2 == gabarito[2]:
   pontos += 1
   print("Correto")

else:
    pontos += 0
    print("Incorreto")

questao3 = input("Qual a resposta da terceira pergunta: ")
if questao3 == gabarito[3]:
    pontos += 1
    print("Correto")
else:
    pontos += 0
    print("Incorreto")

questao4 = input("Qual a resposta da quarta pergunta : ")
if questao4 == gabarito[4]:
    pontos += 1
    print("Correto")
else:
    pontos += 0
    print("Incorreto")

questao5 = input("Qual a resposta da quinta pergunta : ")
if questao5 == gabarito[5]:
    pontos += 1
    print("Correto")
else:
    pontos += 0
    print("Incorreto")

questao6 = input("Qual a resposta da sexta pergunta: ")
if questao6 == gabarito[6]:
    pontos += 1
    print("Correto")
else:
    pontos += 0
    print("Incorreto")

questao7 = input("Qual a resposta da setima pergunta : ")
if questao7 == gabarito[7]:
    pontos += 1
    print("Correto")
else:
    pontos += 0
    print("Incorreto")

questao8 = input("Qual a resposta pra oitava pergunta : ")
if questao8 == gabarito[8]:
    pontos += 1
    print("Correto")
else:
    pontos += 0
    print("Incorreto")

questao9 = input("Qual a resposta pra nona pergunta : ")
if questao9 == gabarito[9]:
    pontos += 1
    print("Correto")
else:
    pontos += 0
    print("Incorreto")

questao10 = input("Qual a resposta para decima questão : ")
if questao10 == gabarito[10]:
    pontos += 1
    print("Correto")
else:
    pontos += 0
    print("Incorreto")

print(f"Você possui {pontos} questões acertadas !")


