from time import sleep
print('CONTAGEM REGRESSIVA EM', end='')
for c in range(3):
    print('.', end='')
    sleep(1)
for c in range(10, 0, -1):
    print(f'\n{c}'.replace(' ', ''), end='')
    sleep(1)
print('\nFELIZ ANO NOVOOOOO!🎉🎉🥳🥳')