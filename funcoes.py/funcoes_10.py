import os 
os.system("clear")
from datetime import date

ano_nascimento= float(input("Digite seu ano de nascimento: "))
def calcular(idade):
    resultado = date.today().year - idade
    return resultado
idade = calcular(ano_nascimento)
print(f"idade:{idade}")