# Variaveis de controle
c = s = 0

""" Estrutura de repetição para ler os valores do usuário e calcular a soma
dos valores digitados até o usuários digitar o valor 999 """
while True:

    n = int(input(f'Digite o {c + 1}º valor [999 para parar]: '))
    
    if n == 999:
        break

    s += n
    c += 1
    
print(f'Foi digitado {c} números e a soma entre eles foi {s}')
