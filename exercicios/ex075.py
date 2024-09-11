num = (int(input('1º número: ')),
       int(input('2º número: ')),
       int(input('3º número: ')),
       int(input('4º número: ')),)
print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vez(es)')
if 3 in num:
    print(f'O primeiro número 3 apareceu na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado')
print(f'Tivemos como números pares: ', end='')
for pares in num:
    if pares % 2 == 0:
        print(pares, end=' ')