from locust import HttpUser, task, between, constant_pacing
import sys


class SignupUser(HttpUser):
    host = "https://clipboard-unco-cs350.vercel.app/"
    mode = input("Mode? (varied/const): ")
    if mode == "const":
        wait_time = constant_pacing(1)
    else:
        wait_time = between(1, 5)  # Random wait time between tasks

    def on_start(self):
        # Function called when a user starts a task, you can perform setup here if needed.
        pass

    @task
    # This is an example of the power of Locust Load Testing
    def getPages(self):
        self.client.get("/")
        self.client.get("Calendar")
        self.client.get("Profile")
        self.client.get("login")
        self.client.get("signup")
        self.client.get("Project")
        self.client.get("Projects/create/")
        self.client.get("create-tasklist/")
        self.client.get("logout")
