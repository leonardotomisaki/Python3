lista = []
imp = []
par = []

while True:
    valor = int(input("Digite um número: "))
    lista.append(valor)
    continuar = str(input("Quer continuar [S/N]? "))
    if valor % 2 == 0:
        par.append(valor)
    else:
        imp.append(valor)
    if continuar == "N" or continuar == "n":
        break
print("=-" * 30)
print(f"Lista = {lista}")
print(f"Impares = {imp}")
print(f"Pares = {par}")
