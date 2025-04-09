import os
os.system("clear")


def inflacionar (preço):
    if preço < 100:
        resultado = preço * 1.10
    else:
        resultado = preço * 1.20
    return resultado

def descontar (preço):
    if preço < 100:
        resultado = preço * 0.10
    else:
        resultado = preço * 0.20
        return resultado
    
preço_produto= float(input("Digite o preço do produto: "))

preço_inflacionado= inflacionar(preço_produto)
preço_descontado = descontar(preço_produto)

print(f"Preço  com aumento: {preço_inflacionado}")
print(f"Valor do desconto: {preço_descontado}")
