# Scalability Report of MongoDB for our App

## Milestone 7 - Design - Joel LeFevre

# Checking our current MongoDB Usage against the caps on our free MongoDB plan
* [Current Usage](MongoDBScalability.png)
    * Our current usage is ~606 KB of our cap of 512MB on our current free shared plan.
        * This means that our current data usage can grow by ~845 times before we have to expand our storage solution.

# Checking the scaling options offered by MongoDB at https://www.mongodb.com/pricing

    * We could move to a serverless plan with up to 1TB of storage at $.25 per GB-Month, alongside $.10 for each million times data is read from MongoDB and $1.00 per million writes to the DB.
    * This would also include 2 free daily backups with a cost of $2.50/hour restored by using the backup
