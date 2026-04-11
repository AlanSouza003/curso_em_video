n1 = float(input('Digite um valor: '))
km = n1*0.001
hm = n1*0.01
dam = n1*0.1
dm = n1*10
cm = n1*100
mm = n1*1000
print('A medida de {0}m é igual á:'.format(n1))
print('KM = {:.3f}\nHm = {:.3f}\nDAM = {:.2f}\nDm = {:.0f}'.format(km, hm, dam, dm))
print('CM = {:.0f}\nMM = {:.0f}'.format(cm, mm))
