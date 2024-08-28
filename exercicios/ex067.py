n = tab = resul = 0
while True:
    print('=-'*30)
    n = int(input('Digite o número que você quer saber a tabuada: '))
    print('=-'*30)
    if n < 0:
        break
    for tab in range(1, 11, 1):
        resul = n * tab
        print(f'{n} X {tab} = {resul}')
print('PROGRAMA ENCERRADO.')