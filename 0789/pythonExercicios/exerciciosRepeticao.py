"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
while True:
    nota = int(input("Nota entre 0 e 10: "))
    if not 0 < nota > 10:
        break

"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
 mostrando uma mensagem de erro e voltando a pedir as informações.
"""
while True:
    usuario = input("Escolha um nome de usuário: ")
    senha = input("Escolha uma senha: ")

    if usuario == senha:
        print("O nome de usuário não pode ser igual à senha!")
    else:
        break
"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""

while True:
    nome = input("Nome: ")
    
    if len(nome) <= 3:
        print("O nome tem que ter mais do que 3 caractéres!")
    else:
        break

while True:
    idade = int(input("Idade: "))

    if not 0 < idade <= 150:
        print("Insira uma idade entre 0 e 150")
    else:
        break
    
while True:
    salario = float(input("Salário: "))

    if not salario > 0:
        print("Insira um salário maior do que 0!")
    else:
        break

while True:
    sexo = input("Sexo: ")
    
    if sexo == 'f' or sexo == 'm':
        break
    else:
        print("Insira um género existente!")

while True:
    estado_civil = input("Estado Civil: ")

    if estado_civil == 's' or estado_civil == 'c' or estado_civil == 'v' or estado_civil == 'd':
        break
    else:
        print("Insira um estado civil existente!")

"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população 
de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários 
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""
"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população 
de B seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários 
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""

pais_a = 80000
pais_b = 200000

anos = 0

while True:
    if pais_a < pais_b:
        pais_a *= 1.03
        pais_b *= 1.015
        anos += 1
    elif pais_a >= pais_b:
        print(f"O pais A vai demorar {anos} anos até chegar à população do pais B")
        break


"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
"""
while True:
    anos = 0

    pais_a = int(input("População: "))
    taxa_pais_a = float(input("Taxa de crescimento do Pais A (%): ")) / 100
    pais_b = int(input("População: "))      
    taxa_pais_b = float(input("Taxa de crescimento do Pais B (%): ")) / 100

    while pais_a < pais_b:
        pais_a += pais_a * taxa_pais_a
        pais_b += pais_b * taxa_pais_b
        anos += 1

    print(f"Levará {anos} anos para a população do País A ultrapassar ou igualar a população do País B.")

    repetir = input("Deseja repetir o programa? (s/n): ").lower()
    if repetir != 's':
        break

"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. Depois modifique o programa para que ele mostre os números um ao lado do outro.
"""
for i in range(1, 21):
    print(i, end=' ')

"""
Faça um programa que leia 5 números e informe o maior número.
"""
# Inicializar a variável para armazenar o maior número
maior_numero = float('-inf')

# Ler os 5 números e encontrar o maior
for i in range(5):
    numero = float(input(f"Digite o número {i + 1}: "))
    if numero > maior_numero:
        maior_numero = numero

print(f"O maior número digitado é: {maior_numero}")

"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
soma = 0 #cria a varivel para atribuir a soma para depois fazer a media

for i in range(5): #crio um for que vai de 0 a 4
    numero = float(input(f"Digite o número {i + 1}: "))
    soma += numero

media = soma / 5

# Exibir os resultados
print(f"A soma dos números é: {soma}")
print(f"A média dos números é: {media}")
"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""

for i in range(50): # cria um loop for com range de 50
    if i % 2 != 0: # se não restar 0 quando i for divisivel por 2, então o numero é ímpar
        print(i)

for i in range (1, 51, 2): # Este código começará em 1, terminará em 50 e 
    print(i)               # incrementará de 2 em 2, exibindo apenas os números ímpares dentro do intervalo especificado.
"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
"""

num1 = int(input("Número 1:"))
num2 = int(input("Número 2:"))

for i in range(num1 + 1, num2):
    print(i)
"""
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
Altere o programa anterior para mostrar no final a soma dos números.
"""
num1 = int(input("Número 1:"))
num2 = int(input("Número 2:"))

soma = 0

for intervalo in range(num1 + 1, num2):
    print(intervalo)
    soma += intervalo

print(soma)
"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
"""
numTabuada = int(input("Insira o número no qual pretende saber a tabuada: "))

if numTabuada > 0:
    for i in range(11):
        soma = i * numTabuada
        print(f"{numTabuada} X {i} = {soma}")
else:
    print("Insira um número maior que 0")
"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
"""
base = int(input("Qual a base: "))
expoente = int(input("Qual o expoente: "))

