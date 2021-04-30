import pygame


n = intstr(input('Digite um número: '))
print('''Digite:
[1] para binário
[2] para octal
[3] para hexadecimal''')
n1 = int(input(': '))
b = bin(n)
o = oct(n)
h = hex(n)
if n1 == 1:
    print('{} para binário é {}'.format(n, b))
elif n1 == 2:
    print('{} para octal é {}'.format(n, o))
elif n1 == 3:
    print('{} para hexadecimal é {}'.format(n, h))
else:
    print('Digite 1, 2 ou 3. Seu fedido!')
