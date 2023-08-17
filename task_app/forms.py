from django import forms
from task_app.models import TaskModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['taskTitle', 'taskDescription']
        labels = {
            'taskTitle': 'Title',
            'taskDescription': 'Description'
        }