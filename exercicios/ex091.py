alunos = dict()
alunos['Nome'] = str(input("Nome: "))
alunos['Média'] = float(input("Média: "))
if(alunos['Média'] >= 7):
    alunos['Situação'] = 'Aprovado'
else:
    alunos['Situação'] = 'Reprovado'
for k, v in alunos.items():
    print(f'{k} do aluno é {v}')