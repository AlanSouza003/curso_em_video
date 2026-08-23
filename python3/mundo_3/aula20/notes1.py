"""
def sum(a, b):
    print(f"A = {a} e B = {b}")
    s = a + b
    print(f"A soma de A + B é {s}")
#Programa Principal
sum(4, 5) # ? Deixando assim ele segue o fluxo normal do programa.
sum(b=4, a=5) # ! Podemos inverter os valores dessa forma.
"""
"""
# Funções com tuplas
def count(*num): # ? Aqui seria para fazer o calculo de todos o valores dentro de uma tupla
    print(sum(num))
count(2, 1, 7)
count(8, 0)
count(4, 4, 7, 6, 2)
def count(*num): # ? Nesta função verifica o tamanho da tupla.
    size = len(num)
    print(f"Recebido os valores {num} e são ao todo {size} números.")
count(2, 1, 7)
count(8, 0)
count(4, 4, 7, 6, 2)
"""
# Funções com listas
def double(lists):
    pos = 0
    while pos < len(lists):
        lists[pos] *= 2
        pos += 1
    print(values)
values = [6, 3, 9, 1, 0, 2]
double(values)