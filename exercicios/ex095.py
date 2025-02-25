tab = dict()
gols = list()
jogador = list()
cont = 0
while True:
    tab.clear()
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
    jogador.append(tab.copy())
    while True:
        continuar = str(input("Quer continuar [S/N]? ")).upper()
        if(continuar in "SN"):
            break
        print("ERRO! Digite S ou N.")
    if(continuar == "N"):
        break
print("-=" * 40)
print(f"{'COD':<4} {'Jogador':<15} {'Gols':<20} {'Total':<5}")
print("-=" * 40)
for k, v in enumerate(jogador):
    print(f"{k:<4} {v['Jogador']:<15} {str(v['Gols']):<20} {v['Total']:<5}")
print("-=" * 40)
while True:
    busca = int(input("Mostrar dados de qual jogador (999 para parar)? "))
    if(busca == 999):
        break
    if(busca >= len(jogador)):
        print("ERRO! JOGADOR NÃO ENCONTRADO!")
    else:
        print(f"DADOS DO JOGADOR {jogador[busca]["Jogador"]}")
        for i, g in enumerate(jogador[busca]["Gols"]):
            print(f"No jogo {i + 1} fez {g} gols")
        print("-=" * 40)
print("FINALIZADO")