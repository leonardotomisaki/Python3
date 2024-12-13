def dobro(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] *= 2
        pos += 1


valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobro(valores)
print(valores)
