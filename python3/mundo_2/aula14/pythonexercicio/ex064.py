# Titulo
print('='*25)
print('GERADOR DE VALORES')
print('='*25)

# Variaveis de controle
c = n = s =  0

# Estrutura de repetição para calcular os valores exceto a flag 999.
while n != 999:
        n = int(input('Digite um valor inteiro [999 para parar]: '))
        s += n
        if n == 999:
            s -= 999
            c -= 1
        c += 1
print(f'O total de valores digitado foi {c} e soma total dos valores foi {s}.')
