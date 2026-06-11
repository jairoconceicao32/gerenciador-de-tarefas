from src.database.connection import Connection
from src.models.task import Task

class Repository:
    def __init__(self):
        self.connection = Connection('task.db')
        self.connection.execute("""
            CREATE TABLE IF NOT EXISTS tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                description TEXT,
                status TEXT
            )
        """)
        self.connection.commit()

    def add_task(self, task: Task):
        self.connection.execute("""
            INSERT INTO tasks(name, description, status)
            VALUES (?, ?, ?)
        """, (
            task.name,
            task.description,
            task.status.value
        ))
        task.task_id = self.connection.get_id()
        self.connection.commit()
        return task
    
    def get_all_tasks(self):
        self.connection.execute("""
            SELECT id, name, description, status FROM tasks
        """)
        rows = self.connection.fetchall()
        tasks = []
        for row in rows:
            task = Task(
                task_id=row[0],
                name=row[1],
                description=row[2],
                status=row[3]
            )
            tasks.append(task)
        return tasks

    def get_task_by_id(self, task_id: int):
        self.connection.execute("""
            SELECT id, name, description, status FROM tasks WHERE id = ?
        """, (task_id,))
        row = self.connection.fetchone()
        if row:
            task = Task(
                task_id=row[0],
                name=row[1],
                description=row[2],
                status=row[3]
            )
            return task
        return None

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
        self.connection.execute("""
            UPDATE tasks SET name = ?, description = ?, status = ? WHERE id = ?
        """, (
            task.name,
            task.description,
            task.status.value,
            task.task_id
        ))
        self.connection.commit()

