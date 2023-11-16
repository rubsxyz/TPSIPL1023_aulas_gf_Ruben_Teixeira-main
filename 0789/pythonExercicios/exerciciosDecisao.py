"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
num1 = int(input("Insira o primeiro número: "))
num2 = int(input("Insira o segundo número: "))

if (num1 > num2):
    print(f"O número maior é {num1}")
else:
    print(f"O número maior é {num2}")



"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
num = int(input("Insira um valor: "))

if (num >= 1):
    print("O número é positivo")
elif (num == 0):
    print("O número é nulo")
else:
    print("O número é negativo")

"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
sexo = input("O seu sexo é Feminino [F], ou Masculino [M]: ")

match (sexo):
    case 'F' | "f":
        print("O seu sexo é Feminino")
    case 'M' | 'm':
        print("O seu sexo é Masculino")
    case _:
        print("Sexo Inválido")

"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante
"""
vogal_consoante = input("Escreva uma letra do alfabeto: ")

match (vogal_consoante):
    case 'A' | "a" | 'E' | 'e' | 'I' | "i" | 'O' | 'o' | 'U' | 'u':
        print("Vogal")
    case _:
        print("Consoante")

letra = input("Escreva uma letra do alfabeto: ")

if letra in 'AEIOUaeiou':
    print("Vogal")
else:
    print("Consoante")

"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""

nota1 = int(input("Insira o valor da primeira nota: "))
nota2 = int(input("Insira o valor da segunda nota: "))

soma_media = nota1 + nota2
media = soma_media / 2

if (media == 10):
    print(f"Aprovado com Distinção com nota de {media}")
elif (media >= 7):
    print(f"Aprovado com nota de {media}") 
else:
    print(f"Reprovado com nota de {media}")

"""
Faça um Programa que leia três números e mostre o maior deles.
"""

num1 = int(input("Primeiro Número: "))
num2 = int(input("Segundo Número: "))
num3 = int(input("Terceiro Número: "))

if (num1 > num2 and num1 > num3):
    print(f"O número maior é {num1}")
elif (num2 > num1 and num2 > num3):
    print(f"O número maior é {num2}")
else: 
    print(f"O número maior é {num3}")
"""
Faça um Programa que leia três números e mostre o maior e o menor deles.
"""
num1 = int(input("Primeiro Número: "))
num2 = int(input("Segundo Número: "))
num3 = int(input("Terceiro Número: "))

maior = num1
menor = num1

if num2 > maior:
    maior = num2

if num2 < menor:
    menor = num2

if num3 > maior:
    maior = num3

if num3 < menor:
    menor = num3

print(f"O número maior é {maior}")
print(f"O número menor é {menor}")
"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""
preco_produto1 = float(input("Digite o preço do primeiro produto: "))
preco_produto2 = float(input("Digite o preço do segundo produto: "))
preco_produto3 = float(input("Digite o preço do terceiro produto: "))

preco_mais_baixo = preco_produto1
produto_mais_barato = "Produto 1"

if preco_produto2 < preco_mais_baixo:
    preco_mais_baixo = preco_produto2
    produto_mais_barato = "Produto 2"

if preco_produto3 < preco_mais_baixo:
    preco_mais_baixo = preco_produto3
    produto_mais_barato = "Produto 3"
print(f"O produto mais barato é {produto_mais_barato} com o preço de {preco_mais_baixo:.2f}€")
"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""

num1 = int(input("Primeiro Número: "))
num2 = int(input("Segundo Número: "))
num3 = int(input("Terceiro Número: "))

if num1 >= num2 and num1 >= num3:
    maior = num1
    if num2 >= num3:
        meio = num2
        menor = num3
    else:
        meio = num3
        menor = num2
elif num2 >= num1 and num2 >= num3:
    maior = num2
    if num1 >= num3:
        meio = num1
        menor = num3
    else:
        meio = num3
        menor = num1
else:
    maior = num3
    if num1 >= num2:
        meio = num1
        menor = num2
    else:
        meio = num2
        menor = num1

print(f"Números em ordem decrescente: {maior}, {meio}, {menor}")
"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""
print("Em que turno você estuda? ")
turno = input("Digite (M-matutino ou V-Vespertino ou N- Noturno): ")

match turno:
    case 'M' | 'm':
        print("Bom dia!")
    case 'V' | 'v':
        print("Boa Tarde!")
    case 'N' | 'n':
        print("Boa Noite!")
    case _: 
        print("Valor Inválido")
"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""
salario = float(input("Qual o seu salário: "))

if salario <= 280:
    aumento = 20
elif salario <= 700:
    aumento = 15
elif salario <= 1500:
    aumento = 10
else:
    aumento = 5

valor_aumento = (salario * aumento) / 100
novo_salario = salario + valor_aumento

print(f"O seu salário antes do reajuste é de: {salario}R$")
print(f"O percentual de aumento aplicado é de {aumento}%")
print(f"O valor do aumento é de {valor_aumento}R$")
print(f"O novo salário, após o aumento, é de {novo_salario}R$")
"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, 
mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. 

O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% 

Imprima na tela as informações, dispostas conforme o exemplo abaixo. 

No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""

valor_hora = float(input("Quanto ganha por hora: "))
horas = int(input("Quantas horas você trabalha: "))

salario_bruto = horas * valor_hora

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 5
elif salario_bruto <= 2500:
    ir = 10
else:
    ir = 20

ir_total = (salario_bruto * ir) / 100
inss = (salario_bruto * 10) / 100
fgts = (salario_bruto * 11) / 100

sindicato = (salario_bruto * 3) / 100

total_descontos = ir_total + inss
salario_liquido = salario_bruto - total_descontos

print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"IR ({ir}%): R$ {ir_total:.2f}")
print(f"INSS (10%): R$ {inss:.2f}")
print(f"FGTS (11%): R$ {fgts:.2f}")
print(f"Sindicato (3%): R$ {sindicato:.2f}")
print(f"Total de descontos: R$ {total_descontos:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

dia = int(input("Digite um número (1 a 7) para obter o dia da semana: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda-feira")
elif dia == 3:
    print("Terça-feira")
elif dia == 4:
    print("Quarta-feira")
elif dia == 5:
    print("Quinta-feira")
elif dia == 6:
    print("Sexta-feira")
elif dia == 7:
    print("Sábado")
else:
    print("Valor inválido. Digite um número de 1 a 7 para obter o dia da semana.")
"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0            A
  Entre 7.5 e 9.0             B
  Entre 6.0 e 7.5             C
  Entre 4.0 e 6.0             D
  Entre 4.0 e zero            E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""

nota_1 = int(input("Nota do 1 teste: "))
nota_2 = int(input("Nota do 2 teste: "))


if (nota_1 and nota_2 <= 10):

    media_notas = float((nota_1 + nota_2) / 2)

    if (media_notas < 4.0 ):
        conceito = "E"
    elif (media_notas > 4.0 and media_notas < 6.0):
        conceito = "D"
    elif (media_notas > 6.0 and media_notas < 7.5):
        conceito = "C"
    elif (media_notas > 7.5 and media_notas < 9.0):
        conceito = "B"
    elif (media_notas > 9.0 and media_notas < 10.0):
        conceito = "A"

    if conceito in ("A", "B", "C"):
        conceito_final = "APROVADO"
    else:
        conceito_final = "REPROVADO"

    print(f"Obteve a nota de {media_notas}, o conceito correspodente é '{conceito}' quer dizer que está {conceito_final}") 
else:
    print("Por favor insira uma nota existente 0-10")
"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
lado_1 = float(input("1º lado do triângulo: "))
lado_2 = float(input("2º lado do triângulo: "))
lado_3 = float(input("3º lado do triângulo: "))

if ((lado_1 + lado_2) > lado_3 and (lado_1 + lado_3) > lado_2 and (lado_2 + lado_3) > lado_1):
    print("É um triângulo")
    if (lado_1 == lado_2 == lado_3):
        print("Triângulo Equilátero")
    elif (lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3):
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Não é um triângulo")

"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;
"""
a = float(input("Valor de A: "))

