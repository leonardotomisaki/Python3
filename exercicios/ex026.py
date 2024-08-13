frase = input('Digite uma frase:').upper().strip()
print('Nessa frase aparece {} vezes a letra A'.format(frase.count('A')))
print('A primeira letra A aparece na posição {}'.format(frase.find('A') + 1))
print('A última letra A aparece na posição {}'.format(frase.rfind('A') + 1))