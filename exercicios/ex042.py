r1 = float(input('Primeira reta:'))
r2 = float(input('Segunda reta:'))
r3 = float(input('Terceira reta:'))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('É possivel formar um triângulo ', end='')
    if r1 != r2 and r2 != r3:
        print('ESCALENO!')
    elif r1 == r2 and r2 == r3:
        print('EQUILÁTERO!')
    else:
        print('ISÓSCELES!')
else:
    print('Não é possivel formar um triângulo com essas medidas!')
