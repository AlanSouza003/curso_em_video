from random import randint
import os

listagem_tupla = ()
for c in range(0, 5):
    n_aleatorio = randint(1,10)
    listagem_tupla += (n_aleatorio,)
for lista in listagem_tupla:
    print(lista, end=" ")
print(f"\nO maior número gerado foi: {max(listagem_tupla)}")
print(f"O menor número gerado foi: {min(listagem_tupla)}")
