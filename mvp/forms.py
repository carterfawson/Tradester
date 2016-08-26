from django.forms import ModelForm
from .models import customer

class TaskForm(ModelForm):
        class Meta:
            model = customer
            fields = ['name', 'email', 'phone', 'zip', 'task', 'description']
