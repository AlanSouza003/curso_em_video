# Titulo
print('=' * 30)
print(f'{'10 TERMOS DE UMA PA':^30}')
print('=' * 30)
# Variavel s recebendo o valor 0
s = 0
# Pedindo ao usuário para escolher o primeiro termo e a razão
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
d = t + (10 - 1) * r
# Estrutura de repetição para a realização da PA.
for c in range(t, d + 1, r):
    print(c, end=' ⭢ ')
print('ACABOU')