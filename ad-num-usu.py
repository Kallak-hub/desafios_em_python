import random 

escolha_maquina = random.randint(1, 100)

while True:
    try:
        escolha_usuario = int(input("Escolha um número entre 1 e 100: "))

        if escolha_usuario == escolha_maquina:
            print(f"Acertou! o número era {escolha_maquina}")
            break

        elif escolha_usuario < escolha_maquina:
            print("Muito baixo!")

        elif escolha_usuario > escolha_maquina:
            print("Muito alto!")
            
        else:
            print("Resposta errada, tente novamente")
            

    except ValueError:
        print("Digite apenas números!")