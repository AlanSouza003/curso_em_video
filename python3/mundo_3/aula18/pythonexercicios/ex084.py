list_people = list()
data = list()
greater_weight = lower_weight = 0
while True:
    data.append(
        str(input("Nome: "))
    )
    data.append(
        float(input("Peso: "))
    )
    if len(list_people) == 0:
        greater_weight = lower_weight = data[1]
    else:
        if data[1] > greater_weight:
            greater_weight = data[1]
        if data[1] < lower_weight:
            lower_weight = data[1]
    list_people.append(data[:])
    data.clear()
    more_one = str(input("Deseja continuar? [S/n]")).strip().lower()
    if more_one in ['não', 'nao', 'n']:
        break
print("─" * 30)
print(f"Foram cadastradas um total de {len(list_people)} pessoas.")
print(f"O maior peso foi {greater_weight}kg, pertencente a: ", end='')
for people in list_people:
    if people[1] == greater_weight:
        print(f'[{people[0]}]', end=' ')
print(f"\nO menor peso foi {lower_weight}kg, pertencente a: ", end='')
for people in list_people:
    if people[1] == lower_weight:
        print(f"[{people[0]}]", end=' ')
print()