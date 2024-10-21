import random
import time
sorteio = dict()
lista = list()
for c in range(0, 4):
    sorteio[f'Jogador {c + 1}'] = random.randint(1, 6)
print("VALORES SORTEADOS")
for k, v in sorteio.items():
    time.sleep(0.5)
    print(f'O {k} tirou {v}')
print("-=" * 30)
print("RANKING DOS JOGADORES")
lista.append(sorteio.copy())