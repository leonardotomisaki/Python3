import time
def contador(inicio, fim, passo):
    cont = 0
    if inicio < fim:
        if passo == 0:
            passo = 1
        cont = inicio - passo
        while cont < fim:
            cont += passo
            time.sleep(0.4)
            print(cont, end=" ")
            if cont == fim:
                print("FIM!")
    elif inicio > fim:
        if passo == 0:
            passo = 1
        cont = inicio + passo
        while cont > fim:
            cont -= passo
            time.sleep(0.4)
            print(cont, end=" ")
            if cont == fim:
                print("FIM!")
    elif fim == inicio:
        print(f"{inicio} FIM!")

def linha():
    print("-=" * 30)

# Programa Principal
i = 1
f = 10
p = 1
linha()
print(f"Contagem de {i} até {f} de {p} em {p}")
contador(1,10,1)
linha()
i = 10
f = 0
p = 2
print(f"Contagem de {i} até {f} de {p} em {p}")
contador(10, 0, 2)
linha()
print("Personalize uma contagem!")
i = int(input("INÍCIO: "))
f = int(input("FIM: "))
p = int(input("PASSO: "))
print(f"Contagem de {i} até {f} de {p} em {p}")
contador(i, f, p)
linha()