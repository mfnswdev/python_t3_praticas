# main.py

def cadastrar_produto(produtos):
    print("\n=== Cadastro de Produto ===")
    codigo = input("Digite o código do produto (13 dígitos numéricos): ")
    
    # Validar código
    if not codigo.isdigit() or len(codigo) != 13:
        print("Código inválido. O código deve conter 13 dígitos numéricos.")
        return

    nome = input("Digite o nome do produto (começando com letra maiúscula): ")
    
    # Validar nome
    if not nome or not nome[0].isupper():
        print("Nome inválido. Deve começar com uma letra maiúscula.")
        return

    preco_str = input("Digite o preço do produto (com duas casas decimais): ")
    
    # Validar preço
    try:
        preco = float(preco_str)
    except ValueError:
        print("Preço inválido. Digite um número válido.")
        return

    produtos.append({"codigo": codigo, "nome": nome, "preco": preco})
    print("Produto cadastrado com sucesso!")

def excluir_produto(produtos):
    print("\n=== Exclusão de Produto ===")
    codigo = input("Digite o código do produto a ser excluído: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return

    print("Produto não encontrado. Verifique o código e tente novamente.")

def listar_produtos(produtos):
    print("\n=== Lista de Produtos ===")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

def consultar_preco(produtos):
    print("\n=== Consulta de Preço ===")
    codigo = input("Digite o código do produto para consultar o preço: ")

    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}")
            return

    print("Produto não encontrado. Verifique o código e tente novamente.")

def main():
    produtos = []  

    while True:
        print("\n=== Menu de Opções ===")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produto(produtos)
        elif opcao == "2":
            excluir_produto(produtos)
        elif opcao == "3":
            listar_produtos(produtos)
        elif opcao == "4":
            consultar_preco(produtos)
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
