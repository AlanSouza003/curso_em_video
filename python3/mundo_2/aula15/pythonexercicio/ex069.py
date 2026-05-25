# Variaveis de controle

c_maior_18 = c_homem = c_mulher_menos_20 = 0
continuar = ''

while True:
    print(
        f'=' * 20
    )
    print(
        f'\033[1;96m{'CADASTRANDO':^20}\033[0m'
    )
    print(
        f'=' * 20
    )

    idade_str = str(
        input(f'\033[1;97mDIGITE SUA IDADE:\033[0m ')
    ).strip().upper()

    if idade_str.isnumeric():

        idade = int(idade_str)

        sexo = str(
            input(f'\033[1;97mDIGITE SEU SEXO: [M/F]\033[0m ')
        ).strip().upper()

        while sexo not in ['M', 'F', 'MASCULINO', 'FEMININO']:

            print(
                f'\033[1;91mVALOR INCORRETO! TENTE NOVAMENTE.\033[0m'
            )

            print(
                f'\033[1;97m-\033[0m' * 25
            )

            sexo = str(
                input(f'\033[1;97mDIGITE SEU SEXO: [M/F]\033[0m ')
            ).strip().upper()

        if sexo == 'M' or sexo == 'MASCULINO':

            c_homem += 1

        if idade >= 18:

            c_maior_18 += 1

        if idade < 20 and sexo == 'F' or sexo == 'FEMININO':

            c_mulher_menos_20 += 1

        continuar = str(
            input(f'\033[1;96mDeseja continuar? [S/N]\033[0m ')
        ).strip().upper()

        while continuar not in ['S', 'N', 'SIM', 'NÃO']:

            print(
                f'\033[1;91mVALOR INCORRETO! TENTE NOVAMENTE.\033[0m'
            )

            print(
                f'\033[1;97m-\033[0m' * 25
            )

            continuar = str(
                input(f'\033[1;96mDeseja continuar? [S/N]\033[0m ')
            ).strip().upper()

    else:

        print(
            f'\033[1;91mVALOR INCORRETO! TENTE NOVAMENTE.\033[0m'
        )

        print(
            f'\033[1;97m-\033[0m' * 25
        )

    if continuar == 'N':
        break
print()

print(
    f'\033[1;92m=======CADASTRO REALIZADO=======\033[0m\n'
    f'\033[1;95mDADOS CADASTRAIS\033[0m\n'
    f'\033[1;97mMAIOR DE 18 ANOS: {c_maior_18}\033[0m\n'
    f'\033[1;97mHOMENS CADASTRADOS: {c_homem}\033[0m\n'
    f'\033[1;97mMULHERES MENORES DE 20 ANOS: {c_mulher_menos_20}\033[0m\n'
)
