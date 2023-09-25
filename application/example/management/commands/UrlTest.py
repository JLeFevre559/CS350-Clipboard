from django.core.management.base import BaseCommand
import requests

class Command(BaseCommand):
    help = 'Checks for live deployment of website'

    def handle(self, *args, **options):
        # Define the URL of the webpage you want to check
        url = 'https://clipboard-unco-cs350.vercel.app/'
        
        try:
            # Send a GET request to the URL
            response = requests.get(url)
            
            # Check that the response status code is in the 2xx range
            if 200 <= response.status_code < 300:
                self.stdout.write(self.style.SUCCESS('URL exists and returned a successful status code.'))
            else:
                self.stdout.write(self.style.ERROR(f'URL returned a {response.status_code} status code.'))
        
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f'Error while checking URL: {str(e)}'))
