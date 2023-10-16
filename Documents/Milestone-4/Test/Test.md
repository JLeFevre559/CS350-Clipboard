# Converting Model Tests for Trello Clone App To Django Framework

### 1. [Project Model Test](https://github.com/JLeFevre559/CS350-Clipboard/blob/main/application/example/tests.py#L11-L23)
- **Description**: Ensures that a new project can be created with the expected attributes.
- **Code**:
\```python
class ProjectModelTest(TestCase):
    def test_create_project(self):
        ...
\```

### 2. [Task List Model Test](https://github.com/JLeFevre559/CS350-Clipboard/blob/main/application/example/tests.py#L25-L37)
- **Description**: Confirms that a task list associated with a project can be correctly created.
- **Code**:
\```python
class TaskListModelTest(TestCase):
    def test_create_task_list(self):
        ...
\```

### 3. [Task Model Test](https://github.com/JLeFevre559/CS350-Clipboard/blob/main/application/example/tests.py#L39-L53)
- **Description**: Tests the creation of a task within a task list. Ensures all attributes of a task are set correctly.
- **Code**:
\```python
class TaskModelTest(TestCase):
    def test_create_task(self):
        ...
\```

### 4. [Profile Model Test](https://github.com/JLeFevre559/CS350-Clipboard/blob/main/application/example/tests.py#L55-L72)
- **Description**: Checks the creation and updating of user profiles, including the ability to set a profile picture.
- **Code**:
\```python
class ProfileModelTest(TestCase):
    def test_create_profile(self):
        ...
    def test_create_profile_picture(self):
        ...
\```

## View Tests

### 5. [Project Views Test Case](https://github.com/JLeFevre559/CS350-Clipboard/blob/main/application/example/tests.py#L74-L121)
- **Description**: Tests different views related to the `Project` model. This includes listing, viewing details, creating, updating, and deleting projects.
- **Code**:
\```python
class ProjectViewsTestCase(TestCase):
    ...
\```

### 6. [Profile Views Test Case](https://github.com/JLeFevre559/CS350-Clipboard/blob/main/application/example/tests.py#L123-L132)
- **Description**: Tests the view of the user's profile, ensuring that the profile data is correctly displayed.
- **Code**:
\```python
class ProfileViewsTestCase(TestCase):
    ...
\```

### 7. [Update Task Status View Test Case](https://github.com/JLeFevre559/CS350-Clipboard/blob/main/application/example/tests.py#L134-L187)
- **Description**: Tests updating a task's status, covering scenarios like successful AJAX updates, invalid requests, and non-existent tasks.
- **Code**:
\```python
class UpdateTaskStatusViewTestCase(TestCase):
    ...
\```
