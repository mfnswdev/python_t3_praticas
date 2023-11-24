# Lista de tarefas
tarefas = []

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa registrada.")
        return
    
    print("Lista de tarefas:")
    for idx, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa['realizada'] else "[ ]"
        print(f"{idx}. {tarefa['descricao']} {status}")

def registrar_tarefa():
    descricao = input("Digite a descrição da tarefa a ser registrada: ").capitalize()
    nova_tarefa = {'descricao': descricao, 'realizada': False}
    tarefas.append(nova_tarefa)
    print("Tarefa registrada!!!")

def marcar_como_realizada():
    listar_tarefas()
    idx_tarefa = int(input("Digite o ID da tarefa a ser marcada como realizada: ")) - 1
    if 0 <= idx_tarefa < len(tarefas) and not tarefas[idx_tarefa]['realizada']:
        tarefas.insert(0, tarefas.pop(idx_tarefa))
        tarefas[0]['realizada'] = True
        print("Tarefa marcada como realizada!")
    else:
        print("Tarefa não encontrada ou já realizada.")

def editar_tarefa():
    listar_tarefas()
    idx_tarefa = int(input("Digite o ID da tarefa a ser editada: ")) - 1
    if 0 <= idx_tarefa < len(tarefas):
        nova_descricao = input("Digite a nova descrição da tarefa: ").capitalize()
        tarefas[idx_tarefa]['descricao'] = nova_descricao
        print("Tarefa editada!")
    else:
        print("Tarefa não encontrada.")

# Loop principal do aplicativo
while True:
    print("\n===== ToDoList =====")
    print("1. Listar tarefas")
    print("2. Registrar nova tarefa")
    print("3. Marcar tarefa como realizada")
    print("4. Editar tarefa")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        listar_tarefas()
    elif opcao == "2":
        registrar_tarefa()
    elif opcao == "3":
        marcar_como_realizada()
    elif opcao == "4":
        editar_tarefa()
    elif opcao == "0":
        print("Saindo do aplicativo ToDoList. Até mais!")
        break
    else:
        print("Opção inválida. Escolha novamente.")


