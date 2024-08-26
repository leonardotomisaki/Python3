maior = 0
menor = 0
for peso in range(1, 6):
    massa = float(input('Peso da {}ª pessoa:'.format(peso)))
    if peso == 1:
        maior = massa
        menor = massa
    else:
        if massa > maior:
            maior = massa
        if massa < menor:
            menor = massa
print('O maior peso registrado é {}KG'.format(maior))
print('O menor peso registrado é {}KG'.format(menor))