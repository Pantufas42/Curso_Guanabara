d = int(input('Por quantos dias o carro foi alugado?'))
km = float(input('Durante esse tempo, por quantos kilômetros ele rodou?'))
p1 = d * 60
p2 = km * 0.15
p3 = p1 + p2
print('Total a pagar: R${:.2f}'.format(p3))
