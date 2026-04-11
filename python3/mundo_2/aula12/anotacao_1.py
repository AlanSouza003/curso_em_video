# Condições Alinhadas

# A condição "if" só tem dois caminhos "verdadeiro" ou "falso", supomos que haverá outro caminho
# mais rápido. Como if so mostra dois caminhos o "verdadeiro" e "falso" temos outra condição que se chama
# "elif" que é a simplificação de "if" e "else".
# Obs: O "elif" pode ser utilizado dentro do "if" quantas vezes for necessário, já o "else" pode ser usado
# nenhuma ou uma vez. Ah, o "elif" só pode ser usado dentro do "if".

nome = str(input('Digite seu nome: '))
if nome == 'Alan':
    print('Que nome Perfeito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Que nome popular!')
else:
    print('Que nome estranho.')
print(f'Tenha um ótimo dia, {nome}!')