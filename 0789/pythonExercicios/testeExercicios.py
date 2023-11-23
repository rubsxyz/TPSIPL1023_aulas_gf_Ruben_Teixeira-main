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
