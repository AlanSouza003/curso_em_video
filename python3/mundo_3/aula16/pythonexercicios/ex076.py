lista_de_compras = (
    "Caneta", 1.99, "Caderno", 10.00, "Lápis de Cor", 6.99, "Grampeador", 7.00,
    "Régua", 3.50, "Calculadora", 20.00, "Mochila", 150.00
)

for posicao, produto in enumerate(lista_de_compras):
    if posicao % 2 == 0:
        print(f"{produto:.<30}", end="")
    else:
        print(f"R${produto:>7.2f}")
    