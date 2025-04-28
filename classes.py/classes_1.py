import os 
os.system("clear")

from dataclasses import dataclass

@dataclass
class Pessoa():
   
    nome: str
    idade:int
    peso: float
    altura:float

Pessoa1 = Pessoa ("Joao", 19, 84, 1.85)

print("Exibindo dados: ")
print(f"nome: {Pessoa1.nome}, idade: {Pessoa1.idade}, peso: {Pessoa1.peso}, altura: {Pessoa1.altura} ")