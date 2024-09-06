tabela = ('Botafogo','Fortaleza','Palmeiras','Flamengo','Cruzeiro','São Paulo','Bahia','Vasco','Atlético-MG','Internacional','Bragantino','Athletico-PR','Criciúma','Juventude',
'Grêmio','Fluminense','Corinthians','Vitória','Cuiabá','Atlético-GO')

print(f'Tabela do Brasileirão: {tabela}')
print('-=' * 20)
print(f'Os 5 primeiros são: {tabela[0:5]}')
print('-=' * 20)
print(f'Os 4 últimos são: {tabela[len(tabela) - 1: len(tabela) - 5: -1]}')
print('-=' * 20)
print(sorted(tabela))
print('-=' * 20)
print(f'O Grêmio está na {tabela.index('Grêmio') + 1}ª posição na tabela')

