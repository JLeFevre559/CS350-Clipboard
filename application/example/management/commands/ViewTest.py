from django.core.management.base import BaseCommand
from django.test import Client
from django.urls import reverse

class Command(BaseCommand):
    help = 'Checks the Views for the Index'

    def handle(self, *args, **options):
        # Initialize a Client object
        client = Client()

        # Use the reverse function to get the URL of the view you want to test
        url = reverse('Index')

        # Use the client to get the response
        response = client.get(url)

        # Now you can work with the response as needed
        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS('View exists and responded with a 200 OK status.'))
        else:
            self.stdout.write(self.style.ERROR('View does not exist or responded with an error status.'))
