lista = []
continuar = ""
valor = 0
cont = 0
while True:
    valor = int(input("Digite um número: "))
    lista.append(valor)
    continuar = str(input("Quer continuar [S/N]? "))
    if valor == 5:
        cont += 1
    if continuar == "N" or continuar == "n":
        break
lista.sort(reverse=True)
print("=-" * 30)
print(f"Foram digitados {len(lista)} números")
print(f"Lista = {lista}")
if cont >= 1:
    print(f"O valor 5 foi digitado, e aparece na lista {cont} vezes")
else:
    print("O número 5 não foi digitado, e não aparece na lista")