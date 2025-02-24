def interface():
    print("-" * 40)
    print("MENU PRINCIPAL".center(40))
    print("-" * 40)
    print("1 - Ver pessoas cadastradas")
    print("2 - Cadastrar nova Pessoa")
    print("3 - Sair do sistema")

def opçoes(entrada):
    global opcao
    while True:
        try:
            opcao = int(input(entrada))
        except (ValueError, TypeError):
            print("ERRO! Digite um número inteiro válido")
            continue
        except (KeyboardInterrupt):
            print(f"\nExecução interrompida pelo usuário.")
            print("Volte Sempre!")
            break
        else:
            if (opcao < 1 or opcao >= 4):
                print("ERRO! Digite uma opção válida")
            else:
                return opcao

def novoCadastro():
    registro = {}
    while True:
        nome = str(input("Nome: ")).strip()
        if not nome.isalpha():
            print("ERRO! Digite um nome válido.")
            continue

        while True:
            try:
                idade = int(input("Idade: "))
                break  # Sai do loop se a idade for válida
            except (TypeError, ValueError):
                print("ERRO! Digite uma idade válida.")

        registro[nome] = idade
        print(f"Novo registro de {nome}")

        continuar = input("Deseja adicionar outra pessoa? (s/n): ").strip().lower()
        if continuar != 's':
            break
    return registro

def cadastrados(registro):
    if not registro:
        print("Nenhuma pessoa cadastrada")
    else:
        print("-" * 40)
        print("PESSOA CADASTRADAS".center(40))
        print("-" * 40)
        for nome, idade in registro.items():
            print(f"{nome}: {idade} anos")
        print("-" * 40)


def sair():
    print("Saindo sistema...Até mais!")
    exit()