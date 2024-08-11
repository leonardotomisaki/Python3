dias = int(input('Quantos dias o carro foi alugado?'))
km = float(input('Quantos km foram rodados?'))
valor = dias * 60 + km * 0.15
print('O valor final a pagar é {:.2f}'.format(valor))