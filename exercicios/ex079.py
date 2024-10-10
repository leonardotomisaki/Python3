lista = []
continuar = ""
valor = 0
while True:
    valor = int(input("Digite um número: "))
    if valor not in lista:
        print("Valor adicionado")
        lista.append(valor)
    else:
        print("Valor já encontrado! Valor não adicionado!")
    lista.sort()
    continuar = str(input("Quer continuar? "))
    if continuar == "N" or continuar == "n":
        break
print(lista)