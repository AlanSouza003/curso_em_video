# co = float(input('Comprimento do cateto oposto: '))
# ca = float(input('Comprimento do cateto adjacente: '))
# sc = (ca ** 2) + (co ** 2)
# hip = sc**(1/2) pode ser também com o comando import sqrt mais simples
# print('A hipotenusa vai medir {:.2f}'.format(hip))

# FORMATO SIMPLIFICADO

from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = hypot(ca, co)
print('A hipotenusa vai medir {:.2f}'.format(hip))