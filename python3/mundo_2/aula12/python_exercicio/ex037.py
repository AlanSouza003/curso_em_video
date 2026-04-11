from time import sleep
# Tabela de cores
cor = {'limpa':'\033[0m', 'ciano':'\033[1;96m', 'branco':'\033[1;97m',
       'roxo':'\033[1;95m', 'vermelho':'\033[1;91m'}
# Titulo
print(f'{cor['branco']}-={cor['limpa']}'*15)
print(f'{cor['ciano']}{'BASE NUMÉRICA':^30}{cor['limpa']}')
print(f'{cor['branco']}-={cor['limpa']}'*15)
# Pedindo para o usuário digitar um número inteiro.
valor = int(input(f'{cor['roxo']}Digite um valor inteiro: {cor['limpa']}'))
# Pedindo para o usuário escolhe a opção de conversão.
print(f'{cor['branco']}-{cor['limpa']}'*25)
print(f'{cor['branco']}DESEJA CONVERTER PARA:{cor['limpa']}')
print(f'{cor['ciano']}[1] BINÁRIO{cor['limpa']}')
print(f'{cor['ciano']}[2] OCTAL{cor['limpa']}')
print(f'{cor['ciano']}[3] HEXADECIMAL{cor['limpa']}\n{cor['branco']}{'-'*25}{cor['limpa']}')
escolha = int(input(f'{cor['roxo']}Escolha umas das opções acima: {cor['limpa']}'))
print(f'{cor['branco']}PROCESSANDO...{cor['limpa']}')
sleep(3)
# Estrutura de condição aninhada para a escolha da conversão desejada pelo usuário.
print(f'{cor['branco']}-{cor['limpa']}'*24)
print(f'{cor['branco']}{'RESULTADO':^24}{cor['limpa']}')
print(f'{cor['branco']}-{cor['limpa']}'*24)
if escolha == 1:
    print(f'{cor['branco']}O VALOR {valor} CONVERTIDO PARA{cor['limpa']} {cor['ciano']}BINÁRIO{cor['limpa']} '
          f'{cor['branco']}É {bin(valor)[2:]}{cor['limpa']}.')
elif escolha == 2:
    print(f'{cor['branco']}O VALOR {valor} CONVERTIDO PARA{cor['limpa']} {cor['ciano']}OCTAL{cor['limpa']} '
          f'{cor['branco']}É {oct(valor)[2:]}{cor['limpa']}.')
elif escolha == 3:
    print(f'{cor['branco']}O VALOR {valor} CONVERTIDO PARA{cor['limpa']}{cor['ciano']}HEXADECIMAL{cor['limpa']} '
          f'{cor['branco']}É {hex(valor)[2:]}{cor['limpa']}.')
else:
    print(f'{cor['vermelho']}A OPÇÃO {cor['limpa']}{cor['branco']}{escolha}{cor['limpa']} '
          f'{cor['vermelho']}NÃO EXISTE. TENTE NOVAMENTE.{cor['limpa']}')