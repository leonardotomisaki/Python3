soma = 0
media = 0
nome_velho = 0
maior_idade = 0
tot_mulher = 0
for p in range(1, 5):
    print('------ {}ªPESSOA ------'.format(p))
    nome = str(input('Nome:')).strip().upper()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo:')).strip().upper()
    soma = soma + idade
    if p == 1 and sexo == 'M':
        maior_idade = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade:
        maior_idade = idade
        nome_velho = nome
    if sexo == 'F' and idade > 20:
         tot_mulher = tot_mulher + 1
media = soma / 4
print('A média de idade entre as 4 pessoas é {}'.format(media))
print('O homem mais velho registrado é o {}, e ele tem {} anos'.format(nome_velho, maior_idade))
print('Há {} mulheres com mais de 20 anos'.format(tot_mulher))

