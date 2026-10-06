from lib.colors import c
from lib.interface import *

def fileExist(name):
    try:
        f = open(name, 'rt')
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True

def newFile(name):
    try:
        f = open(name, 'wt+')
        f.close()
    except FileExistsError:
        print(f"{c[2]}Erro ao criar o arquivo \"{name}\" :({c[0]}")
    else:
        print(f"{c[3]}Arquivo \"{name}\" foi criado com sucesso!{c[0]}")

def readFile(name):
    try:
        f = open(name, 'rt')
    except Exception:
        print(f"{c[2]}ERRO: na leitura do arquivo \"{name}\".{c[0]}")
    else:
        header('PESSOAS CADASTRADAS', 3)
        print(f.read())
    finally:
        f.close()

def register(file, name='<desconhecido>', age=0):
    try:
        f = open(file, 'at')
    except Exception:
        print(f"{c[2]}ERRO: NA ABERTURA DO ARQUIVO!{c[0]}")
    else:
        try:
            f.write(f'{name:.<30}{age} anos\n')
        except Exception:
            print(f"{c[2]}HOUVE UMA FALHA AO REGISTRAR OS DADOS!{c[0]}")
        else:
            print(f"{c[3]}Usuário {name} registrado com sucesso!{c[0]}")
            f.close()