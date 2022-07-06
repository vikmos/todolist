from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import redirect
from .models import Task
from .forms import TaskForm

def task_list(request):
    current_tasks = Task.objects.filter(create_date__lte=timezone.now()).\
    exclude(task_status=True).order_by('create_date')
    end_tasks = Task.objects.filter(create_date__lte=timezone.now()).\
    exclude(task_status=False).order_by('create_date')
    tasks = {'current_tasks': current_tasks, 'end_tasks': end_tasks}
    return render(request, 'todolist/task_list.html', {'tasks': tasks})

def task_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.author =request.user
            task.creat_date = timezone.now()
            task.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'todolist/task_new.html', {'form': form})

