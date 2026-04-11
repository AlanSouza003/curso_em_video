num = int(input('Me de um valor: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('ANALISANDO O VALOR...')
print('-'*20)
print('A unidade é: {}'.format(u).upper())
print('A dezena é: {}'.format(d).upper())
print('A centena é: {}'.format(c).upper())
print('O milhar é: {}'.format(m).upper())
