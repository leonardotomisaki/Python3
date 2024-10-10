lista = []
menor = 0
maior = 0
pos_maior = 0
pos_menor = 0
for pos in range(0, 5):
    lista.append(int(input("Digite um número: ")))
    if(pos == 0):
        maior = menor = lista[pos]
        pos_maior = pos
        pos_menor = pos
    elif(lista[pos] > maior):
        maior = lista[pos]
        pos_maior = pos
    elif(lista[pos] < menor):
        menor = lista[pos]
        pos_menor = pos
print("=-" * 30)
print(f"Lista: {lista}")
print(f"O maior valor registrado foi {maior}, e está nas posições: ", end="")
for i, v in enumerate(lista):
    if v == maior:
        print(f"{i}... ", end='')
print()
print(f"O menor valor registrado foi {menor}, e está nas posições: ", end="")
for i, v in enumerate(lista):
    if v == menor:
        print(f"{i}... ", end="")