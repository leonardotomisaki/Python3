num1 = int(input('1º número: '))
num2 = int(input('2º número: '))
num3 = int(input('3º número: '))
num4 = int(input('4º número: '))
tupla = (num1, num2, num3, num4)
pares = 0
if num1 % 2 == 0:
    pares = num1
elif num2 % 2 == 0:
    pares = num2
elif num3 % 2 == 0:
    pares = num3
elif num4 % 2 == 0:
    pares = num4
print(f'Você digitou os valores {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vez(es)')
print(f'O primeiro número 3 apareceu na posição {tupla.index(3) + 1}')
print(f'Tivemos como números pares: {pares}')