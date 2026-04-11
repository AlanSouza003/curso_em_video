# Estrutura de repetição FOR.

# Laços de Repetição (Parte 1).

# Criando um laço até chegar onde queremos e para isso precisamos que no dentro do laço
# tenhamos um contador para definir a chegada e parar o programa. Isso chamamos laço com variável de controle.
# Exemplo no português claro:
#   laço c no intervalo(1, 10)
#       passo
#   pega

# Exemplo na linguagem python:
#   for c in range(1, 10):
#       passo
#   pega

# Supondo que tenhamos outra situação no código em que teríamos um obstáculo, como iríamos resolver?
# Exemplo no português claro:
#   laço c no intervalo(0, 3)
#       passo
#       pula
#   passo
#   pega

# Exemplo na linguagem python:
#   for c in range(0,3):
#       passo
#       pula
#   passo
#   pega

# E se tivermos que pegar moedas no entre um caminho e outro? Como faríamos?

# Exemplo no português claro:
#   laço c no intervalo(0, 3)
#       se (moeda) entao
#           pega
#       passo
#       pula
#   passo
#   pega

# Exemplo na linguagem python:
#   for c in range(0,3):
#       if moeda:
#           pega
#       passo
#       pula
#   passo
#   pega
