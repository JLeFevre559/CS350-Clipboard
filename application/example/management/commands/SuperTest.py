from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand): ## To be tested later DON'T RUN
    help = 'Runs all current Tests'

    def handle(self, *args, **options):
        call_command('ModelTest') ## Doesn't work until MongoDB is taken care of
        call_command('ViewTest') ## Works if setting change allowed users
        call_command('UrlTest') ## Works

