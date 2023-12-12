"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
numeros = [1,2,3,4,5,6,7,8,123,412]
for i in numeros:
    print(i, end=" ")

# ou
print("\n")

numeros2 = []

for i in range(1,6):
    numeros2.append(i)
    
for elem in numeros2:
    print(elem, end=" ")
"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
numeros = [1,2,3,4,5,6,7,8,123,412,]
for i in reversed(numeros):
    print(i, end=" ")
"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
nota_lista = []

for i in range(1,5):
    notas = int(input(f"Insira a nota {i}: "))
    nota_lista.append(notas) #adiciona a nota a lista 

media = sum(nota_lista) #soma os numeros da lista
print(f"Media: {media / 4:.2f}")
"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
"""
vetor = []
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes = 0

for i in range(1,11):
    caracteres = input(f"Insira o {i} caracter: ")

    if caracteres not in vogais:
        vetor.append(caracteres)
        consoantes += 1

print(f"Existem {consoantes} consoantes")
print(f"Vetor de consoantes: {vetor}")
# cria as listas
vetor_total = []
vetor_par = []
vetor_impar = []

for i in range(1,21):
    vetor_total.append(i)

    if i % 2 == 0:
        vetor_par.append(i) #se for par adiciona ao array par
    else:
        vetor_impar.append(i) #se for impar adiciona ao array impar

print(f"TOTAL:", *vetor_total)
print(f"PAR:", *vetor_par)
print(f"IMPAR:", *vetor_impar)

"""
Faça um Programa que peça as quatro notas de 10 alunos, 
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""
media = []
num_alunos_7 = 0

for i in range(1,5):
    nota_1 = int(input(f"Aluno {i} | Nota 1: "))
    nota_2 = int(input(f"Aluno {i} | Nota 2: "))
    nota_3 = int(input(f"Aluno {i} | Nota 3: "))
    nota_4 = int(input(f"Aluno {i} | Nota 4: "))

    media.append((nota_1 + nota_2 + nota_3 + nota_4) / 4)

print(media)

for elm in media:
    if elm >= 7:
        num_alunos_7 += 1

print(f"Existem {num_alunos_7} com media maior ou igual a 7")
"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
vetor = []

for i in range(1,6):
    num_inteiro = int(input(f"Number {i}: "))
    vetor.append(num_inteiro)

soma = sum(vetor)
produto = 1
for elemento in vetor:
    produto *= elemento

print(f"A soma dos números: {soma}")
print(f"A multiplicação dos números: {produto}")
print("Os números:", *vetor)
"""
Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. 

Imprima a idade e a altura na ordem inversa a ordem lida.
"""

idade = []
altura = []

for i in range(1,6):
    idade_pessoa = int(input(f"Idade pessoa {i}: "))
    altura_pessoa = float(input(f"Altura pessoa {i}: "))

    idade.append(idade_pessoa)
    altura.append(altura_pessoa)

print("\nIdade: ", end="")
for elm in reversed(idade):
    print(elm, end=" ")

print("\nAltura: ", end="")
for elm in reversed(altura):
    print(f"{elm}", end=" ")
"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
"""

vetor_A = [1,2,3,4,5,6,7,8,9,10]
vetor_quadratico = []
soma_quadrados = 0

for elm in vetor_A:
    soma = elm * elm
    print(f"Soma: {elm} * {elm} = {soma}")
    vetor_quadratico.append(soma)
    soma_quadrados += soma

print("\n", *vetor_quadratico)
print("A soma dos quadrados dos elementos do vetor é:", soma_quadrados)
"""
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
intercalados dos dois outros vetores.
"""

vetor_1 = [1,3,5,7,9,11,13,15,17,19]
vetor_2 = [2,4,6,8,10,12,14,16,18,20]
vetor_3 = []

for elm in range(len(vetor_1)): #len retorna o tamanho do vetor, e necessario para retornar o tamanho da array
    vetor_3.append(vetor_1[elm])
    vetor_3.append(vetor_2[elm])

print(*vetor_3)
"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
"""
vetor_1 = [1,2,3,4,5,6,7,8,9,10]
vetor_2 = [11,22,33,44,55,66,77,88,99,100]
vetor_3 = [111,222,333,444,555,666,777,888,999,1000]
vetor_4 = []

