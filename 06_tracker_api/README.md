# 📘 Task Tracker API

A simple, fast, and fully validated REST API for managing **Users** and their **Tasks**, built with **FastAPI** and **Pydantic** 🚀

---

## 📦 Features

- 🧑 Create and fetch users
- ✅ Assign tasks to users
- 🗓️ Validate task due dates (no past deadlines!)
- 🔄 Update task status with allowed values only
- 🧾 List all tasks for a user

---

## 🧰 Tech Stack

- ⚡ [FastAPI](https://fastapi.tiangolo.com/)
- 🛡️ [Pydantic](https://docs.pydantic.dev/)
- 🐍 Python 3.10+

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/Ayesha1130/-Quarter_04_Learning-/tree/main/06_tracker_api
cd task-tracker-api
```

### 2. Create a Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # on Linux/Mac
venv\Scripts\activate     # on Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the API

```bash
uvicorn main:app --reload
```

---

## 📂 File Structure

```
task-tracker-api/
├── main.py          # FastAPI app and endpoints
├── schemas.py       # Pydantic models and validators
├── storage.py       # In-memory USERS and TASKS
└── README.md        # Project documentation
```

---

## 📬 API Endpoints

### 👤 Users

| Method | Endpoint           | Description             |
|--------|--------------------|-------------------------|
| POST   | `/users/`          | Create a new user       |
| GET    | `/users/{user_id}` | Get user by ID          |

### ✅ Tasks

| Method | Endpoint                  | Description                   |
|--------|---------------------------|-------------------------------|
| POST   | `/tasks/`                 | Create a new task             |
| GET    | `/tasks/{task_id}`        | Get task by ID                |
| PUT    | `/tasks/{task_id}`        | Update task status            |
| GET    | `/users/{user_id}/tasks`  | List all tasks for a user     |

---

## 🧪 Status Values Allowed

- `pending`
- `in_progress`
- `completed`

---

## 📝 Example Task Object

```json
{
  "id": 1,
  "title": "Complete FastAPI Project",
  "description": "Build the task tracker app",
  "due_date": "2025-05-20",
  "user_id": 1,
  "status": "pending"
}
```

---

## ❤️ Credits

Built with 💻 and ☕ by [Ayesha Iqbal](https://github.com/Ayesha1130)

---

## 📄 License

MIT License – feel free to use, modify, and distribute!
