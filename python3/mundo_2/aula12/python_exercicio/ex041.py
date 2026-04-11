from datetime import date
ano_atual = date.today().year
cor = {'limpa':'\033[0m', 'verde':'\033[1;92m', 'branco':'\033[1;97m'}
nasc = int(input(f'{cor['branco']}Ano de nascimento: {cor['limpa']}'))
idade = ano_atual - nasc
print(f'{cor['branco']}O atleta tem {idade} anos.{cor['limpa']}')
print(f'{cor['branco']}CLASSIFICAÇÃO: {cor['limpa']}', end='')
if idade <= 9:
    print(f'{cor['verde']}MIRIM.{cor['limpa']}')
elif idade <= 14:
    print(f'{cor['verde']}INFANTIL.{cor['limpa']}')
elif idade <= 19:
    print(f'{cor['verde']}JUNIOR.{cor['limpa']}')
elif idade <= 25:
    print(f'{cor['verde']}SENIOR.{cor['limpa']}')
else:
    print(f'{cor['verde']}MASTER.{cor['limpa']}')
