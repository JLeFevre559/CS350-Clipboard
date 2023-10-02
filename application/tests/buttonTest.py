from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class ButtonFunctionalityTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()  # Assumes Chrome; use webdriver.Firefox() for Firefox

    def tearDown(self):
        self.browser.quit()

    def test_button_functionality(self):
        self.browser.get('https://clipboard-unco-cs350.vercel.app/')  # Replace with the URL of your page

        # Locate the buttons using Selenium's WebDriver
        task1_in_progress_button = self.browser.find_element(By.ID, 'task1InProgress')
        task1_done_button = self.browser.find_element(By.ID, 'task1Done')

        # Click the 'In Progress' button and check the updated status
        task1_in_progress_button.click()
        task1_status = self.browser.find_element(By.ID, 'task1Status')
        self.assertEqual(task1_status.text, 'In Progress')

        # Click the 'Done' button and check the updated status
        task1_done_button.click()
        self.assertEqual(task1_status.text, 'Done')
