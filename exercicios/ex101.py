

def voto(ano):
    global idade
    from datetime import datetime
    idade = datetime.now().year - ano
    print(f"Com {idade} anos: ")
    if idade < 16:
         print("VOTO NEGADO!")
    elif idade >= 16 and idade < 18 or idade > 65:
         print("VOTO OPCIONAL!")
    else:
         print("VOTO OBRIGATÓRIO!")

# Programa Principal
voto(int(input("Ano de Nascimento: ")))
