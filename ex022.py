n = str(input('Nome completo:')).strip()
nma = n.upper
nmi = n.lower
print('Analisando.......')
print('Seu nome em maiúsculas: {}'.format(nma))
print('Seu nome em minúsculas: {}'.format(nmi))
print('Seu nome tem {} letras'.format(len(n)-n.count(' ')))
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
