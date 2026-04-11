# Divisão de 'string'

# Split

# O comando 'split', ele gera uma lista com todas as palavras de uma cadeia de caracteres. E eles vão ter
# numerações. Com isso o 'split', vai dividir uma 'string', numa lista. Onde cada elemento será
# separado pelo seu splitador. Para usar o comando é dessa forma: frase.split().

# Ex:

# frase = 'Alan no mundo de python'
# print(frase.split())

# Junção de 'string'

# Join

# Esse comando serve para uma junção de uma cadeia de caracteres, diferente do split.
# Para usar este comando é da seguinte maneira: '-'(ou pode ser com espaço).join(frase)

# frase = 'Alan no mundo de python'
# print('-'.join(frase))

# ou

# frase = 'Alan no mundo de python'
# print(' '.join(frase))

# Bónus

# Se utilizarmos aspas triplas, não iremos precisar dar vários prints para cada frase
# somente colocamos aspas tripla que ficará tudo em um só print.

# Ex:

print("""O horizonte pintava-se de tons violeta enquanto o vento soprava segredos entre
as copas das árvores centenárias. No chão, um relógio de bolso antigo, esquecido pelo tempo,
marcava horas de um fuso horário inexistente. Enquanto isso, o café esfriava sobre a mesa de madeira,
ao lado de um livro aberto na página quarenta e dois, onde uma frase sublinhada a lápis dizia:
nem todos os caminhos levam ao mesmo destino, mas todos ensinam a caminhar'.
O silêncio da tarde era apenas interrompido pelo som rítmico de uma gota de água caindo na pia, lembrando que a vida
assim como os rios, nunca para de fluir, mesmo quando fingimos não nota""")