resultado = 1

for _ in range(expoente):
    resultado *= base  # Multiplica a base pelo resultado 'expoente' vezes

print("O resultado é:", resultado)
"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.
"""
pares = 0
impares = 0

for i in range(10):
    num = int(input("Insira um número inteiro: "))
   
    if num % 2 == 0:
        pares += 1
    elif num % 2 != 0:
        impares += 1

print(f"Ao todo tem {pares} números pares")
print(f"Ao todo tem {impares} números ímpares")
"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
"""

num1 = 1
num2 = 1
soma = 0

n = int(input("Quantas séries quer: "))

print(num1, num2, end=" ")

for i in range(2, n):
    soma = num1 + num2

    print(soma, end=" ")

    num2 = num1
    num1 = soma
"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
"""

num1 = 1
num2 = 1
soma = 0

n = int(input("Quantas séries quer: "))

print(num1, num2, end=" ")

for i in range(2, n):
    soma = num1 + num2

    if soma <= 500:
        print(soma, end=" ")

        num2 = num1
        num1 = soma
    else:
        break
"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
soma = 1

factorial = int(input("Factorial: "))

for i in range(factorial):
    print(f"{soma} x {[factorial]}")
    soma *= factorial
    factorial -= 1

print(soma)
"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""
soma = 0 #cria a variavel para ser usada no ciclo for
menor_valor = float('inf')
maior_valor = float('-inf')

n = int(input("Quantos números quer: ")) #cria o input para saber o conjunto de numeros

for i in range(n): #ciclo for com o input do user dado em 'n'
    valores = int(input(f"Insira o {i + 1} valor: ")) #cria o input para saber os numeros dos valores

    soma += valores #faz a soma de todos os numeros dados pelo user na linha 9
    
    # Verifica se o valor atual é menor que o menor valor encontrado até agora
    if valores < menor_valor:
        menor_valor = valores
    
    # Verifica se o valor atual é maior que o maior valor encontrado até agora
    if valores > maior_valor:
        maior_valor = valores

print(f"A soma é: {soma}\nMaior valor: {maior_valor}\nMenor valor: {menor_valor}") #printa tudo
"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""
soma = 0 #cria a variavel para ser usada no ciclo for
menor_valor = float('inf')
maior_valor = float('-inf')

n = int(input("Quantos números quer: ")) #cria o input para saber o conjunto de numeros

for i in range(n): #ciclo for com o input do user dado em 'n'
    valores = int(input(f"Insira o {i + 1} valor: ")) #cria o input para saber os numeros dos valores

    while valores < 0  or valores > 1000: #enquanto os valores nao forem entre 0 e 1000, dá erro e volta a perguntar
        print("Insira apenas valores entre 0 e 1000!")
        valores = int(input(f"Insira o {i + 1} valor: "))

    soma += valores #faz a soma de todos os numeros dados pelo user na linha 9
    
    # Verifica se o valor atual é menor que o menor valor encontrado até agora
    if valores < menor_valor:
        menor_valor = valores
    
    # Verifica se o valor atual é maior que o maior valor encontrado até agora
    if valores > maior_valor:
        maior_valor = valores

print(f"A soma é: {soma}\nMaior valor: {maior_valor}\nMenor valor: {menor_valor}") #printa tudo
"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes 
e limitando o fatorial a números inteiros positivos e menores que 16.
"""
while True:
    soma = 1

    factorial = int(input("Factorial: "))

    while factorial > 16 or factorial < 0:
        print("Insira um número menor que 16, ou que seja inteiro positivo!")
        factorial = int(input("Factorial: "))

    for i in range(1, factorial + 1):
        soma *= i

    print(f"O fatorial de {factorial} é {soma}")

    repetir = input("Repetir? ")
    
    if repetir.lower() != 's':
        print("Obrigado por ter usado esta aplicação!")
        break
"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.
"""
numInteiro = int(input("Número Inteiro: "))

for i in range(2, int(numInteiro ** 0.5) + 1):
    if numInteiro % i == 0:
        print(f"{numInteiro} não é um número primo")
        break
else:
    print(f"{numInteiro} é um número primo")
"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1.

Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível.
"""

numInteiro = int(input("Número Inteiro: "))

if numInteiro < 2:
    print(f"{numInteiro} não é um número primo")
    exit()

divisor = False

