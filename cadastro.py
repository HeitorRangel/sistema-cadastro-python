from banco_de_dados import (
    criar_tabela, adicionar_usuario, listar_usuarios,
    atualizar_usuario, remover_usuario, exportar_usuarios_csv,
    importar_usuarios_csv
)
from tabulate import tabulate 

criar_tabela()

def mostrar_menu():
    print("\nEscolha uma opção:")
    print("1 - Adicionar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Remover usuário")
    print("5 - Exportar para CSV")
    print("6 - Importar de CSV")
    print("7 - Sair")

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
            idade = obter_idade()  # Validação da idade
            cidade = input("Digite a cidade do usuário: ")
            adicionar_usuario(nome, idade, cidade)
            print("Usuário adicionado com sucesso!")

        elif opcao == "2":
            usuarios = listar_usuarios()
            if usuarios:
                headers = ["ID", "Nome", "Idade", "Cidade"]
                print(tabulate(usuarios, headers=headers, tablefmt="grid"))  
            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == "3":
            try:
                id_usuario = int(input("Digite o ID do usuário a ser atualizado: "))
                nome = input("Digite o novo nome do usuário: ")
                idade = obter_idade()
                cidade = input("Digite a nova cidade do usuário: ")
                atualizar_usuario(id_usuario, nome, idade, cidade)
                print("Usuário atualizado com sucesso!")
            except ValueError:
                print("Erro: O ID deve ser um número inteiro válido.")
    

        elif opcao == "4":
            try:
                id_usuario = int(input("Digite o ID do usuário a ser removido: "))
                if remover_usuario(id_usuario):  
                    print("Usuário removido com sucesso!")
            except ValueError:
                print("Erro: O ID deve ser um número inteiro válido.")


        elif opcao == "5":
            exportar_usuarios_csv()
            print("Dados exportados com sucesso!")

        elif opcao == "6":
            importar_usuarios_csv()
            print("Dados importados com sucesso!")

        elif opcao == "7":
            print("Saindo...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
