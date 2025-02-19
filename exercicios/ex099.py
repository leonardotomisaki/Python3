def maior(* num):
    print("Analisando os valores passados...")
    print(num)
    print(f"Foram informados ao todo {len(num)} números")
    maior = num[0]
    for v in num:
        if v > maior:
            maior = v
    print(f"O maior número encontrado é {maior}")

def linha():
    print("-=" * 30)


linha()
maior(1, 2, 3, 4, 5, 6)
linha()
maior(9, 1, 12, 3, 5)
linha()
print("Escolha os números e a quantidade!")
quant = int(input("QUANTIDADE: "))
lista = []
for n in range(1, quant + 1):
    num = int(input(f"{n}º número: "))
    lista.append(num)
maior(* lista)