# AI Learning - Milestone 2 - Shane Loewe

Things I learned from ChatGPT

## can you generate some Playwrite tests for my Checkly testing 

1. Element Visibility
const { expect, test } = require('@playwright/test');

test('Check Element Visibility', async ({ page }) => {
  await page.goto('https://example.com');
  const isLogoVisible = await page.isVisible('img');
  expect(isLogoVisible).toBe(true);
});

2. Test Navigation
const { expect, test } = require('@playwright/test');

test('Navigate to a Page', async ({ page }) => {
  await page.goto('https://example.com');
  const title = await page.title();
  expect(title).toBe('Example Domain');
});

3. Test Element Click
const { expect, test } = require('@playwright/test');

test('Click an Element', async ({ page }) => {
  await page.goto('https://example.com');
  await page.click('a');
  const currentUrl = page.url();
  expect(currentUrl).toBe('https://www.iana.org/domains/example');
});


## Is Checkly a good testing platform?

Checkly is a popular testing platform that specializes in end-to-end monitoring and testing of web applications and APIs. It is known for its simplicity, scalability, and developer-friendly features. Whether Checkly is a good choice for your testing needs depends on your specific requirements and preferences. Here are some factors to consider when evaluating Checkly:

Ease of Use: Checkly offers an easy-to-use interface for creating and managing tests. It provides a clean and intuitive dashboard, making it suitable for both beginners and experienced testers.

Wide Range of Test Types: Checkly supports various types of tests, including browser checks (using Playwright or Puppeteer), API checks, and cron checks. This versatility allows you to comprehensively monitor your web application.

Integration: Checkly integrates with popular development and monitoring tools, such as Slack, PagerDuty, GitHub, and more. Integration capabilities can enhance your testing and alerting workflows.

Scalability: Checkly is designed to handle large-scale testing and monitoring, making it suitable for applications of all sizes. You can easily scale your testing efforts as your application grows.

Developer-Centric: Checkly is developer-focused and offers features like code-driven checks and configuration as code, allowing you to manage your tests as part of your development process.

Pricing: Checkly offers a pricing model based on the number of checks and the check frequency. Pricing can vary depending on your usage, so it's essential to evaluate whether it aligns with your budget.

Community and Support: Checkly has an active community and provides support resources, including documentation and customer support, to help users troubleshoot issues and get started.

Before choosing Checkly or any testing platform, it's a good idea to consider your specific testing needs, budget, and existing toolchain. You may also want to explore alternative testing platforms and compare their features and pricing to make an informed decision that best suits your requirements.