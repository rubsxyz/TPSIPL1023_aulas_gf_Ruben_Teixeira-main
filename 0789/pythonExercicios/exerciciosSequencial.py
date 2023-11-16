"""
Faça um Programa que mostre a mensagem "Alo mundo" na tela.
"""
print("Alo mundo")
"""
------------------------------------------------------------
Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
"""
num = input("Escolha um número à sua escolha: ")
print(num)
"""
------------------------------------------------------------
Faça um Programa que peça dois números e imprima a soma.
"""
num1 = int(input("Escolha o primeiro número à sua escolha para somar: "))
num2 = int(input("Escolha o segundo número à sua escolha para somar: "))

num_total = num1 + num2
print(num_total)
"""
------------------------------------------------------------
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""
nota_1 = int(input("Qual foi a sua primeira nota?: "))
nota_2 = int(input("Qual foi a sua segunda nota?: "))
nota_3 = int(input("Qual foi a sua terceira nota?: "))
nota_4 = int(input("Qual foi a sua quarta nota?: "))

media_total = (nota_1 + nota_2 + nota_3 + nota_4) / 4
print(media_total)
"""
------------------------------------------------------------
Faça um Programa que converta metros para centímetros.
"""
metros = int(input("Insira o número de metros para converter a centímetros: "))
centimetros = metros * 100
print(f"{metros} metros são {centimetros} centimetros")
"""
------------------------------------------------------------
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
raio = int(input("Qual o raio do seu circulo? : "))
area_circulo = 3.1415 * (raio ** 2)

print(f"A area do circulo é {area_circulo}")
"""
------------------------------------------------------------
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
lado_quadrado = int(input("Quanto mede o lado do seu quadrado? : "))
area_quadrado = lado_quadrado * lado_quadrado
dobro_area_quadrado = area_quadrado * 2

print(f"O dobro da área do quadrado é {dobro_area_quadrado}")
"""
------------------------------------------------------------
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
"""
salario_hora = float(input("Quando você ganha por hora? "))
num_horas = int(input("Quantas horas você trabalha por mês? "))

salario_total = salario_hora * num_horas
print(salario_total)
"""
------------------------------------------------------------
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
"""
fahrenheit = int(input("Quantos graus em Fahrenheit a serem convertidos para Celsius? "))
celsius = 5 * ((fahrenheit-32) / 9)

print(f"{fahrenheit} graus em fahrenheit são {celsius} graus Celsius")
"""
------------------------------------------------------------
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
"""
fahrenheit = int(input("Quantos graus em Fahrenheit a serem convertidos para Celsius? "))
celsius = 5 * ((fahrenheit-32) / 9)

print(f"{fahrenheit} graus em fahrenheit são {celsius} graus Celsius")
"""
------------------------------------------------------------
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.
"""
num1 = int(input("Diga-me o primeiro número inteiro"))
num2 = int(input("Diga-me o segundo número inteiro"))
num_real = int(input("Diga-me um número real"))

# o produto do dobro do primeiro com metade do segundo .
resultado1 = (2 * num1) * (num2 / 2)

# a soma do triplo do primeiro com o terceiro
resultado2 = (3 * num1) + num_real

# o terceiro elevado ao cubo
resultado3 = num_real ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {resultado1}")
print(f"A soma do triplo do primeiro com o terceiro é: {resultado2}")
print(f"O terceiro elevado ao cubo é: {resultado3}")
"""
------------------------------------------------------------
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
"""
altura = float(input("Insira a sua altura"))
peso_ideal = (72.7 * altura) - 58

print(f"O seu peso ideal é de {peso_ideal}")
"""
------------------------------------------------------------
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7
"""
altura = float(input("Insira a sua altura (m): "))
sexo = str(input("Você é Homem(H) ou Mulher(M)?: "))

if sexo == "H" or sexo == "h":
    peso_ideal = (72.7 * altura) - 58
    print(f"O seu peso ideal sendo Homem, tendo {altura}m de altura é de {peso_ideal:.2f} kg")
elif sexo == "M" or sexo == "m":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O seu peso ideal sendo Mulher, tendo {altura}m de altura é de {peso_ideal:.2f} kg")
else:
    print("Sexo não reconhecido. Use 'H' para Homem e 'M' para Mulher.")
"""
------------------------------------------------------------
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) 
deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a 
variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável 
multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
"""
peso_peixes = (float(input("Insira o peso de peixes (kg): ")))
peso_limite = 50.00

if peso_peixes > peso_limite:
    excesso = peso_peixes - peso_limite
    multa = excesso * 4.00
    print(f"O peso excedeu o limite em {excesso:.2f} quilos.")
    print(f"João deverá pagar uma multa de {multa:.2f}€.")
else:
    excesso = 0.0
    multa = 0.0
    print("O peso de peixes está dentro do limite.")
"""
------------------------------------------------------------
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
ganhos_hora = float(input("Quanto você ganha por hora? "))
horas_mes = int(input("Quantas horas você trabalha por mês? "))

salario_bruto = ganhos_hora * horas_mes

imposto_renda = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100

# Salario Bruto
salario_liquido = salario_bruto - (imposto_renda + inss + sindicato)

print(f"Você recebe ao mês: {salario_bruto}€")
print(f"Você paga de INSS: {inss}€")
print(f"Você paga de sindicato: {sindicato}€")
print(f"Você recebe de salario liquido: {salario_liquido}€")
"""
------------------------------------------------------------

Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
cobertura_por_litro = 3
tamanho_lata = 18
preco_lata = 80.00

metros_quadrados = float(input("Quantos metros quadrados da área a ser pintada? "))
volume_tinta = metros_quadrados / cobertura_por_litro
quantidade_latas = int(volume_tinta / tamanho_lata) + 1
orcamento_necessario = preco_lata * quantidade_latas


print(f"Você precisa de {quantidade_latas} latas para preencher {metros_quadrados} de area em metros quadrados. "
      f"E terá que pagar {orcamento_necessario}€ por {quantidade_latas} latas")
"""

------------------------------------------------------------
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
metros_quadrados = float(input("Quantos metros quadrados da área a ser pintada? "))

cobertura_litro = 6
preco_lata = 80.0

volume_tinta = metros_quadrados / cobertura_litro

#---

## LATAS DE 18
tamanho_lata = 18
quantidade_latas = (int(volume_tinta / tamanho_lata) + 1)
orcamento_necessario_latas = preco_lata * quantidade_latas

print(f"Você vai precisar de {quantidade_latas:0.0f} lata(s) para {volume_tinta:0.2f} litros para preencher {metros_quadrados} metros quadrados"
      f"e isso custará {orcamento_necessario_latas}€")
#---

## GALOES DE 3.6
preco_galoes = 25.0
tamanho_galoes = 3.6
quantidade_galoes = (int(volume_tinta / tamanho_galoes) + 1)
orcamento_necessario_galoes = preco_galoes * quantidade_galoes

print(f"Você vai precisar de {quantidade_galoes:0.0f} galões para {volume_tinta:0.2f} litros para preencher {metros_quadrados} metros quadrados,"
      f"e isso custará {orcamento_necessario_galoes}€")
"""

------------------------------------------------------------
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
tamanho_arquivo = float(input("Qual o tamanho do seu arquivo (MB): "))
velocidade_internet = float(input("Qual a sua velocidade de um link de Internet (Mbps): "))

tempo_aproximado = tamanho_arquivo / velocidade_internet / 60

print(f"O tempo aproximado de download do arquivo é de: {tempo_aproximado:0.2f} minutssos")