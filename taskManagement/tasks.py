from celery import shared_task
import time

@shared_task
def long_running_task(task_id):
    from .models import Task
    time.sleep(10)
    task = Task.objects.get(id=task_id)
    task.completed = True
    task.save()
    print("--------------------------------")
    print(f"Task {task_id} completed")
    print("--------------------------------")
    return f"Task {task_id} completed"