tab = dict()
gols = list()
cont = 0
tab["Jogador"] = str(input("Jogador: "))
tab["Partidas"] = int(input("Números de partidas jogadas: "))
for g in range(0, tab["Partidas"]):
    num = int(input(f"Gols na partida {g + 1}: " ))
    gols.append(num)
    cont += num
tab["Gols"] = gols
tab["Total"] = cont
print("-=" * 30)
print(tab)
print("-=" * 30)
for k,v in tab.items():
    print(f"{k} é {v}")
print("-=" * 30)
for c in range(0, tab["Partidas"]):
    print(f"    => Na {c + 1}ª Partida: fez {gols[c]} gols")
print(f"Total de Gols: {cont}")
