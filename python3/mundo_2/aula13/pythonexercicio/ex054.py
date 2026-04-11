from datetime import date
ano_atual = date.today().year
idade = 0
cont0 = 0
cont1 = 0
for c in range(1, 8):
    ano_nasc = int(input(f'A {c}º pessoa nasceu em que ano? '))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        cont0 += 1
    if idade < 21:
        cont1 += 1
if cont0 == 1:
    print(f'Ao todo {cont0} pessoa já atingiu a maior idade,\nenquanto {cont1} pessoas são menores de idade.')
elif cont1 == 1:
    print(f'Ao todo {cont0} pessoas já atingiram a maior idade,\nenquanto {cont1} pessoa é menor de idade.')
else:
    print(f'Ao todo {cont0} pessoas já atingiram a maior idade,\nenquanto {cont1} pessoas são menores de idade.')
