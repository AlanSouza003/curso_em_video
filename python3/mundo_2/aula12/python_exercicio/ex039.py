from datetime import date
cor = {'limpa':'\033[0m', 'vermelho':'\033[1;91m', 'verde':'\033[1;92m',
       'amarelo':'\033[1;93m', 'branco':'\033[1;97m','azul':'\033[1;94m'}
# Titulo
print(f'{cor['branco']}-{cor['limpa']}'*30)
print(f'{cor['azul']}{'ALISTAMENTO MILITAR 🪖':^29}{cor['limpa']}')
print(f'{cor['branco']}-{cor['limpa']}'*30)
nome = input(f'{cor['branco']}Digite seu nome: {cor['limpa']}')
ano  = int(input(f'{cor['branco']}Em que você nasceu: {cor['limpa']}'))
sexo = int(input(f'''{cor['branco']}Qual o seu sexo?{cor['limpa']}
{cor['verde']}[ 1 ]{cor['limpa']} {cor['branco']}para MASCULINO{cor['limpa']}
{cor['verde']}[ 2 ]{cor['limpa']} {cor['branco']}para FEMININO\nEscolha a opção: {cor['limpa']}'''))
if sexo == 1:
    print(f'{cor['branco']}Olá, {nome} o alistamento para o sexo masculino é{cor['limpa']} '
          f'{cor['amarelo']}OBIGATÓRIO!{cor['limpa']}')
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade == 18:
        print(f'{cor['branco']}Você nasceu em {ano} tem {idade} anos em {ano_atual}.{cor['limpa']}')
        print(f'{cor['amarelo']}ESTA NA HORA DE SE ALISTAR!{cor['limpa']}')
    elif idade > 18:
        falta_anos = idade - 18
        ano_alis = ano_atual - falta_anos
        print(f'{cor['branco']}Você nasceu em {ano} tem {idade} anos em {ano_atual}.{cor['limpa']}')
        print(f'{cor['vermelho']}ERA PARA TER SE ALISTADO HÁ {falta_anos} ANOS.\nNO ANO {ano_alis}.{cor['limpa']}')
    else:
        falta_anos = 18 - idade
        ano_alis = ano_atual + falta_anos
        print(f'{cor['branco']}Você nasceu em {ano} tem {idade} anos em {ano_atual}.{cor['limpa']}')
        print(f'{cor['verde']}AINDA FALTAM {falta_anos} ANOS! VOCÊ VAI SE ALISTAR EM {ano_alis}{cor['limpa']}!')
else:
    print(f'{cor['verde']}{nome}, você não precisa se alistar. Pois o alistamento '
          f'é obrigatório somente para o sexo masculino.{cor['limpa']}')
