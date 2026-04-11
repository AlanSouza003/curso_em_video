# Tabela de cores
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m','amarelo':'\033[1;93m',
       'branco':'\033[1;97m', 'verde':'\033[1;92m'}
# Variáveis de controle
s = 0
cont = 0
# Pedindo ao usuário para digitar um número
n = int(input(f'{cor['branco']}Digite um número: {cor['limpa']}'))
# Estrutura de repetição para realizar a contagem e a soma para saber se é um número primo.
for c in range(1, n + 1):
    s = n % c # Calculando a variável 'n' com a variável 'c'
    # Estrutura condicional composta para saber se o número é primo pela contagem de zeros.
    if s == 0:
        cont += 1
        c = f'{cor['amarelo']}{c}{cor['limpa']}' # Colorindo os números divisíveis com a cor amarelo.
    elif s != 0:
        c = f'{cor['vermelho']}{c}{cor['limpa']}' # Colorindo os números que não são divisíveis com a cor vermelho.
    print(c, end=' ') # Mostrando na tela a contagem
print(f'\n{cor['branco']}O NÚMERO {n} FOI DIVISÍVEL {cont} VEZES\nPOR ISSO ELE{cor['limpa']}', end=' ')
# Estrutura condicional composta para mostrar na tela se ele é primo ou não
if cont == 2:
    print(f'{cor['verde']}É PRIMO{cor['limpa']}{cor['branco']}!{cor['limpa']}')
else:
    print(f'{cor['vermelho']}NÃO É PRIMO{cor['limpa']}{cor['branco']}!{cor['limpa']}')
