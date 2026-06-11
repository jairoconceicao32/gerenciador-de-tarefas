from src.controllers.controller import create, read, delete

def show_created(manager):
    nome = str(input("Digite o nome da tarefa a ser criada: "))
    descricao = str(input("Digite a descrição da tarefa a ser criada: "))
    success, result = create(nome, descricao, manager)
    if success:
        print(f"Tarefa criada com o id {result.task_id}")
    else:
        print(f"Erro {result}")

def view_tasks(manager):
    result= read(manager)
    if not result:
        print("Nenhuma tarefa cadastrada no sistema.")
        return
    for i in result:
        print(
            f"Identificador da tarefa: {i.task_id}\n"
            f"Nome da tarefa {i.name}\n"
            f"Descrição da tarefa {i.description}"
        )

def show_deleted(manager):
    task_id = str(input("Informe o identificador da tarefa a deletar: "))
    success, result=delete(task_id, manager)
    if success:
        print(f"Tarefa com o identificador {task_id} deletada com sucesso")
    else:
        print(f"{result}")