import socket
import sys
import time
import pyfiglet

while True:
    print(pyfiglet.figlet_format("Kallak-Hub", font="slant"))

    try:
        alvo = input("Digite o IP ou domínio: ").strip()
        hostip = socket.gethostbyname(alvo)

        print(f"\n[*] Escaneando {hostip}\n")

        portas = [
            21, 22, 23, 25, 53, 80,
            110, 139, 143, 443, 445,
            3306, 3389, 5432, 8080
        ]

        inicio = time.time()

        for porta in portas:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.2)

            resultado = sock.connect_ex((hostip, porta))

            if resultado == 0:
                try:
                    servico = socket.getservbyport(porta)
                except:
                    servico = "Desconhecido"

                print(f"[+] Porta {porta:<5} ABERTA | Serviço: {servico}")

            sock.close()

        fim = time.time()
        print(f"\n[*] Scan concluído em {fim - inicio:.2f} segundos")

    except socket.gaierror:
        print("[-] Não foi possível resolver o host.")

    except KeyboardInterrupt:
        print("\n[!] Programa finalizado pelo usuário.")
        sys.exit()

    except Exception as erro:
        print(f"[-] Erro: {erro}")