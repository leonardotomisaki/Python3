matriz = list()
for p in range(0, 9):
     matriz.append(int(input(f"Digite o {p + 1}º número: ")))

print("=-" * 30)
print(f"[  {matriz[0]}  ][  {matriz[1]}  ][  {matriz[2]}  ]")
print(f"[  {matriz[3]}  ][  {matriz[4]}  ][  {matriz[5]}  ]")
print(f"[  {matriz[6]}  ][  {matriz[7]}  ][  {matriz[8]}  ]")