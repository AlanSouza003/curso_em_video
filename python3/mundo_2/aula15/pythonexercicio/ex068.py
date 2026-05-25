from random import randint

c = 0

print(
    f'\033[1;97m=\033[0m' * 20
)
print(
    f'\033[1;94m{'PAR OU IMPAR':^20}\033[0m'
)
print(
    f'\033[1;97m=\033[0m' * 20
)
while True:

    while True:
        escolha = str(
            input(f'\033[1;97mVocê escolhe PAR ou IMPAR?\033[0m ')
        ).upper().strip()
        print(
            f'\033[1;97m-\033[0m' * 25
        )
        if escolha == 'PAR':
            print(
                f'\033[1;92mÓTIMA ESCOLHA! VOCÊ FICOU COM {escolha} '
                'E A MÁQUINA FICOU COM IMPAR\033[0m'
            )
            jogador = int(
                input(f'\033[1;93mQUAL NÚMERO VOCÊ ESCOLHE? \033[0m')
            )
            break
        elif escolha == 'IMPAR':
            print(
                f'\033[1;92mÓTIMA ESCOLHA! VOCÊ FICOU COM {escolha} '
                'E A MÁQUINA FICOU COM PAR\033[0m'
            )
            jogador = int(
                input(f'\033[1;93mQUAL NÚMERO VOCÊ ESCOLHE? \033[0m')
            )
            break
        else:
            print(
                f'\033[1;91mOPÇÃO INVALIDA! TENTE NOVAMENTE\033[0m'
            )
    print(
        f'\033[1;97m-\033[0m' * 25
    )
    maquina = randint(1, 10)
    soma = jogador + maquina
    print(
        f'\033[1;96mVOCÊ JOGOU O NÚMERO {jogador} E A MAQUINA JOGOU O NÚMERO {maquina} '
        f'SOMANDO DEU {soma}\033[0m '
    )
    if escolha == 'PAR' and soma % 2 == 0:
        print(
            f'\033[1;92mO JOGADOR VENCEU!\033[0m'
        )
        c += 1
    elif escolha == 'IMPAR' and soma % 2 == 1:
        print(
            f'\033[1;92mO JOGADOR VENCEU!\033[0m'
        )
        c += 1
    else:
        print(
            f'\033[1;91mO JOGADOR PERDEU!\033[0m'
        )
        break
    print(
        f'\033[1;97m-\033[0m' * 25
    )
print(
    f'\033[1;97m-\033[0m' * 25
)
print(
    f'\033[1;97mFIM DE JOGO. VOCÊ VENCEU {c} PARTIDAS.\033[0m'
)
