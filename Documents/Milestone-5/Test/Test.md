## Milestone 5 - Test - Joel LeFevre

# Reorganized test code

    * I split our test code into separate test files to increase readability

# Added test files for local and live URLS

    * I noticed that we didn't have strong tests for our URLS and HTML, so I added files where we could expand upon those tests
    * I moved some of my team's existing URL tests into these files so they will run when we do python manage.py test

# I closed an issue: 

    * I added the functionality for tasklist status updates

# I closed an issue:

    * I fixed task priority not showing the popup

# I improved the styling of the project details page

# I ran coverage.py, and generated an html report which gave me a table with the current coverage of our code

    * I added up the test lines to calculate our current test coverage
    * I looked through the items that were not at 100% and started to add tests to cover those items

# I added tests for our home page html since our html tests were lacking

# I added tests for items that were missing in the views in the first coverage.py run

    * This revealed an issue in our Signup view where if a user entered a duplicate username it would send a query that caused a MongoDB error
        * I opened a related issue on Github
        * I traced this issue to a call in the clean_username function inherited from django's UserCreationForm
        * I overrode the clean_username function with a query that got all usernames instead of just the one user, and checked if the username was in the cleaned usernames list
    * I also added error messages to the signup view pursuant to this issue
    * I closed this issue on Github

# I ran coverage.py

    * This was to check the coverage after adding those tests

# I changed how we were approaching assignees on tasks

    * I did this by asking for the assignee username instead(Since from the previous closed issue, usernames are unique on our platform)
    * This allowed me to create a method, and related test, that would get all the tasks directly related to a user through their projects, and where their username is the assignee
    * Using this change in idea, I was able to close the add collaborators to project issue, alongside the assign user to a task functionality

# Issues following our usability tests

    * Following the usability test for our website, our tester discovered an issue where if you left the date field blank when creating a task it would throw a MongoDB error
        * I opened an issue regarding this
        * I closed this issue by adding required to the date field in the create task popup

    * The usability tester also discovered an issue where if a user pressed the edit profile button, and without editing any fields, pressed the save or cancel buttons, all related data on their profile would be removed
        * This issue was marked critical, and I removed the functionality of the edit profile button until Shane was able to fix the issue

# I ran coverage.py at the end of milestone

    * I compared the data given to me at this point to the data that I got at the beginning of the milestone
