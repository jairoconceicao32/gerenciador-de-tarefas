from src.services.manager import Manager

def test_manager():
    manager = Manager()
    result = manager.create_task(
        "Criar função no gerenciador em python",
        "Criar uma função que execute tarefas no gerenciador"
    )
    print(result)
    assert result.name == "Criar função no gerenciador em python"
    assert result.description == (
        "Criar uma função que execute tarefas no gerenciador"
    )