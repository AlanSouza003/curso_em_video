list_number = list()
for c in range(0, 5):
    number = int(input(f"Digite o {c+1}ª valor: "))
    if c == 0 or number > list_number[-1]:
        list_number.append(number)
        print("Valor inserido ao final da lista...")
    else:
        pos = 0
        while pos < len(list_number):
            if number <= list_number[pos]:
                list_number.insert(pos, number)
                print(f"Valor inserido na posição {pos} da lista...")
                break
            pos += 1
                
print(f"Os valores digitados em ordem foram: {list_number}")