for elm in range(len(vetor_1)): #len retorna o tamanho do vetor, e necessario para retornar o tamanho da array
    vetor_4.append(vetor_1[elm])
    vetor_4.append(vetor_2[elm])
    vetor_4.append(vetor_3[elm])

print(*vetor_4)
"""
Foram anotadas as idades e alturas de 10 alunos. 
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.
"""
alunos_idades = []
alunos_alturas = []
alunos_13_altura_abaixo_media = 0

for i in range(1,6):
    idades = int(input(f"Aluno {i} | Idade:   "))
    alturas = float(input(f"Aluno {i} | Alturas: "))

    alunos_idades.append(idades)
    alunos_alturas.append(alturas)

media_alturas = sum(alunos_alturas) / len(alunos_alturas)

for i in range(len(alunos_idades)):
    if alunos_idades[i] > 13 and alunos_alturas[i] < media_alturas:
        alunos_13_altura_abaixo_media += 1

print(f"Existem {alunos_13_altura_abaixo_media} alunos com mais de 13 anos e com altura inferior à média ({media_alturas:.2f})cm de altura desses alunos")
"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 

Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""
meses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperaturas = []

for mes in meses:
    temperatura = float(input(f"Qual a temperatura média do mês {mes}: "))
    temperaturas.append(temperatura)

media = sum(temperaturas) / len(temperaturas)
print(f"A média anual das temperaturas é: {media:.2f} °C")

print("Meses com temperaturas acima da média anual:")
for i, temp in enumerate(temperaturas):
    if temp > media:
        print(f"{meses[i]} - Temperatura: {temp:.2f} °C")
"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. 
As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", 
entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
# classificacao = []

# telefonou = int(input("Telefonou para a vítima? (1)sim (2)nao: "))
# if telefonou == 1:
#     classificacao.append(1)
# else:
#     classificacao.append(0)

# local = int(input("Esteve no local do crime? (1)sim (2)nao: "))
# if local == 1:
#     classificacao.append(1)
# else:
#     classificacao.append(0)

# mora_perto = int(input("Mora perto da vítima? (1)sim (2)nao: "))
# if mora_perto == 1:
#     classificacao.append(1)
# else:
#     classificacao.append(0)

# dever = int(input("Devia para a vítima? (1)sim (2)nao: "))
# if dever == 1:
#     classificacao.append(1)
# else:
#     classificacao.append(0)

# trabalhou = int(input("Já trabalhou com a vítima? (1)sim (2)nao: "))
# if trabalhou == 1:
#     classificacao.append(1)
# else:
#     classificacao.append(0)

# if classificacao.count(1) == 2:
#     print("Suspeita")
# elif classificacao.count(1) >= 3 and classificacao.count(1) <= 4:
#     print("Cumplice")
# elif classificacao.count(1) == 5:
#     print("Assassino")
# else:
#     print("Inocente")

perguntas = ["Telefonou para a vítima?", 
             "Esteve no local do crime?", 
             "Mora perto da vítima?", 
             "Devia para a vítima?", 
             "Já trabalhou com a vítima?"
            ]

respostas = []

for i in range(len(perguntas)):
    res = input(f"{perguntas[i]} [S]im ou [N]ão ")
    respostas.append(res)

sim = 0
for i in range(len(respostas)):
    if respostas[i] == 'S' or respostas[i] == 's':
        sim += 1

suspeitas = "Inocente"
if sim == 2:
    suspeitas = "Suspeita"
elif sim >= 3 and sim <=4 :
    suspeitas = "Cúmplice"
elif sim == 5:
    suspeitas = "Assassino"

print(suspeitas)
"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). 
 
Após esta entrada de dados, faça:

