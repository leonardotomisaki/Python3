import datetime
atual = datetime.date.today().year
ano = 0
idade = 0
for maior in range(0, 8, idade >= 18):
    ano = int(input('Digite seu ano de nascimento:'))
    idade = atual - ano
    print('Dos 7 anos digitados {} são de maioridade'.format(maior))
    print('Dos 7 anso digitados {} não são miore de idades'.format(maior))
