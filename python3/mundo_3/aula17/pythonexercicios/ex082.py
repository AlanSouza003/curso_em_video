list_number = list()
list_odd = list()
list_pair = list()

while True:
    list_number.append(
        int(input("Digite um valor: "))
    )
    more_one = str(input("Deseja continuar? [S/n]")).lower()
    if more_one in ['n', 'não', 'nao']:
        break
    elif more_one not in ['s', 'sim']:
        print('Erro! Digite "S" ou "Sim" para continuar')
        list_number.pop()
print(f"Os valores adicionados a lista foram: {list_number}")

for number in list_number:
    if number % 2 == 0:
        list_pair.append(number)
    else:
        list_odd.append(number)

print(
    f"A lista com os valores pares: {list_pair}\n"
    f"A lista com os valores ímpares: {list_odd}"
)