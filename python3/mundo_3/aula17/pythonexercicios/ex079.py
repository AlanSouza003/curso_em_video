lista_num = list()

while True: 
    num = int(input("Digite qualquer valor: "))
    lista_num.append(num)
    add_outro_num = str(input("Deseja adicionar outro valor? [S/n]")).lower()
    if add_outro_num in 'nnaonão':
        break