for i in range(2, int(numInteiro ** 0.5) + 1):
    if numInteiro % i == 0:
        print(f"{numInteiro} não é um número primo. É divisivel por {i}")
        divisor = True
        break
else:
    print(f"{numInteiro} é um número primo")
"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. 
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. 
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""
divisoes = 0

n = int(input("Até qual número primo quer saber: 1-"))

for i in range(2, n + 1):
    primo = True
    for j in range(2, int(i ** 0.5) + 1):
        divisoes += 1
        if i % j == 0:
            primo = False
            break
    if primo:
        print(f"Primo: {i}")

print(f"Número total de divisões: {divisoes}")
"""
Faça um programa que calcule e mostre a média aritmética de N notas.
"""
soma_notas = 0
qtd = 0
notas_qtd = int(input("Quer calcular quantas notas: "))

for i in range(notas_qtd):
    notas = int(input(f"Nota {i + 1}: "))
    soma_notas += notas
    qtd += 1

soma_total = soma_notas / qtd
print(f"A soma das notas é: {soma_notas}\nQue dá de média: {int(soma_total)} " )
"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da 
turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.
"""
soma_idades = 0

pessoas = int(input("Quantas pessoas: "))

for i in range(pessoas):
    idade = int(input(f"Pessoa {i + 1}, qual a sua idade: "))
    soma_idades += idade

media = soma_idades / pessoas
print(f"A média das idades da turma é: {int(media)}")

if 0 < media <= 25:
    print("A turma é Jovem")
elif 26 < media < 60:
    print("A turma é Adulta")
else:
    print("A turma é Idosa")
"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.
"""
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0

eleitores = int(input("Qual o número total de eleitores: "))

for i in range(eleitores):
    voto = int(input(f"Eleitor {i + 1}, vota em que candidato? 1, 2 ou 3: "))

    while voto < 1 or voto > 3:
        print("Por favor, vote 1, 2 ou 3")
        voto = int(input(f"Eleitor {i + 1}, vota em que candidato? 1, 2 ou 3: "))

    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1

print(f"Candidato 1: {candidato_1}")
print(f"Candidato 2: {candidato_2}")
print(f"Candidato 3: {candidato_3}")
"""
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.
"""
alunos_total = 0
turmas = int(input("Quantas Turmas: "))

for i in range(turmas):
    alunos_turma = int(input(f"Alunos da Turma {i + 1}: "))
    
    while alunos_turma > 40:
        print("A turma não pode ter mais doque 40 alunos!") 
        alunos_turma = int(input(f"Alunos da Turma {i + 1}: "))
    
    alunos_total += alunos_turma

media = alunos_total / turmas
print(f"A média de alunos é de: {int(media)}")
"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
qtd_cd = int(input("Quantidade de CD's: "))

valor_total_cd = 0

for i in range(qtd_cd):
    cd_valor = int(input(f"Quanto gastou no CD {i + 1}: "))
    valor_total_cd += cd_valor

media_cd = valor_total_cd / qtd_cd

print(f"O valor médio gasto em cada CD é de: {int(media_cd)}")
"""
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela que contém o 
número de itens que o cliente comprou e ao lado o valor da conta. 

Desta forma a atendente da caixa precisa apenas contar quantos itens o cliente está a levar e olhar na tabela de preços.

Você foi contratado para desenvolver o programa que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, 
conforme o exemplo abaixo:

Lojas Quase Dois - Tabela de preços
1 - R$ 1.99
2 - R$ 3.98
...
50 - R$ 99.50
"""
soma = 0

items = int(input("Quantos items quer pagar: "))

while items >= 51 or items <= 0:
    print("Só pode escolher entre 1 e 50 items!!")
    items = int(input("Quantos items quer pagar: "))

for i in range(13):
    print("*", end="")
    if i == 12:
        print("CAIXA", end="")
        caixa = True
        if caixa:
            for i in range(14):
                print("*", end="")

for i in range(1, 51):
    soma += 1.99

    if i == items:
        print(f"\nTerá que pagar {soma:.2f}€ por {i} items")
