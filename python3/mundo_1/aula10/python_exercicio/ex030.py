from time import sleep
#Tabela de cores
VERMELHO_CLARO = '\033[1;91m'
AMARELO_CLARO  = '\033[1;93m'
ROXO_CLARO     = '\033[1;95m'
CIANO_CLARO    = '\033[1;96m'
BRANCO_BRILHO  = '\033[1;97m'
RESET          = '\033[0m'
NEGRITO        = '\003[1m'
n = int(input(f'{AMARELO_CLARO}{'Escolha um número: '.upper()}{RESET}'))
print(f'{ROXO_CLARO}PROCESSANDO...{RESET}')
sleep(3)
if n % 2 == 0:
   print(f'{BRANCO_BRILHO}{'O número que você escolheu: {} é '.format(n).upper()}{CIANO_CLARO}PAR.{RESET}')
else:
    print(f'{BRANCO_BRILHO}{'O número que você escolheu: {} é '.format(n).upper()}{VERMELHO_CLARO}IMPAR.{RESET}')
