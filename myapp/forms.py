from django import forms
from ftplib import MAXLINE

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200, widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label='Descripcion de la tarea', widget=forms.Textarea(attrs={'class': 'area'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del project", max_length=200, widget=forms.TextInput(attrs={'class': 'input-project'}))