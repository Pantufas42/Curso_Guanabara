c = float(input('\033[1;36mValor casa: R$'))
s = float(input('\033[1;36mSalário: R$'))
a = int(input('\033[1;36mEm quantos anos vai pagar: '))
p = c / (a * 12)
st = s / 100 * 30
if st >= p:
    print('\033[1;32mACEITO!')
elif s == 0:
    print('\033[1;35mVocê é desempregado!')
else:
    print('\033[1;31mRECUSADO!')