"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia da tabelinha, 
que já é um sucesso na sua loja de 1,99. 

Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, 
de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:

Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
"""
soma = 0

paes = int(input("Quantos pães quer comprar: "))

while paes >= 51 or paes <= 0:
    print("Só pode escolher entre 1 e 50 pães!")
    paes = int(input("Quantos pães quer comprar: "))

for i in range(13):
    print("*", end="")
    if i == 12:
        print("CAIXA", end="")
        caixa = True
        if caixa:
            for i in range(14):
                print("*", end="")

for i in range(1, 51):
    soma += 0.18

    if i == paes:
        if i == 1:
            print(f"\nTerá que pagar {soma:.2f}€ por {i} pão")
        else:
            print(f"\nTerá que pagar {soma:.2f}€ por {i} pães")
"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências. 
Faça um programa que implemente uma caixa registradora rudimentar. 

O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias. 
Um valor zero deve ser informado pelo operador para indicar o final da compra. 

O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, 
para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, 
para registrar a próxima compra. 

A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara 
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
"""

preco_produto = []
recomecar_caixa = True

while recomecar_caixa:
    soma_produtos = 0
    num_produto = 0

    while True:
        num_produto += 1
        preco = float(input(f"Preço do Produto {num_produto} (Valor 0 se não houver mais produtos): "))
        
        preco_produto.append(preco)
        
        if preco == 0:
            break
        
        soma_produtos += preco

    valor_dinheiro = float(input("Qual o valor em dinheiro: "))

    while valor_dinheiro <= 0 or valor_dinheiro < soma_produtos:
        print("Valor tem que ser maior que 0, ou maior que a soma dos produtos escolhidos!")
        valor_dinheiro = float(input("Qual o valor em dinheiro: "))

    troco = valor_dinheiro - soma_produtos

    print(f"Lojas Tabajara")

    for i in range(num_produto):
        print(f"Produto {i + 1}: {preco_produto[i]}")

    print(f"Total: {soma_produtos:.2f} ")
    print(f"Dinheiro: {valor_dinheiro:.2f} ")
    print(f"Troco: {troco:.2f} ")

    recomecar = int(input("Quer recomeçar o programa? Sim(1) | Não(2): "))

    if recomecar == 1:
        recomecar_caixa == True
    elif recomecar == 2:
        print("Volte sempre!")
        break
    else:
        while True:
            print("Escolha apenas 1 ou 2!")
            recomecar = int(input("Quer recomeçar o programa? Sim(1) | Não(2): "))

            if recomecar == 1:
                recomecar_caixa == True
                break
            elif recomecar == 2:
                print("Volte sempre!")
                exit()
"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 

Ex.: 5!=5.4.3.2.1=120. 

A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120
"""
factorial = int(input("Escolha o factorial: "))
print(f"Factorial de: {factorial}")
print(f"{factorial}! =", end=" ")

soma = 1

for i in range(1, factorial + 1):
    soma *= i
    print(factorial + 1 - i, end="")
    if i != factorial:
        print(" . ", end="")

print(f" = {soma}")
"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas,
e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas.
"""
maior_temp = float('-inf')
menor_temp = float('inf')
temp_soma = 0
media = 0

temp = int(input("Quantas temperaturas quer medir: "))

for i in range(temp):
    temperaturas = float(input(f"Temperatura {i + 1}: "))
    
    temp_soma += temperaturas

    if temperaturas < menor_temp:
        menor_temp = temperaturas

    if temperaturas > maior_temp:
        maior_temp = temperaturas

media = temp_soma / i

print(f"Menor Temperatura: {menor_temp}\nMaior Temperatura: {maior_temp}\nMédia: {media}")
"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia. 
Um número primo é aquele que é divisível apenas por um e por ele mesmo.
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
"""

primo = int(input("Insira um número: "))

for i in range(2, int(primo ** 0.5) + 1):
    if primo % i == 0:
        print(f"{primo} não é um número primo. É divisivel por {i}")
"""
Encontrar números primos é uma tarefa difícil. 

Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário.
"""
try:

    n = int(input("Até que número quer saber os números primos: "))

    print(f"Números primos até {n}: ", end = "")

    for i in range(2, n + 1):
        primo = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(f"{i}", end=", ")

except ValueError:
    print("Insira um número válido")
"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, 
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, 
conforme exemplo abaixo:

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
"""
soma = 0

num_inteiro = int(input("Number: "))

val_inicial = int(input("Comecar por: "))
val_final = int(input("Terminar em: "))

while val_final < val_inicial:
    print("Valor final nao pode ser menor que o valor inicial!!")
    val_final = int(input("Terminar em: "))

for i in range(val_inicial, val_final + 1):
    soma = i * num_inteiro
    print(f"{num_inteiro} x {i} = {soma}")