Mostre a quantidade de valores que foram lidos; 
Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
Calcule e mostre a soma dos valores;
Calcule e mostre a média dos valores;
Calcule e mostre a quantidade de valores acima da média calculada;
Calcule e mostre a quantidade de valores abaixo de sete;
Encerre o programa com uma mensagem;
"""
abaixo_sete = 0
notas = []
mensagem = ['Obrigado por ter jogado :D']
while True:
    nota = int(input("Qual a nota: "))
    if nota == -1:
        break
    else:
        notas.append(nota)

print(notas)
print("Um ao lado do outro:\n",*notas)
print("Ordem inversa: ")
for elm in reversed(notas):
    print(f"{elm}", end="\n")
print("Soma dos valores: ",sum(notas))
media = sum(notas) / len(notas)
print(f"Media dos valores: {media:.2f}")
print(f"Quantidade de valores acima da media {media:.2f}: ", end="")
for elm in notas:
    if elm > media:
        print(elm, end=" ")
for elm in notas:
    if elm < 7:
        abaixo_sete += 1
print(f"\nQuantidade de valores abaixo de 7: ", end="")
print(abaixo_sete, end=" ")
print("\n", *mensagem)

"""
Utilize uma lista para resolver o problema a seguir. 
Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 

Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, 
ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores
receberam salários nos seguintes intervalos de valores:

$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""
contadores = [0] * 9

limites_salario = [300, 400, 500, 600, 700, 800, 900, 1000, float('inf')]

vendas_brutas = [3000, 2500, 700, 1200, 550, 950, 800]

for vendas in vendas_brutas:
    salario = 200 + 0.09 * vendas 
    indice = next(i for i, limite in enumerate(limites_salario) if salario < limite)
    contadores[indice] += 1 

for i, contador in enumerate(contadores):
    if i < 8:
        print(f"${200 + i * 100} - ${299 + i * 100}: {contador} vendedores")
    else:
        print(f"$1000 em diante: {contador} vendedores")
"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
O resultado do atleta será determinado pela média dos cinco valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 

O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Andre Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
saltitos = ['Primeiro Salto', 'Segundo Salto', 'Terceiro Salto', 'Quarto Salto', 'Quinto Salto']

while True:
    saltos = []

    nome_atleta = input("Nome do atleta: ")
    if nome_atleta != '':
        for i in range(1,6):
            salto = float(input(f"{saltitos[i - 1]}: "))
            saltos.append(salto)
    
        print("Resultado Final:")
        print(f"Atleta: {nome_atleta}")
        for elm in saltos:
            print(elm, end=" - ")
        print(f"\nMédia dos saltos: {sum(saltos) / len(saltos)} m")
    else:
        print("\nObrigado por ter usado o programa")
        break
"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor jogador após cada jogo. 

Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas telefonistas, 
para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, 
utilizando a linguagem de programação C++. 

Para computar cada voto, a telefonista digitará um número, entre 1 e 23, 
correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi encerrada. 
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de aviso, e voltando a pedir outro número. 

Após o final da votação, o programa deverá exibir:
O total de votos computados;
Os númeos e respectivos votos de todos os jogadores que receberam votos;
O percentual de votos de cada um destes jogadores;
O número do jogador escolhido como o melhor jogador da partida, juntamente com o número de votos e o percentual de votos dados a ele.
Observe que os votos inválidos e o zero final não devem ser computados como votos. 

O resultado aparece ordenado pelo número do jogador. O programa deve fazer uso de arrays. 
O programa deverá executar o cálculo do percentual de cada jogador através de uma função. 
Esta função receberá dois parâmetros: o número de votos de um jogador e o total de votos. 
A função calculará o percentual e retornará o valor calculado. Abaixo segue uma tela de exemplo. 
O disposição das informações deve ser o mais próxima possível ao exemplo. 
Os dados são fictícios e podem mudar a cada execução do programa. 
Ao final, o programa deve ainda gravar os dados referentes ao resultado da votação em um arquivo texto no disco, 
obedecendo a mesma disposição apresentada na tela.

Enquete: Quem foi o melhor jogador?

Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 9
Número do jogador (0=fim): 10
Número do jogador (0=fim): 11
Número do jogador (0=fim): 10
Número do jogador (0=fim): 50
Informe um valor entre 1 e 23 ou 0 para sair!
Número do jogador (0=fim): 9
Número do jogador (0=fim): 9
Número do jogador (0=fim): 0

Resultado da votação:

Foram computados 8 votos.

