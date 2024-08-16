n1 = float(input('Digite o primeiro número:'))
n2 = float(input('Digite o segundo número:'))
n3 = float(input('Digite o terceiro número:'))
if n1<n2 and n1<n3:
    print('Dos números que você digitou {} é o menor'.format(n1))
if n2<n1 and n2<n3:
    print('Dos números que você digitou {} é o menor'.format(n2))
if n3<n1 and n3< n2:
     print('Dos números que você digitou {} é o menor'.format(n3))
if n1>n2 and n1> n3:
     print('Dos números que você digitou {} é o maior'.format(n1))
if n2>n3 and n2>n1:
     print('Dos números que você digitou {} é o maior'.format(n2))
if n3>n1 and n3> n2:
    print('Dos números que você digitou {} é o maior'.format(n3))

