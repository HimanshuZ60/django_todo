from django.shortcuts import render

from todo.models import Task

def home(requests):
    tasks = Task.objects.filter(completed = False).order_by('-updated_at')

    completed_task = Task.objects.filter(completed = True)
    context = {
        'tasks': tasks,
        'completed_task' : completed_task
    }
    return render(requests, 'home.html', context)