Jogador Votos           %
9               4               50,0%
10              3               37,5%
11              1               12,5%
O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
"""
votos_computados = 0
votos = []
votos_por_jogador = []

while True:
    numero = int(input("Número do jogador (0=fim): "))

    while numero > 23 or numero < 0:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        numero = int(input("Número do jogador (0=fim): "))

    if numero == 0:
        break
    elif numero > 0 or numero < 23:
        votos.append(numero)
        votos_computados += 1

print(f"\nResultado da votação: \n")
print(f"Foram computados {votos_computados} votos. \n")

print(votos)
votos_unicos = set() # Criando um conjunto (set) para armazenar números únicos

for elm in votos:
    votos_unicos.add(elm)

for elm in votos_unicos:
    print(elm, end="\n")
"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de organizações:
"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe ao final o resultado da mesma. 
O programa deverá ler os valores até ser informado o valor 0, que encerra a entrada dos dados. 

Não deverão ser aceitos valores além dos válidos para o programa (0 a 6). 
Os valores referentes a cada uma das opções devem ser armazenados num vetor. 

Após os dados terem sido completamente informados, o programa deverá calcular a percentual de cada um dos concorrentes 
e informar o vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""
servidores = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
votos = []


print("Windows Server > 1\nUnix > 2\nLinux > 3\nNetware > 4\nMac OS > 5\nOutro > 6\n")

while True:
    voto_sistema_operativo = int(input("Qual o melhor Sistema Operacional para uso em servidores? "))

    while voto_sistema_operativo > 6 or voto_sistema_operativo < 0:
        print("Insira um valor valido! (0 a 6)")
        voto_sistema_operativo = int(input("Qual o melhor Sistema Operacional para uso em servidores? "))
        
    if voto_sistema_operativo != 0:
        votos.append(voto_sistema_operativo)

    if voto_sistema_operativo == 0:
        break
    
    windows_server = votos.count(1)
    unix = votos.count(2)
    linux = votos.count(3)
    netware = votos.count(4)
    macos = votos.count(5)
    outro = votos.count(6)

    total = windows_server + unix + linux + netware + macos + outro
    
percentual_windows_server = (windows_server / total) * 100
percentual_unix = (unix / total) * 100
percentual_linux = (linux / total) * 100
percentual_netware = (netware / total) * 100
percentual_macos = (macos / total) * 100
percentual_outro = (outro / total) * 100

mais_votado = max(votos)

print(f"O sistema operacional mais votado foi o {servidores[mais_votado]}.")
print("\nSistema Operacional\tVotos\t%")
print("-------------------\t-----\t---")
print(f"{servidores[0]}\t\t{windows_server}\t{percentual_windows_server:.2f}")
print(f"{servidores[1]}\t\t\t{unix}\t{percentual_unix:.2f}")
print(f"{servidores[2]}\t\t\t{linux}\t{percentual_linux:.2f}")
print(f"{servidores[3]}\t\t\t{netware}\t{percentual_netware:.2f}")
print(f"{servidores[4]}\t\t\t{macos}\t{percentual_macos:.2f}")
print(f"{servidores[5]}\t\t\t{outro}\t{percentual_outro:.2f}")
print("-------------------\t-----")
print(f"Total\t\t\t{total}")

print(f"O sistema operacional mais votado foi o {servidores[mais_votado]}.")
"""
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono.
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte forma de cálculo:
a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá apresentar:
O salário de cada funcionário, juntamente com o valor do abono;
O número total de funcionário processados;
O valor total a ser gasto com o pagamento do abono;
O número de funcionário que receberá o valor mínimo de 100 reais;
O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa, apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.
Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses carros faz com um litro de combustível. Calcule e mostre:
O modelo do carro mais econômico;
Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada execução do programa.
Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100

Situação                        Quantidade              Percentual
1- necessita da esfera                  40                     40%
2- necessita de limpeza                 30                     30%
3- necessita troca do cabo ou conector  15                     15%
4- quebrado ou inutilizado              15                     15%
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre       456123789
anderson        1245698456
antonio         123456456
carlos          91257581
cesar           987458
rosemary        789456125
Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

1    alexandre       434,99 MB             16,85%
2    anderson       1187,99 MB             46,02%
3    antonio         117,73 MB              4,56%
4    carlos           87,03 MB              3,37%
5    cesar             0,94 MB              0,04%
6    rosemary        752,88 MB             29,16%

Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal.
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""