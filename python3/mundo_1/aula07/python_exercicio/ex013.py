sal = float(input('Qual o salário do funcionário? R$'))
novsal = sal + (15/100*sal)
print('O antigo salário do funcionário de R${:.2f},'.format(sal), end=' ')
print('passa a ser R${:.2f}!'.format(novsal))
