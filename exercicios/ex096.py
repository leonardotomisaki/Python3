def linha():
    print("-=" * 10)
def area(larg, comp):
    area = larg * comp
    print(f"A área de um terreno {larg} X {comp} é de {area}m²")

linha()
print("CALCULADORA DE ÁREA")
linha()
larg = float(input("Largura (M): "))
comp = float(input("Comprimento (M): "))
area(larg, comp)




def area():
    larg = float(input("LARGURA (m): "))
    comp = float(input("COMPRIMENTO (m): "))
    total = larg * comp
    print(f"A área de um terreno {larg}X{comp} é de {total}m²")

def linha():
    print("-" * 30)

print("CONTROLE DO TERRENO")
linha()
area()
