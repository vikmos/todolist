from django.shortcuts import render
from django.utils import timezone
from .models import Task

def task_list(request):
    current_tasks = Task.objects.filter(create_date__lte=timezone.now()).\
            exclude(task_status=False).order_by('create_date')
    end_tasks = Task.objects.filter(create_date__lte=timezone.now()).\
            exclude(task_status=True).order_by('create_date')
    tasks = {'current_tasks': current_tasks, 'end_tasks': end_tasks}
    return render(request, 'todolist/task_list.html', {'tasks': tasks})
