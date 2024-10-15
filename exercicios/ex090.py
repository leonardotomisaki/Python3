notas = []
continuar = ""

while True:
    nome = input("Nome: ")
    n1 = float(input("Primeira nota: "))
    n2 = float(input("Segunda nota: "))

    # Calcula a média das notas
    media = (n1 + n2) / 2

    # Cria uma sublista com o nome, as notas e a média
    aluno = [nome, [n1, n2], media]

    # Adiciona a sublista à lista principal
    notas.append(aluno)

    continuar = input("Quer continuar [S/N]? ").strip().upper()

    if continuar == "N":
        break

# Exibe a lista com nomes, notas e médias dos alunos
for aluno in notas:
    print(f"Aluno: {aluno[0]}, Notas: {aluno[1]}, Média: {aluno[2]:.2f}")