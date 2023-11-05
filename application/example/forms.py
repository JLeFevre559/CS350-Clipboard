from django import forms
from django.forms import CharField, EmailField, DateField, SelectDateWidget
from .models import Project, TaskList, Tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from datetime import date

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["name", "description"]



class ProfileCreationForm(UserCreationForm):
    date_of_birth = DateField(
        required=True,
        widget=SelectDateWidget(years=range(date.today().year, 1920, -1)),
        initial=date(date.today().year, 1, 1),
    )  # datetime shows a range of values from 1920 - current year
    profile_color = forms.CharField(widget=forms.HiddenInput(), required=False)

    # This overrides the clean_username method to avoid a db call that was causing an error
    def clean_username(self):
        username = self.cleaned_data.get('username')
        all_usernames = get_user_model().objects.values_list('username', flat=True)
        if username in all_usernames:
            raise forms.ValidationError("A user with that username already exists.")
        return username

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
