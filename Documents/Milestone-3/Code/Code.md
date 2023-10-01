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
```

### Snippet 2: Detailed Task Information
### Detailed Task Information
Upon clicking a task, detailed information such as assignee, task specifics, and due dates are displayed in a popup.

```html
<div class="popup" id="popup1">
    <!-- Popup Content -->
</div>
```
### Snippet 3: Status Updates
### Status Updates

Users have the ability to update task statuses within these popups, making task management convenient and fluid.

```html
<button id="task3InProgress" class="textStatusBox" onclick="updateTaskStatus(1, 'In-progress')">In Progress</button>
<button id="task3Done" onclick="updateTaskStatus(1, 'Done')">Done</button>
```

### Snippet 4: JavaScript Interactivity
### JavaScript Interactivity

JavaScript is leveraged to show or hide popups and update the status of tasks and task lists dynamically, enhancing user experience by providing real-time feedback and interaction without requiring page reloads.

```javascript
function showPopup(popupId) { /* ... */ }
function hidePopup(popupId) { /* ... */ }
function updateTaskStatus(taskNumber, newStatus) { /* ... */ }
```
