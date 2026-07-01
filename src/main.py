from src.database.connection import Connection
from src.repository.repository import Repository
from src.services.manager import Manager
from src.view.view import show_created, view_tasks, show_deleted


def main():
    connection = Connection('task.db')
    task_repository = Repository(connection)
    manager = Manager(task_repository)
    while True:
        print("Menu de tarefas. \n")
        menu = """
            1- Cadastrar tarefa
            2- Listar tarefas
            3- Remover tarefa
            4- Sair
        """
        print(menu)
        escolha=input("Escolha uma opção: ")
        if escolha=="1":
            show_created(manager)
        elif escolha=="2":
            view_tasks(manager)
        elif escolha=="3":
            show_deleted(manager)
        elif escolha=="4":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida.")