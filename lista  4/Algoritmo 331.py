import random

def jogo_marciano():
    print("Bem-vindo ao jogo do Marciano!")
    print("Existem 100 árvores numeradas de 1 a 100.")
    arvore_marciano = int(input("Jogador 1, escolha a árvore (1-100) para o marciano se esconder: "))
    while arvore_marciano < 1 or arvore_marciano > 100:
        arvore_marciano = int(input("Escolha inválida. Digite um número entre 1 e 100: "))

    print("\n" * 50)  # Limpa a tela para o segundo jogador não ver

    print("Jogador 2, tente acertar a árvore onde o marciano está escondido!")
    balas = 5
    acertou = False

    while balas > 0 and not acertou:
        tentativa = int(input(f"Você tem {balas} balas. Em qual árvore deseja atirar? (1-100): "))
        if tentativa == arvore_marciano:
            print("Parabéns! Você acertou o marciano!")
            acertou = True
        else:
            balas -= 1
            if tentativa < arvore_marciano:
                print("O marciano diz: Estou mais à direita!")
            else:
                print("O marciano diz: Estou mais à esquerda!")

    if not acertou:
        print(f"Você errou todas as balas! O marciano foi levado para Marte. Ele estava na árvore {arvore_marciano}.")

if __name__ == "__main__":
    jogo_marciano()