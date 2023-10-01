# Code Milestone 3

## Features and Code Snippets

### Task Listing

The system lists tasks with associated due dates and statuses.

```html
<h4>Tasks Due: 10/26/2023</h4>
<p><span class="popup-trigger" data-popup-id="popup1">Task 1</span>:<span id="task1Status" class="status-not-started">Not Started</span></p>
<button id="task1InProgress" onclick="updateTaskStatus(1, 'In-progress')">In Progress</button>
<button id="task1Done" onclick="updateTaskStatus(1, 'Done')">Done</button>
```

### Snippet 2: Detailed Task Information
### Detailed Task Information
Detailed information of a task, such as assignee and due date, is displayed in a popup upon task selection.

```html
<div class="popup" id="popup1">
    <!-- Popup Content -->
</div>
```
### Snippet 3: Status Updates
### Status Updates

Task statuses can be updated by users within the previously mentioned popups.

```html
<button id="task3InProgress" class="textStatusBox" onclick="updateTaskStatus(1, 'In-progress')">In Progress</button>
<button id="task3Done" onclick="updateTaskStatus(1, 'Done')">Done</button>
```

### Snippet 4: JavaScript Interactivity
### JavaScript Interactivity

JavaScript functions manage popup visibility and dynamic task status updating without page reloads.

```javascript
function showPopup(popupId) { /* ... */ }
function hidePopup(popupId) { /* ... */ }
function updateTaskStatus(taskNumber, newStatus) { /* ... */ }
```
