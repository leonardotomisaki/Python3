dado = list()
banco = []
pesados = list()
leves = list()
maior = 0
menor = 0
while True:
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Peso: ")))
    if(len(banco) == 0):
        maior = dado[1]
        menor = dado[1]
    elif(dado[1] > maior):
        maior = dado[1]
    elif(dado[1] < menor):
        menor = dado[1]
    pesados.append(maior)

    leves.append(menor)
    continuar = str(input("Quer continuar [S/N]? "))
    banco.append(dado[:])
    dado.clear()
    pessoas = len(banco)

    if(continuar == "N" or continuar == "n"):
        break

print("-="*30)
print(f"Lista: {banco}")
print(f"Foram cadastrados {pessoas} pessoas.")
print(f"As pessoa(s) mais pesada registrada(s) tem {maior}kg ", end="")
for p in banco:
    if(p[1] == maior):
        print(f"[{p[0]}] ", end="")
print()
print(f"As pessoa(s) mais leve registrada(s) tem {menor}kg ", end="")
for l in banco:
    if(l[1] == menor):
        print(f"[{l[0]}] ", end="")