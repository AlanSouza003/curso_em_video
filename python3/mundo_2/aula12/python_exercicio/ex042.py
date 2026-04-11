# Tabela de cores
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m','verde':'\033[1;92m',
       'amarelo':'\033[1;93m', 'azul':'\033[1;94m','branco':'\033[1;97m'}
# Titulo
print(f'{cor['azul']}-={cor['limpa']}' * 20)
print(f'{cor['amarelo']}{'ANALISADOR DE TRIÂNGULO V2.0':^40}{cor['limpa']}')
print(f'{cor['azul']}-={cor['limpa']}' * 20)
# Lendo as medidas do triângulo.
m1 = float(input(f'{cor['branco']}Primeira medida: {cor['limpa']}'))
m2 = float(input(f'{cor['branco']}Segunda medida: {cor['limpa']}'))
m3 = float(input(f'{cor['branco']}Terceira medida: {cor['limpa']}'))
# Se formar um triângulo
if m2 + m3 > m1 and m1 + m3 > m2 and m1 + m2 > m3:
    print(f'{cor['branco']}As médidas acima{cor['limpa']} '
          f'{cor['verde']}PODEM FORMAR{cor['limpa']} {cor['branco']}um triângulo!{cor['limpa']}')
    print(f'{cor['branco']}TIPO DO TRIÂNGULO: {cor['limpa']}', end='')
    # Tipos de triângulos
    if m1 == m2 == m3:
        print(f'{cor['verde']}EQUILÁTERO{cor['limpa']}')
    elif m1 == m2 or m2 == m3 or m3 == m1:
        print(f'{cor['verde']}ISÓSCELES{cor['limpa']}')
    elif m1 != m2 != m3 != m1:
        print(f'{cor['verde']}ESCALENO{cor['limpa']}')
#  Se não formar um triângulo
else:
    print(f'{cor['branco']}As médidas acima{cor['limpa']} '
          f'{cor['vermelho']}NÃO PODEM FORMAR{cor['limpa']} {cor['branco']}um triângulo!{cor['limpa']}')