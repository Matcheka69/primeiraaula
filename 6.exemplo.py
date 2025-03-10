import os

os.system

valor=float(input("Digite o valor do produto: "))

print("nOlá usúario, escolha a forma de pagamento: ")
print("nl- Pagamneti à vista")
print("2- Pagamento à prazo")

pagamento= int(input("nDigite a opção desejada (1 ou 2): "))

match pagamento:


    case 1:
        desconto = valor *0.1

        total= valor - desconto


        print("nResumo da compra")
        print(f"Valor do produto: R$ {valor:.2f}")
        print("Forma de pagamento à vista")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Total a pagar: R$ {total:.2f}")

    case 2:
        parcelas = (int(input("\nDigite a quantidade de parcelas (No máximo 6): ")))

        if  1 <= parcelas <= 6:
            
            parcelamento= valor / parcelas

            print("\n Resumo da compra: ")
            print(f"Valor do produto: R$ {valor:.2f}")
            print("Forma de pagamento á prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: {parcelamento:.2f}")
            print(f"Total a pagar: {valor:.2f}")

        else:
            print("Número de parcelas inválido. escolha entre 1 a 6.")
    case _:
        print("Opção inválida. Escolha entre 1 e 2.")


                  