if (a == 0):
    print("Equação não é de segundo grau!")
else:
    b = float(input("Valor de B: "))
    c = float(input("Valor de C: "))

    discriminante = b**2 - 4*a*c

    if discriminante < 0:
            print("A equação não possui raízes reais.")
    elif discriminante == 0:
            x = -b / (2*a)
            print(f"A equação possui uma raiz real: x = {x}")
    else:
            raiz_discriminante = discriminante ** 0.5
            x1 = (-b + raiz_discriminante) / (2*a)
            x2 = (-b - raiz_discriminante) / (2*a)
            print(f"A equação possui duas raízes reais: x1 = {x1} e x2 = {x2}")

"""
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
"""
ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, "é um ano bissexto")
else:
    print(ano, "não é um ano bissexto")
    
"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
"""
dia = int(input("Insira o dia: "))

if (dia < 1 or dia > 31):
    print("Data inválida!")
else:
    mes = int(input("Insira o mês: "))

    if (mes < 1 or mes > 12):
        print("Data inválida!")
    else:
        ano = int(input("Insira o ano: "))

        if (ano < 1):
            print("Data inválida!")

        print(f"{dia:02d}/{mes:02d}/{ano:04d}")

"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades 
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16
"""
num = int(input("Introduza um número inteiro menor que 1000: "))

