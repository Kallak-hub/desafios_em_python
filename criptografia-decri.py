from cryptography.fernet import Fernet
import os

#gera e carrega a chave
def gerar_chave():
    chave = Fernet.generate_key()
    with open("chave.key", "wb") as arquivo:
        arquivo.write(chave)

def carregar_chave():
    return open("chave.key", "rb").read()

#gera uma chave automaticamente se não existir nenhuma
if not os.path.exists("chave.key"):
    gerar_chave()

chave = carregar_chave()
f = Fernet(chave)

#funções de criptografar e descriptografar :0
def criptografar():
    texto = input("Digite a mensagem: ")
    token = f.encrypt(texto.encode())
    print("\nMensagem criptografada:")
    print(token.decode())


def descriptografar():
    token = input("Cole a mensagem criptografada: ")
    try:
        texto = f.decrypt(token.encode()).decode()
        print("\nMensagem original:")
        print(texto)
    except:
        print("Erro ao descriptografar (chave incorreta)")

while True:
    print("\n MENU ")
    print("1: Criptografar")
    print("2: Descriptografar")
    print("3: Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        criptografar()

    elif opcao == "2":
        descriptografar()

    elif opcao == "3":
        break

    else:
        print("Opção inválida, tenta de novo")

#Observação: tenho que melhorar esses "menu".