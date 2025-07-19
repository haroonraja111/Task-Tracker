from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().order_by('-updated_at')
    return render(request, 'tasks/task_list.html' , {'tasks' : tasks})

def task_list_done(request):
    tasks = Task.objects.filter(status='DONE').order_by('-updated_at')
    return render(request, 'tasks/task_list.html', {
        'tasks' : tasks, 
        'title' : 'Completed Task'
    })

def task_list_todo(request):
    tasks = Task.objects.filter(status='TODO').order_by('-updated_at')
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'title': 'Tasks To Do'
    })

def task_list_in_progress(request):
    tasks = Task.objects.filter(status='IN_PROGRESS').order_by('-updated_at')
    return render(request, 'tasks/task_list.html', {
        'tasks': tasks,
        'title': 'Tasks In Progress'
    })


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # or wherever you want to go after creation
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})
    
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')  # or wherever you want to redirect
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task' : task})


def task_mark_in_progress(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'IN_PROGRESS'
    task.save()
    return redirect('task_list')

def task_mark_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.status = 'DONE'
    task.save()
    return redirect('task_list')
    