from lib.interface import *
from lib.arquivo import *

# TODO: Main Program
file = 'log_cadastros.txt'

if not fileExist(file):
    newFile(file)

while True:
    resp = menu(
        ['Ver dados Cadastrados', 'Cadastrar nova Pessoa', 'Sair do Sistema'], 4, 5
    )
    if resp == 1:
        # >>> Listando o conteúdo do arquivo.txt
        readFile(file)
    elif resp == 2:
        # >>> Adicionando uma nova pessoa ao arquivo.txt
        header('NOVO CADASTRO', 4)
        name = str(input(f'{c[8]}Nome: {c[0]}'))
        age = readInt(f'{c[8]}Idade: {c[0]}')
        register(file, name, age)
    elif resp == 3:
        header('SAINDO DO SISTEMA...', 8)
        break
    else:
        print(f'{c[2]}O valor {resp} não existe no menu{c[0]}.')
