n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# print('A soma é {0}, o produto é {1} e a divisão é {2}'.format(s,m,d))
# print('Divisão inteira {0} e potência {1}'.format(di,e))

# Obs: Se quisermos formatar o número para ter apenas duas ou três casa decimais utilizamos o seguinte comando:
# {:.(o número que eu quiser)f}.
# Ex:

# print('A soma é {:.0f}, o produto é {:.2f} e a divisão é {:.3f}'.format(s, m, d))
# print('Divisão inteira {0} e potência {1}'.format(di,e))

# Outra observação sobre o código acima. Como pode ver, o código vai quebra a linha, para que isso não aconteça
# podemos utiliza o seguinte comando ao final do print. Colo camos:, end=''. Assim a linha do código não será
# quebrada.
# Ex:

# print('A soma é {:.0f}, o produto é {:.2f} e a divisão é {:.3f}'.format(s ,m, d), end='')
# print('Divisão inteira {0} e potência {1}'.format(di,e))

# E para quebramos a linha num único print, dessa forma não iremos precisar criar vários prints, somente
# o necessário. Utilizamos o seguinte comando: \n. Assim iremos quebra a linha num único print.
# Ex:

# print('A soma é {:.0f}\nO produto é {:.2f}\nA divisão é {:.3f}'.format(s,m,d))
# print('Divisão inteira {0}\nPotência {1}'.format(di,e))