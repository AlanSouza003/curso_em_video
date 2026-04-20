# Titulo
print("=" * 30)
print(f"{'10 TERMOS DE UMA PA':^30}")
print("=" * 30)

# Variável de controle para o número de termos
c = 0
# Lendo o primeiro termo do usuário
terms = int(input('\033[1;97mPrimeiro Termo: \033[0m'))
# Lendo a razão da PA
reason = int(input('\033[1;97mRazão PA: \033[0m'))

# Estrutura de repetição para mostrar os 10 primeiros termos da PA
while c < 10:
    print(f'\033[1;97m{terms}\033[0m', end=' ⭢ ')
    terms += reason
    c += 1
print('\033[1;93mPAUSA\033[0m')

# perguntando se o usuário deseja mostrar mais termos da PA
more_terms = int(input('\033[1;97mDeseja mostrar mais quantos termos? \033[0m'))

# Estrutura de repetição para mostrar mais termos da PA caso o usuário queira.
while more_terms != 0:
    for _ in range(more_terms):
        print(f'\033[1;97m{terms}\033[0m', end=' ⭢ ')
        terms += reason
        c += 1
    print('\033[1;93mPAUSA\033[0m')
    more_terms = int(input('\033[1;97mDeseja mostrar mais quantos termos? \033[0m'))

# Fim do programa!
print(f'\033[1;97mPROGRAMA FINALIZADO! FOI MOSTRADO {c} TERMOS IMPRIMIDOS!\033[0m')
