from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class TempHomeTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username="testuser", password="testpassword", first_name="John")

    def test_authenticated_user_navigation(self):
        # Log in the user
        self.client.login(username="testuser", password="testpassword")

        # Get the TempHome page
        response = self.client.get(reverse("Index"))  # Replace with the actual URL name

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check if the user's name is displayed on the page
        self.assertContains(response, "Welcome back, John")

        # Check the presence and correctness of links
        self.assertContains(response, 'href="/Project"')
        self.assertContains(response, 'href="/Profile"')

    def test_unauthenticated_user_navigation(self):
        # Logout any authenticated user
        self.client.logout()

        # Get the TempHome page
        response = self.client.get(reverse("Index"))  # Replace with the actual URL name

        # Check the response status code
        self.assertEqual(response.status_code, 200)

        # Check the absence of the user's name
        self.assertNotContains(response, "Welcome, back")
        # Check the presence and correctness of links
        self.assertContains(response, 'href="/accounts/login/"')
        self.assertContains(response, 'href="/signup/"')


    def test_authenticated_user_navbar_links(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("Index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/Project"')  # Check if the "Project" link is present
        self.assertContains(response, 'href="/Profile"')  # Check if the "Profile" link is present


    def test_navbar_logo_link(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("Index"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'href="/"')  # Check if the logo link points to the home page

    def test_navbar_image(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("Index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<img src="../../static/images/Home.png"')  # Check if the navbar image tag is present
