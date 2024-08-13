vel = int(input('Digite a velocidade em que você dirigia:'))
km= vel - 80
multa = km * 7
if vel > 80:
    print('Você estava acima do limite de velocidade. Você foi multado!')
    print('O valor da multa é {}'.format(multa))
else:
    print('Você estava dirigindo dentro do limite de volocidade!')