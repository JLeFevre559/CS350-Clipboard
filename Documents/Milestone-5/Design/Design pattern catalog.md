# Design Patterns for Coding
## Method Standards

* Meaningful Method Names: Choose a descriptive and clear method name that convey their purpose and functionality. 
    - A well-named method should provide a good understanding of what it does.

* Consistent Indentation and Formatting: Maintain consistent indentation and code formatting throughout the method.
    - This includes using proper spacing, alignment, and line breaks to improve code readability.

* Single Responsibility: Follow the Single Responsibility Principle (SRP) by ensuring that each method has a single, well-defined purpose. 
    - A method should do one thing and do it well.

* Appropriate Method Length: Aim for methods that are neither too short nor too long. 
    - Strive to keep methods concise and focused, typically within the range of 10 to 30 lines of code, but this can vary based on context.

* Comments and Documentation: Include comments or method-level documentation to explain the purpose of the method, its parameters, return values, and any important implementation details.     
    - Comments should provide context and clarify the code's intent.
### Method Example
```javascript
function generateAllDaysOfTheWeek(calendar, numbersBetween, today){ // takes the calendar and adds all of the boxes that represent the days of the week.
    for (let i = 1; i < numbersBetween.length+1; i++) { //Handles the numbered of the days of the week
        if("Sunday" == new Date(today.getFullYear(), today.getMonth(), i).toLocaleDateString('en-US', options)) // if day is sunday then a new row is started
            calendar += "<tr>";
        calendar += "<th class=numberedDayOfTheWeek>"+i+ "</th>";// Creates the day of the week box with the apporiate number for that day.
    }
    return calendar
}
```
Here we have a function that has a meaningful name, consistent indentaion and formation, a single responsibility, an appropriate method length and some comments, this is what should be expected when it comes to method standards.

## Variable Standards

* Descriptive Names: Choose variable names that are descriptive and indicative of the variable's purpose.
    - Avoid single-letter or cryptic names like x or temp. Instead, use names like totalPrice or userInput that clarify the variable's role.

* Consistent Casing: Use a consistent casing convention for variable names. 
    - CamelCase is the primary casing for this project.

* Meaningful Prefixes: If necessary, use meaningful prefixes to distinguish the type or purpose of a variable. 
    - For example, you might use strName for a string variable or isReady for a boolean indicating readiness.

* Avoid Reserved Keywords: Avoid using reserved keywords or language-specific terms as variable names, as this can lead to confusion and errors. 
    - Many integrated development environments (IDEs) provide syntax highlighting that can help identify reserved words.

* Consistency Across the Codebase: Maintain consistency in variable naming conventions across your codebase. 
    - When working in a team, ensure that all team members adhere to the same naming standards. This consistency improves code readability and collaboration.

### Variable Example

```javascript
var calendar = "";
const numbersBetween = generateNumbersBetween(firstDayOfLastMonth, lastDayOfLastMonth);
var today = new Date();
```
Here we have three variables, each with a descriptive name, consistent casing, meaningfull prefixes, no use of reserved keywords, and it is consistent across the codebase.

## Comments Standards

* Use Clear and Concise Language: Write comments in a clear and concise manner. 
    - Comments should be easy to understand and provide a brief explanation of the code's purpose or logic.

* Explain "Why" and "How," Not "What": Focus on explaining the "why" and "how" behind the code, rather than stating the obvious "what."
    - Comments should provide context, rationale, and insights into the code's intent and design decisions.

* Comment Regularly: Add comments consistently throughout your code to document critical sections, complex algorithms, and any non-obvious behavior. 
    - This helps other developers, including your future self, understand the code.

* Keep Comments Updated: Maintain your comments by updating them when the code changes. 
    - Outdated comments can be misleading and may cause confusion.

* Avoid Redundant Comments: Avoid writing comments that merely restate the code. 
    - Instead, provide valuable insights or explanations that are not immediately evident from the code itself. 
    - Redundant comments can become outdated and clutter the code.

### Comment Example

```javascript
// Takes the calendar and adds all of the boxes that represent the days of the week.
// Handles the numbered of the days of the week
// If day is sunday then a new row is started
// Creates the day of the week box with the apporiate number for that day.
```

Here are some comments that use clear and consice language, here the why and how can be improved for this example, comments are regularly done in the method, keep comments updated is an ongoing process, and redundant comments are avoided.