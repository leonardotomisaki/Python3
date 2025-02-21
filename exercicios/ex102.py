def fatorial(n=1, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            if c > 1:
                print(c, end=" x ")
            else:
                print(c, end=" = ")
    return f

# Programa Principal
print(fatorial(5, True))