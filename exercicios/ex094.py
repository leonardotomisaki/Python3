lista = list()
dado = dict()
soma = 0
media = 0
while True:
    dado.clear()
    dado["Nome"] = str(input("Nome: "))
    while True:
        dado["Sexo"] = str(input("Sexo [M/F]: ")).upper()
        if(dado["Sexo"] in "MF"):
            break
        print("ERRO! Responda apenas M ou F.")
    dado["Idade"] = int(input("Idade: "))
    lista.append(dado.copy())
    soma += dado["Idade"]
    media = soma / len(lista)
    while True:
        continuar = str(input("Quer continuar [S/N]? ")).upper()
        if(continuar in "SN"):
            break
        print("ERRO! Responda apenas S ou N.")
    print("-" * 30)
    if(continuar == "N" or continuar == "n"):
        break
print()
print(lista)
print()
print("-" * 30)
print(f"- Foram cadastradas {len(lista)}")
print(f"- A média de idade das pessoas cadatradas é {media:5.2f} anos")
print(f"- As mulheres cadastradas foram: ", end="")
for p in lista:
    if(p["Sexo"] in "Ff"):
        print(f"{p["Nome"]}", end=" ")
print()
print(f"- Lista das pessoas com idade acma da média")
print()
for p in lista:
    if(p["Idade"] >= media):
        for k,v in p.items():
            print(f"{k} = {v}; ", end="")
        print()
print("FIM!")