v = int(input('Velocidade do carro: '))
v1 = (v - 80) * 7
if v > 80:
    print('Meliante! Multa de {} reais!'.format(v1))
else:
    print('Tenha um bom dia!')
