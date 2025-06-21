# Simple Django task manager

This is a Django-based Task Management System that allows users to manage tasks and categories through a simple web interface. <br>
Built for the **COMP3011 Web Application Frameworks** assignment.

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

- Use the Django admin panel at `/admin/` to add, update, or delete tasks and categories.

---

## Preview

![1](https://github.com/user-attachments/assets/e28a3f38-7b23-4309-960f-305774e3ad11)

![2](https://github.com/user-attachments/assets/be9bc056-184e-44ef-b3fe-5991179cc4d2)
<br>

![3](https://github.com/user-attachments/assets/6271de14-aad1-494f-b86a-2100966d83df)
<br>

---

