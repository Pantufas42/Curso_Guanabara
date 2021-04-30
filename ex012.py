p = float(input('Digite o preço: R$'))
d = int(input('Digite o desconto (em porcentagem):'))
n = p - (p * d / 100)
print('Preço antigo:{:.2f}\nPreço com desconto de {}%: {:.2f}'.format(p, d, n))
