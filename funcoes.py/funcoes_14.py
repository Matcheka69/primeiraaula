import os 
os.system

opcao= int(input("""
Código /t prato /tValor
01/t Picanha/t 25,00R$
02/t Lasanha/t20,00R$
03/t Strogonoff /t18,00R$
04/t Bife acebolado/t15,00R$
"Digite a opção desejada: """))

soma= 0
valor = 0
match opcao: 
    case 1: 
        print("Prato:Picanha= 25,00")
    case 2:
        print("prato: Lasanha= 20,00")
    case 3:
        print ("prato: Strogonoff = 18,00")
    case 4:
        print("Prato: Bife_acebolado= 15,00")
soma += valor
    
continuar = input("Deseja pedir outro prato? Digite 1 para Sim e 2 para não ")
lista_pratos.appened(opcao)
precos_pratos(valor)   
if continuar == "1":
    break

total a pagar
