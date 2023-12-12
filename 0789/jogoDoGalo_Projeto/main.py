import random

tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
jogador1 = "X"
jogador2 = "O"

def imprimir_tabuleiro():
    print("   |   |   ")
    print(" {} | {} | {} ".format(tabuleiro[0], tabuleiro[1], tabuleiro[2]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {} ".format(tabuleiro[3], tabuleiro[4], tabuleiro[5]))
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" {} | {} | {} ".format(tabuleiro[6], tabuleiro[7], tabuleiro[8]))
    print("   |   |   ")

def verificar_vencedor():
    for i in range(0, 3):
        if tabuleiro[i] == tabuleiro[i + 3] == tabuleiro[i + 6] != " ":
            return tabuleiro[i]

    for i in range(0, 3):
        if tabuleiro[i * 3] == tabuleiro[i * 3 + 1] == tabuleiro[i * 3 + 2] != " ":
            return tabuleiro[i * 3]

    if tabuleiro[0] == tabuleiro[4] == tabuleiro[8] != " ":
        return tabuleiro[0]

    if tabuleiro[2] == tabuleiro[4] == tabuleiro[6] != " ":
        return tabuleiro[2]

    for i in range(0, 9):
        if tabuleiro[i] == " ":
            return None

    return "Empate"

def fazer_jogada(jogador):
    while True:
        posicao = input("Jogador {}: Digite a posição da sua jogada (1-9): ".format(jogador))
        posicao = int(posicao) - 1

        if tabuleiro[posicao] == " ":
            tabuleiro[posicao] = jogador
            break

        print("Posição ocupada. Digite outra posição.")

def main():
    imprimir_tabuleiro()

    jogador = jogador1
    while True:
        fazer_jogada(jogador)
        imprimir_tabuleiro()

        vencedor = verificar_vencedor()
        if vencedor is not None:
            print("O vencedor é o jogador {}!".format(vencedor))
            break

        jogador = jogador1 if jogador == jogador2 else jogador2 # Troca de jogador

if __name__ == "__main__":
    main()
