f = str(input('Uma frase: ')).strip().upper()
print('A letra A aparece {} vezes'.format(f.count('A')))
print('O primeiro A apareceu na posição {}'.format(f.find('A')+1))
#usamos o rfind para o comando find começar a procurar da direita para a esquerda
print('O último A apareceu em {}'.format(f.rfind('A')+1))
