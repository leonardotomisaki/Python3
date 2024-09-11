palavras = ('chao', 'bolsa', 'computador', 'oculos', 'camisa')

vogais = ''
for vog in range(len(palavras)):
    print(f'\nNa palavra {palavras[vog].upper()} temos as vogais: ', end='')
    for letra in palavras[vog]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')