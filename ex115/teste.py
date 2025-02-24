from ex115 import funçoes
registro = {}
while True:
    funçoes.interface()
    opcao = funçoes.opçoes("Escolha sua opção: ")
    if opcao == 1:
        funçoes.cadastrados(registro)
    elif opcao == 2:
        novos_registros = funçoes.novoCadastro()
        registro.update(novos_registros)  # Atualiza o dicionário com novos registros
    elif opcao == 3:
        funçoes.sair()