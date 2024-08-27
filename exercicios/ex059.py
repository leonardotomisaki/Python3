n1 = int(input('1º número: '))
n2 = int(input('2º número: '))
opcoes = 0
while opcoes != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcoes = int(input('Escolha sua opção: '))
    if opcoes == 1:
        soma = n1 + n2
        print('A soma entre os dois números é {}'.format(soma))
    elif opcoes == 2:
        mult = n1 * n2
        print('A multiplicação entre os dois números é {}'.format(mult))
    elif opcoes == 3:
        maior = 0
        if n1 > n2:
            maior = n1 > n2
            print('O maior número digitado é {}'.format(maior))
        else:
            maior = n2 > n1
            print('O maior número digitado é {}'.format(maior))
    elif opcoes == 4:
        n1 = int(input('Novo 1º número: '))
        n2 = int(input('Novo 2º número: '))
    else:
        print('Opção Inválida. Tente novamente')
print('Fim do Programa!')

