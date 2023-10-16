from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project, TaskList, Tasks

class ProjectModelTest(TestCase):
    def test_create_project(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpass')
        project = Project.objects.create(
            name='Test Project',
            description='Test Project Description',
            profile_id=user
        )
        self.assertEqual(project.name, 'Test Project')
        self.assertEqual(project.description, 'Test Project Description')
        self.assertEqual(project.profile_id, user)

class TaskListModelTest(TestCase):
    def test_create_task_list(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpass')
        project = Project.objects.create(
            name='Test Project',
            description='Test Project Description',
            profile_id=user
        )
        task_list = TaskList.objects.create(
            name='Test Task List',
            project=project
        )
        self.assertEqual(task_list.name, 'Test Task List')
        self.assertEqual(task_list.project, project)

class TaskModelTest(TestCase):
    def test_create_task(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpass')
        project = Project.objects.create(
            name='Test Project',
            description='Test Project Description',
            profile_id=user
        )
        task_list = TaskList.objects.create(
            name='Test Task List',
            project=project
        )
        task = Tasks.objects.create(
            assignee='Test Assignee',
            task_name='Test Task',
            description='Test Task Description',
            status='Not Started',
            task_list=task_list
        )
        self.assertEqual(task.assignee, 'Test Assignee')
        self.assertEqual(task.task_name, 'Test Task')
        self.assertEqual(task.description, 'Test Task Description')
        self.assertEqual(task.status, 'Not Started')
        self.assertEqual(task.task_list, task_list)

class ProfileModelTest(TestCase):
    def test_create_profile(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass',
            bio='Test Bio',
            email='test@example.com',
            date_of_birth='2000-01-01'
        )
        self.assertEqual(user.bio, 'Test Bio')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.date_of_birth, '2000-01-01')

    def test_create_profile_picture(self):
        user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass',
            bio='Test Bio',
            email='test@example.com',
            date_of_birth='2000-01-01'
        )
        user.profile_picture = 'profile_pictures/test.jpg'
        user.save()
        self.assertEqual(user.profile_picture, 'profile_pictures/test.jpg')