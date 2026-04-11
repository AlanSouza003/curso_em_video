from time import sleep
# Cores de Texto
RESET      = '\033[0m'
SUBLINHADO = '\033[4m'
# Tabela de Cores
VERMELHO  = '\033[1;31m'
AMARELO   = '\033[1;33m'
AZUL      = '\033[1;34m'
ROXO      = '\033[1;35m'
CIANO     = '\033[1;36m'
print(f'{CIANO}-=-{RESET}'*10)
print(f'  {VERMELHO}ATENÇÃO!{RESET} {AMARELO}RADAR A FRENTE...{RESET}  ')
print(f'{CIANO}-=-{RESET}'*10)
print(f'{AMARELO}--> VELOCIDADE MAXIMA 80KM. <--{RESET}')
km = int(input('Em quantos km está o seu velocimetro? ')) # AQUI VAMOS SABER EM QUANTOS KM O VEÍCULO ESTÁ.
print(f'{ROXO}PROCESSANDO...{RESET}')
sleep(3)
valor = (km - 80)*7.00 # AQUI ESTAMOS FAZENDO O CALCULO DA MULTA, SE PASSAR DE 80KM
porcentagem = (km / 80 - 1) * 100 # NESTA LINHA ESTOU FAZENDO O CALCÚLO DA PORCENTAGEM.
if km > 80:
    print(f'{VERMELHO}MULTADO! A VELOCIDADE MAXÍMA DA PISTA É 80km É VOCÊ PASSOU COM {km}km.{RESET}')
    print(f'{VERMELHO}{porcentagem}% Á MAIS QUE O PERMITIDO. O VALOR DA SUA MULTA É DE {SUBLINHADO}R${valor}{RESET}')
print(f'{AZUL}TENHA UMA ÓTIMA CONDUÇÃO! SE FOR DIRIGIR NÃO BEBA!{RESET}')