# 🎓 Student Task Manager

A simple command-line task management application built using Python.

The **Student Task Manager** allows students to create, view, complete, and delete tasks. Tasks are stored permanently using a JSON file, so they remain available even after restarting the application.

---

## ✨ Features

* ➕ Add new tasks
* 📋 View all tasks
* ✅ Mark tasks as completed
* 🗑️ Delete tasks
* 💾 Save tasks permanently using JSON
* 🔄 Load saved tasks when the application starts

---

## 🛠️ Technologies Used

* Python
* JSON
* Git
* GitHub

---

## 📂 Project Structure

```text
Student-Task-Manager/
│
├── main.py
├── tasks.json
├── .gitignore
└── README.md
```

### `main.py`

Contains the main application logic and menu-driven task management features.

### `tasks.json`

Stores all tasks permanently so they can be loaded when the application starts.

### `.gitignore`

Contains files and folders that should not be tracked by Git.

### `README.md`

Contains the documentation and instructions for the project.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/Sadiq786-coder/studentTaskManager.git
```

### 2. Open the project folder

```bash
cd studentTaskManager
```

### 3. Run the application

```bash
python main.py
```

---

## 💻 Usage

When the application starts, you will see a menu similar to:

```text
===== Student Task Manager =====

1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Delete Task
5. Exit
```

### ➕ Add Task

Select option `1` and enter your task.

Example:

```text
Enter a task: Learn Git
```

### 📋 View Tasks

Select option `2` to view all your tasks.

Example:

```text
1. Learn Git - [Pending]
2. Practice Python - [Completed]
```

### ✅ Mark Task as Completed

Select option `3` and enter the task number you want to mark as completed.

### 🗑️ Delete Task

Select option `4` and enter the task number you want to delete.

### 🚪 Exit

Select option `5` to close the application.

---

## 💾 Data Persistence

The application uses a `tasks.json` file to store tasks.

This means your tasks remain saved even after you close and restart the application.

Example:

```json
[
    {
        "name": "Learn Git",
        "completed": false
    },
    {
        "name": "Practice Python",
        "completed": true
    }
]
```

---

## 🔮 Future Improvements

Planned features include:

* 📅 Add task due dates
* ⭐ Add task priorities
* 🔍 Search tasks
* ✏️ Edit existing tasks
* 📊 Add task statistics
* 🖥️ Create a graphical user interface
* 🌐 Convert the project into a web application
* 🗄️ Use a database for task storage
* 👤 Add multiple student/user accounts

---

## 📚 What I Learned

Through this project, I practiced:

* Python programming
* Functions
* Lists and dictionaries
* File handling
* JSON data storage
* Git version control
* Git branches
* Git commits
* GitHub repositories
* Pull Requests
* Merging branches
* `.gitignore`

---

## 👨‍💻 Author

**Sadiq Syed**

GitHub: [Sadiq786-coder](https://github.com/Sadiq786-coder)

