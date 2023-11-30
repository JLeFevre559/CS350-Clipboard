# Scalability Report of Vercel for our App

## Milestone 7 - Design - Joel LeFevre

# Checking our current Vercel Usage against the caps on our free Vercel plan
* [Current Usage](VercelScalability.png)
    * Excluding the ~800MB of Bandwidth used by the stress test performed by Shane earlier in November, Clipboard used ~400MB of data within the last month of its 100GB cap. 
        * This means that our site usage could grow by ~250x before we hit our bandwidth cap on our current tier of Vercel
        * I also found Vercel's built in usage metrics and graphs interesting to see, as it allowed me to see that excluding our stress test the URLs that had the highest execution time were our home page and updating a task's status in the Project page.

# Checking the scaling options offered by Vercel at https://vercel.com/pricing

    * If we were to start hitting the 100GB Bandwidth cap, we could expand to Vercel's Pro tier for $20 per month per team member, that has a bandwidth cap one order of magnitude higher, and the pro tier also offers limited DDoS protection the free tier does not. 
    * Beyond that, we could expand to Vercel's Enterprise tier that has custom pricing, though this would take contacting their sales team to get a price that was specific for our project


