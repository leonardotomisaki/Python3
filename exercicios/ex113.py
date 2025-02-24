def leiaInt(entrada):
    while True:
        try:
            num = int(input(entrada))
        except(ValueError, TypeError):
            print("ERRO! Por favor digite um número inteiro válido.")
            continue
        except (KeyboardInterrupt):
            print("Execução interrompida pelo usuário.")
            return 0
        else:
            return num

def leiaFloat(entrada):
    while True:
        try:
            num = float(input(entrada))
        except (ValueError, TypeError):
            print("ERRO! Por favor digite um número real válido.")
            continue
        except KeyboardInterrupt:
            print("Execução interrompida pelo usuário.")
            return 0
        else:
            return num
#Programa Principal
i = leiaInt("Digite um número inteiro: ")
r = leiaFloat("Digite um número real: ")
print(f"O valor inteiro foi {i} e valor real foi {r}! ")
