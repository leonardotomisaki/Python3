from random import randint
from time import sleep
comp = randint(0, 5)
print('O computador irá escolher um número entre 0 e 5, tente adivinhar o número!')
jog = int(input('Adivinhe o número escolhido pelo computador entre 0 e 5:'))
print('PROCESSANDO...')
sleep(3)
print('O número que escolhi é {}'.format(comp))

if jog == comp:
    print('Parábens você venceu!')
else:
    print('Você perdeu!')