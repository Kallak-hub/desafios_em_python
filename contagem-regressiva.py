import time
n = int(input("Digite o número para contagem regressiva: "))

for i in range(n):
    print(n - i)
    time.sleep(0.5)

print("Fim")