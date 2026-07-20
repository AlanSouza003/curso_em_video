lista_numerica = list()

for c in range(0, 5):
    lista_numerica.append(
        int(
            input(f"Digite um valor na posição {c}: ")
        )
    )
print(f"Segue os segintes valores atribuidos na lista: {lista_numerica}")
print(
    f"O maior valor digitado foi o {max(lista_numerica)} "
    f"na posição", end=" "
)
for p, v in enumerate(lista_numerica):
    if v == max(lista_numerica):
        print(f"{p}...", end=" ")
print(
    f"\nO menor valor digitado foi o {min(lista_numerica)} "
    f"na posição", end=" "
)
for p, v in enumerate(lista_numerica):
    if v == min(lista_numerica):
        print(f"{p}...", end=" ")
print()
