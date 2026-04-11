# Variáveis de controle.

media = 0
velho = 0
nome = ''
contador = 0

# Estrutura de repetição para ler os nomes, as idades, e o sexo do usuário.

for c in range(1, 5):
    print(f'======= {c}º PESSOA =======')
    nome1 = str(input('NOME: ')).strip()
    idade = int(input('IDADE: ').strip())
    sexo = str(input('SEXO [M/F]: ')).strip().upper()
    media += idade / 4 # Calculando a média de uma idade

    # Estrutura condicional composta para saber a maior idade e o nome do usuário masculino.

    if sexo == 'M':

        if idade == 1:
            velho = c
            nom = nome
        else:
            if idade > velho:
                velho = idade
                nome = nome1

    #  Estrutura condicional para saber quantas mulheres com menos de 20 anos

    if sexo == 'F':
        if idade < 20:
            contador += 1

# Mostrando na tela o resultado.

print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O homem mais velho do gupo tem {velho} anos, e se chama {nome}!')
print(f'Ao todo são {contador} mulheres com menos de 20 anos.')
