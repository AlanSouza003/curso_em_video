def readInt(txt):
    while True:
        try:
            num = int(input(txt))
        except Exception:
            print("\033[1;91mFALHA: Digite um valor inteiro válido.\033[0m")
        except KeyboardInterrupt:
            print(f"\n\033[1;91mUsário interrompeu o programa!\033[0m")
            return 0
        else:
            return num

def readFloat(txt):
    while True:
        try: # |> Operação
            num = float(input(txt))
        except Exception: # |> Falha
            print("\033[1;91mFALHA: Digite um valor real válido.\033[0m")
        except KeyboardInterrupt: # |> Falha
            print(f"\n\033[1;91mUsário preferiu não digitar este número!\033[0m")
            return 0
        else: # |> Deu certo
            return num

# TODO: Main Program
valueI = readInt("Digite um valor inteiro: ")
if valueI >= 0 or valueI <= -1: # >>> Verificando se o valueI é maior que 0 ou menor que -1
    valueF = readFloat("Digite um valor real: ")
else:
    valueF = 0
print(f"O valor inteiro digitado foi o {valueI} é o real foi {valueF}")