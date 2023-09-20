from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Run makemigrations and migrate commands together'

    def handle(self, *args, **options):
        # Run the 'makemigrations' command
        call_command('makemigrations', interactive=False)

        # Run the 'migrate' command
        call_command('migrate', interactive=False)

        self.stdout.write(self.style.SUCCESS('Migrations successfully made and applied.'))
