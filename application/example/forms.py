from django import forms
from .models import Project, TaskList, Tasks

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']