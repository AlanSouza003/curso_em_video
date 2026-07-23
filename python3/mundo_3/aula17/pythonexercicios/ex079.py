import os

def limpatela():
    os.system("cls" if os.name == "nt" else "clear")
list_number = list()
while True: 
    number = int(input("\033[1;97mDigite qualquer valor: \033[0m"))
    if number in list_number:
        print("\033[1;91mValor duplicado! Este valor já foi adicionado a lista.\033[0m")
    else: 
        print("\033[1;92mValor adicionado com sucesso!\033[0m")
        list_number.append(number)
    more_one = str(input("\033[1;97mDeseja adicionar mais um número? "
                         "[S/n]\033[0m")).lower()
    if more_one in 'ssim':
        limpatela()
        print(f"\033[1;96mValores ja adicionados:\033[0m \033[1;97m{list_number}\033[0m")
    elif more_one in 'nnaonão':
        break
list_number.sort()
print("─" * 20)
print(f"Os valores adicionados a lista foram: {list_number}")

