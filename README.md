# Simple Django task manager
This is a Django-based Task Management System that allows users to manage tasks and categories through a simple web interface.

---

## Requirements

Ensure the following are installed:

- **Python 3**

```bash
sudo apt update
sudo apt install python3 python3-pip
```

- **Django**

```bash
pip install django
```

---

## Setup Instructions

1. Extract the project folder (`task_manager`).
2. Open a terminal and navigate into the extracted directory.
3. Start the development server:

```bash
python manage.py runserver
```

---

## Available URLs

| URL | Description |
|-----|-------------|
| `127.0.0.1:8000/` | Home page |
| `127.0.0.1:8000/admin/` | Django admin panel |
| `127.0.0.1:8000/tasks/` | View all tasks |
| `127.0.0.1:8000/categories/` | View all categories |
| `127.0.0.1:8000/tasks/1/` | View a specific task (replace `1` with task ID) |

**Admin Credentials:**

- **Username:** `dae`  
- **Password:** `2025webapp`

---

## Additional Notes

- This project runs on both Windows and Linux.
- It's recommended to use a **virtual environment** before installing dependencies.
- Use the Django admin panel at `/admin/` to add, update, or delete tasks and categories.

---

> Built with Django for COMP3011 Web App Frameworks.