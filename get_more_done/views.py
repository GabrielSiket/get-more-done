from django.shortcuts import render
from django.http import HttpResponse
from get_more_done.models import TaskList

def todolist(request):
    all_tasks = TaskList.objects.all

    return render(request, 'todolist.html', {'all_tasks': all_tasks})

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