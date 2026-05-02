import random
import string
import json

while True:
    nome = input("\nNome (ex: Gmail, Conta do X ou etc..): ")
    tamanho = int(input("Tamanho da senha: "))

    usar_maiusculas = input("Incluir letras maiúsculas? (s/n): ").lower() == "s"
    usar_numeros = input("Incluir números? (s/n): ").lower() == "s"
    usar_simbolos = input("Incluir símbolos? (s/n): ").lower() == "s"

    caracteres = string.ascii_lowercase

    if usar_maiusculas:
        caracteres += string.ascii_uppercase

    if usar_numeros:
        caracteres += string.digits

    if usar_simbolos:
        caracteres += string.punctuation

    senha = "".join(random.choice(caracteres) for _ in range(tamanho))

    print(f"\nSenha gerada: {senha}")

    dados = {
        "nome": nome,
        "senha": senha
    }

    try:
        with open("senhas.json", "r") as arquivo:
            lista = json.load(arquivo)
    except:
        lista = []

    lista.append(dados)

    with open("senhas.json", "w") as arquivo:
        json.dump(lista, arquivo, indent=4)

    print("Senha salva em senhas.json")

    continuar = input("\nGerar outra senha? (s/n): ").lower()
    if continuar != "s":
        break