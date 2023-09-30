# Development Guide - Milestone 3 - Design - Joel LeFevre

## Django Models Development Guide:

### 1. Project Model:
- The `Project` model represents a project that users can manage.
- **Fields:**
  - `id`: Automatically generated UUID as the primary key.
  - `name`: CharField for the project name.
  - `description`: TextField for project description.
  - `profile_id`: ForeignKey to the `Profile` model to link the project to a user's profile.
- Ensure that the model is correctly connected to the `Profile` model via the `profile_id` ForeignKey.

### 2. TaskList Model:
- The `TaskList` model represents a list of tasks within a project.
- **Fields:**
  - `name`: CharField for the task list name.
  - `project`: ForeignKey to the `Project` model to associate the task list with a project.
- Make sure to set up the ForeignKey relationship correctly.

### 3. Tasks Model:
- The `Tasks` model represents individual tasks within a task list.
- **Fields:**
  - `assignee`: CharField for the name of the person assigned to the task.
  - `task_name`: CharField for the task name.
  - `description`: TextField for task description.
  - `status`: CharField with choices for task status (Not Started, In Progress, Done).
  - `due_date`: DateField for task due date (nullable).
  - `task_list`: ForeignKey to the `TaskList` model to link the task to a task list.
  - `priority`: CharField with choices for task priority (High, Medium, Low).
- Ensure that the model is properly linked to the `TaskList` model.

### 4. Profile Model:
- The `Profile` model extends Django's AbstractUser to store user profile information.
- **Fields:**
  - `id`: Automatically generated UUID as the primary key.
  - `bio`: TextField for user bio.
  - `profile_picture`: ImageField for user profile picture (optional).
  - `email`: EmailField for user email.
  - `date_of_birth`: DateField for user's date of birth (nullable).
- Confirm that the model extends `AbstractUser` correctly and includes the necessary fields.

## Django Views Development Guide:

### 1. Index View (Home Page):
- The `Index` view serves as the home page.
- Implement a redirection mechanism to the login page for non-logged-in users if needed.
- Uncomment the `@method_decorator(login_required)` decorator if you want to restrict access to logged-in users only.

### 2. Calendar View:
- The `Calendar` view should display a calendar for users.
- Define the necessary logic and templates to render the calendar.

### 3. Project Views (List, Detail, Create, Update, Delete):
- Create views for managing projects.
- Implement views for listing, displaying details, creating, updating, and deleting projects.
- Utilize Django's generic views (e.g., `ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`) for these operations.
- Make sure the views are restricted to logged-in users (`LoginRequiredMixin`) where necessary.
- Pay attention to URL routing and reverse functions to ensure correct URL patterns.

### 4. Profile View:
- Implement a view for user profiles.
- Create a template and logic to display user profile information.

### 5. CustomLoginView and SignupView:
- `CustomLoginView` should handle custom login logic and render a custom login template.
- `SignupView` should handle user registration and automatically log in users after a successful signup.

Ensure that you thoroughly test each model and view during development. Additionally, consider adding forms and templates for your views as needed. Make use of Django's built-in authentication and form handling capabilities to simplify your development process.

Document your code using comments and docstrings to help other developers understand your code and its purpose. Regularly commit your code to version control (e.g., Git) to track changes and collaborate with others effectively.
