n1 = int(input('Digite o primeiro número inteiro:'))
n2 = int(input('Digite o segundo número inteiro:'))

if n1 > n2:
    print('O número {} é maior!'.format(n1))
elif n1 < n2:
    print('O número {} é maior!'.format(n2))
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais!')