# Titulo
print('=' * 30)
print(f'{'10 TERMOS DE UMA PA':^30}')
print('=' * 30)
# Variavel s recebendo o valor 0
s = 0
# Pedindo ao usuário para escolher o primeiro termo e a razão
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
# Estrutura de repetição para a realização da PA.
while s < 10:

    print(t, end=' ⭢ ')
    t += r
    s += 1

print('ACABOU')
