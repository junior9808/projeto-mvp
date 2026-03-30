from models.task import Task

class TaskService:
    def __init__(self):
        self.tasks = []

    def create_task(self, title: str):
        task = Task(len(self.tasks) + 1, title)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def complete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                return task
        return None

    def delete_task(self, task_id: int):
        for task in self.tasks:
            if task.id == task_id:
                self.tasks.remove(task)
                return True
        return False