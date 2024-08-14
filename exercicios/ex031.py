dist = float(input('Digite a distancia da sua viagem em km:'))
menor = 0.50
maior = 0.45
if dist < 200:
    print('Uma viagem de {} km tem como valor da passagem {}'.format(dist, dist*menor))
else:
    print('Uma viagem de {} km tem como valor da passagem {}'.format(dist, dist*maior))
