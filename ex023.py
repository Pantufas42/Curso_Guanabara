#Jeito brasileiro(preguiçoso):
#n = int(input('Digite um número entre 0 e 9999: '))
#n2 = str(int(10000 + n))
#print('O número {} possui, {} milhares.'.format(n, n2[1]))
#print('O número {} possui, {} centenas. '.format(n, n2[2]))
#print('O número {} possui, {} dezenas. '.format(n, n2[3]))
#print('O número {} possui, {} unidades.'.format(n, n2[4]))
#Jeito "Guanabara"(trabaiador):
n = int(input('Número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(n))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
