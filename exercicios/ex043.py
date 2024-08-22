peso = float(input('Digite seu peso em kg:'))
altura = float(input('Digite sua altura em metros:'))
imc = peso / altura ** 2
print('De a cordo com o seu peso de {} kg e altura de {} metros.'.format(peso, altura))
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print('Voce está no peso ideal!')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso!')
elif imc >= 30 and imc < 40:
    print('Você está com obesidade!')
else:
    print('Você está com obesidade mórbida!')