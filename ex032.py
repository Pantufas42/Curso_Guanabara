from datetime import date
a = int(input('Ano(0 para o ano atual): '))
b = a % 4
if a == 0:
    a = date.today().year
if b == 0:
    print('O ano {} é bissexto!'.format(a))
else:
    print('O ano {} NÃO é bissexto!'.format(a))
