num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    ent = int(input('Digite um número entre 0 e 20: '))
    if ent >= 0 and ent <= 20:
        break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {num[ent]}')