"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, 
para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 

O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 

Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, 
além da média das alturas e dos pesos dos clientes
"""
cliente = 0
cliente_alto = float('-inf')
cliente_baixo = float('inf')
cliente_gordo = float('-inf')
cliente_magro = float('inf')
soma_altura = 0
soma_peso = 0
quantidade_clientes = 0

while True:
    cliente += 1

    codigo_cliente = int(input(f"Codigo Cliente {cliente}: "))

    if codigo_cliente == 0:
        if altura_cliente < cliente_baixo:
            cliente_baixo = altura_cliente
            cod_cliente_baixo = codigo_cliente

        if altura_cliente > cliente_alto:
            cliente_alto = altura_cliente
            cod_cliente_alto = codigo_cliente

        if peso_cliente < cliente_magro:
            cliente_magro = peso_cliente
            cod_cliente_magro = codigo_cliente
        if peso_cliente > cliente_gordo:
            cliente_gordo = peso_cliente
            cod_cliente_gordo = codigo_cliente
        
        print(f"Baixo: {cliente_baixo} Alto: {cliente_alto}")
        print(f"Magro: {cliente_magro} Gordo: {cliente_gordo}")

        media_altura = soma_altura / quantidade_clientes if quantidade_clientes > 0 else 0
        media_peso = soma_peso / quantidade_clientes if quantidade_clientes > 0 else 0

        print(f"Média Altura: {media_altura:.2f} Média Peso: {media_peso:.2f}")
        break

    altura_cliente = float(input(f"Altura Cliente {cliente}: "))
    peso_cliente = float(input(f"Peso(Kg) Cliente {cliente}: "))

    soma_altura += altura_cliente
    soma_peso += peso_cliente
    quantidade_clientes += 1
    
"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 

Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""
try:
    salario_inicial = float(input("Digite o salário inicial do funcionário: "))
    while salario_inicial <= 0:
        print("Digite um salario valido maior que 0!")
        salario_inicial = float(input("Digite o salário inicial do funcionário: "))     

except ValueError:
    print("Digite um numero!")
    salario_inicial = float(input("Digite o salário inicial do funcionário: "))

percentual_aumento = 1.5 / 100
novo_percentual = 0

print(f"No ano 1995 o salario e de: {salario_inicial:.2f}$")

for i in range(1995, 2023 + 1):
    while i == 1996:
        aumento = salario_inicial * percentual_aumento
        salario_total = salario_inicial + aumento

        print(f"No ano {i} o salario e de: {float(salario_total):.2f}$")
        break

    while i >= 1997 and i <= 2023:
        novo_percentual += percentual_aumento + percentual_aumento
        aumento = salario_inicial * novo_percentual
        salario_total = salario_inicial + aumento

        print(f"No ano {i} o salario e de: {float(salario_total):.2f}$")
        break
"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;

A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. 

Faça um programa que determine o salário atual desse funcionário. 
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.
"""
try:
    salario_inicial = float(input("Digite o salário inicial do funcionário: "))
    while salario_inicial <= 0:
        print("Digite um salario valido maior que 0!")
        salario_inicial = float(input("Digite o salário inicial do funcionário: "))     

except ValueError:
    print("Digite um numero!")
    salario_inicial = float(input("Digite o salário inicial do funcionário: "))

percentual_aumento = 1.5 / 100
novo_percentual = 0

print(f"No ano 1995 o salario e de: {salario_inicial:.2f}$")

for i in range(1995, 2023 + 1):
    while i == 1996:
        aumento = salario_inicial * percentual_aumento
        salario_total = salario_inicial + aumento

        print(f"No ano {i} o salario e de: {float(salario_total):.2f}$")
        break

    while i >= 1997 and i <= 2023:
        novo_percentual += percentual_aumento + percentual_aumento
        aumento = salario_inicial * novo_percentual
        salario_total = salario_inicial + aumento

        print(f"No ano {i} o salario e de: {float(salario_total):.2f}$")
        break
"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando 
a sua altura em centímetros. 

Encontre o aluno mais alto e o mais baixo. 

Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""
aluno_alto = float("-inf")
aluno_baixo = float("inf")

