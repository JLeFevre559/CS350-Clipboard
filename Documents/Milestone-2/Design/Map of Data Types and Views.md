# Map of Data Types and Views

## Data Types

### **Project**
- **Field**: `name` (Character Field)

### **TaskList**
- **Field**: `name` (Character Field)
- **Relation**: `project` (Foreign Key to Project)

### **Tasks**
- **Field**: `assignee` (Character Field)
- **Field**: `task_name` (Character Field)
- **Field**: `description` (Text Field)
- **Field**: `status` (Character Field with Choices)
- **Field**: `due_date` (Date Field)
- **Relation**: `task_list` (Foreign Key to TaskList)

### **Profile**
- **Field**: `bio` (Text Field)
- **Field**: `profile_picture` (Image Field)
- **Field**: `email` (Email Field)
- **Field**: `date_of_birth` (Date Field)
- **Relation**: `projectlist` (Foreign Key to Project)

## Views

### **Project**
- **CRUD Operations**: list, detail, create, update, delete

### **TaskList**
- **CRUD Operations**: list (within a project), detail, create (within a project), update, delete

### **Tasks**
- **CRUD Operations**: list (within a tasklist), detail, create (within a tasklist), update, delete

### **Profile**
- **CRUD Operations**: list, detail, create, update, delete
