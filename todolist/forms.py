from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    text = forms.CharField(label='Введите новое задание:',
            widget = forms.widgets.TextInput(attrs={'size': '100'}))
    class Meta:
        model = Task
        fields = ('text',)

