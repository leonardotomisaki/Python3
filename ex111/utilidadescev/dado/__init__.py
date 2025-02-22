def leiaDinheiro(msg):
    validador = False
    entrada = str(input(msg)).replace(",", ".").strip()
    while validador is False:

        if entrada.isalpha() or entrada == "":
            print(f"ERRO: '{entrada}' é um preço inválido!")
            entrada = str(input("Digite o preço: ")).replace(",", ".").strip()
        else:
            validador = True
            return float(entrada)



