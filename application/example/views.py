# example/views.py
from datetime import datetime
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

class Index(TemplateView):
    template_name = 'TempHome.html'

class Calendar(TemplateView):
    template_name = 'Calendar.html'

class Project(TemplateView):
    template_name = 'Project.html'

class Profile(TemplateView):
    template_name = 'Profile.html'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class SignupView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        # Automatically log in the user after successful signup
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)
    