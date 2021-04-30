medida = float(input('Uma distância em metros '))
dm = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('{} metros corresponde a:'.format(medida))
print('{}mm'.format(mm))
print('{}cm'.format(cm))
print('{}dm'.format(dm))
print('{}dam'.format(dam))
print('{}hm'.format(hm))
print('{}km'.format(km))
