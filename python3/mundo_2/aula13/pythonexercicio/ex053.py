# Pedindo ao usuário que escreva uma frase

f = str(input('Digite uma frase: ')).strip().upper() # Comandos para tirar os espaços e deixar as letras em maiúsculas

# Transformando a frase em uma lista

palav = f.split()

# Juntando tudo

junt = ''.join(palav)
inver = ''

for letra in range(len(junt) - 1, -1, -1):
    inver += junt[letra]
print(f'O INVERSO DE {junt} É {inver}!')

# Estrutura de repetição para mostrar se ele é ou não é um palíndromo

if inver == junt:
    print('ELE É UM PALÍNDROMO!')
else:
    print('ELE NÃO É UM PALÍNDROMO!')
