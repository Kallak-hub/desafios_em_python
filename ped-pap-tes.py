import random

simbolos = ["tesoura", "papel", "pedra"]

pontuação_usu = 0
pontuação_sim = 0

while True:
    try:
        escolha_sim = random.choice(simbolos)
        escolha_usu = input("pedra, papel ou tesoura? ")

        if escolha_usu == escolha_sim:
            print("Empate!")

        elif escolha_usu == "pedra" and escolha_sim == "tesoura":
            print("Pedra vence tesoura")
            pontuação_usu += 1

        elif escolha_usu == "tesoura" and escolha_sim == "papel":
            print("Tesoura vence papel")
            pontuação_usu += 1

        elif escolha_usu == "papel" and escolha_sim == "pedra":
            print("Papel vence pedra")
            pontuação_usu += 1

        else:
            print("Você perdeu!")
            pontuação_sim += 1

        print(f"Usúario: {pontuação_usu} | Máquina: {pontuação_sim}")

    except ValueError:
        print("Digite apenas pedra, papel ou tesoura!")