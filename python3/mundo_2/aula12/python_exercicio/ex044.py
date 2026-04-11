# Tabela de cores
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m','verde':'\033[1;92m',
       'amarelo':'\033[1;93m', 'branco':'\033[1;97m', 'ciano':'\033[1;96m'}
# Titulo
print(f'{cor['ciano']}========== LOJAS SOUZA =========={cor['limpa']}')
# Lendo o valor e a escolha de pagamento do usuário
valor = float(input(f'{cor['branco']}Digite o valor do produto: R${cor['limpa']}'))
escolha = int(input(f'''{cor['amarelo']}Escolha a forma de pagamento:{cor['limpa']}
{cor['verde']}[ 1 ]{cor['limpa']} {cor['branco']}Á vista/cheque{cor['limpa']}
{cor['verde']}[ 2 ]{cor['limpa']} {cor['branco']}Á vista no cartão{cor['limpa']}
{cor['verde']}[ 3 ]{cor['limpa']} {cor['branco']}No cartão parcelado em 2x{cor['limpa']}
{cor['verde']}[ 4 ]{cor['limpa']} {cor['branco']}No cartão parcelado 3x ou mais.{cor['limpa']}
{cor['amarelo']}Digite a forma: {cor['limpa']}'''))
# Estrutura condicional para mostra na tela a forma de pagamento
# do usuário conforme a escolha de pagamento.
if escolha == 1:
    pag = valor - (valor * 10 / 100)
    print(f'{cor['branco']}Sua compra é de R${valor:.2f}\ne com desconto de 10% fica por R${pag:.2f}{cor['limpa']}')
elif escolha == 2:
    pag = valor - (valor * 5 / 100)
    print(f'{cor['branco']}Sua compra é de R${valor:.2f}\ne com desconto de 5% fica por R${pag:.2f}{cor['limpa']}')
elif escolha == 3:
    pag = valor / 2
    print(f'{cor['branco']}Sua compra é de R${valor:.2f}\ndividido em 2x R${pag:.2f}{cor['limpa']}')
elif escolha == 4:
    quant = int(input(f'{cor['branco']}Quantas vezes: {cor['limpa']}'))
    pag = valor + (valor * 20 / 100)
    parc_total = pag / quant
    print(f'{cor['branco']}Sua compra é de R${valor:.2f} dividio em {quant}x de R${parc_total} '
          f'com juros.{cor['limpa']}\n'
          f'{cor['branco']}Então sua compra que era R${valor:.2f} passa a ser R${pag:.2f}, no total.{cor['limpa']}')
else:
    print(f'{cor['vermelho']}Opção {escolha} INVALIDA! Tente novamente.{cor['limpa']}')
    print(f'{cor['branco']}Sua compra que era R${valor:.2f} continua sendo R${valor:.2f}{cor['branco']}')
