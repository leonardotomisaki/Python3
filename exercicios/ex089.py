notas = list()
continuar = ""
soma = 0
while True:
    nome = str(input("Nome: "))
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))
    soma = n1 + n2
    media = soma / 2
    continuar = str(input("Quer continuar [S/N]? "))
    aluno = [nome, [n1, n2], media]
    notas.append(aluno[:])

    if(continuar in "Nn"):
        break
for aluno in notas:
    print(f"Aluno: {aluno[0]}, Notas: {aluno[1]}, Média: {aluno[2]:.2f}")
