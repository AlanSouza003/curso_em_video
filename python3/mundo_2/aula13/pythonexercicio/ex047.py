from time import sleep
print('NÚMEROS PARES')
for cont in range(2, 51, 2):
    print(f'{cont} |'.replace('50 |', '50'), end=' ')
    sleep(1)
