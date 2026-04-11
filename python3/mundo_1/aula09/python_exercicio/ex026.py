filtro = input('Digite uma frase: ').lower().strip()
print('A letra "A" aparece {} vezes.'.format(filtro.count('a')))
print('A primeira letra "A" apareceu na posição {}.'.format(filtro.find('a')+1))
print('A última letra "A" apareceu na posição {}.'.format(filtro.rfind('a')+1))


