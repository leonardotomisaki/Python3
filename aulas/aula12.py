nome = str(input('Qual o seu nome?')).strip()
if nome == 'Leonardo':
    print('Que nome lindo!')
elif nome == 'João' or nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é muito popular no Brasil')
else:
    print('Seu nome é muito normal.')
print('Tenha um bom dia. {}!'.format(nome))