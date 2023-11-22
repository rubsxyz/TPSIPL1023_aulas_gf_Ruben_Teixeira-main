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
        