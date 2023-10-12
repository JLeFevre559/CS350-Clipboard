from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project, TaskList, Tasks, Profile
from django.urls import reverse
from django.http import JsonResponse
import json
from datetime import datetime

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

class DeleteTaskListViewTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = Profile.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a project and a task list associated with that project
        self.project = Project.objects.create(name='Test Project', description='Project Description', profile_id=self.user)
        self.task_list = TaskList.objects.create(name='Test Task List', project=self.project)

    def test_delete_task_list(self):
        # Send a POST request to delete the task list
        url = reverse('delete_task_list')  # Adjust this URL name according to your project's URL configuration
        data = {
            'tasklist_id': str(self.task_list.id),
            'confirmation': 'yes'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the task list and associated tasks have been deleted
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'message': 'Tasklist successfully deleted'})

        # Check if the task list and associated tasks no longer exist in the database
        self.assertFalse(TaskList.objects.filter(id=self.task_list.id).exists())
        self.assertFalse(Tasks.objects.filter(task_list=self.task_list.id).exists())

    def test_delete_task_list_with_task(self):
        task = Tasks.objects.create(
            assignee='Test Assignee',
            task_name='Test Task',
            description='Test Task Description',
            status='Not Started',
            task_list=self.task_list
        )
        # Send a POST request to delete the task list
        url = reverse('delete_task_list')  # Adjust this URL name according to your project's URL configuration
        
        data = {
            'tasklist_id': str(self.task_list.id),
            'confirmation': 'yes'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the task list and associated tasks have been deleted
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'message': 'Tasklist successfully deleted'})

        # Check if the task list and associated tasks no longer exist in the database
        self.assertFalse(TaskList.objects.filter(id=self.task_list.id).exists())
        self.assertFalse(Tasks.objects.filter(task_list=self.task_list.id).exists())
        self.assertFalse(Tasks.objects.filter(id=task.id).exists())

    def test_delete_task_list_invalid_request(self):
        # Send an invalid request (e.g., missing 'confirmation')
        url = reverse('delete_task_list')  # Adjust this URL name according to your project's URL configuration
        data = {
            'tasklist_id': str(self.task_list.id)
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the view returns a 400 Bad Request response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {'error': 'Invalid request'})

    def test_delete_task_list_tasklist_not_found(self):
        # Send a request to delete a non-existent task list
        url = reverse('delete_task_list')  # Adjust this URL name according to your project's URL configuration
        data = {
            'tasklist_id': None,
            'confirmation': 'yes'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the view returns a 404 Not Found response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'error': 'TaskList not found'})

class UpdateTaskListViewTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = Profile.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a project and a task list associated with that project
        self.project = Project.objects.create(name='Test Project', description='Project Description', profile_id=self.user)
        self.task_list = TaskList.objects.create(name='Test Task List', project=self.project)

    def test_update_task_list(self):
        # Send a POST request to update the task list name
        url = reverse('update_task_list')  # Adjust this URL name according to your project's URL configuration
        data = {
            'tasklist_id': str(self.task_list.id),
            'name': 'New Task List Name'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the task list name has been updated
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'message': 'Tasklist successfully updated'})

        # Check if the task list's name has changed in the database
        updated_task_list = TaskList.objects.get(id=self.task_list.id)
        self.assertEqual(updated_task_list.name, 'New Task List Name')

    def test_update_task_list_tasklist_not_found(self):
        # Send a request to update a non-existent task list
        url = reverse('update_task_list')  # Adjust this URL name according to your project's URL configuration
        data = {
            'tasklist_id': None,
            'name': 'New Task List Name'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the view returns a 404 Not Found response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'error': 'TaskList not found'})

    def test_update_task_list_invalid_request(self):
        # Send an invalid request (e.g., wrong request type)
        url = reverse('update_task_list')  # Adjust this URL name according to your project's URL configuration
        data = {
            'tasklist_id': str(self.task_list.id)
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='NOT_AJAX_REQUEST')

        # Check if the view returns a 400 Bad Request response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {'error': 'Invalid request'})

        # Test again with no name field
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(json.loads(response.content), {'error': 'Invalid request, new name cannot be none'})

class DeleteTaskViewTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = Profile.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a project and a task list associated with that project
        self.project = Project.objects.create(name='Test Project', description='Project Description', profile_id=self.user)
        self.task_list = TaskList.objects.create(name='Test Task List', project=self.project)
        self.task = Tasks.objects.create(
            assignee='Test Assignee',
            task_name='Test Task',
            description='Test Task Description',
            status='Not Started',
            task_list=self.task_list
        )

    def test_delete_task(self):
        # Send a POST request to delete the task list
        url = reverse('delete_task')  # Adjust this URL name according to your project's URL configuration
        data = {
            'task_id': str(self.task.id),
            'confirmation': 'yes'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the task list and associated tasks have been deleted
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'message': 'Task successfully deleted'})

        # Check if the task no longer exists in the database
        self.assertFalse(Tasks.objects.filter(task_list=self.task.id).exists())


    def test_delete_task_invalid_request(self):
        # Send an invalid request (e.g., missing 'confirmation')
        url = reverse('delete_task')  # Adjust this URL name according to your project's URL configuration
        data = {
            'task_id': str(self.task.id)
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the view returns a 400 Bad Request response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {'error': 'Invalid request'})

    def test_delete_task_task_not_found(self):
        # Send a request to delete a non-existent task list
        url = reverse('delete_task')  # Adjust this URL name according to your project's URL configuration
        data = {
            'task_id': None,
            'confirmation': 'yes'
        }
        response = self.client.post(url, data, content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the view returns a 404 Not Found response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'error': 'Task not found'})

class UpdateTaskViewTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = Profile.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a project and a task associated with that project
        self.project = Project.objects.create(name='Test Project', description='Project Description', profile_id=self.user)
        self.task_list = TaskList.objects.create(name='Test Task List', project=self.project)
        self.task = Tasks.objects.create(
            assignee='Test Assignee',
            task_name='Test Task',
            description='Test Task Description',
            status='Not Started',
            task_list=self.task_list,
            priority = 'High'
        )

    def test_update_task(self):
        # Send a POST request to update the task name
        url = reverse('update_task')  # Adjust this URL name according to your project's URL configuration
        date = datetime.fromisoformat('2023-10-13T00:00:00.000+00:00').date()
        data = {
            'task_id': str(self.task.id),
            'name': 'New Task Name',
            'assignee': 'New Assignee',
            'due_date': '2023-10-13T00:00:00.000+00:00',
            'description': 'New Description',
            'priority': 'Low'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the task name has been updated
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), {'message': 'Task successfully updated'})

        # Check if the task's data has changed in the database
        updated_task = Tasks.objects.get(id=self.task.id)
        self.assertEqual(updated_task.task_name, 'New Task Name')
        self.assertEqual(updated_task.assignee, 'New Assignee')
        self.assertEqual(updated_task.due_date, date)
        self.assertEqual(updated_task.description, 'New Description')
        self.assertEqual(updated_task.priority, 'Low')

    def test_update_task_task_not_found(self):
        # Send a request to update a non-existent task 
        url = reverse('update_task')  # Adjust this URL name according to your project's URL configuration
        date = datetime.fromisoformat('2023-10-13T00:00:00.000+00:00').date()
        data = {
            'task_id': None,
            'name': 'New Task Name',
            'assignee': 'New Assignee',
            'date': str(date),
            'description': 'New Description',
            'priority': 'Low'
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='XMLHttpRequest')

        # Check if the view returns a 404 Not Found response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {'error': 'Task not found'})

    def test_update_task_invalid_request(self):
        # Send an invalid request (e.g., wrong request type)
        url = reverse('update_task')  # Adjust this URL name according to your project's URL configuration
        date = datetime.fromisoformat('2023-10-13T00:00:00.000+00:00').date()
        data = {
            'task_id': str(self.task.id),
            'date': str(date)
        }
        response = self.client.post(url, json.dumps(data), content_type='application/json', HTTP_X_REQUESTED_WITH='NOT_AJAX_REQUEST')

        # Check if the view returns a 400 Bad Request response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {'error': 'Invalid request'})
