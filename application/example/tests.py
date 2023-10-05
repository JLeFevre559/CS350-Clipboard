from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project, TaskList, Tasks, Profile
from django.urls import reverse

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

class ProjectViewsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.project = Project.objects.create(
            name='Test Project',
            description='Test Project Description',
            profile_id=self.user
        )
        self.tasklist = TaskList.objects.create(
            name='Test TaskList',
            project=self.project
        )
        self.task = Tasks.objects.create(
            task_name='Test Task',
            description='Test Task Description',
            status='Not Started',
            task_list=self.tasklist
        )
        self.client.login(username='testuser', password='testpassword')

    def test_project_list_view(self):
        response = self.client.get(reverse('Project'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')

    def test_project_detail_view(self):
        response = self.client.get(reverse('project-detail', args=[str(self.project.id)]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Project')
        self.assertContains(response, 'Test TaskList')
        self.assertContains(response, 'Test Task')

    def test_project_create_view(self):
        response = self.client.post(reverse('project-create'), {
            'name': 'New Test Project',
            'description': 'New Test Project Description',
        })
        self.assertEqual(response.status_code, 302)  # Redirects to project detail
        new_project = Project.objects.get(name='New Test Project')
        self.assertIsNotNone(new_project)

    def test_project_update_view(self):
        response = self.client.post(reverse('project-update', args=[str(self.project.id)]), {
            'name': 'Updated Test Project',
            'description': 'Updated Test Project Description',
        })
        self.assertEqual(response.status_code, 302)  # Redirects to project detail
        updated_project = Project.objects.get(id=self.project.id)
        self.assertEqual(updated_project.name, 'Updated Test Project')

    def test_project_delete_view(self):
        response = self.client.post(reverse('project-delete', args=[str(self.project.id)]), {
            'delete': 'yes',
        })
        self.assertEqual(response.status_code, 302)  # Redirects to project list
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(id=self.project.id)

class ProfileViewsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.client.login(username='testuser', password='testpassword')

    def test_profile_view(self):
        response = self.client.get(reverse('Profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile')