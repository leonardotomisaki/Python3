from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8,):
    ano = int(input('Em que ano a {}ª pessoa nasceu:'.format(pessoas)))
    idade = atual - ano
    if idade >= 18:
        totmaior += + 1
    else:
        totmenor += + 1
print('A quantidade de pessoas maiores de idade são {}'.format(totmaior))
print('A quantidade de pessoas menor de idade são {}'.format(totmenor))


