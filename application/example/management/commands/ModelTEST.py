from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import models
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser
import uuid

# stores project info and profile id of the user it belongs to
class Project(models.Model):
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

class Command(BaseCommand):
    help = 'Checks Models to ensure they are working data fields'

    def handle(self, *args, **options):
        # Create sample data for testing
        project = Project.objects.create(name="Sample Project")
        task_list = TaskList.objects.create(name="Sample Task List", project=project)
        task = Tasks.objects.create(
            assignee="John",
            task_name="Sample Task",
            description="Sample description",
            status="Not Started",
            due_date="2023-09-30",
            task_list=task_list,
        )
        profile = Profile.objects.create(
            bio="Sample bio",
            email="john@example.com",
            date_of_birth="1990-01-01",
        )

        self.test_project_model()
        self.test_task_list_model()
        self.test_tasks_model()
        self.test_profile_model()

    def test_project_model(self):
        project = Project.objects.get(name="Sample Project")
        self.assertEqual(project.name, "Sample Project")

    def test_task_list_model(self):
        task_list = TaskList.objects.get(name="Sample Task List")
        self.assertEqual(task_list.name, "Sample Task List")

    def test_tasks_model(self):
        task = Tasks.objects.get(task_name="Sample Task")
        self.assertEqual(task.assignee, "John")
        self.assertEqual(task.description, "Sample description")
        self.assertEqual(task.status, "Not Started")
        self.assertEqual(task.due_date, "2023-09-30")

    def test_profile_model(self):
        profile = Profile.objects.get(email="john@example.com")
        self.assertEqual(profile.bio, "Sample bio")
        self.assertEqual(profile.date_of_birth, "1990-01-01")