brasil = list()
estado = dict()
for c in range(0, 3):
    estado['UF'] = str(input("Unidade Federativa: "))
    estado['Sigla'] = str(input("Sigla do Estado: "))
    brasil.append(estado)
print(brasil)