def fatorial(n, show = False):
    for f in range(n, 1, -1):
            f *= n
    if show == True:
        for i in range(n, 1, -1):
            print(i, end=" x ")
        print("1 =", f)
    return f

# Programa Principal
print(fatorial(2, True))