# Importando as classes das listas
from class_ListaNomes import ListaNomes
from class_ListaDatas import ListaDatas
from class_ListaSalarios import ListaSalarios
from class_ListaIdades import ListaIdades
from datetime import datetime
from class_Data import Data

# Funções para manipular as listas
def incluir_nome(lista_nomes):
    nome = input("Digite um nome para incluir na lista: ")
    lista_nomes.entradaDeDados(nome)
    print("Nome adicionado com sucesso!")

def incluir_salario(lista_salarios):
    try:
        salario = float(input("Digite um salário para incluir na lista: "))
        lista_salarios.entradaDeDados(salario)
        print("Salário adicionado com sucesso!")
    except ValueError:
        print("Por favor, digite um número válido para o salário.")

def incluir_data(lista_datas):
    try:
        dia = int(input("Digite o dia: "))
        mes = int(input("Digite o mês: "))
        ano = int(input("Digite o ano: "))
        
        nova_data = Data(dia, mes, ano)
        lista_datas.entradaDeDados(nova_data) 
        print("Data adicionada com sucesso!")
    except ValueError:
        print("Por favor, digite uma data válida.")

def incluir_idade(lista_idades):
    try:
        nova_idade = int(input("Digite a idade: "))
        lista_idades.entradaDeDados(nova_idade) 
        print("Idade adicionada com sucesso!")
    except ValueError:
        print("Por favor, digite uma idade válida.")

def percorrer_listas(*listas):
    for lista in listas:
        print(lista)

def calcular_folha_salarial(lista_salarios):
    novo_salario = lista_salarios.calcularReajuste(10)
    print(f"Nova folha salarial com reajuste de 10%: {novo_salario}")

def modificar_datas(lista_datas):
    lista_datas.modificarDatasAnteriores2019()
    print("Datas modificadas conforme especificado!")

# Menu de opções
def menu():
    # Cria instâncias das listas
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    while True:
        print("\nMenu de Opções:")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes, datas, salários e idades")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_nome(nomes)
        elif opcao == "2":
            incluir_salario(salarios)
        elif opcao == "3":
            incluir_data(datas)
        elif opcao == "4":
            incluir_idade(idades)
        elif opcao == "5":
            percorrer_listas(nomes, datas, salarios, idades)
        elif opcao == "6":
            calcular_folha_salarial(salarios)
        elif opcao == "7":
            modificar_datas(datas)
        elif opcao == "8":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    menu()
