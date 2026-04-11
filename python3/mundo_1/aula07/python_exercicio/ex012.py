preco = float(input('Qual o valor do produto? R$'))
desconto =  preco - (5/100*preco)
print('O valor do produto é R${}. Com 5% de desconto passa a ficar por R${:.2f}'.format(preco,desconto))
