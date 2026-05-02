print("Pense em um número entre 1 e 100")

baixo = 1
alto = 100
tentativas = 0

while True:
    try:
        chute = (baixo + alto) // 2
        tentativas += 1

        resposta = input(f"O número é {chute}? (maior/menor/acertou): ")

        if resposta == "acertou":
            print(f"Acertei em {tentativas} tentativas!")
            break
        elif resposta == "maior":
            baixo = chute + 1
        elif resposta == "menor":
            alto = chute - 1
            
    except ValueError:
        print("Digite apenas números!")