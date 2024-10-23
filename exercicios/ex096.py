tab = dict()
jogador = list()

while True:
    tab.clear()
    gols = list()  # Reiniciar a lista de gols para cada jogador
    cont = 0  # Reiniciar o contador para cada jogador
    tab["Jogador"] = str(input("Jogador: "))
    tab["Partidas"] = int(input("Números de partidas jogadas: "))

    for g in range(tab["Partidas"]):  # Corrigir o loop para a quantidade de partidas
        num = int(input(f"Gols na partida {g + 1}: "))
        gols.append(num)
        cont += num

    tab["Gols"] = gols
    tab["Total"] = cont
    jogador.append(tab.copy())

    while True:
        continuar = str(input("Quer continuar [S/N]? ")).upper()
        if continuar in "SN":
            break
        print("ERRO! Digite S ou N.")

    if continuar == "N":
        break

# Exibição do gráfico com espaçamento melhorado
print("-=" * 40)
print(f"{'COD':<4} {'Jogador':<15} {'Gols':<20} {'Total':<5}")
print("-=" * 40)

for k, v in enumerate(jogador):
    print(f"{k:<4} {v['Jogador']:<15} {str(v['Gols']):<20} {v['Total']:<5}")

print("-=" * 40)
