prod = continuar = caro = barato =''
preço = cont = total = menor = 0
print('-=' * 20)
print('LOJA TECH DO JAPA')
print('-=' * 20)
while True:
    prod = str(input('Produto: '))
    preço = float(input('Preço: R$ '))
    print('-=' * 20)
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    print('-=' * 20)
    while continuar not in "SN":
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
    total = total + preço
    if preço > 1000:
        cont += 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço
            barato = prod
    if continuar == 'N':
        break
print(f'O valor total de sua compra será de {total:.2f}')
print(f'Foram registrados {cont} produtos com valor acima de R$1000.00')
print(f'O nome do produto mais barato é {prod} e ele custa R${menor}')
