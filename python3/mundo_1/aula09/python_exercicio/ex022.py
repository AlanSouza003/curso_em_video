nome = input('Digite seu nome completo: ').strip()
print('Seu nome em letras maiúsculas é: {}!'.format(nome.upper()).upper())
print('Seu nome em letras minúsculas é: {}!'.format(nome.lower()))
print('Sem contar os espaços seu nome tem ao todo {} letras.'.format(len(nome.replace(' ', ''))))
# Ou
# print('Sem contar os espaços seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
div = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(div[0], len(div[0])).upper())
# Ou
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
