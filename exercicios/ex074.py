import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)
num3 = random.randint(0, 100)
num4 = random.randint(0, 100)
num5 = random.randint(0, 100)
tupla = (num1, num2, num3, num4, num5)
maior = max(tupla)
menor = min(tupla)
print(f'Os números sorteados foram: {tupla}')
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')