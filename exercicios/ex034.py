salario = float(input('Digite seu  salário:'))
maior = 10 / 100 * salario + salario
menor = 15 / 100 * salario + salario
if salario > 1250.00:
    print('O valor de seu salário com aumento é {}'.format(maior))
else:
    print('O valor de seu salário é {}'.format(menor))