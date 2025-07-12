from django.shortcuts import render

from todo.models import Task

def home(requests):
    tasks = Task.objects.filter(completed = False).order_by('-updated_at')
    context = {
        'tasks': tasks
    }
    return render(requests, 'home.html', context)