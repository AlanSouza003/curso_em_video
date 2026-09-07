import moeda

# TODO: Main Program

value = float(input("Digite um valor: R$"))
print(f"A metade de {value} é R${moeda.half(value)}")
print(f"O dobro de {value} é R${moeda.double(value)}")
print(f"Com aumento de 10% temos R${moeda.rise(value, 10)}")
print(f"Reduzindo em 13% temos R${moeda.cutback(value, 13)}")