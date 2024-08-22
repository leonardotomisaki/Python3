import random
print('Vamos jogar Jokenpô!')
print('-=' * 15)
itens = ['PEDRA!', 'PAPEL!', 'TESOURA!']
comp = random.randint(0,2)
print('''Suas opções são:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jog = int(input('Escolha sua jogada:'))
print('-=' * 15)
print('O computador escolheu {}'.format(itens[comp]))
if jog == 1:
    print('Você escolheu PEDRA!')
elif jog == 2:
    print('Você escolheu PAPEL!')
elif jog == 3:
    print('Você escolheu TESOURA!')
else:
    print('Jogada inválida! Tente novamente.')
print('-=' * 15)
if jog == 1 and comp == 0 or jog == 2 and comp == 1 or jog == 3 and comp == 2: # Jogo Empata.
    print('EMPATE!')
elif jog == 1 and comp == 1 or jog == 2 and comp == 2 or jog == 3 and comp == 0 : # Computador Ganha
    print('O Computador GANHOU!')
else: # Jogador Ganha
    print('O Jogador GANHOU!')