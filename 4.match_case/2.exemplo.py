import os
os.system ("clear")

opcao= int(input("""
Código \t Prato\t Valor
1 \t Picanha \t R$25,00
2 \t Lasanha \t R$20,00
3 \t Strogonoff \t R$18,00
4 \t Bife acebolado\t R$15,00
5 \t Pão com ovo\t R$5,00                         
                 
Digite a opção desejada:  
"""))

match opcao: 
    case 1: 
        print("Prato:Picanha= 25,00")
    case 2:
        print("prato: Lasanha= 20,00")
    case 3:
        print ("prato: Strogonoff = 18,00")
    case 4:
        print("Prato: Bife_acebolado= 15,00")
    case 5:
        print("prato: Pão_com_ovo= 5,00")
    case _:
        print("opção inválida.")