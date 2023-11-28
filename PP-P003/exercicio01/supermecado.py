produtos = []

def inserir_produtos():
    codigo = input("Digite o codigo do produto (4 caracteres): ")
    while len(codigo) != 4 or not codigo.isdigit():
        print("Código inválido. Deve conter 4 caracteres.")
        codigo = input("Digite o codigo do produto (4 caracteres): ")
        
    nome = input("Digite o nome do produto: ").capitalize() 
    try:
        preco = float(input("Digite o preço do produto: "))
    except:
        print('Insira um valor numérico.')   
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco})
    print("Produto cadastrado com sucesso !!.")
    

def excluir_produto():
    codigo = input("Digite o codigo do produto a ser excluido: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            produtos.remove(produto)
            print("Produto Removido Com Sucesso!!")
            return
    print("Produto não encontrado!!")
    
def listar_produtos():
    if not produtos:
        print("Nenhum Produto Cadastrado!!!")
        return
    
    print("Lista de Produtos:")
    for i, produto in enumerate(produtos, start=1):
        print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: {produto['preco']:.2f}")   

def consultar_precos():
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto["codigo"] == codigo:
            print(f"O preço do produto {produto['nome']} é R${produto['preco']:.2f}")
            return
    print("Produto não encontrado.")
    
