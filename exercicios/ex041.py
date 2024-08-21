idade = int(input('Digite sua idade:'))
if idade <= 9:
    print(' Sua categoria é:Mirim')
elif idade <= 14:
    print('Sua categoria é: Infantil')
elif idade <= 19:
    print('Sua categoria é:Junior')
elif idade == 20:
    print('Sua categoria é: Sênior')
elif idade > 20:
    print('Sua categoria é: Master')