from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("hello/<str:username>", views.hello_world, name="hello"),
    path("projects/", views.projects, name="projects"),
    path("tasks/", views.tasks, name="tasks"),
    path("create_task/", views.create_task, name="new_task"),
    path("create_project/", views.create_project, name="new_project"),
    path("projects/<int:id>", views.project_detail, name="project_detail"),
]
