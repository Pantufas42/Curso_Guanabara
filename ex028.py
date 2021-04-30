from random import choice
from time import sleep
import playsound
print('Vou pensar em um número de 0 a 5...')
sleep(2)
print('Processando...')
sleep(5)
print('Pronto! Pensei!')
sleep(1)
n = int(input('Agora adivinhe que número eu pensei!\n:'))
c = (0, 1, 2, 3, 4, 5)
d = choice(c)
if d == n:
    playsound.playsound('ex028(miseravi).mp3')
    sleep(2)
    print('Acertô miseravi!')
else:
    playsound.playsound('ex028.mp3')
    sleep(2)
    print('ERRRRRROU (pensei no {})'.format(d))
