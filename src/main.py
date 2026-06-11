from src.services.manager import Manager
from src.view.view import show_created, view_tasks, show_deleted


def main():
    t = Manager()
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
            show_created(t)
        elif escolha=="2":
            view_tasks(t)
        elif escolha=="3":
            show_deleted(t)
        elif escolha=="4":
            print("Saindo do gerenciador de tarefas.")
            break
        else:
            print("Opção inválida.")