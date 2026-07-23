list_number = list()
count_numbers = 0
while True:
    list_number.append(
        int(input("Digite um valor: "))
    )
    count_numbers += 1
    more_one = str(input("Deseja continuar? [S/n]")).lower()
    if more_one in 'nnãonao':
        break
    elif more_one not in 'ssim':
        print('Erro! Digite "S" ou "Sim" para continuar')
        count_numbers -= 1
        list_number.pop()
print("─" * 20)
list_number.sort(reverse=True)
print(
    f"O total de números adicionados a lista foram {count_numbers}\n"
    f"Valores digitados em forma decrescente: {list_number}"
)
if 5 in list_number:
    print(f"O valor 5 se encontra na lista, e está na posição", end=' ')
    for position, number in enumerate(list_number):
        if number == 5:
            print(f"{position}...",end=' ')
    print()
else:
    print(f"O valor 5 não foi encontrado na lista.")
        


