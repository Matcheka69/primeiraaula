import os
os.system

altura = float(input("Olá usúario, para saber seu peso ideal digite sua altura: "))

sexo = input("Digite seu sexo( M para masculino e F para feminino)")

match sexo:
        case "M":
            peso_ideal = (72.7 * altura) - 58
            print(f"Seu peso ideal é:{peso_ideal:.2f} kg")


        case "F":

            peso_ideal = (62.1 * altura) - 58
            print(f"Seu peso ideal é: {peso_ideal:.2f}kg")

        case _:
            print("Opção inválida.")



        
