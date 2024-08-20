from django import forms
from ftplib import MAXLINE

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200)
    description = forms.CharField(label='Descripcion de la tarea', widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del project", max_length=200)