import moeda

# TODO: Main Program

value = float(input("Digite um valor: R$"))
print(f"A metade de {moeda.moeda(value)} é {moeda.moeda(moeda.half(value))}")
print(f"O dobro de {moeda.moeda(value)} é {moeda.moeda(moeda.double(value))}")
print(f"Com aumento de 10% temos {moeda.moeda(moeda.rise(value, 10))}")
print(f"Reduzindo em 13% temos {moeda.moeda(moeda.cutback(value, 13))}")