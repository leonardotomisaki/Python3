import random
comp = list()
print("=" * 20)
print(" JOGA DA MEGA SENA")
print("=" * 20)
jogos = int(input("Quantos jogo você quer sortear? "))
for c in range(jogos):
    simp = []
    for num in range(0, 6):
        valores = random.randint(1,60)
        simp.append(valores)
    comp.append(simp)
for sort in range(0, jogos):
    print(f"Jogo {sort + 1}: ",end="")
    print(f"{comp[sort]}")