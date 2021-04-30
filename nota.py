n1 = float(input('Primeiro semestre: '))
n2 = float(input('Segundo semestre: '))
m = (n1 + n2) / 2
if m < 6:
    print('Sua média foi {:.0f}. Reprovado!'.format(m))
else:
    print('Sua média foi {:.0f}. Aprovado!'.format(m))
