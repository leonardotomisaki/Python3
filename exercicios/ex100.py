import random


def sorteia():
    lista = []
    for n in range(5):
        numSort = random.randint(1, 20)
        lista.append(numSort)
    print(f"Os números sorteados são {lista}")
    somaPar(lista)
def somaPar(lista):
    soma = 0
    pares = []
    for v in lista:
        if v % 2 == 0:
            pares.append(v)
            soma += v
    print(f"Os números pares encontrados são {pares}")
    print(f"A soma dos núemros pares é {soma}")


# Programa Principal
sorteia()
