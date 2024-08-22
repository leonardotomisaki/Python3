num = int(input('Digite um número inteiro:'))
print('''Escolha uma das ddas bases para conversão:
[ 1 ]  converter para BINÁRIO
[ 2 ]  converter para OCTAL
[ 3 ]  converter para HEXADECIMAL''')
opçao = int(input('Escolha sua opção:'))
if opçao == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num, bin(num)[2:]))
elif opçao == 2:
    print('O número {} convertido para OCTAL é {}'.format(num, oct(num)[2:]))
elif opçao == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')