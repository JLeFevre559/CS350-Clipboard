# Button Functionality Test

This test script is designed to verify the functionality of two buttons on a webpage. It's written using Django's `TestCase` and Selenium WebDriver for automated browser interaction.

## Code Breakdown:

```python
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class ButtonFunctionalityTest(TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()  # Initiates a Chrome browser instance

    def tearDown(self):
        self.browser.quit()  # Closes the browser instance

    def test_button_functionality(self):
        self.browser.get('https://clipboard-unco-cs350.vercel.app/')  # Navigates to the webpage

        # Locates the buttons using their HTML id attributes
        task1_in_progress_button = self.browser.find_element(By.ID, 'task1InProgress')
        task1_done_button = self.browser.find_element(By.ID, 'task1Done')

        # Clicks 'In Progress' button and checks the updated status
        task1_in_progress_button.click()
        task1_status = self.browser.find_element(By.ID, 'task1Status')
        self.assertEqual(task1_status.text, 'In Progress')  # Verifies the status text

        # Clicks 'Done' button and checks the updated status
        task1_done_button.click()
        self.assertEqual(task1_status.text, 'Done')  # Verifies the status text

## Explanation:

### Importing Necessary Modules:
- `TestCase` from Django to create a test case class.
- `webdriver` and `By` from Selenium to automate browser interaction and locate HTML elements.

### ButtonFunctionalityTest Class:
- A class for the test case, inheriting from `TestCase`.

### setUp Method:
- Runs before each test, initializing a Chrome browser instance.

### tearDown Method:
- Runs after each test, closing the browser instance.

### test_button_functionality Method:
- The core test method.
  - Navigates to the webpage.
  - Locates the buttons.
  - Clicks the buttons and verifies the status text updates correctly.

This automated test ensures the buttons on the specified webpage are working as expected by updating the task status text upon each button click.
