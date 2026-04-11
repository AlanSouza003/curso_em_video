# Análise de uma ‘string’

# Para analisarmos uma ‘string’, e sabermos qual o tamanho dela iremos utilizar o comando
# len(frase)

# Ex

# frase = 'Alan no mundo de python'
# print(len(frase))

# Outro comando é o: frase.count('n'). Aqui ele vai contar quantas letras 'n' tem no código.

# frase = 'Alan no mundo de python'
# print(frase.count('n'))

# Uma forma já de contar já com o fatiamento: frase.count('n',0,11).
# lembrando que nesse comando ele vai-so mostrar que tem apenas três letras 'n'.

# Ex

# frase = 'Alan no mundo de python'
# print(frase.count('n',0,11))

# Para encontrar uma palavra na frase usamos o comando: frase.find('undo'). Aqui ele mostra em qual posição
# começou o 'undo'.

# Ex:

# frase = 'Alan no mundo de python'
# print(frase.find('undo'))

# Um outro comando é para dizer se realmente existe aquela palavra numa frase com o operador 'in',
# que pode ser utilizado dessa maneira: 'Alan' in frase
# O programa vai retorna como True ou False.

# frase = 'Alan no mundo de python'
# print('Alan' in frase)