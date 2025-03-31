import os 
import time
os.system("clear")

soma= 0
for i in range(5):
    nota = int(input(f"Digite um número: "))
    #soma= soma + nota
    soma += nota
    print()
    print(f"soma: {soma}")


print("\nFIM DO PROGRAMA")