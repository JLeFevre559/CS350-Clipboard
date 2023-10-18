# Engineering Report

## Milestone 4 - Code - Joel LeFevre

* What did I do?
    * I spoke with the team and planned out what features we could finish for this milestone, and we also decided upon using github for our issue tracking
    * I fleshed out the data collected on sign up, and made sure that the sign up functionality worked
    * I added the ability for a user to edit a project
    * With the help of ChatGPT, and looking at the tests already developed by our team, I created a tests.py file for running tests with the built in django tests
        * I added model tests with help from ChatGPT
        * I added view tests with help from ChatGPT
        * I fixed the tests, and items that were being tested so they all worked as expected
        * Using MongoDB for testing was very slow, so I added an if statement to our settings.py to run tests locally if doing tests
            * This cut our testing time down from ~80s to ~6s before I added more tests
    * I added the view and tests for updating task status
    * I added the ability for users to update task status
    * I added the view and tests for deleting tasklists
    * I added the view and tests for updating tasklists
    * I added the ability for users to create, see, edit, and delete tasklists
    * I added the view and tests for deleting tasks
    * I added the view and tests for updating tasks
    * I added the ability for users to create, see, edit, and delete tasks
    * I fixed the functionality for the task popup to properly show the data related to the tasks
    * While doing these things, I added issues that I noticed to our Github issue tracker.

* What will I do? 
    * For Milestone 5 I will be in the testing seat, so I will be looking to check all of our tests to ensure that they are covering everything they should be.
    * I will look to break our tests.py file into multiple testing files to make the code cleaner and more readable
    * I will look into reducing runtime on our tests
    * I will look into increasing our testing coverage of the live website

* What challenges do I have?
    * I am unsure of how we will tackle the calendar
    * I was unable to get the html of the task popup to update until a ctrl+f5 reload

* Engineering investment
    * I spent about 28 hours on Code for Milestone 4
    * Our team met for 4 hours

* 5-minute Video Demo
    * https://youtu.be/dkwaIupXSPw