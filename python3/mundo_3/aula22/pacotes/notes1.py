"""
# PACOTE
- Pacote nada mais, nada menos, que pastas que contém modulos
"""
from uteis import numeros

# TODO: Programa Principal
num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f"O fatorial de {num} é {fat}.")
print(f"O dobro de {num} é {numeros.dobro(num)}.")
print(f"O triplo de {num} é {numeros.triplo(num)}.")