list_number = [[], []]
for count in range(0, 7):
    number = int(input(f"Digite o {count+1}ª valor: "))
    if number % 2 == 0:
        list_number[0].append(number)
    if number % 2 == 1:
        list_number[1].append(number)
print("─" * 30)
list_number[0].sort()
list_number[1].sort()
print(f"A lista de números pares em ordem são: {list_number[0]}")
print(f"A lista de números ímpares em ordem são: {list_number[1]}")
