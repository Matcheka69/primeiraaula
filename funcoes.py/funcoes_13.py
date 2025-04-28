import os
os.system ("clear")


QUANTIDADE_NUMEROS = 6
lista_numeros = []

def pares_impares(lista):
    pares = 0
    ímpares = 0
    for numero in lista:
        if numero % 2 == 0:
            pares+=1
        return pares, ímpares
    print(" = LISTA DE NUMEROS=")
    for in range(QUANTIDADE_NUMEROS):
        numero = int(input(f"Digite o {i+1}=numero))