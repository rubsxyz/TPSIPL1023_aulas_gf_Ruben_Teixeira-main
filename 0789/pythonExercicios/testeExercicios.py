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
