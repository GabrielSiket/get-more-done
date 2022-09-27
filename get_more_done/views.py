from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from get_more_done.models import TaskList
from get_more_done.forms import TaskForm



def todolist(request):
    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(request, ("New Task Added!"))
        return redirect('todolist')
    else:
        all_tasks = TaskList.objects.all
        return render(request, 'todolist.html', {'all_tasks': all_tasks})


def delete_task(request, task_id):
    task = TaskList.objects.get(pk=task_id)
    task.delete()
    return redirect('todolist')

def edit_task(request, task_id):
    if request.method == "POST":
        task = TaskList.objects.get(pk=task_id)
        form = TaskForm(request.POST or None, instance = task)
        if form.is_valid():
            form.save()

        messages.success(request, ("Task Edited!"))
        return redirect('todolist')
    else:
        task_obj = TaskList.objects.get(pk=task_id)
        return render(request, 'edit.html', {'task_obj': task_obj})


def contact(request):
    context = {
        'contact_text': "Welcome to Contact Page !",

    }
    return render(request, 'contact.html', context)


def about(request):
    context = {
        'about_text': "Welcome to About Page !",

    }
    return render(request, 'about.html', context)
