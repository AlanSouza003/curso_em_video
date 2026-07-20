lanche = ("Hamburguer", "Suco", "Pizza", "Pudim")
# del(lanche)
lanche[0:3] = ("Chocolate", "Refrigerante")
# lanche[1] = "Refrigerante"  # ! Comprovando que as tuplas são imutáveis.

# ? Existem duas maneiras de fazer um print para mostrar os componentes dentro de uma tupla
# ? abaixo segue as duas estruturas com o comando for. Ambos vão ter a mesma saída.

# # 1º - Sem mostrar a posição.
# for comida in lanche:
#     print(f'{comida}')

# # 2º - Mostrando a posição com o comando len.
# for cont in range(0, len(lanche)):
#     print(f'{lanche[cont]}, na posição {cont+1} da tupla.')

# # 3º - Segunda forma de mostra a posição usando o enumerate com duas variáveis no comando for.
# for posicao, comida in enumerate(lanche):
#     print(f'{posicao + 1} - {comida}')

# ? Para colocar a tupla em ordem tanto numerica quanto alfabetica ou por tamanho usamos o sorted. Exemplo:

# print(sorted(lanche))

# ? E para vermos a posição de uma valor em uma tupla sem a estrutura for, utilizamos o index.
a = (2, 3, 4)
b = (5, 4, 8, 3)
c = a + b
print(lanche)
# print(c.index(4, 3)) # ! Essa forma de encontra a posição de um número repetido, chamamos de 'deslocamento'.