num_centenas = num // 100
num_dezenas = (num % 100) // 10
num_unidades = num % 10

if num > 1000:
    print("O número é maior do que 1000")
else:
    print(f"O número tem {num_centenas} centenas, {num_dezenas} dezenas e {num_unidades} unidades")

"""
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.
"""

nota_1 = int(input("Insira a sua primeira nota: "))
nota_2 = int(input("Insira a sua segunda nota: "))
nota_3 = int(input("Insira a sua terceira nota: "))

media_notas = int((nota_1 + nota_2 + nota_3) / 3)

print(media_notas)

if media_notas == 10:
    print("Aprovado com Distinção")
elif media_notas <= 6:
    print("Reprovado")
else:
    print("Aprovado")
    
"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
"""
valor_saque = int(input("Valor do saque: "))
#cria o input valor saque

notas_100 = 0
notas_50 = 0
notas_10 = 0
notas_5 = 0
notas_1 = 0
#cria as variaveis das notas disponiveis para saque, e dá o valor de 0 a cada uma delas.

while valor_saque > 0: #enquanto o valor_saque for maior que 0 os if's vão sendo executados
    if valor_saque >= 100: #se o valor_saque for maior que 100, então adiciona 1 nota de 100
        notas_100 += 1
        valor_saque -= 100 #retira 100 de valor_saque
    elif valor_saque >= 50:
        notas_50 += 1
        valor_saque -= 50
    elif valor_saque >= 10:
        notas_10 += 1
        valor_saque -= 10
    elif valor_saque >= 5:
        notas_5 += 1
        valor_saque -= 5
    else:
        notas_1 += 1
        valor_saque -= 1

if notas_100 > 0:
    print(f"Notas de 100 reais: {notas_100}")

if notas_50 > 0:
    print(f"Notas de 50 reais: {notas_50}")

if notas_10 > 0:
    print(f"Notas de 10 reais: {notas_10}")

if notas_5 > 0:
    print(f"Notas de 5 reais: {notas_5}")

if notas_1 > 0:
    print(f"Notas de 1 real: {notas_1}")

"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).
"""
numInteiro = int(input("Insira um número inteiro: "))

if (numInteiro % 2) == 0:
    print("Par")
else:
    print("Ímpar")

"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.
"""
entrada = input("Insira um número: ") #cria o input e guarda o numero na variavel "num"

num = float(entrada) #cria uma variável para exibir um float (o numero decimal)
    
if num.is_integer(): # is_integer é a funcao de arredondamento citada no enunciado, este if vê se o número inserido é um inteiro
    print(f"{entrada} é um número inteiro.")
else:
    print(f"{num} é um número decimal.")

"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.
"""

#cria os inputs, como float porque futuramente vai ser necessário a verificação de decimal ou inteiro
entrada1 = float(input("Insira um número: "))
entrada2 = float(input("Insira outro número: "))
                 
#cria o input do menu
operacao_opcao = int(input("Qual operação deseja realizar: \n(1) Par ou Ímpar\n(2) Positivo ou Negativo\n(3) Inteiro ou Decimal\n"))


if operacao_opcao == 1: #se a escolha do menu for 1, então
    if (entrada1) % 2 == 0: #se a 'entrada1' for divisivel por 2 sem deixar restos, então o número é par
        print(f"{entrada1} é par!")
    else:
        print(f"{entrada1} é ímpar!") 
    
    if (entrada2) % 2 == 0:
        print(f"{entrada2} é par!")
    else:
        print(f"{entrada2} é ímpar!") 

elif operacao_opcao == 2: #se a escolha do menu for 2, então
    if entrada1 < 0: #se a 'entrada1' for menor que 0, então é negativo
        print(f"{entrada1} é Negativo!")
    else: #se a 'entrada1' for maior que 0, então é negativo
        print(f"{entrada1} é Positivo!")

    if entrada2 < 0:
        print(f"{entrada2} é Negativo!")
    else:
        print(f"{entrada2} é Positivo!")

