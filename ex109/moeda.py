def aumentar(p=0, porcent=0, format=False):
    porcentagem = (porcent/100) * p
    aumento = p + porcentagem
    return aumento if format is False else moeda(aumento)
def diminuir(p, porcent = 0, format=False):
    porcentagem = (porcent/100) * p
    reduzido = p - porcentagem
    return reduzido if format is False else moeda(reduzido)
def dobro(p = 0, format=False):
    dobro = p * 2
    return dobro if format is False else moeda(dobro)

def metade(p = 0, format=False):
    divido = p / 2
    return divido if format is False else moeda(divido)

def moeda(p = 0, moeda = "R$"):
    return f"{moeda}{p:.2f}".replace(".", ",")