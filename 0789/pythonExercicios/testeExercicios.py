"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
numeros = [1,2,3,4,5,6,7,8,123,412,]
for i in numeros:
    print(i, end=" ")

# ou
print("\n")

numeros2 = []

for i in range(1,6):
    numeros2.append(i)
    
for elem in numeros2:
    print(elem, end=" ")