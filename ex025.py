n = str(input('Qual é o seu nome? ')).strip()
#Meu jeito fedido:
#n = str(input('Qual é o seu nome? ')).strip()
#np = (n[0:].lower() == 'bauchspiess')
#print('É da família? {}'.format(np))
#Jeito ipeto do Guanabara:
n = str(input('Qual é o seu nome? ')).strip()
print('Você é da família? {}'.format('bauchspiess' in n.lower))

