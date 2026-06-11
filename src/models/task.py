from enum import Enum

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"
    

class Task:
    _transition={
        TaskStatus.PENDING: [TaskStatus.IN_PROGRESS, TaskStatus.CANCELED],
        TaskStatus.IN_PROGRESS: [TaskStatus.COMPLETED, TaskStatus.FAILED, TaskStatus.CANCELED],
        TaskStatus.COMPLETED: [],
        TaskStatus.FAILED: [],
        TaskStatus.CANCELED: []
    }
    def __init__(self, name, description, status=TaskStatus.PENDING, task_id=None):
        self.task_id=task_id
        self.name=name
        self.description=description
        self.status= self._parse_status(status)

    def __repr__(self):
        return f"Task(task_id={self.task_id}, name={self.name}, status={self.status})"

    @staticmethod
    def _parse_status(status):
        if isinstance(status, TaskStatus):
            return status
        if isinstance(status, str):
            try:
                return TaskStatus(status)
            except ValueError:
                raise ValueError(f"Status inválido {status}")
        raise TypeError("Status deve ser do tipo TaskStatus ou texto")


    def update_status(self, new_status):
        new_status = self._parse_status(new_status)
        if new_status in self._transition[self.status]:
            self.status= new_status
        else:
            raise ValueError(f"Invalid status transition from {self.status} to {new_status}")

    
    def start(self):
        self.update_status(TaskStatus.IN_PROGRESS)
    
    def cancel(self):
        self.update_status(TaskStatus.CANCELED)

    def fail(self):
        self.update_status(TaskStatus.FAILED)
    
    def complete(self):
        self.update_status(TaskStatus.COMPLETED)