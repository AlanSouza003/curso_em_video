test = list()
test.append('Alan')
test.append(23)
people = list()
people.append(test[:])
test[0] = 'Claudia'
test[1] = 45
people.append(test[:])
for p in people:
    print(f"{p[0]} tem {p[1]} anos de idade.")