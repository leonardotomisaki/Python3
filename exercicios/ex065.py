n = 0
continuar = ''
cont = 0
soma = 0
media = 0
maior = 0
menor = 0
while continuar != 'N':
    n = int(input('Digite um número: '))
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    cont = cont + 1
    soma = soma + n
    media = soma / cont
    if n == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
print('Você digitou {} números e a média deles é {}'.format(cont, media))
print('O maior valor é {} e o menor valor é {}'.format(maior, menor))


