from random import choice
a1 = str(input('Nome do primeiro candidato: '))
a2 = str(input('Nome do segundo candidato: '))
a3 = str(input('Nome do terceiro candidato :'))
a4 = str(input('Nome do quarto candidato :'))
lista = (a1, a2, a3, a4)
escolhido = choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
