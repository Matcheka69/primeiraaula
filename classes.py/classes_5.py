import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome:str
    data_de_nascimento: int
    rg: int
    cpf: int

    def exibindo_dados(self):
        print("\nExibindo_dados: ")
        print(f"nome: {self.nome}, data_de_nascimento: {self.data_de_nascimento}, rg: {self.rg}, cpf: {self.cpf}")
        