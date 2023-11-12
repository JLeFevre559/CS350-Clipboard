# Customer Acceptance meeting - Milestone 6 - Requirements - Joel LeFevre

### Meeting Plan

* Issues that need to be pushed to first release

* Show current release checklist

* Showcase what we have for first release
    * Showcase ClipboardUser Project with tasks
    * Show how that shows all our planned functionality for first release is implemented
    * Showcase calendar
    * Show tasks for previous months as well
    * Show that there is a task from another account

* Show user feedback that we have up to this point

* Show test coverage

* Show burndown graph

### Release criteria checklist

# Web App Release Criteria

## Functionality and User Experience
- [+] All critical features are fully functional.
- [+] User interfaces are consistent and user-friendly.
- [+] Browser compatibility testing on major browsers (e.g., Chrome, Firefox, Safari, Edge).
- [-] Mobile responsiveness and usability on various devices and screen sizes.
    * We did not develop for mobile use for this release because we expected the majority of users to be on desktop
- [+] Accessibility compliance (WCAG) for users with disabilities.
    * Website is usable in greyscale
    * Website makes use of header elements to guide screen readers using visual hierarchy
- [/] Performance optimizations (e.g., page load times, responsiveness).
    * MongoDB can be slow sometimes, but the website rarely takes more than 2-3 seconds to respond

## Security
- [-] Comprehensive security testing, including penetration testing.
- [+] Data encryption for sensitive information (HTTPS, SSL/TLS).
- [+] User authentication and authorization mechanisms are secure.
- [+] Protection against common web application vulnerabilities (e.g., XSS, CSRF).
- [-] Regular security audits and updates planned.

## Testing and Quality Assurance
- [+] Thorough unit testing for code modules and components.
- [+] Integration testing to ensure different parts of the application work together.
- [+] Regression testing to confirm new changes haven't affected existing functionality.
- [-] Performance testing to check for bottlenecks or scalability issues.
- [-] Compatibility testing on different devices and browsers.
- [/] Test cases for critical user scenarios.
    * We have some test cases that represent critical scenarios
- [+] Automated testing scripts and tools are in place.
- [+] Test coverage reports are reviewed.

## Data Management
- [/] Database backups and disaster recovery plans.
    * We currently have someone working on a database backup plan
- [+] Data migration from the previous version if applicable.
- [+] Data integrity checks and validation.
- [-] Compliance with data protection regulations (e.g., GDPR).
    * We aren't certain what else we would need to be in compliance with GDPR, but we know that currently we are not in compliance since users are unable to delete their accounts without directly contacting the developers. This will be something added in our 1.1 Release

## Deployment
- [+] Deployment process documented and tested.
- [+] Rollback plan in case of deployment issues.
- [+] Deployed on staging environment for final testing.
    * Checkly tests run before final deployment
- [+] Scheduled release date and time confirmed.

## Monitoring and Logging
- [+] Monitoring tools and alerts set up (e.g., error tracking, performance monitoring).
- [-] Logging and auditing of user actions and system events.
- [-] Error handling and logging implemented for debugging.

## Documentation
- [/] Updated user documentation, including user guides and FAQs.
    * This is in progress, but will be completed by the release day
- [/] Internal documentation for developers and support staff.
- [-] Change log and release notes for users and stakeholders.

## User Acceptance Testing (UAT)
- [+] Conduct UAT with a select group of users or stakeholders.
- [+] Address and resolve UAT feedback and issues.

## Support and Training
- [-] Support team prepared for user inquiries and issues.
- [-] Training for support staff and end-users on new features.
- [-] Helpdesk or support ticket system in place.
    * These features were not part of our initial contract

## Legal and Compliance
- [/] Compliance with all relevant laws and regulations.
- [+] Licensing and intellectual property rights.
    * We either created our graphics from scratch or used royalty and attribution free icons

## Post-Release Plan
- [+] Monitoring and support post-release.
- [+] Regular updates and maintenance plan.
- [/] Feedback collection mechanisms for users.

## Contingency and Rollback
- [/] Defined rollback procedure in case of critical issues.
- [-] Contingency plan for handling unexpected problems.

## Stakeholder Communication
- [+] Notify stakeholders about the release date and any expected downtime.
- [-] Communication plan for keeping stakeholders and users informed.

## Feedback and Improvement
- [-] Mechanism for collecting user feedback and bug reports.
- [-] Process for prioritizing and implementing improvements and bug fixes.


### Client Acceptance Meeting

* The meeting with the client went well, and they were happy with what they got. However, if this were a real work environment with real money on the line it's likely they would have expected the release checklist to be more filled out.