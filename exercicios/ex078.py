lista = []
menor = 0
maior = 0
c_maior = 0
c_menor = 0
for valores in range(0, 5):
    lista.append(int(input("Digite um valor: ")))

for c, v in enumerate(lista):
    if c == 0:
        maior = v
        menor = v
        c_maior = c
        c_menor = c
    elif v > maior:
        maior = v
        c_maior = c
    elif v < menor:
        menor = v
        c_menor = c
print(f"O maior valor registrado foi {maior}, e está localizado na posição {c_maior}")
print(f"O menor valor registrado foi {menor}, e está localizado na posição {c_menor}")