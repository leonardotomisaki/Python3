import math
n = int(input('Digite um número: '))
c = n
f = 0
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = math.factorial(n)
    c = c - 1
print('{}'.format(f))
