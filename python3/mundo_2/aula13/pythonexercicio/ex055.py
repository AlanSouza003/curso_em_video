maior_peso = 0
menor_peso = 0
for c in range(1, 6):
    peso = float(input(f'Qual o {c}º peso? kg'))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
        if peso < menor_peso:
            menor_peso = peso
print(
    f'O maior peso lido foi o {maior_peso}Kg.\nEnquanto o menor peso lido foi o {menor_peso}Kg.'
)
