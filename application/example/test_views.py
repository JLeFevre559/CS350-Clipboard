from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Project, TaskList, Tasks, Profile
from django.urls import reverse
from django.http import JsonResponse
import json
from datetime import datetime
from .views import (
    check_tasklist_status,
    get_all_tasks_for_user,
    generate_random_dark_color,
)
from datetime import date


class ProjectViewsTestCase(TestCase):
    def setUp(self):
        self.date = datetime.fromisoformat("2023-10-13T00:00:00.000+00:00").date()
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.project = Project.objects.create(
            name="Test Project",
            description="Test Project Description",
            profile_id=self.user,
        )
        self.tasklist = TaskList.objects.create(
            name="Test TaskList", project=self.project
        )
        self.task = Tasks.objects.create(
            task_name="Test Task",
            description="Test Task Description",
            status="Not Started",
            task_list=self.tasklist,
            due_date=self.date,
        )
        self.client.login(username="testuser", password="testpassword")

    def test_project_list_view(self):
        response = self.client.get(reverse("Project"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")

    def test_project_detail_view(self):
        response = self.client.get(
            reverse("project-detail", args=[str(self.project.id)])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Project")
        self.assertContains(response, "Test TaskList")
        self.assertContains(response, "Test Task")
        self.assertContains(response, "Not Started")
        self.assertContains(response, "Oct. 13, 2023")

    def test_project_create_view(self):
        response = self.client.post(
            reverse("project-create"),
            {
                "name": "New Test Project",
                "description": "New Test Project Description",
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirects to project detail
        new_project = Project.objects.get(name="New Test Project")
        self.assertIsNotNone(new_project)

    def test_project_update_view(self):
        response = self.client.post(
            reverse("project-update", args=[str(self.project.id)]),
            {
                "name": "Updated Test Project",
                "description": "Updated Test Project Description",
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirects to project detail
        updated_project = Project.objects.get(id=self.project.id)
        self.assertEqual(updated_project.name, "Updated Test Project")

    def test_project_delete_view(self):
        # add a task and task list to the project
        tasklist = TaskList.objects.create(name="Test TaskList", project=self.project)
        task = Tasks.objects.create(
            task_name="Test Task",
            description="Test Task Description",
            status="Not Started",
            task_list=tasklist,
            due_date=self.date,
        )
        # Test that the project isn't deleted when no is selected
        response = self.client.post(
            reverse("project-delete", args=[str(self.project.id)]),
            {
                "delete": "no",
            },
        )
        self.assertEqual(response.status_code, 302)  # Check for a redirect
        self.assertEqual(
            response.url, reverse("Project")
        )  # Check that it redirects to the project list

        # Check that the project still exists in the database
        self.assertTrue(Project.objects.filter(pk=self.project.pk).exists())

        # Check that the task list and task still exist in the database
        self.assertTrue(TaskList.objects.filter(pk=tasklist.pk).exists())
        self.assertTrue(Tasks.objects.filter(pk=task.pk).exists())

        # Check that it can delete the project
        response = self.client.post(
            reverse("project-delete", args=[str(self.project.id)]),
            {
                "delete": "yes",
            },
        )
        self.assertEqual(response.status_code, 302)  # Redirects to project list
        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(id=self.project.id)
        
        # Check that the task list and task are deleted
        with self.assertRaises(TaskList.DoesNotExist):
            TaskList.objects.get(id=tasklist.id)

        with self.assertRaises(Tasks.DoesNotExist):
            Tasks.objects.get(id=task.id)


class ProfileViewsTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_profile_view(self):
        response = self.client.get(reverse("Profile"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Profile")


class UpdateTaskStatusViewTestCase(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="testuser1", password="testpass"
        )
        project = Project.objects.create(
            name="Test Project", description="Test Project Description", profile_id=user
        )
        self.task_list = TaskList.objects.create(name="Test Task List", project=project)
        self.task = Tasks.objects.create(
            assignee="Test Assignee",
            task_name="Test Task",
            description="Test Task Description",
            status="Not Started",
            task_list=self.task_list,
        )

    def test_update_task_status_ajax(self):
        url = reverse("update_task_status")

        # Define the data to send in the AJAX request
        data = {"task_id": str(self.task.id), "new_status": "In Progress"}
        # Send a POST AJAX request to update the task status
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",  # Simulate an AJAX request
        )
        # Check that the response is a JSON response
        self.assertIsInstance(response, JsonResponse)

        # Parse the JSON response
        response_data = json.loads(response.content)

        # Check that the response contains the expected message
        self.assertEqual(response_data["message"], "Task status updated successfully")

        # Check that the task status has been updated in the database
        updated_task = Tasks.objects.get(id=self.task.id)
        self.assertEqual(updated_task.status, "In Progress")

        # Check that the request returns an overall status of the tasklist
        taskList_Overall_Status = response_data["tasklist_status"]
        self.assertEqual(taskList_Overall_Status, "In Progress")

        # Check that the request returns the ID of the tasklist
        tasklist_id = response_data["tasklist_id"]
        self.assertEqual(tasklist_id, str(self.task.task_list.id))

    def test_check_tasklist_status(self):
        # check if it can check that the status is not started
        result = check_tasklist_status(str(self.task.task_list.id))
        self.assertEqual(result, "Not Started")

        # Check if it can check that the status is in progress
        self.task.status = "In Progress"
        self.task.save()
        result = check_tasklist_status(str(self.task.task_list.id))
        self.assertEqual(result, "In Progress")

        # Check if it can check that the status is done
        self.task.status = "Done"
        self.task.save()
        result = check_tasklist_status(str(self.task.task_list.id))
        self.assertEqual(result, "Done")

        Tasks.objects.create(
            assignee="Test Assignee",
            task_name="Test Task",
            description="Test Task Description",
            status="Not Started",
            task_list=self.task_list,
        )

        # Check again with two tasks, one not started, one done
        result = check_tasklist_status(str(self.task.task_list.id))
        self.assertEqual(result, "In Progress")

    def test_update_task_status_invalid_request(self):
        # Define the URL for the view
        url = reverse("update_task_status")

        # Send a GET request (invalid) instead of a POST request
        response = self.client.get(url)

        # Check that the response is a JSON response with a 400 status code
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 400)

        # Parse the JSON response
        response_data = json.loads(response.content)

        # Check that the response contains the expected error message
        self.assertEqual(response_data["error"], "Invalid request")

    def test_update_task_status_task_not_found(self):
        # Define a non-existent task ID
        non_existent_task_id = "00000000-0000-0000-0000-000000000000"

        # Define the URL for the view
        url = reverse("update_task_status")

        # Define the data to send in the AJAX request
        data = {"task_id": non_existent_task_id, "new_status": "In Progress"}

        # Send a POST AJAX request with a non-existent task ID
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",  # Simulate an AJAX request
        )

        # Check that the response is a JSON response with a 404 status code
        self.assertIsInstance(response, JsonResponse)
        self.assertEqual(response.status_code, 404)

        # Parse the JSON response
        response_data = json.loads(response.content)

        # Check that the response contains the expected error message
        self.assertEqual(response_data["error"], "Task not found")


class DeleteTaskListViewTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = Profile.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

        # Create a project and a task list associated with that project
        self.project = Project.objects.create(
            name="Test Project", description="Project Description", profile_id=self.user
        )
        self.task_list = TaskList.objects.create(
            name="Test Task List", project=self.project
        )

    def test_delete_task_list(self):
        # Send a POST request to delete the task list
        url = reverse(
            "delete_task_list"
        )  # Adjust this URL name according to your project's URL configuration
        data = {"tasklist_id": str(self.task_list.id), "confirmation": "yes"}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the task list and associated tasks have been deleted
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.content), {"message": "Tasklist successfully deleted"}
        )

        # Check if the task list and associated tasks no longer exist in the database
        self.assertFalse(TaskList.objects.filter(id=self.task_list.id).exists())
        self.assertFalse(Tasks.objects.filter(task_list=self.task_list.id).exists())

    def test_delete_task_list_with_task(self):
        task = Tasks.objects.create(
            assignee="Test Assignee",
            task_name="Test Task",
            description="Test Task Description",
            status="Not Started",
            task_list=self.task_list,
        )
        # Send a POST request to delete the task list
        url = reverse(
            "delete_task_list"
        )  # Adjust this URL name according to your project's URL configuration

        data = {"tasklist_id": str(self.task_list.id), "confirmation": "yes"}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the task list and associated tasks have been deleted
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.content), {"message": "Tasklist successfully deleted"}
        )

        # Check if the task list and associated tasks no longer exist in the database
        self.assertFalse(TaskList.objects.filter(id=self.task_list.id).exists())
        self.assertFalse(Tasks.objects.filter(task_list=self.task_list.id).exists())
        self.assertFalse(Tasks.objects.filter(id=task.id).exists())

    def test_delete_task_list_invalid_request(self):
        # Send an invalid request (e.g., missing 'confirmation')
        url = reverse(
            "delete_task_list"
        )  # Adjust this URL name according to your project's URL configuration
        data = {"tasklist_id": str(self.task_list.id)}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the view returns a 400 Bad Request response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {"error": "Invalid request"})

    def test_delete_task_list_tasklist_not_found(self):
        # Send a request to delete a non-existent task list
        url = reverse(
            "delete_task_list"
        )  # Adjust this URL name according to your project's URL configuration
        data = {"tasklist_id": None, "confirmation": "yes"}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the view returns a 404 Not Found response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {"error": "TaskList not found"})


class UpdateTaskListViewTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = Profile.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

        # Create a project and a task list associated with that project
        self.project = Project.objects.create(
            name="Test Project", description="Project Description", profile_id=self.user
        )
        self.task_list = TaskList.objects.create(
            name="Test Task List", project=self.project
        )

    def test_update_task_list(self):
        # Send a POST request to update the task list name
        url = reverse(
            "update_task_list"
        )  # Adjust this URL name according to your project's URL configuration
        data = {"tasklist_id": str(self.task_list.id), "name": "New Task List Name"}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the task list name has been updated
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.content), {"message": "Tasklist successfully updated"}
        )

        # Check if the task list's name has changed in the database
        updated_task_list = TaskList.objects.get(id=self.task_list.id)
        self.assertEqual(updated_task_list.name, "New Task List Name")

    def test_update_task_list_tasklist_not_found(self):
        # Send a request to update a non-existent task list
        url = reverse(
            "update_task_list"
        )  # Adjust this URL name according to your project's URL configuration
        data = {"tasklist_id": None, "name": "New Task List Name"}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the view returns a 404 Not Found response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {"error": "TaskList not found"})

    def test_update_task_list_invalid_request(self):
        # Send an invalid request (e.g., wrong request type)
        url = reverse(
            "update_task_list"
        )  # Adjust this URL name according to your project's URL configuration
        data = {"tasklist_id": str(self.task_list.id)}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="NOT_AJAX_REQUEST",
        )

        # Check if the view returns a 400 Bad Request response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {"error": "Invalid request"})

        # Test again with no name field
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        self.assertEqual(
            json.loads(response.content),
            {"error": "Invalid request, new name cannot be none"},
        )


class DeleteTaskViewTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = Profile.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

        # Create a project and a task list associated with that project
        self.project = Project.objects.create(
            name="Test Project", description="Project Description", profile_id=self.user
        )
        self.task_list = TaskList.objects.create(
            name="Test Task List", project=self.project
        )
        self.task = Tasks.objects.create(
            assignee="Test Assignee",
            task_name="Test Task",
            description="Test Task Description",
            status="Not Started",
            task_list=self.task_list,
        )

    def test_delete_task(self):
        # Send a POST request to delete the task list
        url = reverse(
            "delete_task"
        )  # Adjust this URL name according to your project's URL configuration
        data = {"task_id": str(self.task.id), "confirmation": "yes"}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the task list and associated tasks have been deleted
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.content), {"message": "Task successfully deleted"}
        )

        # Check if the task no longer exists in the database
        self.assertFalse(Tasks.objects.filter(task_list=self.task.id).exists())

    def test_delete_task_invalid_request(self):
        # Send an invalid request (e.g., missing 'confirmation')
        url = reverse(
            "delete_task"
        )  # Adjust this URL name according to your project's URL configuration
        data = {"task_id": str(self.task.id)}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the view returns a 400 Bad Request response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {"error": "Invalid request"})

    def test_delete_task_task_not_found(self):
        # Send a request to delete a non-existent task list
        url = reverse(
            "delete_task"
        )  # Adjust this URL name according to your project's URL configuration
        data = {"task_id": None, "confirmation": "yes"}
        response = self.client.post(
            url,
            data,
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the view returns a 404 Not Found response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {"error": "Task not found"})


