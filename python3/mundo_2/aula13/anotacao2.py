# Lembrando que no python ele sempre ignora o último número. Então se quiser que ele vai de 1 até 6
# invés de colocar 1 até 6 colocaremos de 1 até 7.
# Exemplo:

# Aqui ele vai até o número 5
# for c in range(1, 6):
#     print(c)

# Aqui ele vai até o número 6 (o número desejado).
# for c in range(1, 7):
#     print(c)

# Se quiser fazer ele contar de forma decrescente então:
# for c in range(7, 0, -1):
#     print(c)

# E podemos também fazer pulando casa de dois em dois, de três em três, etc.
# for c in range(0, 7, 2):
#     print(c)

# Exemplo prático perguntando ao usuário

# n = int(input('Digite um número: '))
# for c in range(0, n + 1):
#     print(c)

# Exemplo pulando em passo em passo:

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
if f > i:
    for cc in range(i, f + 1, p):
        print(f'{cc},'.replace(f'{f},', f'{f}.'), end='')
else:
    for cd in range(i, f - 1, -p):
        print(f'{cd},'.replace(f'{f},', f'{f}.').replace(f'{i}.', f'{i},'), end='')