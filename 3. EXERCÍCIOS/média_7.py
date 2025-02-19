import os
os.system("clear")


primeira_nota=float (input("Digite sua nota: "))
segunda_nota= float (input("digite sua nota: "))
terceira_nota= float(input("digite sua nota: "))






soma=primeira_nota+segunda_nota+terceira_nota
media=soma/3



if media < 7:
    print("REPROVADO")
elif media:
    print("APROVADO")

