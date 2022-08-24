from django.forms import ModelForm
from App.models import TaskMan
from App.models import Action
from django import forms


class TODOForm(forms.ModelForm):
    class Meta:
        model = TaskMan
        fields = ['title' , 'status' , 'priority']

class TasksForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ['user']