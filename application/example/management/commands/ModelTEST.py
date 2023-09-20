from django.test import TestCase
from .models import Project, TaskList, Tasks, Profile

class ModelTestCase(TestCase): ## not working currently

    def setUp(self):
        # Create sample data for testing
        self.project = Project.objects.create(name="Sample Project")
        self.task_list = TaskList.objects.create(name="Sample Task List", project=self.project)
        self.task = Tasks.objects.create(
            assignee="John",
            task_name="Sample Task",
            description="Sample description",
            status="Not Started",
            due_date="2023-09-30",
            task_list=self.task_list,
        )
        self.profile = Profile.objects.create(
            bio="Sample bio",
            email="john@example.com",
            date_of_birth="1990-01-01",
            projectlist=self.project,
        )

    def test_project_model(self):
        project = Project.objects.get(name="Sample Project")
        self.assertEqual(project.name, "Sample Project")

    def test_task_list_model(self):
        task_list = TaskList.objects.get(name="Sample Task List")
        self.assertEqual(task_list.name, "Sample Task List")
        self.assertEqual(task_list.project, self.project)

    def test_tasks_model(self):
        task = Tasks.objects.get(task_name="Sample Task")
        self.assertEqual(task.assignee, "John")
        self.assertEqual(task.description, "Sample description")
        self.assertEqual(task.status, "Not Started")
        self.assertEqual(task.due_date, "2023-09-30")
        self.assertEqual(task.task_list, self.task_list)

    def test_profile_model(self):
        profile = Profile.objects.get(email="john@example.com")
        self.assertEqual(profile.bio, "Sample bio")
        self.assertEqual(profile.date_of_birth, "1990-01-01")
        self.assertEqual(profile.projectlist, self.project)