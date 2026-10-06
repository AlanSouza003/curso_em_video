from lib.colors import c

def readInt(txt, cor=0):
    while True:
        try:
            num = int(input(f"{c[cor]}{txt}{c[0]}"))
        except Exception:
            print(f"{c[2]}FALHA: Digite um valor inteiro válido.{c[0]}")
        except KeyboardInterrupt:
            print(f"\n{c[2]}Usário interrompeu o programa!{c[0]}")
            return 0
        else:
            return num

def line(leen=42):
    return f'{c[8]}─{c[0]}' * leen

def header(txt, cor=0):
    print(line())
    print(f"{c[cor]}{txt.center(42)}{c[0]}")
    print(line())

def menu(list, c1=0, c2=0):
    header("Menu Principal", 8)
    count = 1
    for o in list:
        print(f"{c[c1]}{count} -{c[0]} {c[c2]}{o}{c[0]}")
        count += 1
    print(line())
    opcion = readInt(f'Sua Opção: ', 4)
    return opcion
