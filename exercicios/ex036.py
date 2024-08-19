casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar?'))
mes = anos * 12
prest = casa / mes
print('De acordo com os dados passados:')
if prest < 30 / 100 * salario:
    print('O valor de prestação mensal é de R$ {}'.format(prest))
else:
    print('Não será possivel realizar o empréstimo, pois o valor de prestação mensal excede 30% de seu salário!')