from src.controllers.controller import create, read, delete
from src.exceptions.errors import ValidationError, NotFoundError, DatabaseError

def show_created(manager):
    nome = str(input("Digite o nome da tarefa a ser criada: "))
    descricao = str(input("Digite a descrição da tarefa a ser criada: "))
    try:
        result = create(nome, descricao, manager)
        print(f"Tarefa criada com o id {result.task_id}")
    except ValidationError as e:
        print(f"Dado inválido: {e}")
    except DatabaseError as e:
        print(f"Erro no banco de dados: {e}")

def view_tasks(manager):
    try:
        result = read(manager)
    except DatabaseError as e:
        print(f"Erro no banco de dados: {e}")
        return
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
    try:
        result=delete(task_id, manager)
        print(f"Tarefa com o identificador {task_id} deletada com sucesso")
    except ValidationError as e:
        print(f"Dado inválido: {e}")
    except NotFoundError as e:
        print(f"Não encontrada: {e}")
    except DatabaseError as e:
        print(f"Erro no banco de dados: {e}")
