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