for i in range(10):
    student_num = int(input(f"Stundent's {i + 1} number: "))
  
    while student_num <= 0:
        print("Student number should be higher than 0!")
        student_num = int(input(f"Stundent's {i + 1} number: "))

    height_value = float(input(f"Student's {i + 1} height(cm): "))

    while height_value <= 0:
        print("Student height should be higher than 0!")
        height_value = float(input(f"Student's {i + 1} height(cm): "))

    if height_value < aluno_baixo:
        aluno_baixo = height_value
        aluno_baixo_number = student_num

    if height_value > aluno_alto:
        aluno_alto = height_value
        aluno_alto_number = student_num

print(f"Aluno Baixo: {aluno_baixo}, Numero {aluno_baixo_number}")
print(f"Aluno Alto: {aluno_alto}, Numero {aluno_alto_number}")
"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
Código da cidade;
Número de veículos de passeio (em 1999);
Número de acidentes de trânsito com vítimas (em 1999). 

Deseja-se saber:
Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
Qual a média de veículos nas cinco cidades juntas;
Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
menor_acidentes = float('inf')
maior_acidentes = float('-inf')
soma_veiculos = 0
soma_acidentes = 0
soma_cidades_menos_2000 = 0

for i in range(1, 6):
    codigo_cidade = int(input(f"Código da cidade {i}: "))
    num_veiculos = int(input(f"Cidade {i} - Número de veículos de passeio: "))
    num_acidentes_vitimas = int(input(f"Cidade {i} - Acidentes de trânsito com vítimas: "))

    if num_acidentes_vitimas < menor_acidentes:
        menor_acidentes = num_acidentes_vitimas
        codigo_menor_acidentes = codigo_cidade

    if num_acidentes_vitimas > maior_acidentes:
        maior_acidentes = num_acidentes_vitimas
        codigo_maior_acidentes = codigo_cidade

    soma_veiculos += num_veiculos

    if num_veiculos < 2000:
        soma_acidentes += num_acidentes_vitimas
        soma_cidades_menos_2000 += 1

media_veiculos = soma_veiculos / 5
media_acidentes = soma_acidentes / soma_cidades_menos_2000

print(f"\nO menor indice de acidentes corresponde a cidade {codigo_menor_acidentes} com: {menor_acidentes} acidentes")
print(f"\nO maior indice de acidentes corresponde a cidade {codigo_maior_acidentes} com: {maior_acidentes} acidentes")
print(f"\nA media dos veiculos da: {media_veiculos} veiculos")
print(f"\nA media de acidentes nas cidades com menos de 2000 veiculos da: {int(media_acidentes)} acidentes")
"""
Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão nos seguintes intervalos: 
[0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
"""
numeros_0_25 = 0
numeros_26_50 = 0
numeros_51_75 = 0
numeros_76_100 = 0

while True:
    numero = int(input("Numeros Positivos (ou negativo para terminar): "))

    while numero > 100:
        print("Digite apenas numeros abaixo de 100!")
        numero = int(input("Numeros Positivos (ou negativo para terminar): "))

    if numero < 0: break

    if 0 <= numero <= 25: numeros_0_25 += 1
    elif 26 <= numero <= 50: numeros_26_50 += 1
    elif 51 <= numero <= 75: numeros_51_75 += 1
    elif 76 <= numero <= 100: numeros_76_100 += 1


print(f"Numeros [0-25]: {numeros_0_25}")
print(f"Numeros [26-50]: {numeros_26_50}")
print(f"Numeros [51-75]: {numeros_51_75}")
print(f"Numeros [76-100]: {numeros_76_100}")
"""
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 

Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido. 

Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""
valor_total = 0

while True:
    codigo_refeicao = int(input("Código do Item (ou -1 para encerrar): "))

    if codigo_refeicao == -1:
        break

    quantidade = int(input(f"Quantidade do item {codigo_refeicao}: "))

    if codigo_refeicao == 100:
        preco_item = 1.20
    elif codigo_refeicao == 101:
        preco_item = 1.30
    elif codigo_refeicao == 102:
        preco_item = 1.50
    elif codigo_refeicao == 103:
        preco_item = 1.20
    elif codigo_refeicao == 104:
        preco_item = 1.30
    elif codigo_refeicao == 105:
        preco_item = 1.00
    else:
        print("Código inválido.")
        continue

    total = preco_item * quantidade
    valor_total += total
    print(f"Valor a ser pago pelo item {codigo_refeicao}: R$ {total:.2f}")

print(f"Total a pagar: R$ {valor_total:.2f}")
"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
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
Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
Exemplo:
  12376489
  => 98467321
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
Imprima no final a soma da série.
"""