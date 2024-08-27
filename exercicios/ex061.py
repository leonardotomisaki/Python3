n = int(input('1º termo: '))
razao = int(input('Digite a Razão: '))
termo = n
cont = 1
while cont <= 10:
    print('{} - '.format(termo), end='')
    termo = termo + razao
    cont = cont + 1
print('FIM!')
