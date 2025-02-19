def escreva(txt):
    palavra = txt
    lista = list(palavra)
    pos = 0
    quant = 0
    while pos <= len(lista):
        quant += 1
        pos += 1
    print("~" * quant)
    print(txt)
    print("~" * quant)


escreva("EXÉRCITO")
escreva("AR CONDICIONADO")
escreva("GUSTAVO GUANABARA")