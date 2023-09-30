# Models code - Milestone 3 - Design - Joel LeFevre (Creating these models was a team effort)

from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser
import uuid

# stores project info and profile id of the user it belongs to
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(default="None")
    profile_id = models.ForeignKey('Profile', on_delete=models.CASCADE)
    
# stores tasklist info and project id of the project it belongs to
class TaskList(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

# stores task info and task list id of the task list it belongs to
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

# stores profile information and extends AbstractUser to allow use of django's user auth
class Profile(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bio = models.TextField(max_length=1000, default="None")
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    email = models.EmailField(max_length=200, default="None")
    date_of_birth = models.DateField(blank=True, null=True)

