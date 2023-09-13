from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse_lazy

class Project(models.Model):
    name = models.CharField(max_length=200)

class TaskList(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Tasks(models.Model):
    assignee = models.CharField(max_length=200)
    taskName = models.CharField(max_length=200)
    description = models.TextField(default="None")
    status = models.CharField(max_length=200, default="None")
    dueDate = models.CharField(max_length=200, default="None")
    task_list = models.ForeignKey(TaskList, on_delete=models.CASCADE)
