from random import randint
from time import sleep
from operator import itemgetter
game = {}
ranking_game = []
for c in range(0, 4):
    game[f"Player {c+1}"] = randint(1,6)
print("Valores sorteados: ")
for k, v in game.items():
    print(f"O {k} tirou {v}")
    sleep(1)
ranking_game = sorted(game.items(), key=itemgetter(1), reverse=True)
print("Ranking dos jogadores:")
for i, v in enumerate(ranking_game):
        print(f"{i+1}º Lugar: {v[0]} com {v[1]}")
        sleep(1)
