prod = continuar = caro =''
preço = cont = total = 0
print('-=' * 20)
print('LOJA TECH DO JAPA')
print('-=' * 20)
while True:
    prod = str(input('Produto: '))
    preço = float(input('Preço: '))
    print('-=' * 20)
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    print('-=' * 20)
    total = total + preço
    if preço > 1000:
        cont += 1
    if continuar == 'N':
        print(f'O valor total de sua compra será de {total:.2f}')
        print(f'Foram registrados {cont} produtos com valor acima de R$1000.00')
