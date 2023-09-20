## Map of Data Types and Views

---

### Collections

#### **Project**
- `name`: String

---

#### **TaskList**
- `name`: String
- `project`: ObjectID (Reference to Project)

---

#### **Tasks**
- `assignee`: String
- `task_name`: String
- `description`: String
- `status`: Enum { 'Not Started', 'In Progress', 'Done' }
- `due_date`: Date
- `task_list`: ObjectID (Reference to TaskList)

---

#### **Profile**
- `bio`: String
- `profile_picture`: File 
- `email`: String
- `date_of_birth`: Date
- `projectlist`: Array of ObjectIDs (Reference to Projects)

---

### Views (Still valid for a web application, even if you're using MongoDB)

#### **Project**
- **CRUD Operations**: list, detail, create, update, delete

---

#### **TaskList**
- **CRUD Operations**: list (within a project), detail, create (within a project), update, delete

---

#### **Tasks**
- **CRUD Operations**: list (within a tasklist), detail, create (within a tasklist), update, delete

---

#### **Profile**
- **CRUD Operations**: list, detail, create, update, delete

