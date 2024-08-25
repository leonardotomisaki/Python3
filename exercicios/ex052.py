num = int(input('Digite um número:'))
if num / 1 == num and num / num == 1:
    print('{} é um número primo!'.format(num))
elif num % 2 == 0 or num % 3 == 1:
    print('{} não é número primo!'.format(num))