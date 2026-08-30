def sheet(player='<desconhecido>', goals=0):
    """
    -> Mostra a ficha do jogador: nome e gol(s)

    :param player: (opcional) Recebe o nome do jogador
    :param goals: (opcional) Quantidade de gol(s).
    """
    print(f"O jogador {player} fez {goals} gol(s) no campeonato.")

# TODO: Main Program
name = str(input("Nome do jogador: "))
goal = str(input("Quantidade de gols: "))
if goal.isnumeric():
    goal = int(goal)
else:
    goal = 0
if name.strip() == '':
    sheet(goals=goal)
else:
    sheet(name, goal)
