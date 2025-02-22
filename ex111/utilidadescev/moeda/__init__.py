def aumentar(p=0, porcent=0):
    porcentagem = (porcent/100) * p
    aumento = p + porcentagem
    return moeda(aumento)
def diminuir(p, porcent = 0):
    porcentagem = (porcent/100) * p
    reduzido = p - porcentagem
    return moeda(reduzido)
def dobro(p = 0):
    dobro = p * 2
    return moeda(dobro)

def metade(p = 0):
    divido = p / 2
    return moeda(divido)

def moeda(p = 0, moeda = "R$"):
    return f"{moeda}{p:.2f}".replace(".", ",")

def resumo(p=0, aumento=0, reduçao=0 ):
    a = aumentar(p, aumento)
    r = diminuir(p, reduçao)
    m = metade(p)
    d = dobro(p)
    print("-" * 30)
    print("RESUMO DO PREÇO".center(30))
    print("-" * 30)
    print(" Preço analisado:   ", end="")
    print(moeda(p))
    print(" Dobro do preço:   ", end="")
    print(d)
    print(" Metade do preço:   ", end="")
    print(m)
    print(f" {aumento}% de aumento:   ", end="")
    print(a)
    print(f" {reduçao}% de redução:   ", end="")
    print(r)
    print("-" * 30)
