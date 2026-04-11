dias = int(input('Quantos dias? '))
km = float(input('Quantos quilometros rodados? '))
total = (dias * 60) + (km * 0.15)
print('O valor total do aluguel a ser pago é R${:.2f}!'.format(total))
