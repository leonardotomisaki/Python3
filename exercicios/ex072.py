num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
ent = int(input('Digite um número entre 0 e 20: '))
ind = num[ent]
if ent >= 0 and ent <= 20:
    print(f'Você digitou o número {ind}')
else:
    while ent != ent >= 0 and ent <= 20:
        ent = int(input('Tente novamente. Digite um número entre 0 e 20: '))
        ind = num[ent]
    print(f'Você digitou o número {ind}')