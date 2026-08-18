import os
peoples = {}
peoples_data = []
average = 0
while True:
    peoples['nome'] = str(input("Nome: "))
    while True:
        peoples['sexo'] = str(input("Sexo: [M/F]")).upper()
        if peoples['sexo'] in ['M', 'F']:
            break
        print('Erro! Digite apenas "M" ou "F".')
    peoples['idade'] = int(input("Idade: "))
    peoples_data.append(peoples.copy())
    while True:
        more_one = str(input("Deseja cadastrar mais uma pessoa? [S/n]")).upper()
        if more_one in ['S', 'SIM', 'NÃO', 'N']:
            break
        print('Erro! Digite apenas "Sim" ou "Não". E se quiser abreviar "S" ou "N"')
    if more_one not in ['SIM', 'S']:
        break
print('─' * 50)
print(f" => O grupo tem {len(peoples_data)} pessoas cadastradas.")
for age in peoples_data:
    average += age['idade'] / len(peoples_data)
print(f" => A média de idade do grupo é de: {average:.2f} anos.")
print(f" => As mulheres do grupo são: ", end='')
for sex in peoples_data:
    if sex['sexo'] == 'F':
        print(f"{sex['nome']}", end=' ')
print("\n => Lista de pessoas acima da média:")
for above_average in peoples_data:
    print()
    for k, v in above_average.items():
        if above_average['idade'] > average:
            print(f"   {k} = {v};", end=' ')
print('─' * 50)
print("<< PROGRAMA ENCERRADO >>")
