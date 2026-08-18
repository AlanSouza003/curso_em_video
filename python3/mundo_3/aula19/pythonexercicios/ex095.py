player = {}
players = []
goals = []
while True:
    player['jogador'] = str(input('Nome do jogador: '))
    matches = int(input(f'Quant de partidas do {player["jogador"]}: '))
    for c in range(matches):
        goals.append(int(input(f"  => Quant de gols na partida {c+1}: ")))
    player['gols'] = goals[:]
    player['total'] = sum(goals)
    players.append(player.copy())
    goals.clear()
    while True:
        more_one = str(input("Deseja continuar? [S/n]")).upper()
        print('─' * 50)
        if more_one in ['S', 'SIM', 'NÃO', 'N']:
            break
        print('Erro! Digite apenas "Sim" ou "Não". E se quiser abreviar "S" ou "N"')
    if more_one in ['N', 'NÃO']:
        break
print(f"{'No.':<5} {'NOME':<15} {'GOLS':<15} {'TOTAL'}")
print('─' * 50)
for k, v in enumerate(players):
    print(f'{k:<5}', end=' ')
    for p in v.values():
        print(f"{f'{p}':<15}", end=' ')
    print()
print('─' * 50)
while True:
    detail = int(input("Deseja visualizar dados de qual jogador (999 interromper)? "))
    if detail == 999:
        break
    if detail <= len(players) - 1:
        print(f" => Levantamento do jogador {players[detail]['jogador']}")
        for i, g in enumerate(players[detail]['gols']):
            print(f"   -> Na partida {i+1} fez {g} gols.")
    else:
        print(f"Jogador {detail} inexistente no banco de dados.")
    print('─' * 50)
print("<<< PROGRAMA ENCERRADO >>>")
