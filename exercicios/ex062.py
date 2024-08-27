n = int(input('1º termo: '))
razao = int(input('Digite a Razão: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo = termo + razao
        cont = cont + 1
    print('PAUSA')
    mais = int(input('Quantos mais termos você quer mostrar? '))
print('Progressão finalizada com {} termos!'.format(total))
