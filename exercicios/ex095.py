tab = dict()
lista = list()
gols = list()
cont = 0
while True:
    tab["Jogador"] = str(input("Jogador: "))
    tab["Partidas"] = int(input("Número de partidas jogadas: "))
    lista.append(tab)
    for g in range(0, tab["Partidas"]):
        num = int(input(f"Gols na partida {g + 1}: "))
        gols.append(num)
        cont += num
    continuar = str(input("Quer continuar [S/N]? "))
    if(continuar == "N" or continuar == "n"):
        break
print("-=" * 30)
print("COD NOME             GOLS             TOTAL")
print("-" * 50)
for k,v in tab.items():
    print(f"   {v}               {gols}          {cont}")