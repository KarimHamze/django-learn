from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('hello/', views.hello, name='hello'),
    path('projects/', views.projects, name='projects'),
    path('task/', views.task, name='task'),
    path('create_task/', views.create_task, name='create_task'),
    path('create_projects/', views.create_projects, name='create_projects'),
]