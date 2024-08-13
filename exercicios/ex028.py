from random import randint
comp = randint(0, 5)
print('O computador irá escolher um número entre 0 e 5, tente adivinhar o número!')

adv = int(input('Adivinhe o número escolhido pelo computador entre 0 e 5:'))
print('O número que escolhi é {}'.format(comp))