def aumentar(p = 0, porcent = 0):
    porcentagem = (porcent/100) * p
    aumento = p + porcentagem
    return aumento
def diminuir(p, porcent = 0):
    porcentagem = (porcent/100) * p
    reduzido = p - porcentagem
    return reduzido
def dobro(p = 0):
    dobro = p * 2
    return dobro

def metade(p = 0):
    divido = p / 2
    return divido

def moeda(p = 0, moeda = "R$"):
    return f"{moeda}{p:.2f}".replace(".", ",")