class UpdateTaskViewTest(TestCase):
    def setUp(self):
        # Create a user and log them in
        self.user = Profile.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

        # Create a project and a task associated with that project
        self.project = Project.objects.create(
            name="Test Project", description="Project Description", profile_id=self.user
        )
        self.task_list = TaskList.objects.create(
            name="Test Task List", project=self.project
        )
        self.task = Tasks.objects.create(
            assignee="Test Assignee",
            task_name="Test Task",
            description="Test Task Description",
            status="Not Started",
            task_list=self.task_list,
            priority="High",
        )

    def test_update_task(self):
        # Send a POST request to update the task name
        url = reverse(
            "update_task"
        )  # Adjust this URL name according to your project's URL configuration
        date = datetime.fromisoformat("2023-10-13T00:00:00.000+00:00").date()
        data = {
            "task_id": str(self.task.id),
            "name": "New Task Name",
            "assignee": "New Assignee",
            "due_date": "2023-10-13T00:00:00.000+00:00",
            "description": "New Description",
            "priority": "Low",
        }
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the task name has been updated
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            json.loads(response.content), {"message": "Task successfully updated"}
        )

        # Check if the task's data has changed in the database
        updated_task = Tasks.objects.get(id=self.task.id)
        self.assertEqual(updated_task.task_name, "New Task Name")
        self.assertEqual(updated_task.assignee, "New Assignee")
        self.assertEqual(updated_task.due_date, date)
        self.assertEqual(updated_task.description, "New Description")
        self.assertEqual(updated_task.priority, "Low")

        # Call update task with different items None to check that they are not updated
        data = {
            "task_id": str(self.task.id),
            "name": None,
            "assignee": "New Assignee",
            "due_date": None,
            "description": "New Description",
            "priority": None,
        }
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )
        updated_task = Tasks.objects.get(id=self.task.id)
        self.assertEqual(updated_task.task_name, "New Task Name")
        self.assertEqual(updated_task.due_date, date)
        self.assertEqual(updated_task.priority, "Low")

    def test_update_task_task_not_found(self):
        # Send a request to update a non-existent task
        url = reverse(
            "update_task"
        )  # Adjust this URL name according to your project's URL configuration
        date = datetime.fromisoformat("2023-10-13T00:00:00.000+00:00").date()
        data = {
            "task_id": None,
            "name": "New Task Name",
            "assignee": "New Assignee",
            "date": str(date),
            "description": "New Description",
            "priority": "Low",
        }
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the view returns a 404 Not Found response
        self.assertEqual(response.status_code, 404)
        self.assertEqual(json.loads(response.content), {"error": "Task not found"})

    def test_update_task_invalid_request(self):
        # Send an invalid request (e.g., wrong request type)
        url = reverse(
            "update_task"
        )  # Adjust this URL name according to your project's URL configuration
        date = datetime.fromisoformat("2023-10-13T00:00:00.000+00:00").date()
        data = {"task_id": str(self.task.id), "date": str(date)}
        response = self.client.post(
            url,
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="NOT_AJAX_REQUEST",
        )

        # Check if the view returns a 400 Bad Request response
        self.assertEqual(response.status_code, 400)
        self.assertEqual(json.loads(response.content), {"error": "Invalid request"})


class SignupViewTestCase(TestCase):
    def test_signup_form_valid(self):
        # Create a user registration form data
        form_data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword",
            "email": "test@email.com",
            "date_of_birth": datetime.today().date(),
            "first_name": "john",
            "last_name": "doe",
        }
        response = self.client.post(reverse("signup"), form_data)
        self.assertEqual(response.status_code, 302)  # Redirects to success_url
        all_usernames = get_user_model().objects.values_list("username", flat=True)
        self.assertTrue("testuser" in all_usernames)
        user = Profile.objects.get(username="testuser")
        self.assertIsNotNone(user)
        self.assertIsNotNone(user.profile_color)

        # Add any other assertions you need, e.g., check if the user is logged in

    def test_signup_form_invalid(self):
        # Create an invalid user registration form data (e.g., mismatched passwords)
        form_data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "invalidpassword",
            # Add other required fields as needed for your form
        }
        response = self.client.post(reverse("signup"), form_data)
        # print("\n TEST FORM INVALID")
        # print(response.content.decode('utf-8'))
        self.assertEqual(
            response.status_code, 200
        )  # Form submission fails, stays on the same page
        user = get_user_model().objects.filter(username="testuser")
        self.assertFalse(user.exists())

    def test_signup_form_already_registered(self):
        # Create a user with the same username before attempting registration
        user = get_user_model().objects.create_user(
            username="testuser", password="testpassword"
        )
        form_data = {
            "username": "testuser",
            "password1": "testpassword",
            "password2": "testpassword",
            "email": "test@email.com",
            "date_of_birth": datetime.today().date(),
            "first_name": "john",
            "last_name": "doe",
        }
        response = self.client.post(reverse("signup"), form_data)
        self.assertEqual(
            response.status_code, 200
        )  # Form submission fails, stays on the same page
        self.assertContains(response, "A user with that username already exists.")

    def test_generate_random_dark_color(self):
        # Generate a random dark color
        dark_color = generate_random_dark_color()

        # Check if the color is in the correct format (e.g., #RRGGBB)
        self.assertRegex(dark_color, r"^#[0-9A-Fa-f]{6}$")

        # Check the brightness of the color
        r, g, b = (
            int(dark_color[1:3], 16),
            int(dark_color[3:5], 16),
            int(dark_color[5:7], 16),
        )
        brightness = (r * 299 + g * 587 + b * 114) / 1000
        self.assertLess(brightness, 128)  # Ensure it's a dark color


