# example/views.py
from datetime import datetime
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model

class Index(TemplateView):
    template_name = 'TempHome.html'
    user = get_user_model()

    # this redirects to the login page when a non-logged in user tries to view the home page
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(Index, self).dispatch(*args, **kwargs)

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
    