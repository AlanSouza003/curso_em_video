tupla_de_palavras = (
    "python", "alfabeto", "java", "linguagem", "html", "foco", "aprendendo",
    "fe", "node", "javascript", "comida", "lanche", "escola", "igreja"
)

for palavra in tupla_de_palavras:
    print(f'\nNa palavra {palavra.upper()} temos', end=' ')
    for vogais in palavra:
        if vogais in "aeiou":
            print(vogais, end=' ')