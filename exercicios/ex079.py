lista = []
continuar = ""
valor = 0
while True:

    valor = int(input("Digite um número: "))
    if valor not in lista:
        lista.append(valor)
    else:
        lista.append(valor)
        lista.pop()
    continuar = str(input("Quer continuar? "))
    if continuar == "N" or continuar == "n":
        break
print(lista)