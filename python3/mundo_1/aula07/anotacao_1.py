# No Python temos outra forma de utilizar os operadores.
# Ex:

#     Para usar a potencia podemos utiliza o comando pow(), mas podemos perde a ordem de
#     precedência.

# print(pow(4,3))
# print(4**3)

# E para calcularmos a Raiz quadrada podemos utilizar o comando numero**(1/2).
# Assim conseguimos calcular a raiz quadrada.

# print(81**(1/2))

# Podemos também utilizar os operadores para formar strings.

# Ex:

# print('='*20)
# print('Olá' + 'Oi')
# print('Olá'*5)

# Podemos fazer também alinhamentos

# Ex:

# nome = input('Digite seu nome: ')
# print('Prazer em te conhecer {:>20}!'.format(nome))
# Aqui eu estaria alinhando o nome para a direita com o sinal de > ou para esquerda
# usando <.

# E para deixarmos centralizado usamos.

nome = input('Digite seu nome: ')
print('Prazer em te conhecer {:^20}!'.format(nome))
# E tem mais. Podemos colocar qualquer sinal antes do circunflexo
# Exemplo: {:=^20} ou {:-^20}, e por ai vai.