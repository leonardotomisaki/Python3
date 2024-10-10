banco = list()
dado = list()
for c in range(0,3):
    dado.append(str(input("Digite o nome: ")))
    dado.append(int(input("Digite a idade: ")))
    banco.append(dado[:])
    dado.clear()
totmaior = totmenor = 0
for p in banco:
    if p[1] >= 18:
        print(f"{p[0]} é maior de 18")
        totmaior += 1
    else:
        print(f"{p[0]} é menor de 18 anos")
        totmenor +=1
print(f"Foram registrados {totmaior} pessoas maiores de 18 anos e {totmenor} menores de 18 anos")