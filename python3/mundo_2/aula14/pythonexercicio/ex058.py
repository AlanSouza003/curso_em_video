# importando blibliotecas necessárias para o jogo...
from random import randint
from time import sleep

cont = 1

#FAZ O COMPUTADOR VAI "PENSAR"
maquina = randint(0,10) 

print('\033[1;93m-=-\033[0m'*18)
print('\033[1;96mTente adivinhar qual número irei pensar de 0 á 10...\033[0m')
print('\033[1;93m-=-\033[0m'*18)

#O JOGADOR VAI TENTAR ADIVINHAR O NÚMERO ESCOLHIDO PELA MÁQUINA.
jogador = int(input(f'\033[1;94mAdivinhe o número que escolhi: \033[0m'))
print('\033[1;95mPROCESSANDO\033[0m', end='', flush=True)

# Estrutura de repetição para criar um efeito de "processando" com pontos.
for c in range(0,3):

    print('\033[1;97m.\033[0m', end='', flush=True)
    sleep(1)

""" Enquanto o jogador não acertar o número, o jogo continua e o jogador recebe dicas se o número é maior ou menor
do que o número escolhido pela máquina. O contador de tentativas é incrementado a cada tentativa do jogador. """
while jogador != maquina:

    if maquina > jogador:

        # O JOGADOR VAI TENTAR ADIVINHAR NOVAMENTE
        jogador = int(input(f'\n\033[1;97mMais... Tente novamente. \033[0m'))

    else:

        # O JOGADOR VAI TENTAR ADIVINHAR NOVAMENTE
        jogador = int(input(f'\n\033[1;97mMenos... Tente novamente. \033[0m'))

    # vai contar quantas tentativas o jogador fez para acertar o número.
    cont += 1 

# Saida de dados afirmando que o jogador acertou o número
print(f'\n\033[1;92mPARABÉNS, VOCÊ ACERTOU! O número que pensei foi {maquina}!\033[0m')

# Mostra a quantidade de tentativas que o jogador fez para acertar o número e finaliza o jogo.
print(f'\033[1;97mVocê precisou de {cont} tentativas para acertar o número!\033[0m')

# Fim do jogo!
print(f'\033[1;97mFim do jogo!\033[0m')
