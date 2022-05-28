from django.shortcuts import render
from django.utils import timezone
from .models import Task

def task_list(request):
    tasks = Task.objects.filter(create_date__lte=timezone.now()).order_by('create_date')
    return render(request, 'todolist/task_list.html', {'tasks': tasks})
