from random import randint
from time import sleep
def prize_draw(lis):
    print("Sorteando 5 valores", end=' ')
    for draft in range(0, 5):
        num = randint(0, 10)
        lis.append(num)
        print(num, end=' ', flush=True)
        sleep(0.9)
    print("PRONTO!")
def even_sum(pair):
    s = 0
    for p in pair:
        if p % 2 == 0:
            s += p
    print(f"Somando os valores pares de {numbers}, temos {s}.")
    
# TODO: Main Program
numbers = []
prize_draw(numbers)
even_sum(numbers)