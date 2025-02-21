from time import sleep
# Códigos ANSI para cores no terminal
c = {
    1: "\033[41m",  # Fundo Vermelho
    2: "\033[42m",  # Fundo Verde
    3: "\033[43m",  # Fundo Amarelo
    4: "\033[44m",  # Fundo Azul
    5: "\033[45m",  # Fundo Roxo
    6: "\033[47m",  # Fundo Branco
    0: "\033[m"  # Reset (Sem cor)
}
def ajuda(coman):
    titulo(f"Acessando o manual do comando '{coman}'")
    print(c[6], end = "")
    help(coman)
    print(c[0], end = "")

def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(c[cor], end="")
    print("~" * tam)
    print(f"  {msg}")
    print("~" * tam)
    print(c[0], end="")
    sleep(1)
#Programa Principal
comando = ""
while True:
    titulo("SISTEMA DE AJUDA PYHELP", 2)
    comando = str(input("Função ou Biblioteca: "))
    if comando.upper().strip() == "FIM":
        break
    else:
        ajuda(comando)
titulo("ATÉ LOGO!", 1)