numA = [1, 4, 5, 7] # # Aqui temos uma lista de números 
numA[1] = 3 # ? Aqui estamos mudando o 2º valor da lista que seria o 4.
numA.append(6) # ? Estamos adicionando um valor a lista.
# num.sort() # ? Usando o 'sort()', colocamos a lista em ordem.
# num.sort(reverse=True) # ! Dessa forma colocamos a lista em ordem reversa.
numA.insert(2, 7) # ? Com o comando 'insert' conseguimos inserir qualquer valor no lugar em que queremos
# num.pop() # ? Remove o ultimo valor da lista
numA.remove(7) # ? Remove o contéudo da lista
numB = numA[:] # ! Esse metodo é utiliza para criar uma copia de uma lista.
numB[1] = 4
print(numA, numB)
