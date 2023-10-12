# example/views.py
from datetime import datetime
from typing import Any
from django.db import models, IntegrityError
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth import get_user_model
from .models import Project, TaskList, Tasks
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProjectForm, ProfileCreationForm
from django.urls import reverse
from django.shortcuts import redirect, render
from uuid import uuid4
import json


class Index(TemplateView):
    template_name = "TempHome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            # User is logged in, so add data for logged-in users.
            # For example, you can pass the user object to the template.
            user = self.request.user
            context["user"] = user

        return context

    # user = get_user_model()

    # this redirects to the login page when a non-logged in user tries to view the home page
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(Index, self).dispatch(*args, **kwargs)


class Calendar(TemplateView):
    template_name = "Calendar.html"


class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = "Projects/project.html"
    context_object_name = "projects"

    def get_queryset(self):
        # Get all projects related to the user's profile
        projects = Project.objects.filter(profile_id=self.request.user)
        # Get all task lists related to the user's projects
        # tasklists = TaskList.objects.filter(project__in=projects)
        # # Get all tasks related to the user's task lists
        # tasks = Tasks.objects.filter(task_list__in=tasklists)
        queryset = {
            "projects": projects,
            # 'tasklists': tasklists,
            # 'tasks': tasks,
        }

        return queryset


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "Projects/project_detail.html"
    context_object_name = "project"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_project = self.object
        tasklists = TaskList.objects.filter(project=this_project)
        # Inside your view
        tasks = Tasks.objects.filter(task_list__in=tasklists)
        context["tasklists"] = tasklists
        context["tasks"] = tasks

        return context


class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "Projects/project_form.html"
    form_class = ProjectForm
    success_url = reverse_lazy("/Project")

    def form_valid(self, form):
        form.instance.profile_id = (
            self.request.user
        )  # Set the profile_id to the current user's profile
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "project-detail", args=[str(self.object.id)]
        )  # Use 'pk' to set the project's primary key


class ProjectUpdateView(LoginRequiredMixin, UpdateView):
    model = Project
    template_name = "Projects/project_form.html"
    form_class = ProjectForm

    def get_success_url(self):
        return reverse_lazy("project-detail", args=[str(self.object.id)])


class ProjectDeleteView(LoginRequiredMixin, DeleteView):
    model = Project
    template_name = "Projects/project_confirm_delete.html"
    success_url = reverse_lazy("Project")

    def post(self, request, *args, **kwargs):
        if "delete" in request.POST and request.POST["delete"] == "yes":
            # User confirmed deletion, proceed to delete the project
            self.object = self.get_object()
            self.object.delete()
            return redirect(self.success_url)
        else:
            # User canceled deletion, redirect back to project list
            return redirect(self.success_url)


class Profile(LoginRequiredMixin, TemplateView):
    template_name = "Profile.html"


class CustomLoginView(LoginView):
    template_name = "registration/login.html"


class SignupView(FormView):
    form_class = ProfileCreationForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        # Automatically log in the user after successful signup
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


def create_tasklist(request):
    if request.method == "POST":
        project_id = request.POST.get("project_id")
        tasklist_name = request.POST.get("tasklist_name")

        # Create a new TaskList associated with the project
        project = Project.objects.get(id=project_id)
        TaskList.objects.create(id=uuid4(), name=tasklist_name, project=project)

        # Redirect back to the project detail page
        return redirect("project-detail", pk=project_id)

    return render(request, "project_detail.html")


def create_task(request):
    if request.method == "POST":
        tasklist_id = request.POST.get("tasklist_id")
        task_name = request.POST.get("task_name")
        description = request.POST.get("description")
        due_date = request.POST.get("due_date")
        priority = request.POST.get("priority")

        # Create a new Task associated with the tasklist
        tasklist = TaskList.objects.get(id=tasklist_id)
        Tasks.objects.create(
            task_name=task_name,
            task_list=tasklist,
            description=description,
            due_date=due_date,
            priority=priority,
        )

        # Redirect back to the project detail page (or wherever you prefer)
        return redirect("project-detail", pk=tasklist.project.id)

    return render(request, "project_detail.html")


def update_task_status(request):
    if request.method == "POST" and (
        request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"
    ):
        # Get the task ID and new status from the AJAX request
        data = json.loads(request.body.decode("utf-8"))
        task_id = data.get("task_id")
        new_status = data.get("new_status")

        # Assuming you have a Task model, update the status
        try:
            task = Tasks.objects.get(id=task_id)
            task.status = new_status
            task.save()
            return JsonResponse({"message": "Task status updated successfully"})
        except Tasks.DoesNotExist:
            return JsonResponse({"error": "Task not found"}, status=404)

    return JsonResponse({"error": "Invalid request"}, status=400)

def delete_task_list(request):
    if request.method == 'POST' and (request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'):
        data = json.loads(request.body.decode('utf-8'))
        tasklist_id = data.get('tasklist_id')
        confirmation = data.get('confirmation')

        if confirmation == 'yes':
            try:
                tasklist = TaskList.objects.get(id=tasklist_id)
                tasks = Tasks.objects.filter(task_list=tasklist_id)
                for task in tasks:
                    task.delete()
                tasklist.delete()
                return JsonResponse({'message': 'Tasklist successfully deleted'})
            except TaskList.DoesNotExist:
                return JsonResponse({'error': 'TaskList not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)
	
def update_task_list(request):
    if request.method == 'POST' and (request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'):
        data = json.loads(request.body.decode('utf-8'))
        tasklist_id = data.get('tasklist_id')
        new_name = data.get('name')
        if new_name == None:
            return JsonResponse({'error': 'Invalid request, new name cannot be none'}, status=400)
        try:
            tasklist = TaskList.objects.get(id=tasklist_id)
            tasklist.name = new_name
            tasklist.save()
            return JsonResponse({'message': 'Tasklist successfully updated'})
        except TaskList.DoesNotExist:
            return JsonResponse({'error': 'TaskList not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def delete_task(request):
    if request.method == 'POST' and (request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'):
        data = json.loads(request.body.decode('utf-8'))
        task_id = data.get('task_id')
        confirmation = data.get('confirmation')

        if confirmation == 'yes':
            try:
                task = Tasks.objects.get(id=task_id)
                task.delete()
                return JsonResponse({'message': 'Task successfully deleted'})
            except Tasks.DoesNotExist:
                return JsonResponse({'error': 'Task not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def update_task(request):
    if request.method == 'POST' and (request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'):
        data = json.loads(request.body.decode('utf-8'))
        task_id = data.get('task_id')
        new_name = data.get('name')
        new_assignee = data.get('assignee')
        new_due_date_str = data.get('due_date')
        new_description = data.get('description')
        new_priority = data.get('priority')
        try:
            task = Tasks.objects.get(id=task_id)
            if new_name == None:
                new_name = task.task_name
            task.task_name = new_name
            task.assignee = new_assignee
            if new_due_date_str == None:
                new_due_date = task.due_date
            else:
                new_due_date = datetime.fromisoformat(new_due_date_str)
            task.due_date = new_due_date
            task.description = new_description
            if new_priority not in ['High', 'Medium', 'Low']:
                new_priority = task.priority
            task.priority = new_priority
            task.save()
            return JsonResponse({'message': 'Task successfully updated'})
        except Tasks.DoesNotExist:
            return JsonResponse({'error': 'Task not found'}, status=404)
    return JsonResponse({'error': 'Invalid request'}, status=400)