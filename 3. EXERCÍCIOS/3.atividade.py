import os
os.system("clear")

primeiro_numero=float (input("Digite o primeiro número: "))
segundo_numero= float (input("digite o segundo número: "))


media= (primeiro_numero+segundo_numero)/2
produto= (primeiro_numero*segundo_numero)

if primeiro_numero>segundo_numero:
    menor=segundo_numero
    maior=primeiro_numero
else:
    menor= primeiro_numero
    maior= segundo_numero

print("\nexibindo resultados: ")
print(f"media: {media}")
print(f"produto: {produto}")
print(f"menor: {menor}")
print(f"maior: {maior}")


