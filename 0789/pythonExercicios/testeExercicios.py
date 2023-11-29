"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
vetor_total = []
vetor_par = []
vetor_impar = []

for i in range(1,21):
    vetor_total.append(i)

    if i % 2 == 0:
        vetor_par.append(i)
    else:
        vetor_impar.append(i)

print(f"Total: {vetor_total}")
print(f"PAR: {vetor_par}")
print(f"IMPAR: {vetor_impar}")