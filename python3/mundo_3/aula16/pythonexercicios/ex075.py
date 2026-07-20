lista_tupla = ()
cont_9 = 0
for numeros in range(0, 4):
    n = int(
        input(f"Digite o {numeros+1}º valor: ")
    )
    lista_tupla += (n,)
    if n == 9:
        cont_9 += 1
print(f"Você digitou os valores {lista_tupla}")
print(f"O valor 9 apareceu {cont_9} vezes.")
if lista_tupla.count(3):
    print(f"O valor 3 se encontra na {lista_tupla.index(3) + 1}º posição.")
else:
    print(f"O valor 3 não foi encontrado em nenhuma das posições.")
print("Os valores pares encontrados foram: ", end="")
for pares in lista_tupla:
    if pares % 2 == 0:
        print(pares, end=" ")
print()