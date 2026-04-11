from random import randint
from time import sleep
# Tabela de Cores
VERMELHO = '\033[1;31m'
VERDE    = '\033[1;32m'
AMARELO  = '\033[1;33m'
AZUL     = '\033[1;34m'
ROXO     = '\033[1;35m'
RESET    = '\033[0m'
NEGRITO  = '\033[1m'

maquina = randint(0,5) #FAZ O COMPUTADOR VAI "PENSAR"
print(f'{AMARELO}-=-{RESET}'*18)
print(f'{AZUL}Tente adivinhar qual número irei pensar de 0 á 5...{RESET}')
print(f'{AMARELO}-=-{RESET}'*18)
jogador = int(input(f'{NEGRITO}Adivinhe o número que escolhi: {RESET}')) #O JOGADOR VAI TENTAR ADIVINHAR
print(f'{ROXO}PROCESSANDO...{RESET}')
sleep(3)
if maquina == jogador:
    print(f'{VERDE}Uau, você usou telepatia? Pensamos no mesmo número! Pensei', end=' ')
    print(f'{VERDE}no {maquina} e você também! PARABÉNS!{RESET}')
else:
    print(f'{VERMELHO}Você ERROU, eu pensei no {maquina} e você no {jogador}! LOSER!{RESET}')
