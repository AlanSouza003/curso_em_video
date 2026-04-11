from random import randint
from time import sleep
# Tabela de cores
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m','verde':'\033[1;92m',
       'amarelo':'\033[1;93m', 'branco':'\033[1;97m', 'ciano':'\033[1;96m',
       'roxo':'\033[1;95m'}
# Titulo
print(f'{cor['ciano']}={cor['limpa']}' * 30)
print(f'{cor['branco']}{'PEDRA🪨, PAPEL📃':^28}{cor['limpa']}')
print(f'{cor['branco']}{'E TESOURA✂️':^30}{cor['limpa']}')
print(f'{cor['ciano']}={cor['limpa']}' * 30)
# Pedido para o usuário escolher a opção desejada
jogador = int(input(f'''{cor['roxo']}Você escolhe:
{cor['verde']}[ 0 ]{cor['limpa']} {cor['branco']}PEDRA{cor['limpa']}
{cor['verde']}[ 1 ]{cor['limpa']} {cor['branco']}PAPEL{cor['limpa']}
{cor['verde']}[ 2 ]{cor['limpa']} {cor['branco']}TESOURA{cor['limpa']}
{cor['roxo']}Digite sua jogada:{cor['limpa']} '''))
# O jogo so vai ser rodado se a jogada igualar a estrutura condicional composta
if jogador == 0 or jogador == 1 or jogador == 2:
       print(f'{cor['amarelo']}JO{cor['limpa']}')
       sleep(1)
       print(f'{cor['ciano']}KEN{cor['limpa']}')
       sleep(1)
       print(f'{cor['roxo']}PÔ{cor['limpa']}{cor['branco']}!!{cor['limpa']}')
       # Escolhendo a opção da máquina
       game = ['PEDRA', 'PAPEL', 'TESOURA']
       maquina = randint(0, 2)
       print(f'{cor['ciano']}-={cor['limpa']}' * 15)
       print(f'{cor['branco']}A Máquina jogou:{cor['limpa']} '
             f'{cor['vermelho']}{game[maquina]}{cor['limpa']}')
       print(f'{cor['branco']}O Jogador jogou:{cor['limpa']} '
             f'{cor['verde']}{game[jogador]}{cor['limpa']}')
       print(f'{cor['ciano']}-={cor['limpa']}' * 15)
       # Estrutura condicional para mostrar na tela quem ganhou o game.
       if jogador == 0 and maquina == 1:
           print(f'{cor['vermelho']}A MÁQUINA VENCEU!{cor['limpa']}')
       elif jogador == 0 and maquina == 2 :
           print(f'{cor['verde']}O JOGADOR VENCEU!{cor['limpa']}')
       elif jogador == 1 and maquina == 2:
           print(f'{cor['vermelho']}A MÁQUINA VENCEU!{cor['limpa']}')
       elif jogador == 1 and maquina == 0:
           print(f'{cor['verde']}O JOGADOR VENCEU!{cor['limpa']}')
       elif jogador == 2 and maquina == 0:
           print(f'{cor['vermelho']}A MÁQUINA VENCEU!{cor['limpa']}')
       elif jogador == 2 and maquina == 1:
           print(f'{cor['verde']}O JOGADOR VENCEU!{cor['limpa']}')
       else:
           print(f'{cor['amarelo']}EMPATE. JOGUEM DE NOVO!{cor['limpa']}')
else:
       print(f'{cor['vermelho']}JOGADA INVALIDA! TENTE NOVAMENTE.{cor['limpa']}')
