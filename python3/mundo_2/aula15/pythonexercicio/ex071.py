
print(
    f"{'\033[1;95m-\033[0m' * 25}\n"
    f"{'\033[1;97mBANCO ASZ\033[0m':^35}\n"
    f"{'\033[1;95m-\033[0m' * 25}\n"
    f"\033[1;97mCÉDULAS DISPONÍVEIS: R$50, R$20, R$10 E R$1\033[0m\n"
    f"{'\033[1;95m-\033[0m' * 25}"
)
while True:
    saque = int(
        input('\033[1;97mVALOR DO SAQUE: R$\033[0m')
    )
    notas_disponiveis = [50, 20, 10, 1]
    indice_nota = 0

    print(
        f"{'\033[1;95m-\033[0m' * 25}\n"
        f"\033[1;96mSERÁ ENTREGUE:\033[0m"
    )

    while saque > 0 and indice_nota < len(notas_disponiveis):

        nota_atual = notas_disponiveis[indice_nota]

        quant_notas = saque // nota_atual

        if quant_notas > 0:
            if quant_notas == 1:
                print(
                    f'\033[1;97m0{quant_notas} NOTA DE R${nota_atual},00\033[0m'
                )
            elif 1 < quant_notas < 9:
                print(
                    f'\033[1;97m0{quant_notas} NOTAS DE R${nota_atual},00\033[0m'
                )
            else:
                print(
                    f'\033[1;97m{quant_notas} NOTAS DE R${nota_atual},00\033[0m'
                )

        saque %= nota_atual

        indice_nota += 1

    if saque > 0:
        print(
            '\033[1;91mATENÇÃO\033[0m\033[1;97m!\nNÃO HÁ CÉDULAS DISPONIVEIS PARA O RESTANTE\033[0m '
            '\033[1;97mDO VALOR DO SEU SAQUE!\033[0m\n'
            '\033[1;92mO VALOR RESTANTE SERÁ ESTORNADO PARA SUA CONTA.\033[0m'

        )
    print(
        f"{'\033[1;95m-\033[0m' * 25}"
    )
    outro_saque = str(
        input(f'\033[1;95mDESEJA REALIZAR OUTRO SAQUE? [S/N]: \033[0m')
    ).strip().upper()
    print(
        f"{'\033[1;95m-\033[0m' * 25}"
    )
    if outro_saque not in ['S', 'SIM']:
        break
print(
    '\033[1;92m====== O BANCO ASZ, AGRADECE! VOLTE SEMPRE! ======\033[0m'
)
