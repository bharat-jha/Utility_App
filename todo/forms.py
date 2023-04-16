from django import forms   
from .models import TodoList

class Addtask(forms.ModelForm):
    class Meta: 
        model = TodoList
        exclude = ['Owner']