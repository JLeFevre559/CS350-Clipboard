# Live Production Environment - Requirements - Milestone 6 - Joel LeFevre

* I changed the structure of our project on both github and vercel to support a live production environment
    * I added a production branch in our github that is connected to our main site https://clipboard-unco-cs350.vercel.app/
    * I added a test environment server that is connected to main on our github repo https://clipboard-unco-cs350-test-env.vercel.app/

* This means that when we push to main in our github we will be able to see changes in the test environment, and we can do a pull request from production to our changes in main to update the production environment.