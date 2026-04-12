from math import factorial

#  1º versão com a estrutura While.
print('========== CALCULO FATORIAL ==========')
n = int(input('Digite um número: '))
fat = factorial(n)
print(f'Calculando {n}! =', end=' ')
while n > 0:
    print(f'{n} x'.replace('1 x', '1'), end=' ')
    n -= 1
print(f'= {fat}')

# 2º versão com a estrutura For
""" print('========== CALCULO FATORIAL ==========')
n = int(input('Digite um número: '))
fat = factorial(n)
print(f'Calculando {n}! =', end=' ')
for c in range(n, 0, -1):
    print(f'{c} x'.replace('1 x', '1'), end=' ')
print(f'= {fat}')  """  