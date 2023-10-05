from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project, TaskList, Tasks, Profile
from django.urls import reverse
from django.http import JsonResponse
import json

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

class UpdateTaskStatusViewTestCase(TestCase):

    def setUp(self):
        user = get_user_model().objects.create_user(username='testuser1', password='testpass')
        project = Project.objects.create(
            name='Test Project',
            description='Test Project Description',
            profile_id=user
        )
        task_list = TaskList.objects.create(
            name='Test Task List',
            project=project
        )
        self.task = Tasks.objects.create(
            assignee='Test Assignee',
            task_name='Test Task',
            description='Test Task Description',
            status='Not Started',
            task_list=task_list
        )

    def test_update_task_status_ajax(self):
        url = reverse('update_task_status')

        # Define the data to send in the AJAX request
        data = {
            'task_id': str(self.task.id),
            'new_status': 'In Progress'
        }
        # Send a POST AJAX request to update the task status
        response = self.client.post(
            url,
            json.dumps(data),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'  # Simulate an AJAX request
        )
        # Check that the response is a JSON response
        self.assertIsInstance(response, JsonResponse)

        # Parse the JSON response
        response_data = json.loads(response.content)

        # Check that the response contains the expected message
        self.assertEqual(response_data['message'], 'Task status updated successfully')

        # Check that the task status has been updated in the database
        updated_task = Tasks.objects.get(id=self.task.id)
        self.assertEqual(updated_task.status, 'In Progress')

    def test_update_task_status_invalid_request(self):
        # Define the URL for the view
        url = reverse('update_task_status')

        # Send a GET request (invalid) instead of a POST request
        response = self.client.get(url)

        # Check that the response is a JSON response with a 400 status code
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 400)

        # Parse the JSON response
        response_data = json.loads(response.content)

        # Check that the response contains the expected error message
        self.assertEqual(response_data['error'], 'Invalid request')

    def test_update_task_status_task_not_found(self):
        # Define a non-existent task ID
        non_existent_task_id = '00000000-0000-0000-0000-000000000000'

        # Define the URL for the view
        url = reverse('update_task_status')

        # Define the data to send in the AJAX request
        data = {
            'task_id': non_existent_task_id,
            'new_status': 'In Progress'
        }

        # Send a POST AJAX request with a non-existent task ID
        response = self.client.post(
            url,
            json.dumps(data),
            content_type='application/json',
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'  # Simulate an AJAX request
        )

        # Check that the response is a JSON response with a 404 status code
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 404)

        # Parse the JSON response
        response_data = json.loads(response.content)

        # Check that the response contains the expected error message
        self.assertEqual(response_data['error'], 'Task not found')
