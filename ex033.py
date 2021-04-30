a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
m = a
#Verificando se "a" é o menor...
if b < a and b < c:
    m = b
if c < a and c < b:
    m = c
ma = b
#Verificando se "b" é o maior...
if a > b and a > c:
    a = ma
if c > a and c > b:
    c = ma
print('Menor: {}'.format(m))
print('maior: {}'.format(ma))
