import os
from empresa import *

def main():
    caminho_arquivo = os.path.abspath("dados_empregados.txt")

    empregados = ler_dados_arquivo(caminho_arquivo)

    while True:
        print("\n=== Empresa ===")
        print("1. Reajustar salários em 10%")
        print("2. Listar informações dos empregados")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            reajusta_dez_porcento(empregados)
            print("Salários reajustados em 10%.")
        elif opcao == "2":
            listar_empregados(empregados)
        elif opcao == "0":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def listar_empregados(empregados):
    if not empregados:
        print("Nenhum empregado cadastrado.")
        return

    print("Lista de empregados:")
    for i, empregado in enumerate(empregados, start=1):
        print(f"{i}. Nome: {empregado['nome']} {empregado['sobrenome']}, Ano de Nascimento: {empregado['ano_nascimento']}, RG: {empregado['rg']}, Ano de Admissão: {empregado['ano_admissao']}, Salário: R${empregado['salario']:.2f}")

if __name__ == "__main__":
    main()
