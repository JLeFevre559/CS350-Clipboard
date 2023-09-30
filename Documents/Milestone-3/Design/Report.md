# Engineering Report

## Milestone 3 - Design - Joel LeFevre

* What did I do?
    * I used ChatGPT to flesh out the data models that we would need for our project
    * I used ChatGPT to turn that list of models into a relational database graph using DBML, then used a DBML visualization tool to identify if anything was missing or unnecessary
    * I updated our Profile model to use the built in Django model for users
        * I also updated our Profile model to use a UUID instead of an incremented int id
    * I fixed an issue with django not being able to find models.py
    * I used my previous work on the visualization to update our models, and had ChatGPT make an updated DBML of our models
    * I worked with Shane to add a connection to a MongoDB database he set up, updated the requirements of our app, and hooked up a .env file to protect the credentials of our database
        * I messaged my team to make sure they could get their database and .env files working on their local environments 
    * I used a favicon generator to turn Alex's previous work on our logo into a favicon for our site
    * I added a login/sign up page, created a superuser in the terminal, and tested it with the superuser
        * The sign up page still is working as a view, but it does not have working functionality
    * I worked to update the work Alex did and create views and html to for CRUD operations for the Projects model
        * I have create, read, and delete operations working, but still need to implement the functionality for update
    * I was unsure what the expectations were for the development guide, as I couldn't find anything relevant in the lessons for this milestone, so I used ChatGPT to help create a development guide for our app

* What will I do? 
    * For Milestone 4, I will be in the coding seat, and I will be looking to finish the CRUD operations for the Project models
    * I will work to update the html and css on the pages that we've added to make sure they fit with the planned structure of our website
    * I will work with my team members to make sure we settle on a testing system that everyone is comfortable with, since I know that Alex is looking into testing options
        * After this, I will work with my team to make sure all of our models, views, and features are being tested systematically 

* What challenges do I have?
    * I am not sure how to lock down and do test driven development, because I am not familiar with the techniques and syntax to test the views and models that I'm making
        * I will look into this further after I talk with Alex on Monday, and we lock down a testing process
    * I am not familiar enough with MongoDB to do queries to get information, and with our bottom-up database styling, it's important that we get this figured out so we can show the specific relevant data to our individual users
        * A possible solution would be to switch to a top-down style and store our projects/tasklists/tasks in arrays since I know that is supported by MongoDB
            * This may be more work than learning to do the correct queries

* Engineering investment
    * I spent about 16 hours on Requirements for Milestone 3
    * Our team met for 4 hours

* 5-minute Video Demo
    * https://youtu.be/GnvXJPCl3Oc