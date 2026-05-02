import qrcode
import cv2

while True:
    print("\n1: Gerar o QR Code")
    print("2: Ler o QR Code")
    print("3: Sair")

    opcao = input("Escolha: ")

    if opcao == "1": #gerar
        dados = input("Digite o conteúdo: ")
        nome = input("Nome do arquivo (sem .png): ")

        img = qrcode.make(dados)
        img.save(f"{nome}.png")

        print("O QR Code foi criado!")

    elif opcao == "2": #ler
        caminho = input("Caminho da imagem: ")

        img = cv2.imread(caminho)
        detector = cv2.QRCodeDetector()

        dados, _, _ = detector.detectAndDecode(img)

        if dados:
            print("Conteúdo:", dados)
        else:
            print("Não foi possível ler, tente de novo!")

    elif opcao == "3": #sair, auto explicativo
        break