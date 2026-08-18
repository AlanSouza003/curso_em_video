utilization_player = {}
goals = []
utilization_player['nome'] = str(input("Nome do jogador: "))
matches = int(input(f"Partidas que o {utilization_player['nome']} jogou: "))
for c in range(matches):
    goals.append(int(input(f"Quant. de gols na {c+1}º partida: ")))
utilization_player['gols'] = goals[:]
utilization_player['total'] = sum(goals)
print('─' * 50)
print(utilization_player)
print('─' * 50)
for k, v in utilization_player.items():
    print(f"O campo {k} tem o valor {v}.")
print('─' * 50)
print(f"O jogador {utilization_player['nome']} jogou {len(utilization_player['gols'])} partidas.")
for i, g in enumerate(utilization_player['gols']):
    print(f"  => Na partida {i}, fez {g} gols.")
print(f"No total {utilization_player['nome']} fez {utilization_player['total']} gols.")
