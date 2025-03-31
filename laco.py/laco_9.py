import os 
os.system("clear")

pares = 0
ímpares = 0

print(" NÚMEROS PARES E ÍMPARES: ")
for i in range(5):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        pares += 1
    else: ímpares += 1

print()
print(f"Pares: {pares}")
print(f"Ímpares: {ímpares}")

print("\nFIM DO PROGRAMA")