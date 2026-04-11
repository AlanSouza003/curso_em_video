# Criando um laço de repetição para somar números pares
s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        s += n
        cont += 1
if cont == 1:
    print(f'A soma total de {cont} valor par é {s}')
else:
    print(f'A soma total dos {cont} valores pares é {s}')