s = float(input('\033[1;mSalário do trabalhador: R$'))
s1 = s / 100 * 10 + s
s2 = s / 100 * 15 + s
if s > 1250:
    print('\033[1;31mNovo salário: R${:.2f}'.format(s1))
else:
    print('\033[1;31mNovo salário: R${:.2f}'.format(s2))

