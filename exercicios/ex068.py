import random
Par_Imp = venc = ''
comp = jog = soma = cont = Cont_Comp = Cont_Jog = 0
print('-=' * 20)
print('IMPAR OU PAR')
print('-=' * 20)
while True:
    Par_Imp = str(input('Escolha IMPAR OU PAR: ')).upper().strip()
    comp = random.randint(1, 11)
    jog = int(input('Jogue um número: '))
    print(f'Computador: {comp}')
    print('-=' * 20)
    soma = comp + jog
    cont = cont + 1
    if Par_Imp == 'IMPAR' and soma % 2 != 0:
        print('Jogador Ganhou!')
        venc = 'Jogador'
        if venc == 'Jogador':
            Cont_Jog = Cont_Jog + 1
    elif Par_Imp == 'IMPAR' and soma % 2 == 0:
        print('Computador Ganhou!')
        venc = 'Computador'
        if venc == 'Computador':
            Cont_Comp = Cont_Comp + 1
    elif Par_Imp == 'PAR' and soma % 2 != 0:
        print('Computador Ganhou!')
        venc = 'Computador'
        if venc == 'Computador':
            Cont_Comp = Cont_Comp + 1
    elif Par_Imp == 'PAR' and soma % 2 == 0:
        print('Jogador Ganhou!')
        venc = 'Jogador'
        if venc == 'Jogador':
            Cont_Jog = Cont_Jog + 1
    if venc == 'Computador':
        print(f'''De {cont} partida(s):
    O jogador ganhou {Cont_Jog} vez(es) e computador ganhou {Cont_Comp} vez(es)''')
        break
print('-=' * 20)
print('PROGRAMA FINALIZADO')
