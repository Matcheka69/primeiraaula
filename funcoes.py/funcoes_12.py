import os
os.system("clear")

peso= float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura: " ))

def calcular_imc(peso, altura): 
    imc = peso / altura ** 2
    return imc

if calcular_imc (peso, altura) < 18.5:
    print('abaixo do peso')
elif calcular_imc (peso, altura) < 24.9:
    print('peso normal')