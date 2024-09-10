palavras = ('chao', 'bolsa', 'computador', 'oculos', 'camisa')

vogais = ''
for vog in range(len(palavras)):
    if palavras[vog]:
        vogais = 'aeiou'
    print(f'Na palavra {palavras[vog]} temos as vogais: {vogais} ')