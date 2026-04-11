v1 = int(input('Digite o primeiro valor: '))
v2 = int(input('Digite o segundo valor: '))
v3 = int(input('Digite o terceiro valor: '))
if v1 >= v2 and v1 >= v3:
    print('O MAIOR número digitado foi o {}.'.format(v1))
else:
    if v2 >= v1 and v2 >= v3:
        print('O MAIOR número digitado foi o {}.'.format(v2))
    else:
        if v3 >= v1 and v3 >= v2:
            print('O MAIOR número digitado foi o {}.'.format(v3))
if v1 <= v2 and v1 <= v3:
    print('O MENOR número digitado foi o {}.'.format(v1))
else:
    if v2 <= v1 and v2 <=3:
        print('O MENOR número digitado foi o {}.'.format(v2))
    else:
        if v3 <= v1 and v3 <= v2:
            print('O MENOR número digitado foi o {}.'.format(v3))
