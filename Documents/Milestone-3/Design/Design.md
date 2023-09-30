# Milestone 3 - Design - Joel LeFevre

Setup the initial web hosting for the project.


## What I did for Milestone 3

### Created DBML of our Models

I used ChatGPT to flesh out the data models that we would need for our project
    * I used ChatGPT to turn that list of models into a relational database graph using DBML, then used a DBML visualization tool to identify if anything was missing or unnecessary

### Connected our MongoDB database to our project

I worked with Shane to add a connection to a MongoDB database he set up, updated the requirements of our app, and hooked up a .env file to protect the credentials of our database
    * I messaged my team to make sure they could get their database and .env files working on their local environments 

### Created CRUD views for the project model

I worked to update the work Alex did and create views and html to for CRUD operations for the Projects model
    * I have create, read, and delete operations working, but still need to implement the functionality for update

### Added primitive login/signup pages

I added a login/sign up page, created a superuser in the terminal, and tested it with the superuser
    * The sign up page still is working as a view, but it does not have working functionality


### Status Video 

I created a summary of the test and deployment work completed.  View the video at https://youtu.be/GnvXJPCl3Oc


## What I will do for Milestone 4

* For Milestone 4, I will be in the coding seat, and I will be looking to finish the CRUD operations for the Project models, and start on the other models
* I will work to update the html and css on the pages that we've added to make sure they fit with the planned structure of our website
* I will work with my team members to make sure we settle on a testing system that everyone is comfortable with, since I know that Alex is looking into testing options
* After this, I will work with my team to make sure all of our models, views, and features are being tested systematically 


## Concerns and Challenges

* I am not sure how to lock down and do test driven development, because I am not familiar with the techniques and syntax to test the views and models that I'm making
        * I will look into this further after I talk with Alex on Monday, and we lock down a testing process
    * I am not familiar enough with MongoDB to do queries to get information, and with our bottom-up database styling, it's important that we get this figured out so we can show the specific relevant data to our individual users
        * A possible solution would be to switch to a top-down style and store our projects/tasklists/tasks in arrays since I know that is supported by MongoDB
            * This may be more work than learning to do the correct queries

