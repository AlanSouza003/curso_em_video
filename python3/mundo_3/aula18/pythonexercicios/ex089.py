general_list = []

while True:
    studenty = str(input("Aluno: "))
    notes1 = float(input("1ª nota: "))
    notes2 = float(input("2ª nota: "))
    average = (notes1 + notes2) / 2
    general_list.append([studenty, [notes1, notes2], average])
    more_one = str(input("Deseja continuar? [S/n]")).upper()
    if more_one not in ['SIM','S']:
        break
print('-=' * 15)
print(f"{'BOLETIM':^30}")
print('-=' * 15)
print()
print(f"{'No.':<5} {'NOME':<12} {'MÉDIA'}")
print('─' * 27)
for i, s in enumerate(general_list):
    print(f"{i:<5} {s[0]:<13} {s[2]:.1f}")
print('─' * 27)
while True:
    see_notes = int(input("Deseja ver a nota de qual aluno? (999 interromper): "))
    if see_notes == 999:
        print("Programa finalizado!")
        break
    if see_notes <= len(general_list) - 1:
        print(f"As notas do aluno {general_list[see_notes][0]} foram: "
              f"{general_list[see_notes][1]}")
        print('─' * 27)
    else: 
        print("Este aluno não possui registro no boletim.\n"
              "Tente novamente.")
        print('─' * 27)
print("<<<< Volte quando quiser! >>>>")