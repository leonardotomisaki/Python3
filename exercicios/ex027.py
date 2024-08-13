nome = str(input('Digite seu Nome:'))
div = nome.split()
PN = div[0]
UN = div[len(div)-1]
print('Seu primeiro nome é {}'.format(PN))
print('Seu último nome é {}'.format(UN))
