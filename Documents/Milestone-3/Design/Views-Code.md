# Views code - Milestone 3 - Design - Joel LeFevre (Creating these views was a team effort)

# example/views.py
from datetime import datetime
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm
from django.urls import reverse
from django.shortcuts import redirect

class Index(TemplateView):
    template_name = 'TempHome.html'
    user = get_user_model()

    # this redirects to the login page when a non-logged in user tries to view the home page
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(Index, self).dispatch(*args, **kwargs)

class Calendar(TemplateView):
    template_name = 'Calendar.html'


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'Projects/project.html'  
    context_object_name = 'projects'

class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = 'Projects/project_detail.html'  
    context_object_name = 'project'


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'Projects/project_form.html'
    form_class = ProjectForm
    success_url = reverse_lazy('/Project')

    def form_valid(self, form):
        form.instance.profile_id = self.request.user  # Set the profile_id to the current user's profile
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('project-detail', args=[str(self.object.id)])  # Use 'pk' to set the project's primary key
    

class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = 'Project/project_form.html'
    form_class = ProjectForm

    def get_success_url(self):
        return reverse_lazy('project-detail', args=[str(self.object.id)])

class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = 'projects/project_confirm_delete.html'
    success_url = reverse_lazy('Project')

    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST and request.POST['delete'] == 'yes':
            # User confirmed deletion, proceed to delete the project
            self.object = self.get_object()
            self.object.delete()
            return redirect(self.success_url)
        else:
            # User canceled deletion, redirect back to project list
            return redirect(self.success_url)

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
    