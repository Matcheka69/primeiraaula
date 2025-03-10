import os
os.system

nome = input("Digite seu nome:  ")
nota_um = float(input("Digite sua nota: "))
nota_dois = float(input("Digite sua nota: "))



media= (nota_um + nota_dois)/2


if media > 9:
    print("Você está aprovado pelo conceito A")
elif media >7.5:
    print("Você está aprovado pelo conceito B")   
elif media >=6:
    print("Você está aprovado pelo conceito C") 
elif media >=4:
    print("Você está reprovado pelo conceito D")
else: 
    print("Você esta reprovado pelo conceito E")
print(f"media: {media}")