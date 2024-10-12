lista = list()
impar = list()
par = list()
for c in range(0, 7):
    valor = int(input("Digite um número: "))
    lista.append(valor)
    if(valor % 2 == 0):
        par.append(valor)
        par.sort()
    else:
        impar.append(valor)
        impar.sort()
print(f"Lista: {lista}")
print(f"Impares: {impar}")
print(f"Pares: {par}")