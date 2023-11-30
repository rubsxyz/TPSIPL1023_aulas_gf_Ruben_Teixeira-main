"""
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos 
intercalados dos dois outros vetores.

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