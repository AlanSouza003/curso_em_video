import moeda

# TODO: Main Program

value = float(input("Digite um valor: R$"))
print(f"A metade de {moeda.moeda(value)} é {moeda.half(value, False)}")
print(f"O dobro de {moeda.moeda(value)} é {moeda.double(value, True)}")
print(f"Com aumento de 10% temos {moeda.rise(value, 10, True)}")
print(f"Reduzindo em 13% temos {moeda.cutback(value, 13, True)}")