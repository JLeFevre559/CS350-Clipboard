from django.core.management.base import BaseCommand
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Connect to MongoDB and perform some task'

    def handle(self, *args, **options):
        uri = "mongodb+srv://clipboarduncocs350:Z8iMzNf3BEi8ZeGC@cluster0.zuvxgs6.mongodb.net/?retryWrites=true&w=majority&appName=AtlasApp"

        # Create a new client and connect to the server
        client = MongoClient(uri)

        # Send a ping to confirm a successful connection
        try:
            client.admin.command('ping')
            self.stdout.write(self.style.SUCCESS("Successfully connected to MongoDB!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {e}"))