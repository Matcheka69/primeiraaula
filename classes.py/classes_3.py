import os
os . system("clear")

from dataclasses import dataclass

@dataclass
class Endereco:
     logadouro:str
     numero: str



@dataclass
class Pessoa:
     nome: str
     idade: int
     endereço: Endereco

     def exibir_dados(self):
        print(f"Nome:{self.nome},\
                idade:{self.idade},\
                Logadouro:{self.endereco.logadouro},\
                numero:{self.endereco.numero}")

endereco1 = Endereco("Rua A", "33")
pessoa1 = Pessoa("Marta", 22, endereco1)


print("Dados da pessoa: ")
pessoa1.exibir_dados()

