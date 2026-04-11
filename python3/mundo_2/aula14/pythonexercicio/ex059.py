""" importando a função sleep do módulo time para criar uma pausa 
entre as mensagens de finalização do programa."""
from time import sleep

# Variavel opção para armazenar a escolha do usuário no menu de opções.
opcao = 0

# Lendo o valor de dois números do usuário para realizar as operações matemáticas e comparações.
n1 = float(input('\033[1;97mDigite um número: \033[0m'))
n2 = float(input('\033[1;97mDigite outro número: \033[0m'))

""" Estrutura de repetição while para exibir o menu de opções e realizar as 
operações até que o usuário escolha a opção de sair do programa (opção 5). """
while opcao != 5:

    # Menu de opções
    print('\033[1;97m=\033[0m'*20)
    print('\033[1;92m[ 1 ]\033[0m \033[1;97mSomar\033[0m\n'
          '\033[1;92m[ 2 ]\033[0m \033[1;97mMultiplicar\033[0m\n'
          '\033[1;92m[ 3 ]\033[0m \033[1;97mMaior\033[0m\n'
          '\033[1;92m[ 4 ]\033[0m \033[1;97mNovos Números\033[0m\n'
          '\033[1;92m[ 5 ]\033[0m \033[1;97mSair do Programa\033[0m')
    
    # Lendo a escolha do usuário
    opcao_str = str(input('\033[1;93m>>>> Digite a opção: \033[0m'))

    """ convertendo a string digitada pelo usuário para um número inteiro, 
    caso seja um valor numérico. """
    if opcao_str.isnumeric():
        opcao = int(opcao_str)

    # Estrutura condicional para verificar a escolha do usuário e realizar as operações correspondentes.
    if 1 <= opcao <= 5:

        # Adição
        if opcao == 1:

            s = n1 + n2
            print(f'\033[1;92mA soma entre {n1} + {n2} é {s}\033[0m'.replace('.0', ''))

        # Multiplicação
        elif opcao == 2:

            m = n1 * n2
            print(f'\033[1;92mO produto entre {n1} × {n2} é {m}\033[0m'.replace('.0', ''))

        # Maior que
        elif opcao == 3: 

            if n1 > n2: 
                maior = n1
                menor = n2

            elif n1 < n2:
                maior = n2
                menor = n1

            else: 

                print('\033[1;95mAmbos os valores são iguais.\033[0m')
            print(f'\033[1;92mO valor {maior} é maior que valor {menor}\033[0m'.replace('.0', ''))
        # Pedindo novos valores e reiniciando o loop de acordo com os novos números solicitados
        elif opcao == 4:

            print('\033[1;92mDigite os novos números: \033[0m')
            n1 = float(input('\033[1;97mDigite um número: \033[0m'))
            n2 = float(input('\033[1;97mDigite outro número: \033[0m'))

        """ Mostrando a mensagem de opção invalida apois o usuário ter digitado um número que não estava
        entre 1 e 5 """
    else: 

       print(f'\033[1;91mOpção "{opcao_str.upper()}" invalida! Tente novamente.\033[0m\n', end='')

# Mostra a mensagem de finalização do programa com uma animação de pontos.
print('\033[1;97m=\033[0m'*20)
print('\033[1;97mFinalizando\033[0m', end='', flush=True)

# Comando for para criar uma animação de pontos, onde cada ponto é impresso a cada segundo.
for c in range(0, 3):
    print('\033[1;97m.\033[0m', end='', flush=True)
    sleep(1)
# Pulando uma linha para separar a animação da mensagem final do programa.
print()

# Mensagem de finalização do programa.
print('\033[1;97m=\033[0m'*20)
print('\033[1;96mPROGRAMA ENCERRADO!\033[0m')
