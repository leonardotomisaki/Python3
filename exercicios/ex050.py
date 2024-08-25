s = 0
num = 0
cont = 0
for c in range(1, 6, num % 2 == 0):
    num = int(input('Digite o {} valor:'.format(c)))
    if num % 2 == 0:
        s = s + num
        cont = cont + 1
print('A soma entre os {} números pares digitados é {}'.format(cont, s))