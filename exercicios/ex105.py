def notas(*notas, sit = False):
    """
    Função para analisar as notas e situação de vários alunos.
    :param notas: Um ou mais notas dos alunos(recebe várias).
    :param sit: Parâmetro opcional, indicando se mostra ou não a situação dos alunos.
    :return: Dicionário com total, maior, menor ,média de notas e situação dos alunos.
    """
    dados = {}
    total = len(notas)
    maior = notas[0]
    menor = notas[0]
    soma = 0
    media = 0
    for nota in notas:
        if maior > nota:
            maior = nota
        elif menor < nota:
            menor = nota
        soma += nota
    media = soma / len(notas)
    dados["Total"] = total
    dados["Maior"] = maior
    dados["Menor"] = menor
    dados["Média"] = media

    if sit == True:
        cond = ""
        if media < 5:
            cond = "RUIM"
        elif media >= 5 and media < 7:
            cond = "RAZOÁVEL"
        else:
            cond = "BOM"
        dados["SITUAÇÃO"] = cond
    print(dados)


#Programa Principal
print("-" * 30)
notas(5, 5, 5, 5, sit = True)
notas(10, 4, 6, 9, sit = True)
help(notas)