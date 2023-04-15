from random import randint


def main():
    numeroAleatorio = randint(0, 100)
    deveContinuar = True

    print("Bem-vindo ao Jogo de Adivinhação de Número!")
    print("Estou pensando em um número de 0 a 100.\n")

    dificuldade = input("Escolha uma dificulade ('fácil' ou 'difícil'): ").lower()

    while dificuldade not in ["fácil", "difícil"]:
        dificuldade = input("Digite apenas 'fácil' ou 'difícil': ").lower()

    if dificuldade == "fácil":
        vidas = 10
    else:
        vidas = 5

    while deveContinuar:
        print(f"\nVocê tem {vidas} vidas restantes.")
        vidas -= 1
        palpite = input("Dê um palpite: ")

        while not palpite.isnumeric():
            palpite = input("Digite um número entre 0 e 100: ")

        palpite = int(palpite)

        if palpite == numeroAleatorio or vidas == 0:
            deveContinuar = False
        elif palpite > numeroAleatorio:
            print("\nMuito alto. Adivinhe novamente!")
        elif palpite < numeroAleatorio:
            print("\nMuito baixo. Adivinhe novamente!")

    if palpite == numeroAleatorio:
        print(f"\nVocê ganhou! O número era {numeroAleatorio}!")
    else:
        print(f"\nVocê perdeu... O número era {numeroAleatorio}.")


if __name__ == "__main__":
    main()
