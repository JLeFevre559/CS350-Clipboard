from django import forms
from django.forms import CharField, EmailField, DateField, SelectDateWidget
from .models import Project, TaskList, Tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
import datetime


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description"]


class ProfileCreationForm(UserCreationForm):
    date_of_birth = DateField(
        required=True,
        widget=SelectDateWidget(years=range(1920, datetime.date.today().year)),
        initial=datetime.date.today(),
    )  # datetime shows a range of values from 1920 - current year
    profile_color = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = get_user_model()
        fields = [
            "username",
            "email",
            "date_of_birth",
            "password1",
            "password2",
            "first_name",
            "last_name",
        ]
