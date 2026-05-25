print('='*20)
print(f'{"TABUADA":^20}')
print('='*20)

while True:

    n = int(input('Deseja ver a tabuada de qual valor: '))

    if n < 0:
        break

    c = 1
    while c <= 10:

        print(f'{n} x {c:>2} = {n * c:>2}')
        c += 1

print('PROGRAMAM FINALIZADO!')
