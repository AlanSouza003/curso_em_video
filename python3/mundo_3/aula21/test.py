"""
def contador(i, f, p):
    ""
    -> Faz uma contagem e mostra na tela.

    Args:
        i (int): inicio de uma contagem
        f (int): fim de uma contagem
        p (int): passos da contagem
        (return): sem retorno
    ""
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
help(contador) # ? A função help pode ser usada sem a docstring também, ela vai gerar tipo um menu
"""
"""
# * PARAMETROS OPCIONAIS
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 4, 5)
somar(3, 5)
somar(5)
somar()
"""
# * ESCOPO DE VARIAVEIS
"""
# Escopo global
def teste():
    print(f'Na função teste, n vale {n}') 
# TODO: Main Program 
n = 2 
teste()
print(f'No programa principal, n vale {n}')
"""
"""
# Escopo Local
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
# TODO: Main Program
n = 2 
teste()
print(f'No programa principal, n vale {n}')
# ! print(f'No programa principal, x vale {x}') Vai dá erro.
"""
"""
# Criando uma variavel global/local 
def teste(y):
    n = 8
    y += 4
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, y vale {y}')
    print(f'Na função teste, x vale {x}')
# TODO: Main Program
n = 2 
teste(n)
print(f'No programa principal, n vale {n}')
"""
"""
# Utilizando a função "global" para trocar o valor da varialvel global sem criar uma local
# da mesma
def teste(y):
    global n
    n = 8
    y += 4
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, y vale {y}')
    print(f'Na função teste, x vale {x}')
# TODO: Main Program
n = 2 
teste(n)
print(f'No programa principal, n vale {n}')
"""
# * RETORNANDO VALORES
"""
# Retornando valores fora da função com o comando return.
def somar(a=0, b=0, c=0):
    s = a + b + c
    return s # * Com esse comando consigo mandar o print formatado da forma que quero
# TODO: Main Program
r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(4)
print(f'Meus calculos deram {r1}, {r2} e {r3}')
"""
