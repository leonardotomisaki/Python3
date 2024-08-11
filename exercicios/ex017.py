import math 
co = float(input('Digte comprimento do cateto oposto:'))
ca = float(input('Digite o compimento do adjacente:'))
hi = math.hypot(co, ca)
print('Um triângulo retângulo com cateto oposto de {} e cateto adjacente de {} tem a hipotenusa com valor de {}'.format(co, ca, hi))