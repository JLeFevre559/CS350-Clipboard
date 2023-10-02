from django import forms
from django.forms import CharField, EmailField, DateField, SelectDateWidget
from .models import Project, TaskList, Tasks
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
import datetime

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class ProfileCreationForm(UserCreationForm):
    username = CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    first_name = CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=32, help_text='First name')
    last_name=CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=32, help_text='Last name')
    email=EmailField(required = True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), max_length=64, help_text='Enter a valid email address')
    password1=CharField(required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2=CharField(required = True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}))
    birthdate = DateField(required = True, widget=SelectDateWidget(years=range(1920,datetime.date.today().year)), initial=datetime.date.today().year) # datetime shows a range of values from 1920 - current year

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'birthdate', 'password1', 'password2']