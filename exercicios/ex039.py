from datetime import date
ano = int(input('Digite seu ano de nascimento:'))
data = date.today().year
idade = data - ano
tempo= idade - 18
if idade < 18:
    print('Faltam {} anos para você se alistar no exército!'.format(tempo - tempo - tempo))
elif idade == 18:
    print('Este ano você precisa se alistar no exército!')
elif idade > 18:
    print('Já se passaram {} anos, desde que você se alistou!'.format(tempo))