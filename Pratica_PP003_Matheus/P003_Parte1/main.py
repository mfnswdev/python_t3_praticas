from supermecado import *

def main():
    while True:
        print("\n=== Supermercado ===")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_produtos()
        elif opcao == "2":
            excluir_produto()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            consultar_precos()
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()