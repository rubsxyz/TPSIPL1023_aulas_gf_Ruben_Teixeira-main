from classes import *

listaAlunos:list[Aluno] = []
turma = Turma('TPSIPL ', 1023)

def pedir_aluno() -> Aluno:
    nome = input("Nome do Aluno: ")
    num = None
    while num == None:
        try:
            num = int(input("Numero do Aluno: "))
        except:
            print("O valor tem de ser numerico")

    aluno = Aluno(num, nome, turma)
    return aluno

def add_alunos():
    novo_aluno = "s"
    while novo_aluno == "s":
        
        al = pedir_aluno()
        listaAlunos.append(al)
        novo_aluno = input("s para add novo aluno: ").lower()

def listar_alunos():
    if len(listaAlunos) == 0:
        print("Sem alunos existentes")
    
    else:
        for aluno in listaAlunos:
            print(aluno)