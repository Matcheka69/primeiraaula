import os
os.system("clear")

primeiro_numero=float(input("digite o primeiro_numero: "))
segundo_numero=float(input("digite o segundo numero: "))


if primeiro_numero < segundo_numero:
    menor= primeiro_numero
    maior= segundo_numero
else:
    menor= segundo_numero
    maior= primeiro_numero

print(f"menor: {menor} ")
print(f"maior: {maior} ")
print(f"o primeiro numero que voce digitou foi:{menor}")
print(f"o segundo numero que voce digitou foi: {maior}")

