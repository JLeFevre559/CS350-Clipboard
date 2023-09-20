## What are some potential data types for a trello clone app?

## Data Types for a Trello Clone App

---

### **Board**
- **Field**: `name`
  - Type: Character Field
- **Field**: `description`
  - Type: Text Field
- **Relation**: `members`
  - Type: Many-to-Many relation to User
- **Relation**: `owner`
  - Type: Foreign Key to User

---

### **List** (Columns on a board e.g., "To Do", "In Progress", "Done")
- **Field**: `name`
  - Type: Character Field
- **Field**: `position`
  - Type: Integer Field (to maintain order of lists on the board)
- **Relation**: `board`
  - Type: Foreign Key to Board

---

### **Card** (Individual tasks or items)
- **Field**: `title`
  - Type: Character Field
- **Field**: `description`
  - Type: Text Field
- **Field**: `due_date`
  - Type: Date Field
- **Relation**: `list`
  - Type: Foreign Key to List
- **Relation**: `assignees`
  - Type: Many-to-Many relation to User
- **Relation**: `labels`
  - Type: Many-to-Many relation to Label
- **Field**: `position`
  - Type: Integer Field (to maintain order of cards in a list)

---

### **User** (People using the app)
- **Field**: `username`
  - Type: Character Field
- **Field**: `email`
  - Type: Email Field
- **Field**: `password`
  - Type: Hashed Password Field
- **Field**: `profile_picture`
  - Type: Image Field

---

### **Label** (Color-coded labels for cards)
- **Field**: `name`
  - Type: Character Field
- **Field**: `color`
  - Type: Character Field (representing the color code)
