from datetime import datetime
from src.database.connection import Connection
from src.models.task import Task
from src.models.deadline import Deadline

class Repository:
    def __init__(self, connection):
        self.connection = connection
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                status TEXT,
                start_date date null,
                end_date date null
            )
        """)
        self.connection.commit()

    def add_task(self, task: Task):
        start, end = self._extract_dates(task)
        self.connection.execute("""
            INSERT INTO tasks(name, description, status, start_date, end_date)
            VALUES (?, ?, ?, ?, ?)
        """, (
            task.name,
            task.description,
            task.status.value,
            start,
            end
        ))
        task.task_id = self.connection.get_id()
        self.connection.commit()
        return task
    
    def get_all_tasks(self):
        self.connection.execute("""
            SELECT id, name, description, status, start_date, end_date FROM tasks
        """)
        return [self._to_task(row) for row in self.connection.fetchall()]
    
    def get_task_by_id(self, task_id: int):
        self.connection.execute("""
            SELECT id, name, description, status, start_date, end_date FROM tasks WHERE id = ?
        """, (task_id,))
        row = self.connection.fetchone()
        return self._to_task(row) if row else None
    
    def delete_task(self, task_id: int):
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        self.connection.execute("""
            DELETE FROM tasks WHERE id = ?
        """, (task_id,))
        self.connection.commit()
        return True
    
    def update_task(self, task: Task):
        start, end = self._extract_dates(task)
        self.connection.execute("""
            UPDATE tasks SET name = ?, description = ?, status = ?, start_date = ?, end_date = ? WHERE id = ?
        """, (
            task.name,
            task.description,
            task.status.value,
            start,
            end,
            task.task_id
        ))
        self.connection.commit()


    def _extract_dates(self, task: Task):
        if task.deadline:
            return (
                task.deadline.start_date.isoformat(),
                task.deadline.end_date.isoformat(),
            )
        return None, None

    
    def _to_task(self, row) -> Task:
        deadline = None
        if row[4] and row[5]:
            deadline = Deadline(
                start_date=datetime.fromisoformat(row[4]),
                end_date=datetime.fromisoformat(row[5]),
            )
        return Task(
            task_id=row[0],
            name=row[1],
            description=row[2],
            status=row[3],
            deadline=deadline,
        )