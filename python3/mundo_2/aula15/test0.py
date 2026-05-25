# Testes

# Criando um contador da maneira tradicional com o comando while
""" c = 1

while c <= 10:

    print(c, ' ⭢ ', end='')
    c += 1

print('FINISH') """

# Criando um loop infinito
c = 1

while True:

    print(c, ' ⭢ ', end='')
    if c == 10:
        break
    c += 1

print('FINISH')
