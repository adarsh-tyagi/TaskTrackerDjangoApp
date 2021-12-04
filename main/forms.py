from .models import Task
from django.forms import ModelForm

# Form for task creation
class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title']
