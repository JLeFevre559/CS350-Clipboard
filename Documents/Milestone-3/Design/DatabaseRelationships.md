# Database Relationships in DBML - Joel LeFevre

Table Project {
  id UUID [primary key]
  name varchar(200)
  description text [default: "None"]
  created_at datetime
}

Table TaskList {
  id UUID [primary key]
  name varchar(200)
  project_id UUID [ref: > Project.id]
}

Table Task {
  id UUID [primary key]
  assignee varchar(200)
  task_name varchar(200)
  description text [default: "None"]
  status varchar(20) [note: "Choices: 'Not Started', 'In Progress', 'Done'"]
  due_date date [default: null]
  task_list_id UUID [ref: > TaskList.id]
  assigned_users varchar(255) // Store user ids as a comma-separated string
  priority varchar(50) [default: "None", note: "Choices: 'High', 'Medium', 'low'"]
}

Table Profile {
  id UUID [primary key]
  bio text(1000) [ default: "None"]
  profile_picture varchar(255) [note: "Upload path: 'profile_pictures/'",default: ""]
  email varchar(200) [default: "None"]
  date_of_birth date [default: null]
  projectlist_id UUID [ref: > Project.id, default: null]
}