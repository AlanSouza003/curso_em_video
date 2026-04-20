# Titulo
print('='*25)
print(f'{'SEQUÊNCIA FIBONACCI':^25}')
print('='*25)

# Variaveis de controle para calcular a sequência fibonacci
f1 = 0
f2 = 1
c = 3

# Lendo o valor do usuário para mostrar a sequência fibonacci
terms = int(input('Quantos termos você deseja para realiza a sequência? '))

# Mostrando na tela os dois primeiro termos fibonacci
print(f'{f1} ➔ {f2}', end=' ')

""" Estrutura de repetição para mostrar os termos fibonacci de acordo com o número 
de termos escolhido """
while c <= terms:

    fibonacci = f1 + f2
    print(f' ➔ {fibonacci}', end=' ')
    f1 = f2
    f2 = fibonacci
    c += 1

print('➔ FINISH')
