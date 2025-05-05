import os
os.system("clear")
from dataclasses import dataclass

@dataclass
class Autor:
    nome:str
    bibliografia:str

@dataclass
class Livro:
    titulo: str
    ano:int
    autor: Autor

    def exibir_resultados(self):
        print(f'Título: {self.titulo} /nAno: {self.ano} \nAutor: {self.autor.nome}')

print("= Solicitando dados para o usúario =")
livro = Livro(
    titulo =input("Digite o título do livro: "),
    ano = int(input("Digite o ano de publicação: ")),
    autor= Autor(
    nome= input("Digite o nome do autor: "
    bibliografia = input ("Digite as informações de bibliografia do autor: ")))
    )