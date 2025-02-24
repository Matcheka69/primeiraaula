import os
os.system("clear")

login_cadastrado= "marta"
senha_cadastrada= "123"

import os
os.system("clear")

login=input("digite o login: ")
senha=input("digite o senha: ")

if login == login_cadastrado and senha_cadastrada == senha_cadastrada:
    print("Bem-vindo")
else:
    print("Login ou senha inválidos!")