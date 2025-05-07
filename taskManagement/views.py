from django.shortcuts import render, redirect
from .models import Task
from .tasks import long_running_task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_list.html', {'tasks': tasks})

def create_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        task = Task.objects.create(title=title, description=description)
        long_running_task.delay(task.id)
        return redirect('task_list')
    return render(request, 'create_task.html')