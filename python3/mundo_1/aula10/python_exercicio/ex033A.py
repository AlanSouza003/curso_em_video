# Modo simplificado do exercicio.
v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
menor = v1
if v2<=v1 and v2 <= v3:
    menor = v2
if v3 <= v1 and v3 <= v2:
    menor = v3
print('O MENOR número digitado foi o {}.'.format(menor))
maior = v1
if v2 >= v1 and v2 >= v3:
    maior = v2
if v3 >= v1 and v3 >= v2:
    maior = v3
print('O MAIOR número digitado foi o {}.'.format(maior))