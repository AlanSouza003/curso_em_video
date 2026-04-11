# Lendo o valor para realizar a tabuada
n = int(input('Digite um número: '))
print('-' * 20)
print(f'{f'TABUADA DO {n}':^20}')
print('-' * 20)
# Laço para realização da tabuada
for t in range(1, 11):
    print('|{:>2} x {:>2} = {:>2}|'.format(n, t, n*t))
