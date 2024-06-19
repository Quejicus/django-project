from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404
from .forms import CreateNewTask


def index(request):
    title = "Django course!!"
    return render(request, "index.html", {"title": title})


def about(request):
    username = "quejicus"
    return render(request, "about.html", {"username": username})


def hello_world(username):
    return HttpResponse(f"<h1>Hello, {username}</h1>")


def projects(request):
    projects = list(Project.objects.all().values())
    return render(request, "projects.html", {"projects": projects})


def tasks(request):
    tasks = Task.objects.all()
    return render(request, "tasks.html", {"tasks": tasks})


def create_task(request):
    return render(request, "create_task.html", {"form": CreateNewTask})
