def ficha(nome = "<desconhecido>", gols = 0):
    print(f"O jogador {nome} fez {gols} gols na temporada!")

# Programa Principal
jogador = input("Nome do jogador: ").strip()
num = input("Número de gols: ").strip()
if jogador == "":
    jogador = "<desconhecido>"
if num.isdigit():
    num = int(num)
else:
    num = 0
ficha(jogador, num)
