people = list()
data = list()
for count in range(0, 3):
    data.append(
        str(input("Digite seu nome: "))
    )
    data.append(
        int(input("Digite sua idade: "))
    )
    people.append(data[:])
    data.clear()

print(people)