from datetime import date
ano = int(input('Digite seu ano de nascimento:'))
data = date.today().year
idade = data - ano
tempo= idade - 18
print('Quem nasceu em {} tem {} anos.'.format(ano, idade))
if idade < 18:
    print('Faltam {} anos para você se alistar no exército!'.format(tempo - tempo - tempo))
    print('Seu alistamento será em {}'.format(data + (18 - idade)))
elif idade == 18:
    print('Este ano você precisa se alistar no exército!')
elif idade > 18:
    print('Já se passaram {} anos, desde que você se alistou!'.format(tempo))
    print('Seu alistamento foi em {}'.format(data - tempo))