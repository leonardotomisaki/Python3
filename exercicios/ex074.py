import random

num = (random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100),random.randint(0, 100))
maior = max(num)
menor = min(num)
print(f'Os números sorteados foram: ', end='')
for valores in num:
    print(f'{valores} ', end='' )
print(f'\nO maior número é {maior}')
print(f'O menor número é {menor}')