class CalendarViewTest(TestCase):
    def setUp(self):
        # Create a test user profile
        self.user_profile = Profile.objects.create(
            username="testuser", email="test@email.com"
        )
        self.user_profile.save()

        self.user_profile2 = Profile.objects.create(
            username="testuser1", email="test@email.com"
        )
        self.user_profile2.save()

        # Create a test project, task list, and tasks associated with the user
        self.project = Project.objects.create(
            name="Test Project",
            description="Project Description",
            profile_id=self.user_profile,
        )
        self.project.save()
        self.task_list = TaskList.objects.create(
            name="Test Task List", project=self.project
        )
        self.task_list.save()
        self.task1 = Tasks.objects.create(
            assignee="testuser",
            task_name="Task 1",
            task_list=self.task_list,
            due_date=date(2023, 10, 1),
        )
        self.task1.save()

        # Create a project from a separate user with the first user assigned to a task
        self.project2 = Project.objects.create(
            name="Test Project2",
            description="Project Description",
            profile_id=self.user_profile2,
        )
        self.project2.save()
        self.task_list2 = TaskList.objects.create(
            name="Test Task List", project=self.project2
        )
        self.task_list2.save()
        self.task2 = Tasks.objects.create(
            assignee="testuser",
            task_name="Task 2",
            task_list=self.task_list2,
            due_date=date(2023, 10, 15),
        )
        self.task2.save()

        # Create a task not associated with the user to ensure that it is not present
        self.task3 = Tasks.objects.create(
            task_name="Task 3", task_list=self.task_list2, due_date=date(2023, 11, 1)
        )
        self.task3.save()

    def test_get_all_tasks_for_user(self):
        # Call the utility function to get all tasks for the user
        tasks_for_user = get_all_tasks_for_user(self.user_profile.id)

        # Verify that the tasks are correctly retrieved
        self.assertEqual(tasks_for_user.count(), 2)  # Check the number of tasks

        # Verify that the tasks belong to the correct user
        self.assertTrue(self.task1 in tasks_for_user)
        self.assertTrue(self.task2 in tasks_for_user)
        self.assertFalse(self.task3 in tasks_for_user)

    def test_get_all_tasks_for_user_filtered_by_month_and_year(self):
        # Call the utility function with a specific month and year
        tasks_for_user = get_all_tasks_for_user(
            self.user_profile.id, month=10, year=2023
        )

        # Verify that the tasks are correctly filtered
        self.assertEqual(
            tasks_for_user.count(), 2
        )  # Check the number of tasks in October 2023

        # Verify that the tasks belong to the correct user
        self.assertTrue(self.task1 in tasks_for_user)
        self.assertTrue(self.task2 in tasks_for_user)
        self.assertFalse(self.task3 in tasks_for_user)

        # Check that the tasks are all in the correct month and year
        for task in tasks_for_user:
            self.assertTrue(task.due_date.month == 10)
            self.assertTrue(task.due_date.year == 2023)

    def test_get_all_tasks_for_user_filtered_by_month_and_year_no_tasks(self):
        # Call the utility function with a specific month and year where there are no tasks
        tasks_for_user = get_all_tasks_for_user(
            self.user_profile.id, month=11, year=2023
        )

        # Verify that no tasks are returned for November 2023
        self.assertEqual(tasks_for_user.count(), 0)

    def test_get_all_tasks_for_user_no_profile(self):
        # Call the utility function with a non-existent profile ID
        tasks_for_user = get_all_tasks_for_user(None)

        # Verify that the function returns None for a non-existent profile
        self.assertIsNone(tasks_for_user)


class CreateTaskListTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="testuser1", password="testpass"
        )
        self.project = Project.objects.create(
            name="Test Project", description="Test Project Description", profile_id=user
        )
        self.tasklist_name = "Test Task List"

    def test_create_tasklist(self):
        # Define the URL for the project detail page, adjust as needed
        url = reverse("create-tasklist")

        # Simulate a POST request to create a task list
        response = self.client.post(
            url, {"project_id": self.project.id, "tasklist_name": self.tasklist_name}
        )

        # Check if the task list was created
        self.assertEqual(response.status_code, 302)  # Should be a redirect

        # Verify that the task list exists
        task_list_exists = TaskList.objects.filter(name=self.tasklist_name).exists()
        self.assertTrue(task_list_exists)

        # Check if the redirection URL is correct
        self.assertEqual(
            response.url, reverse("project-detail", args=[self.project.id])
        )

        # Test that the fallback return works
        url = reverse("create-tasklist")  # Replace with your URL name
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, 200
        )  # Check for a successful GET request
        self.assertTemplateUsed(
            response, "TempHome.html"
        )  # Check that the correct template is used


class CreateTaskTest(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="testuser1", password="testpass"
        )
        self.project = Project.objects.create(
            name="Test Project", description="Test Project Description", profile_id=user
        )
        self.task_list = TaskList.objects.create(
            name="Test Task List",
            project=self.project,
        )
        self.task_name = "Test Task"
        self.task_due_date = datetime.today().date()
        self.task_priority = "High"
        self.task_description = "Test description"
        self.assignee = "Test Assignee"

    def test_create_task(self):
        # Define the URL for the project detail page, adjust as needed
        url = reverse("create-task")

        # Simulate a POST request to create a task list
        response = self.client.post(
            url,
            {
                "tasklist_id": self.task_list.id,
                "task_name": self.task_name,
                "description": self.task_description,
                "due_date": self.task_due_date,
                "priority": self.task_priority,
            },
        )

        # Check if the task list was created
        self.assertEqual(response.status_code, 302)  # Should be a redirect

        # Verify that the task list exists
        task = Tasks.objects.get(task_name=self.task_name)
        self.assertTrue(task != None)

        # Check that the data in the task is the same as the input data
        self.assertEqual(task.task_name, self.task_name)
        self.assertEqual(task.description, self.task_description)
        self.assertEqual(task.due_date, self.task_due_date)
        self.assertEqual(task.priority, self.task_priority)
        self.assertEqual(task.task_list, self.task_list)
        self.assertEqual(task.status, "Not Started")

        # Check if the redirection URL is correct
        self.assertEqual(
            response.url, reverse("project-detail", args=[self.project.id])
        )

        # Test that the fallback return works
        url = reverse("create-task")  # Replace with your URL name
        response = self.client.get(url)

        self.assertEqual(
            response.status_code, 200
        )  # Check for a successful GET request
        self.assertTemplateUsed(
            response, "TempHome.html"
        )  # Check that the correct template is use


class UpdateProfileViewTest(TestCase):
    def setUp(self):
        # Create a test user for the profile
        self.user = get_user_model().objects.create_user(
            username="testuser",
            password="testpassword",
        )
        self.user_id = self.user.id

    def test_update_profile_view(self):
        # Simulate a POST request with JSON data
        data = {
            "user_id": str(self.user_id),
            "first_name": "Updated First Name",
            "last_name": "Updated Last Name",
            "email": "updated.email@example.com",
            "bio": "Updated bio information",
        }
        response = self.client.post(
            reverse("update_profile"),
            json.dumps(data),
            content_type="application/json",
            HTTP_X_REQUESTED_WITH="XMLHttpRequest",
        )

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Check if the user's profile information has been updated
        self.user.refresh_from_db()  # Refresh the user object from the database
        self.assertEqual(self.user.first_name, "Updated First Name")
        self.assertEqual(self.user.last_name, "Updated Last Name")
        self.assertEqual(self.user.email, "updated.email@example.com")
        self.assertEqual(self.user.bio, "Updated bio information")

        # Check if the response is a JSON response with a success message
        data = response.json()
        self.assertEqual(data["message"], "User successfully updated")

    def test_update_profile_view_invalid_request(self):
        # Simulate an invalid POST request without the required JSON data
        response = self.client.post(reverse("update_profile"))

        # Check if the response status code is 400 Bad Request
        self.assertEqual(response.status_code, 400)

        # Check if the response is a JSON response with an error message
        data = response.json()
        self.assertEqual(data["error"], "Invalid request")
