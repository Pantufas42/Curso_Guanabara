s = float(input('Salário atual:'))
a = int(input('Digite o aumento (em porcentagem):'))
p = s + (s * a / 100)
print('O novo salário do funcionário é: {}'.format(p))
