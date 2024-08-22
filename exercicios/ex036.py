casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar?'))
prest = casa / (anos * 12)
min = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos.'.format(casa, anos))
print('O valor de prestação mensal é de R$ {:.2f}'.format(prest))
if prest <= min:
    print('Empréstimo pode ser Concedido!')
else:
    print('Não será possivel realizar o empréstimo, pois o valor de prestação mensal excede 30% de seu salário!')