matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
sum_pairs = 0
sum_three_column = greater_two_column = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f"Digite um valor [{l}, {c}]: "))
        if matrix[l][c] % 2 == 0:
            sum_pairs += matrix[l][c]
        if c == 2:
            sum_three_column += matrix[l][c]
        if l == 1:
            if c == 0:
                greater_two_line = matrix[l][c]
            else:
                if matrix[l][c] > greater_two_line:
                    greater_two_line = matrix[l][c]
print("─" * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matrix[l][c]:^5}]", end='')
    print("")
print("─" * 30)
print(f"A soma dos valores pares da matriz é: {sum_pairs}")
print(f"A soma dos valores da terceira coluna foi: {sum_three_column}")
print(f"O maior valor da segunda linha foi: {greater_two_line}")