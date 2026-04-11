from time import sleep
# Tabela de cores
cor = {'limpa':'\033[m','amarelo':'\033[1;93m',
        'roxo':'\033[1;95m', 'vermelho':'\033[1;91m',
         'branco':'\033[1;97m', 'verde':'\033[1;92m',
          'invertido':'\033[7;1;30;46m'}
# Inicio do programa.
emp = 'EMPRÉSTIMO CONSIGNADO'
design = '-=' * 13
print(f'{cor['invertido']}{design}{cor['limpa']}')
print(f'{cor['invertido']}{'{:^26}'.format(emp)}{cor['limpa']}')
print(f'{cor['invertido']}{design}{cor['limpa']}')
casa = float(input(f'{cor['amarelo']}QUAL O VALOR DA CASA?{cor['limpa']} R$'))
sal = float(input(f'{cor['amarelo']}VALOR DO SALÁRIO?{cor['limpa']} R$'))
anos = float(input(f'{cor['amarelo']}EM QUANTOS ANOS?{cor['limpa']} '))
print(f'{cor['roxo']}PROCESSANDO...{cor['limpa']}')
sleep(3)
# Calculo das parcelas
parc = 12 * anos
prest_mens = casa / parc
# Formatação para "." ficar em milhar e a "," em decimal.
casa_format  = f'R${casa:,.2f}'.replace('.', 'X').replace(',', '.').replace('X', ',')
prest_format = f'R${prest_mens:,.2f}'.replace('.', 'X').replace(',', '.').replace('X', ',')
parc_format  = f'{parc:.0f}x'
print(f'{cor['branco']}O VALOR DO EMPRÉSTIMO DE {casa_format}\nPARCELADO EM {parc_format} DE '
      f'{prest_format} FOI{cor['limpa']}',end=' ')
# As condições compostas.
if prest_mens <= (30 / 100 * sal):
    print(f'{cor['verde']}APROVADO{cor['limpa']}{cor['branco']}!{cor['limpa']}')
else:
    print(f'{cor['vermelho']}NEGADO{cor['limpa']}{cor['branco']}.{cor['limpa']}')
