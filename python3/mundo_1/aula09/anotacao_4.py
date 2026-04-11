# Transformação de uma ‘string’

# Caso eu queira substituir uma palavra por outra no python, eu tenho que utilizar o
# comando 'replace', assim eu posso substitiur uma palavra por outra.

# Ex:

# frase = 'Alan no mundo de python'
# print(frase.replace('Alan', 'Alanclei'))

# Com a funcionalida do 'upper', deixamos a frase completa em maiúsculas. Mantendo o que estava em
# maiúsculo.

# Ex:

# frase = 'Alan no mundo de python'
# print(frase.upper())

# Por outro lado seguindo o raciocínio a funcionalidade 'lower', vai deixar tudo
# em minúsculas. o que estava em minúsculo.

# Ex:

# frase = 'Alan no mundo de python'
# print(frase.lower())

# Numa outra funcionalidade é o 'capitalize', o ele deixa apenas a primeira letra da frase inteira
# em maiúscula.

# Ex:

# frase = 'Alan no Mundo de Python'
# print(frase.capitalize())

# Seguindo o mesmo raciocínio do 'capitalize' temos o 'title', que ele vai em palavra por palavra
# deixar a letra em maiúscula.

# frase = 'Alan no mundo de python'
# print(frase.title())

# Uma funcionalidade bem interessante é o 'strip', onde ele remove os espaços que são colocados por acidente
# no início e no final de uma frase.

# Ex:

# frase = '   Estou aprendendo a Programar  '
# print(frase.strip())

# Similar a funcionalidade acima, nós temos o 'rstrip', onde ele vai remover somente os espaços que estiverem
# no último na direita.

# frase = '   Estou aprendendo a Programar  '
# print(frase.rstrip())

# Mesma coisa com o 'lstrip', onde ele remove somente os primeiros espaços que estão na esquerda.

# frase = '   Estou aprendendo a Programar  '
# print(frase.lstrip())