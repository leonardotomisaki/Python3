import random
print('O computador irá pensar em número entre 0 e 10, tente adivinhar o número!')
comp = random.randint(0, 10)
jog = int(input('Adivinhe o número: '))
acertou = False
tent = 0
while not acertou:
    if jog < comp:
        jog = int(input('O número é maior, tente novamente: '))
        tent = tent + 1
    elif jog > comp:
        jog = int(input('O número é menor, tente novamente '))
        tent = tent + 1
    if jog == comp:
        acertou = True
print('Parabéns, você acertou com {} tentativas!'.format(tent))




