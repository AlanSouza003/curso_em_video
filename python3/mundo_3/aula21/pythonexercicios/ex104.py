def readInt(txt):
    while True:
        num = str(input(txt))
        if num.isnumeric():
            num = int(num)
            break
        print("\033[1;91mERRO! Digite um valor inteiro.\033[0m")
    return num

# TODO: Main Program
n = readInt("Digite um valor: ")
print(f"Você digitou o valor {n}.")