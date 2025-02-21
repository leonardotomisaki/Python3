def leiaInt(msg):
    num = input(msg).strip()
    if num.isdigit() == True:
        return num
    else:
        while num.isdigit() == False:
           print("ERRO DIGITE UM NÚMERO INTEIRO VÁLIDO.")
           num = input(msg).strip()
           if num.isdigit() == True:
                return num
#Programa Principal
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}")