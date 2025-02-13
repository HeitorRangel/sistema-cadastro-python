from banco_de_dados import criar_tabela, adicionar_usuario, listar_usuarios, atualizar_usuario, remover_usuario

criar_tabela()

def mostrar_menu():
    print("Escolha uma opção:")
    print("1 - Adicionar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Remover usuário")
    print("5 - Sair")

def obter_idade():
    """Função para validar se a idade inserida é um número positivo."""
    while True:
        try:
            idade = int(input("Digite a idade do usuário: "))
            if idade <= 0:
                print("Idade inválida. A idade deve ser um número positivo.")
            else:
                return idade
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

def menu():
    while True:
        mostrar_menu()
        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            idade = obter_idade()  # Aqui chamamos a função para validar a idade
            cidade = input("Digite a cidade do usuário: ")
            adicionar_usuario(nome, idade, cidade)
            print("Usuário adicionado com sucesso!")

        elif opcao == "2":
            usuarios = listar_usuarios()
            if usuarios:
                print("Usuários cadastrados:")
            for usuario in usuarios:
                print(f"ID: {usuario[0]:<5} | Nome: {usuario[1]:<20} | Idade: {usuario[2]:<3} | Cidade: {usuario[3]:<20}")
            else:
                print("Nenhum usuário cadastrado.")


        elif opcao == "3":
            id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
            nome = input("Digite o novo nome do usuário: ")
            idade = obter_idade()  # Aqui também chamamos a função para validar a idade
            cidade = input("Digite a nova cidade do usuário: ")
            atualizar_usuario(id_usuario, nome, idade, cidade)
            print("Usuário atualizado com sucesso!")

        elif opcao == "4":
            id_usuario = int(input("Digite o ID do usuário a ser removido: "))
            remover_usuario(id_usuario)
            print("Usuário removido com sucesso!")

        elif opcao == "5":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
