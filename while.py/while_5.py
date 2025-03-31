import os
os. system("clear")

while True:
    print("""
CÓDIGO  | DESCRIÇÃO
    1   | Adicionar pessoa
    2   | Exibir Resultados
    3   | Sair
    


""")
    opçao = int(input())
    match opçao:
        case 1:
            idade = int(input("Digite sua idade: "))
            salario = int(input("Digite seu salário: "))
            sexo = int(input("Qual o seu gênero? \nDigite 'f' ou 'm': ")). upper()
        case 2: 
            print (f"Sua idade é: {idade}")
            print (f"Seu salário: {salario}")
            print (f"Seu sexo é: {sexo}")
        case 3:
            exit ("Programa finalizado")
        case _: 
            print ("Opção inválida!")
    