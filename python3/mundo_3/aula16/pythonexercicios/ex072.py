import os
n_extenso = (
    "Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", "Sete", "Oito",
    "Nove", "Dez", "Onze", "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis",
    "Dezessete", "Dezoito", "Dezenove", "Vinte"
)
def limpatela():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    limpatela()
    print("NÚMEROS POR EXTENSO.")
    print("--------------------")
    n = int(
        input("Digite um valor entre 0 e 20: ")
    )
    if 0 <= n <= 20:
        for posicao, numero in enumerate(n_extenso):
            if posicao == n:
                print(f"Você digitou o valor {numero}.")
                break
    else:
        print("Valor errado! Tente novamente.")
        input("De enter para continuar...")
        continue
    break
