from utils import *
import os

menu = """
---------- Menu ---------
|                       |
| Adicionar Aluno --- 1 |
| Listar Alunos ----- 2 |
| Sair -------------- 0 |
|                       |
-------------------------
"""

while True:
    os.system('cls')
    print(menu)
    opt = int(input("Selecione uma opcao: "))

    match opt:
        case 1:
            print("Adicionar Aluno")
            al = pedir_aluno()
            listaAlunos.append(al)
            input("Pressione uma tecla pra continuar")
        case 2:
            print("Listar Aluno")
            listar_alunos()
            input("Pressione uma tecla pra continuar")
        case 0:
            break
        case _:
            print("Opcao invalida")
            input("Pressione uma tecla pra continuar")

print("Saiu do programa")