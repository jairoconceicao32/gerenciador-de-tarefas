from src.exceptions.errors import InvalidNameError, InvalidDescriptionError, InvalidDeadlineError, InvalidTaskidError, NotFoundError

def create(name, description, manager):
    name = name.strip()
    description = description.strip()
    if len(name) < 4:
        raise InvalidNameError("O nome deve conter pelo menos 4 caracteres.")
    if len(description) < 5:
        raise InvalidDescriptionError("A descrição deve conter pelo menos 5 caracteres.")
    return manager.create_task(name, description)

def read(manager):
    tasks = manager.list_tasks()
    return tasks


def delete(task_id, manager):
    task_id = task_id.strip()
    if task_id == "":
        raise InvalidTaskidError("O ID da tarefa não pode ser vazio.")
    try:
        task_id = int(task_id)
    except ValueError:
        raise InvalidTaskidError("Digite apenas números.")
    result = manager.delete_task(task_id)
    if not result:
        raise NotFoundError("Tarefa não encontrada.")
    return result
