from random import randint
from time import sleep

winning_numbers = []
data = []
game = 0

predictions = int(input("Quantos palpites deseja realizar? "))

while True:
    while True:
        numbers = randint(1, 60)
        if numbers not in data:
            data.append(numbers)
        if len(data) == 6:
            break
    data.sort()
    winning_numbers.append(data[:])
    data.clear()
    game += 1
    if game == predictions:
        break
print('-=' * 3, f"SORTEANDO {predictions} JOGOS", '-=' * 3)
for i, g in enumerate(winning_numbers):
    print(f"Jogo {i+1}: {g}")
    sleep(1)
print('-=' * 5, "ÓTIMO JOGO!", '-=' * 5)