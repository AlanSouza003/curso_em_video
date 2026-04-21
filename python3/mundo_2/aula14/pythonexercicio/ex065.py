# Variaveis de Controle
resp = 'S'
c = s = 0
posi = neg = 0

""" Estrutura de repetição para ler os valores do usuário e calcular o maior
e menor valor, a soma total e a média dos valores digitados. """
while resp not in ['N', 'NÃO']:

    
    n = int(input(f'\033[1;97mDigite o {c + 1}º valor: \033[0m'))

    if c == 0:
        maior = menor = n

    else:

        if n > maior:
            maior = n
        if n < menor:
            menor = n

        if n > 0:
            posi += 1

        if n < 0:
            neg += 1
    s += n
    c += 1
    resp = str(input('\033[1;97mDeseja continuar [S/N]? \033[0m')).upper().strip()
    if resp not in ['S', 'SIM'] and resp not in ['N', 'NÃO']:
        s -= n
        c -= 1
        print('\033[1;91mOpção invalida! Tente novamente.\033[0m\n')

media = s / c

print(f'\n\033[1;97mVocê digitou \033[0m', end='')
if s < 0:

    if neg == 1 and posi == 1:
        print(f'\033[1;91m{neg} número negativo\033[0m \033[1;97me\033[0m ' 
              f'\033[1;92m{posi} número positivo.\033[0m')

    elif neg == 1:
        print(f'\033[1;91m{neg} número negativo\033[0m \033[1;97me\033[0m ' 
              f'\033[1;92m{posi} números positivos.\033[0m')

    elif posi == 1:
        print(f'\033[1;91m{neg} números negativos\033[0m \033[1;97me\033[0m ' 
              f'\033[1;92m{posi} número positivo.\033[0m')

    else:
        print(f'\033[1;91m{neg} números negativos\033[0m \033[1;97me\033[0m ' 
              f'\033[1;92m{posi} números positivos.\033[0m')

if s > 0:

    if posi == 1 and neg == 1:
        print(f'\033[1;92m{posi} número positivo\033[0m \033[1;97me\033[0m ' 
              f'\033[1;91m{neg} número negativo.\033[0m')

    elif posi == 1:
        print(f'\033[1;92m{posi} número positivo\033[0m \033[1;97me\033[0m ' 
              f'\033[1;91m{neg} números negativos.\033[0m')

    elif neg == 1:
        print(f'\033[1;92m{posi} números positivos\033[0m \033[1;97me\033[0m ' 
              f'\033[1;91m{neg} número negativo.\033[0m')

    else:
        print(f'\033[1;92m{posi} números positivos\033[0m \033[1;97me\033[0m ' 
              f'\033[1;91m{neg} números negativos.\033[0m')
        
if maior < 0 and menor < 0:
    print(f'\033[1;97mEntre esses números o maior foi o \033[1;91m{maior}\033[0m \033[1;97me menor foi\033[0m ' 
          f'\033[1;91m{menor}.\033[0m')
    
elif maior > 0 and menor > 0:
    print(f'\033[1;97mEntre esses números o maior foi o \033[1;92m{maior}\033[0m \033[1;97me menor foi\033[0m ' 
          f'\033[1;92m{menor}.\033[0m')
    
else:
    print(f'\033[1;97mEntre esses números o maior foi o \033[1;92m{maior}\033[0m \033[1;97me menor foi\033[0m ' 
          f'\033[1;91m{menor}.\033[0m')

if media > 0:
    print(f'\033[1;97mA média do total de números digitados foi\033[0m '
          f'\033[1;92m{media:.2f}\033[0m.')
    
else:
    print(f'\033[1;97mA média do total de números digitados foi\033[0m '
          f'\033[1;91m{media:.2f}\033[0m.')
    