def readMoney(txt):
    while True:
        num = str(input(txt)).strip()
        num_format = num.replace(',', '.')
        if num_format.replace('.', '', 1).isdigit():
            num_final = float(num_format)
            break
        print(f'\033[1;91mERRO! "{num}" é um valor inválido.\033[0m')
    return num_final