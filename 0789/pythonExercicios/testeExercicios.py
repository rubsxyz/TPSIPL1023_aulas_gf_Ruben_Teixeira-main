"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com 
o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). 

Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. 
Após todos os alunos terem respondido informar:

Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A
"""
aluno = 0
repetir_programa = True
maior_acerto = float('-inf')
aluno_maior = 0
menor_acerto = float('inf')
aluno_menor = 0
soma_notas = 0
total_alunos = 0

while repetir_programa:
    aluno += 1
    pontos = 0

    print(f"Aluno {aluno} vai responder!")

    for i in range(1, 11):
        resposta = input(f"Aluno {aluno} | Resposta Questão {i}: ")

        if i == 1 and resposta.lower() == 'a':
            pontos += 1
        elif i == 2 and resposta.lower() == 'b':
            pontos += 1
        elif i == 3 and resposta.lower() == 'c':
            pontos += 1
        elif i == 4 and resposta.lower() == 'd':
            pontos += 1
        elif i == 5 and resposta.lower() == 'e':
            pontos += 1
        elif i == 6 and resposta.lower() == 'e':
            pontos += 1
        elif i == 7 and resposta.lower() == 'd':
            pontos += 1
        elif i == 8 and resposta.lower() == 'c':
            pontos += 1
        elif i == 9 and resposta.lower() == 'b':
            pontos += 1
        elif i == 10 and resposta.lower() == 'a':
            pontos += 1

    soma_notas += pontos
    total_alunos += 1

    if pontos > maior_acerto:
        maior_acerto = pontos
        aluno_maior = aluno
        
    if pontos < menor_acerto:
        menor_acerto = pontos
        aluno_menor = aluno

    repetir = input("Outro aluno vai utilizar o programa? (S)im (N)ao: ")

    if repetir.lower() == 'n': 
        print(f"O aluno {aluno} obteve {pontos} pontos")
        print(f"Maior acerto: {maior_acerto} pelo aluno {aluno_maior}")
        print(f"Menor acerto: {menor_acerto} pelo aluno {aluno_menor}")
        print(f"Total de alunos que utilizaram o sistema: {total_alunos}")
        print(f"Média das notas da turma: {soma_notas / total_alunos}")
        break
    elif repetir.lower() == 's': 
        repetir_programa