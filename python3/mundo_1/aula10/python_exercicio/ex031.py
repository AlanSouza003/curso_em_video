from random import randint
from time import sleep
# Tabela de cores
VERMELHO_CLARO  = '\033[1;91m'
VERDE_CLARO     = '\033[1;92m'
AMARELO_CLARO   = '\033[1;93m'
AZUL_CLARO      = '\033[1;94m'
ROXO_CLARO      = '\033[1;95m'
CIANO_CLARO     = '\033[1;96m'
BRANCO_BRILHO   = '\033[1;97m'
RESET           = '\033[0m'
onibus = 90
ori = input(f'{BRANCO_BRILHO}Digite sua origem: {RESET}')
dest = input(f'{BRANCO_BRILHO}Digite o seu destino: {RESET}')
print(f'{AMARELO_CLARO}{'Sua origem é {} e seu destino é {}!'.format(ori, dest).upper()}{RESET}')
print(f'{CIANO_CLARO}-=-{RESET}'*10)
resp = input('CONFIRME SUA VIAGEM COM [S/N]: ').upper().strip()
print(f'{CIANO_CLARO}-=-{RESET}'*10)
if resp == 'S':
    hora = randint(1,48)
    km = onibus * hora
    print(f'{ROXO_CLARO}PROCESSANDO SUA PASSAGEM...{RESET}')
    sleep(3)
    if km <= 200:
        valor = km * 0.50
    else:
        valor = km * 0.45
    print(f'{VERDE_CLARO}{'Ótimo! Sua viagem foi confirmada! Levará {}h'.format(hora).upper()}{RESET}',end=' ')
    print(f'{VERDE_CLARO}{'com percurso de {}km.'.format(km).upper()}{RESET}')
    print(f'{VERDE_CLARO}{'A passagem custará R${:.2f}!'.format(valor).upper()}{RESET}')
else:
    print(f'{VERMELHO_CLARO}VIAGEM CANCELADA.\nVOLTANDO AO MENU...{RESET}')
print(f'{CIANO_CLARO}-=-{RESET}'*10)