# Tabela de cores
cor = {'limpa':'\033[0m', 'roxo':'\033[1;95m', 'branco':'\033[1;97m',
       'vermelho':'\033[1;91m', 'azul':'\033[1;94m', 'verde':'\033[1;92m',
       'ciano':'\033[1;96m'}
# Titulo
print(f'{cor['branco']}-={cor['limpa']}'*20)
print(f'{cor['azul']}{'MAIOR OU IGUAL QUE':^38}{cor['limpa']}')
print(f'{cor['branco']}-={cor['limpa']}'*20)
# Pedindo para o usuário escolher dois números.
n1 = int(input(f'{cor['roxo']}Escolha um número: {cor['limpa']}'))
n2 = int(input(f'{cor['roxo']}Escolha outro número: {cor['limpa']}'))
print(f'{cor['branco']}-{cor['limpa']}'*25)
print(f'{cor['branco']}{'RESULTADO':^25}{cor['limpa']}')
print(f'{cor['branco']}-{cor['limpa']}'*25)
# Estrutura de condição aninhada para saber qual numero é maior ou igual que.
if n1 > n2:
    print(f'{cor['verde']}O PRIMEIRO valor é maior.{cor['limpa']}')
    print(f'{cor['branco']}Pois {n1} é {cor['limpa']}{cor['verde']}MAIOR{cor['limpa']} '
          f'{cor['branco']}que {n2}.{cor['limpa']}')
elif n2 > n1:
    print(f'{cor['verde']}O SEGUNDO valor é maior.{cor['limpa']}')
    print(f'{cor['branco']}Pois {n2} é {cor['limpa']}{cor['verde']}MAIOR{cor['limpa']} '
          f'{cor['branco']}que {n1}.{cor['limpa']}')
else:
    print(f'{cor['vermelho']}NÃO EXISTE UM VALOR MAIOR.{cor['limpa']}')
    print(f'{cor['branco']}Pois {n1} é {cor['limpa']}{cor['ciano']}IGUAL{cor['limpa']} '
          f'{cor['branco']}á {n2}.{cor['limpa']}')
