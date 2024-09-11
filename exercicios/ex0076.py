list = ('Notebook', 8000,
        'Mouse', 120,
        'Mochila', 150,
        'Teclado', 120,
        'MousePad', 50,
        'Fone', 149.90,
        'Celular', 3200,
        'Pendrive', 100)
print('-'*30)
print(f'{"LISTA DE PREÇOS":^30}')
print('-'*30)
for pos in range(len(list)):
    if pos % 2 == 0:
        print(f'{list[pos]:.<30}', end='')
    else:
        print(f'R${list[pos]:>7.2f}')