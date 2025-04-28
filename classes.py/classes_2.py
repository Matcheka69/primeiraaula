import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class  pessoa():
    nome: str
    email: str
    telefone: int
    endereço: int

    def exibindo_dados(self):
        print("\nExibindo dados: ")
        print(f"nome: {self.nome}, email: {self.email}, telefone: {self.telefone}, endereço: {self.endereço}")

    print("Solicitando dados: ")
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    telefone = float(input("Digite seu telefone: "))
    endereço = float(input("Digit seu endereço: "))


print("Exibindo dados: ")
print(f"nome: {pessoa.nome}, email: {pessoa.email}, telefone: {pessoa.telefone}, endereço: {pessoa.endereço}")