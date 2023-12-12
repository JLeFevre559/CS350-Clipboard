# Scalability Report of Checkly for our App

## Milestone 7 - Design - Joel LeFevre

# Checking our current Checkly usage against the caps on our free Checkly plan
* [Current Usage](ChecklyScalability.png)
    * Our current usage is ~700 checks a month, running 1 check every hour, and every time we push an update, just checking that the home page of the website is up.
        * We currently have this set up to send an email alert if our site is down
        * Our current free plan allows 1.5k monthly checks, of which we are at ~700

# Checking the scaling options offered by Checkly at https://app.checklyhq.com/billing/
    * If we wanted to go up to a check once every 10 minutes we could upgrade to the pro plan for $40 to get 6000 monthly browser checks.
        * We would only be using ~4400 browser checks monthly, which would leave a bit less than 1600 browser checks for deployment checks.
    * Another benefit of the pro plan is allowing all forms of alerts, instead of just emails, so we could get an SMS alert within 10 minutes of the site going down.
