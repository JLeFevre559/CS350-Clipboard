## Milestone 7 - Design - Joel LeFevre

# I closed the outstanding issues from our 1.0 release
    * I fixed the popups for editing a task saving the edits on close
    * I fixed the popups for editing a tasklist saving the edit on close
        * The prior two issues were caused by a misunderstanding of what the default function of a button is in an html form. The default button function if you don't specify a type is "Submit", and this issue was fixed by adding type="Button" to the close buttons
    * I identified the Firefox compatibility issue as version specific
        * I was unable to reproduce the issue at home on the latest version of Firefox, and outside of that issue the site functioned as expected.

# I enhanced the existing features on the project page
    * I removed the task detail popup, and replaced it with expanding tasks
        * This is a feature improvement because in the task detail popup the users could open the edit and delete confirmation popups as well, and a two layer popup felt ugly and messy. 
    * I changed the tasklists to not match size in the rows, and instead fit the tasks inside of them
        * This was due to feedback we got from real users during milestone 6 that it felt weird to have one tasklist that was really long next to another that was short.
    * I changed the tasklists to work in columns where the elements fit together vertically

# I checked the scalability of Clipboard

    * I checked the scalability of our Vercel deployment
        * I checked our current usage and compared it to our current and other offered plans.
    * I checked the scalability of our MongoDB database
        * I checked our current usage and compared it to our current and other offered plans.