elif operacao_opcao == 3: #se a escolha do menu for 3, então
    if entrada1.is_integer(): #se a 'entrada1' for um inteiro 
        print(f"{entrada1} é inteiro")
    else:
        print(f"{entrada1} é decimal")

    if entrada2.is_integer():
        print(f"{entrada2} é inteiro")
    else:
        print(f"{entrada2} é decimal")
else:
    print("Escolha uma opção válida, 1, 2, ou 3.")

"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""

telefonou = input("Telefonou para a vítima? ")
local_crime = input("Esteve no local do crime? ")
mora_perto = input("Mora perto da vítima? ")
dever_favores = input("Devia para a vítima? ")
ja_trabalhou = input("Já trabalhou com a vítima? ")

classificacao = 0

if telefonou.lower() == "sim": classificacao += 1
if local_crime.lower() == "sim": classificacao += 1
if mora_perto.lower() == "sim": classificacao += 1
if dever_favores.lower() == "sim": classificacao += 1
if ja_trabalhou.lower() == "sim": classificacao += 1
        
if classificacao == 2:
    print("Suspeita")
elif classificacao >= 3 and classificacao <= 4:
    print("Cúmplice")
elif classificacao == 5:
    print("Assassino")
else:
    print("Inocente")
"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:

Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro.

Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

tipo_de_combustivel = input("Informe o tipo de combustivel (A-álcool, G-gasolina): ")
litros_vendidos = float(input("Informe os litros vendidos: "))

preco_alcool = 1.90
preco_gasolina = 2.50

valor_a_pagar = 0

if tipo_de_combustivel == "A":
    if litros_vendidos <= 20:
        valor_a_pagar = litros_vendidos * preco_alcool * 0.97
    else:
        valor_a_pagar = litros_vendidos * preco_alcool * 0.95
elif tipo_de_combustivel == "G":
    if litros_vendidos <= 20:
        valor_a_pagar = litros_vendidos * preco_gasolina * 0.96
    else:
        valor_a_pagar = litros_vendidos * preco_alcool * 0.94
else:
    print("Tipo de combustivel inválido")

if valor_a_pagar > 0:
    print(f"Valor a ser pago: {valor_a_pagar:.2f}")

"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, 
receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de bananas adquiridas e 
escreva o valor a ser pago pelo cliente.
"""

fruta_escolha = input("Quer Morangos (M) ou Bananas (B)? ")
fruta = float(input("Quantos kg de fruta quer: "))

total_a_pagar = 0

if fruta_escolha.lower() == "m":
    if fruta <= 5:
        total_a_pagar = fruta * 2.50
    else:
        total_a_pagar = fruta * 2.20

elif fruta_escolha.lower() == "b":
    if fruta <= 5:
        total_a_pagar = fruta * 1.80
    else:
        total_a_pagar = fruta * 1.50

if (fruta > 8) or (total_a_pagar > 25):
    total_a_pagar *= 0.90

print(f"Total a pagar por {fruta}kg é de {total_a_pagar}€")
"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
"""

"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, 
porém não há limites para a quantidade de carne por cliente. 
Se a compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. 
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, 
contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

tipo_carne = input("Qual o tipo de carne que deseja? Filé Duplo | Alcatra | Picanha: ")
quantidade_carne = float(input("Qual a quantidade de carne em KG: "))
cartao_tabajara = input("Pretende usar cartão Tabajara? (S)im ou (N)ao: ")

valor_a_pagar = 0
 
if tipo_carne.lower() == "file duplo":
    if quantidade_carne <= 5:
        valor_a_pagar = quantidade_carne * 4.90
    else:
        valor_a_pagar = quantidade_carne * 5.80
elif tipo_carne.lower() == "alcatra":
    if quantidade_carne <= 5:
        valor_a_pagar = quantidade_carne * 5.90
    else:
        valor_a_pagar = quantidade_carne * 6.80
elif tipo_carne.lower() == "picanha":
    if quantidade_carne <= 5:
        valor_a_pagar = quantidade_carne * 6.90
    else:
        valor_a_pagar = quantidade_carne * 7.80
else:
    print("Tipo de carne inválido!")

if cartao_tabajara.lower() == "s":
    valor_a_pagar = valor_a_pagar * 0.95

if valor_a_pagar > 0:
    print(f"Você vai pagar {valor_a_pagar:.2f}€ por {quantidade_carne:.0f}kg de {tipo_carne}! Obrigado e volte sempre!")