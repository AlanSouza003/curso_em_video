from time import sleep
import pydoc

def title(txt, color):
    line = len(txt) + 5
    print(f"{color}─\033[0m" * line)
    print(f"{color}  {txt}   \033[0m")
    print(f"{color}─\033[0m" * line)

def help(txt):
    text_help = pydoc.plain(pydoc.render_doc(txt))
    for linha in text_help.splitlines():
        print(f'\033[30;47m{linha:<80}\033[0m')

# TODO: Main Program
count = 0
while True:
    if count == 0:
        color_text = '\033[30;42m'
        count = 1
    title("SISTEMA DE AJUDA PyHELP", color_text)
    comand = input("<Função ou Biblioteca> ").strip().lower()
    if comand == 'fim':
        color_text = '\033[30;41m'
        title('<<< ATÉ A PRÓXIMA >>>', color_text)
        break
    if count == 1:
        color_text = '\033[30;46m'
        count = 0
    sleep(1)
    title(f"ACESSANDO O MANUAL DO COMANDO '{comand}'", color_text)
    sleep(1)
    help(comand)
