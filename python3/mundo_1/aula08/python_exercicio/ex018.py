from math import radians, sin, cos, tan

ang = float(input('Informe um ângulo: '))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {:.2f} tem o Seno de: {:.2f}!'.format(ang, seno))
print('O ângulo de {:.2f} tem o Cosseno de: {:.2f}!'.format(ang, coss))
print('O ângulo de {:.2f} tem o Tangente de {:.2f}'.format(ang, tang))
