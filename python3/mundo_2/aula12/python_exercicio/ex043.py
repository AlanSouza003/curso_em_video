# Tabela de cores
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m','verde':'\033[1;92m',
       'amarelo':'\033[1;93m', 'branco':'\033[1;97m'}
# Lendo altura e o peso do usuário
peso = float(input(f'{cor['branco']}Seu peso: {cor['limpa']}'))
altura = float(input(f'{cor['branco']}Sua altura: {cor['limpa']}'))
# Calculando a massa corpórea.
imc = peso / (altura ** 2)
# Mostrando na tela o resultado
print(f'{cor['branco']}O seu IMC é de {cor['limpa']}', end='')
# Estrutura condicional para mostra a classificação do imc do usuário
if imc < 18.5:
    print(f'{cor['amarelo']}{imc:.1f}{cor['limpa']}{cor['branco']}!{cor['limpa']}')
    print(f'{cor['amarelo']}Opaa! Você está {cor['limpa']}', end='')
    print(f'{cor['amarelo']}ABAIXO DO PESO! Precisa ganhar massa.{cor['limpa']}')
elif imc <= 25.5:
    print(f'{cor['verde']}{imc:.1f}{cor['limpa']}{cor['branco']}!{cor['limpa']}')
    print(f'{cor['verde']}Obaa! Você está  no {cor['limpa']}', end='')
    print(f'{cor['verde']}PESO IDEAL! Continue assim.{cor['limpa']}')
elif imc <= 30.5:
    print(f'{cor['amarelo']}{imc:.1f}{cor['limpa']}{cor['branco']}!{cor['limpa']}')
    print(f'{cor['amarelo']}EPAA! Você está no {cor['limpa']}', end='')
    print(f'{cor['amarelo']}SOBREPESO! Fique de olho.{cor['limpa']}')
elif imc <= 40.5:
    print(f'{cor['vermelho']}{imc:.1f}{cor['limpa']}{cor['branco']}!{cor['limpa']}')
    print(f'{cor['vermelho']}STOP! Você está na {cor['limpa']}', end='')
    print(f'{cor['vermelho']}OBESIDADE! CUIDADO{cor['limpa']}.')
else:
    print(f'{cor['vermelho']}{imc:.1f}{cor['limpa']}{cor['branco']}!{cor['limpa']}')
    print(f'{cor['vermelho']}ALERTA VERMELHO! Você está na {cor['limpa']}', end='')
    print(f'{cor['vermelho']}OBESIDADE MÓRBIDA!\nPROCURAR UM MÉDICO URGENTE.{cor['limpa']}')
