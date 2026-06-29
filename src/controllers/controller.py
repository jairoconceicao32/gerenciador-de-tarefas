def create(name, description, manager):
    name = name.strip()
    description = description.strip()
    if len(name) < 4:
        return False, "O nome deve conter pelo menos 4 caracteres."
    if len(description) < 5:
        return False, "A descrição deve conter pelo menos 5 caracteres."
    return True, manager.create_task(name, description)

def read(manager):
    tasks = manager.list_tasks()
    return tasks

def delete(task_id, manager):
    task_id= task_id.strip()
    if task_id=="":
        return False, "O ID da tarefa não pode ser vazio."
    try:
        task_id = int(task_id)
    except ValueError:
        return False, "Digite apenas números."
    result = manager.delete_task(task_id)
    if result:
        return True, "Tarefa deletada com sucesso."
    else:
        return False, "Tarefa não encontrada."