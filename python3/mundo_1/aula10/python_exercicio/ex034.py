# Modúlos
from time import sleep
# Tabela de cores
VERMELHO_CLARO  = '\033[1;91m'
VERDE_CLARO     = '\033[1;92m'
AMARELO_CLARO   = '\033[1;93m'
ROXO_CLARO      = '\033[1;95m'
RESET           = '\033[0m'
sal = float(input(f'{AMARELO_CLARO}{'Qual o seu atual do funcionário?'.upper()}{RESET} R$'))
print(f'{ROXO_CLARO}PROCESSANDO...{RESET}')
sleep(3)
# Calculo de 10% de aumento.
if sal >= 1250.00:
    nsal = sal + (sal * 10) / 100
    print(f'{VERMELHO_CLARO}{'O antigo salário era R${} reais.'.upper().format(sal)}{RESET}')
    print(f'{VERDE_CLARO}{'Com ajuste de 10% passou a ser R${} reais!'.upper().format(nsal)}{RESET}')
# Calculo de 15% de aumento.
else:
    nsal = sal + (sal * 15) / 100
    print(f'{VERMELHO_CLARO}{'O antigo salário era R${} reais.'.upper().format(sal)}{RESET}')
    print(f'{VERDE_CLARO}{'Com ajuste de 15% passou a ser R${} reais!'.upper().format(nsal)}{RESET}')