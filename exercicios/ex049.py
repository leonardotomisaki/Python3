resul = 0
num = int(input('Digite um valor:'))
print('A tabuada do número {} é:'.format(num))
for tab in range(0, 11, 1):
    resul = num * tab
    print('{} X {} = {}'.format(num, tab, resul))