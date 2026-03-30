from fastapi import FastAPI
from services.task_service import TaskService
from utils.helpers import filter_completed, format_task

app = FastAPI()
service = TaskService()

@app.get("/")
def home():
    return {"message": "API de Tarefas rodando"}

@app.post("/tasks")
def create_task(title: str):
    task = service.create_task(title)
    return format_task(task)

@app.get("/tasks")
def get_tasks():
    return [format_task(t) for t in service.list_tasks()]

@app.get("/tasks/completed")
def get_completed_tasks():
    tasks = filter_completed(service.list_tasks())
    return [format_task(t) for t in tasks]

@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int):
    task = service.complete_task(task_id)
    if task:
        return format_task(task)
    return {"error": "Task not found"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    result = service.delete_task(task_id)
    return {"deleted": result}