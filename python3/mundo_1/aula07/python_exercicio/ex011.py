l = float(input('Qual a largura da parede em metros: '))
a = float(input('Qual a altura da parede em metros: '))
s = l * a
t = s/2
print('A sua parede tem uma dimensão de {}x{} e sua área é de {:.3f}m².'.format(l, a, s))
print('Para pintar a sua parede você precisa de {0}l de tinta para poder pinta-la.'.format(t))
