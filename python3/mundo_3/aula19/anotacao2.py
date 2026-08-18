'''brazil = []
state1 = {'uf':'Bahia', 'sigla':'BA'}
state2 = {'uf':'Sergipe', 'sigla':'SE'}
brazil.append([state1])
brazil.append([state2])
print(brazil[0])'''

brazil = []
state = {}

for c in range(0, 3):
    state['uf'] = str(input("Unidade Federativa: "))
    state['sigla'] = str(input("Sigla do Estado: "))
    brazil.append(state.copy())
print(brazil)
for s in brazil:
    for k, v in s.items():
        print(f'O campo {k} tem o valor {v}.')