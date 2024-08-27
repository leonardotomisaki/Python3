n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    cont = cont + 1
    soma = soma + n
    if n == 999:
        cont = cont - 1
        soma = soma - 999
print('Você digitou {} números e soma deles é {}'.format(cont, soma))