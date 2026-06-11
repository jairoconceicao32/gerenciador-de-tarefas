from src.repository.repository import Repository
from src.models.task import Task

class Manager:
    def __init__(self):
        self.task_repository = Repository()

    def create_task(self, name, description):
        new_task = Task(name, description)
        self.task_repository.add_task(new_task)
        return new_task
    
    def list_tasks(self):
        return self.task_repository.get_all_tasks()
    
    def delete_task(self, task_id):
        return self.task_repository.delete_task(task_id)
    
    def update_task(self, task_id, name, description):
        task = self.task_repository.get_task_by_id(task_id)
        if task:
            task.name = name
            task.description = description
            self.task_repository.update_task(task)
            return task
        return None