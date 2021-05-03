n = str(input('Qual é o seu nome? ')).strip()
#Meu jeito burro:
#n = str(input('Qual é o seu nome? ')).strip()
#np = (n[0:].lower() == 'bauchspiess')
#print('É da família? {}'.format(np))
#Jeito esperto do Guanabara:
n = str(input('Qual é o seu nome? ')).strip()
print('Você é da família? {}'.format('bauchspiess' in n.lower))

