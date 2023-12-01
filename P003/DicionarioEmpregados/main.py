# main.py
import os

def reajusta_dez_porcento(empregados):
    # Função para reajustar o salário de cada empregado em 10%
    for empregado in empregados:
        empregado["salario"] *= 1.10  # Aumenta o salário em 10%

def carregar_dados_arquivo(nome_arquivo):
    # Função para ler dados de empregados de um arquivo e armazenar em uma lista
    empregados = []
    try:
        with open(nome_arquivo, 'r') as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(',')
                empregado = {
                    "nome": dados[0],
                    "sobrenome": dados[1],
                    "ano_nascimento": int(dados[2]),
                    "RG": dados[3],
                    "ano_admissao": int(dados[4]),
                    "salario": float(dados[5])
                }
                empregados.append(empregado)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")
    return empregados

def main():
    #arquivo_dados = "./funcionarios.txt"
    #empregados = carregar_dados_arquivo(arquivo_dados)

    arquivo_dados = os.path.abspath("funcionarios.txt")

    empregados = carregar_dados_arquivo(arquivo_dados)

    while True:
        print("\n=== Menu de Opções ===")
        print("1. Reajustar salários em 10%")
        print("2. Exibir informações dos empregados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            reajusta_dez_porcento(empregados)
            print("Salários reajustados em 10%.")
        elif opcao == "2":
            print("\n=== Informações dos Empregados ===")
            for empregado in empregados:
                print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, Ano de Nascimento: {empregado['ano_nascimento']}, RG: {empregado['RG']}, Ano de Admissão: {empregado['ano_admissao']}, Salário: R${empregado['salario']:.2f}")
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
