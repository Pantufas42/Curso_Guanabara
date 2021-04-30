# Jeito trabaiador:
# n = str(input('Nome: ')).strip()
# n2 = n.split()
# print('Seu primeiro nome é {}'.format(n2[0]))
# print('Seu último nome é {}'.format(n2[len(n2)-1]))
# Jeito brazuca:
n = str(input('Digite seu nome todo: ')).split()
# se vc usar o split sua lista terá a primeira palavra como 0 e assim por diante, as se vc colocar -1, ele vai direto
# na última palavra e o -2 vai na penúltima e asim por diante, se vc digitar uma frase com 20 palavras e colocar -20,
# ele vai direto na primeira palavra
print('Seu primeiro nome é {} e seu último nome é {}.'.format(n[0], n[-1]))
