frase = str(input('Digite uma frase:')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if junto == inverso:
    print('A frase é um palindroma.')
else:
    print('A frase não é um palimdromo.')