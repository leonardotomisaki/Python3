import random
import time
from operator import itemgetter
sorteio = dict()
lista = list()
for c in range(0, 4):
    sorteio[f'Jogador {c + 1}'] = random.randint(1, 6)
print("VALORES SORTEADOS")
ranking = list()
for k, v in sorteio.items():
    time.sleep(0.5)
    print(f'O {k} tirou {v}')
print("-=" * 30)
print("RANKING DOS JOGADORES")
ranking = sorted(sorteio.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i + 1}º lugar: {v[0]} com {v[1]}")
