import unittest
from django.test.runner import DiscoverRunner

class AllTests(unittest.TestCase): ## To be tested later DON'T RUN
    def test_run_all_tests(self):
        runner = DiscoverRunner()
        failures = runner.run_tests(["app_name.tests"])
        self.assertEqual(failures, 0, f"Test suite failed with {failures} test(s) failing")

if __name__ == "__main__":
    unittest.main()
