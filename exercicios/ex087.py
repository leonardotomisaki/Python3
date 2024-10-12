matriz = list()
valor = 0
par = 0
comuna = 0
for c in range(0, 9):
    valor = int(input(f"Digite o {c + 1}º valor: "))
    matriz.append(valor)
    if(valor % 2 == 0):
        par += valor
coluna = matriz[2] + matriz[5] + matriz[8]
linha = matriz[3] + matriz[4] + matriz[5]
print("-=" * 30)
print(f"[  {matriz[0]}  ][  {matriz[1]}  ][  {matriz[2]}  ]")
print(f"[  {matriz[3]}  ][  {matriz[4]}  ][  {matriz[5]}  ]")
print(f"[  {matriz[6]}  ][  {matriz[7]}  ][  {matriz[8]}  ]")
print("=-" * 30)
print(f"A soma dos números pares é {par}")
print(f"A soma da 3ª coluna é {coluna}")
print(f"A soma da 2ª linha é {linha}")
