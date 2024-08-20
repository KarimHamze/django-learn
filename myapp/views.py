from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)

def about(request):
    username = 'Karim'
    return render(request, 'about.html', {
        'username': username
    })

def projects(request):
    #projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects.html' , {
        'projects': projects
    })

def task(request): #, title):
    #task = Task.objects.get(title=title)
    return render(request, 'task.html')