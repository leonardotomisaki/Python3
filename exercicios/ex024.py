cidade = str(input('Escreva o nome de sua cidade:')).strip()
print('Sua cidade começa com "Santo"? {}'.format(cidade[:5].upper() == 'SANTO'))