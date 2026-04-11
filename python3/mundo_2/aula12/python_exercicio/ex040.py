cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m', 'verde':'\033[1;92m',
       'amarelo':'\033[1;93m','branco':'\033[1;97m'}
n1 = float(input(f'{cor['branco']}Primeira nota: {cor['limpa']}'))
n2 = float(input(f'{cor['branco']}Segunda nota: {cor['limpa']}'))
m = (n1 + n2) / 2
if m >= 7.0:
    print(f'{cor['branco']}A média foi {m}{cor['limpa']}\n{cor['verde']}APROVADO!{cor['limpa']}')
elif m >= 5.0 or m == 6.9:
    print(f'{cor['branco']}A média foi {m}{cor['limpa']}\n{cor['amarelo']}EM RECUPERAÇÃO!{cor['limpa']}')
else:
    print(f'{cor['branco']}A média foi {m}{cor['limpa']}\n{cor['vermelho']}REPROVADO!{cor['limpa']}')