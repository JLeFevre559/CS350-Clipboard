# Database Relationships in DBML - Joel LeFevre

Table Project {
  id UUID [primary key]
  name varchar(200)
  description text [default: "None"]
  profile_id UUID [ref: > Profile.id]
}

Table TaskList {
  id UUID [primary key]
  name varchar(200)
  project_id UUID [ref: > Project.id]
}

Table Tasks {
  id UUID [primary key]
  assignee varchar(200)
  task_name varchar(200)
  description text [default: "None"]
  status varchar(20) [default: "Not Started", note: "Not Started, In Progress, Done"]
  due_date date [null]
  task_list_id UUID [ref: > TaskList.id]
  priority varchar(50) [default: "None", note: "High, Medium, Low"]
}

Table Profile {
  id UUID [primary key]
  bio text [default: "None"]
  profile_picture varchar(200) [note: "Relative path to profile pictures", null]
  email varchar(200) [default: "None"]
  date_of_birth date [null]
  username varchar(150) [unique]
  first_name varchar(30) [null]
  last_name varchar(150) [null]
  is_staff bool [default: false]
  is_active bool [default: true]
  date_joined datetime [default: `now()`]
}