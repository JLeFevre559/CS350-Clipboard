from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="None")
    
class TaskList(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Tasks(models.Model):
    assignee = models.CharField(max_length=200)
    task_name = models.CharField(max_length=200)
    description = models.TextField(default="None")
    STATUS_CHOICES = (
    ('Not Started', 'Not Started'),
    ('In Progress', 'In Progress'),
    ('Done', 'Done'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Not Started')
    due_date = models.DateField(blank=True, null=True)
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
    PRIORITY_CHOICES = (
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    )
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='None')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=1000, default="None")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    email = models.EmailField(max_length=200, default="None")
    date_of_birth = models.DateField(blank=True, null=True)
    projectlist = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True, null=True)