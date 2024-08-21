prod = float(input('Digite o valor do produto:'))
pag = str(input('Digite a forma de pagamento:')).strip().upper()
vista = (10 / 100) * prod
cartao = (5 / 100) * prod - prod
x3 = (20 / 100) * prod + prod

if pag == 'DINHEIRO' or pag == 'CHEQUE':
    print('O valor do seu produto com 10% de desconto é {}'.format(prod - vista))
elif pag == 'CARTÃO A VISTA':
    print('O valor do seu produto com desconto é {}'.format(prod - cartao))
elif pag == '3X OU MAIS':
    print('O valor de seu produto com 20% de juros é {}'.format(x3))
else:
    print('Forma de Pagamento não aceito')