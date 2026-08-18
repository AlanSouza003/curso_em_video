peoples = {
    'nome':'Alan Souza', 'idade': 23, 'sexo':'M'
}
# del peoples['sexo'] # ? Estou excluido a chave o valor de dentro do dicionario
peoples['nome'] = 'Carvalho' # ! Aqui estou modificando o nome
peoples['peso'] = 87 # * Já neste caso estou adicinando uma nova key e um novo valor.
print(peoples)
'''
print(f'Seu nome é {peoples["nomes"]}.')
print(f'Você tem {peoples["idade"]}')
print(f'Seu sexo é {peoples["sexo"]}')
'''
# * Usando laços:
'''
for k in peoples.keys(): # ! Aqui só vai mostras as keys do dicionario.
    print(k)
'''

'''
for v in peoples.values(): # ! Aqui vai mostra os valores dentro do dicionario.
    print(v)
'''

'''for k, v in peoples.items(): # ! Neste laço já mostra tanto as Keys quanto os valores no dic.
    print(f'{k} é: {v}')'''