def filter_completed(tasks):
    return list(filter(lambda t: t.completed, tasks))

def format_task(task):
    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }