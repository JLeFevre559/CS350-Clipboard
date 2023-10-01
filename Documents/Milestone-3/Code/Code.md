# Clipboard: A Task Management System

**Clipboard** is a web-based task management system, providing a straightforward and user-friendly interface to manage tasks efficiently. It is crafted with HTML, CSS, JavaScript, and embedded into a Django template.

## Features and Code Snippets

### Task Listing

Tasks are distinctly listed with due dates and status, ensuring users are aware of pending work.

```html
<h4>Tasks Due: 10/26/2023</h4>
<p><span class="popup-trigger" data-popup-id="popup1">Task 1</span>:<span id="task1Status" class="status-not-started">Not Started</span></p>
<button id="task1InProgress" onclick="updateTaskStatus(1, 'In-progress')">In Progress</button>
<button id="task1Done" onclick="updateTaskStatus(1, 'Done')">Done</button>
