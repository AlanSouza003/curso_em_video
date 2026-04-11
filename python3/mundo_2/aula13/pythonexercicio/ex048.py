# Declarando o valor das variáveis
s = 0
s_cont = 0
# Estrutura de repetição para o cálculo.
for m in range(1, 500):
    # Estrutura condicional para o calculo dos números divisores de 3
    if m % 3 == 0 and m % 2 == 1:
        s += m
        # Transformando os números em uma 'string'.
        cont = str(m)
        cont_list = cont.split()
        cont_format = len(cont_list)
        # Transfomando os números em inteiros novamente para somalos.
        list_int = int(cont_format)
        s_cont += list_int
# Mostrando na tela o resultado final
print(f'A soma total dos {s_cont} valores entre 1 até 500\nque são divisores de 3 é: {s}')
