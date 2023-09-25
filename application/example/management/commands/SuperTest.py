from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand): ## To be tested later DON'T RUN
    help = 'Runs all current Tests'

    def handle(self, *args, **options):
        call_command('ModelTest')
        call_command('ViewTest')
        call_command('UrlTest')

