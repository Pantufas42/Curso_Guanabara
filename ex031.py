km = float(input('Sua viagem é de quantos quilômetros?'))
p = km * 0.5
if km > 200:
    p2 = km * 0.45
    print('Total a pagar: {:.1f}'.format(p2))
else:
    print('Total a pagar: {:.1f}'.format(p))
