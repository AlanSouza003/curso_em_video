# FATIAMENTO DE CARACTERES
from logging.config import valid_ident

# Aqui vamos aprender a como fatiar uma string. Segue abaixo cada exemplo de fatiamento

# Primeiro fatiamento: frase[5]

# Nesse fatiamento o programa so vai mostrar o que está no bloco 4 pois ele não vai até
# o número em que colocamos e sim até o numero anterior.

# Ex:

# frase = 'Alan no mundo de python'
# print(frase[6])

# Segundo fatiamento: frase[0:8]

# Aqui ele vai começar do bloco 0 e vai até o bloco 8. Lembrando que ele não coloca a letra
# que este no bloco do número em que colocamos.

# Ex

# frase = 'Alan no mundo de python'
# print(frase[0:8])

# Terceiro fatiamento: frase[9:24:2]

# O fatiamento ocorrerá dessa forma: vai começar do bloco 9 até o bloco 24 (só que ele não existe)
# pois coloquei apenas para aparecer o caractere que esta no bloco 23. O número dois representa que ele vai
# até o bloco 24 pulando a cada dois caracteres.

# Ex

# frase = 'Alan no mundo de python'
# print(frase[9:24:2])