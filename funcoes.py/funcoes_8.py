import os
os.system("clear")

def converter_centimetros(n1):
    return metros * 100;
print("= CONVERTER METROS PARA CENTÍMETROS =")
metros = float(input("Digite um número: "))
centimetros = converter_centimetros (metros)

print("\n= RESULTADOS =")
print(f"{metros} metros é igual a {centimetros}centímetros")