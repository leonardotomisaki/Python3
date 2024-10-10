exp = str(input("Digite sua expressão: "))
pilha = list()
for simb in exp:
    if simb == "(":
        pilha.append("(")
    elif simb == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) == 0:
    print("A expressão está correta!")
else:
    print("A espressão está errada!")
