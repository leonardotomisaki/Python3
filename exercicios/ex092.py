from datetime import datetime
clt = dict()
clt["Nome"] = str(input("Nome: "))
clt["Nascimento"] = int(input("Ano de Nascimento: "))
clt["Idade"] = datetime.now().year - clt["Nascimento"]
clt["CTPS"] = int(input("Carteira de Trabalho (0 se não tem): "))
if(clt["CTPS"] == 0):
    print("-=" * 30)
    for k,v in clt.items():
        print(f"{k} é {v}")
    exit()
clt["Contratação"] = int(input("Ano de Contratação: "))
clt["Salário"] = float(input("Salário: "))
clt["Aposentadoria"] = clt["Contratação"] + 35
print("-=" * 30)
for k,v in clt.items():
    print(f"{k} é {v}")