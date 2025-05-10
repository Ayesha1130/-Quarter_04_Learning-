# 🚀 FastAPI – Quick Setup Guide

## 📌 What is FastAPI?

**FastAPI** is a modern and high-performance web framework for building **APIs** with Python. It is designed to be easy to use, fast, and reliable, making it ideal for creating RESTful APIs and web services.

### 🌟 Key Features

- ⚡ **Fast & Efficient**: Comparable in performance to Node.js and Go.
- 🛠️ **Auto-generated Documentation**: Includes Swagger UI and ReDoc out of the box.
- 🧠 **Type-based Validation**: Uses Python type hints to validate request data.
- ⏱️ **Asynchronous Support**: Easily handle many requests at once using async.
- 📦 **Simple Setup**: Works smoothly with modern Python tools like `uv`.

---

## ✅ Why Use FastAPI?

| Feature               | Description                                                              |
|-----------------------|--------------------------------------------------------------------------|
| 🚀 Performance        | FastAPI is extremely fast thanks to ASGI and Pydantic.                   |
| 🧩 Auto Docs          | Comes with built-in API documentation (`/docs` and `/redoc`).            |
| 💡 Type Safety        | Use Python types for cleaner, more robust code.                          |
| 🔄 Async-Ready        | Supports asynchronous code using `async def`.                            |
| 🧰 Developer Friendly | Easy to use and very well-documented.                                    |

---

## 🛠️ Project Setup Using `uv`

Follow these steps to create and run a FastAPI project.

### 🔹 Step 1: Initialize the Project

```bash
uv init task_2
```

Creates a new folder named `task_2` with basic structure.

---

### 🔹 Step 2: Move Into the Project Folder

```bash
cd task_2
```

---

### 🔹 Step 3: Add FastAPI and Dependencies

```bash
uv add fastapi[standard]
```

This installs FastAPI along with `uvicorn`, `pydantic`, etc.

---

### 🔹 Step 4: Activate Virtual Environment

On **Windows**:

```bash
.venv\Scripts\activate
```

On **macOS/Linux**:

```bash
source .venv/bin/activate
```

---

### 🔹 Step 5: Create the `main.py` File

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
```

📌 **Note**: Make sure to use correct Python dictionary syntax:  
✅ `{"message": "Hello, world!"}`  
❌ `{"message:", "Hello, world!"}` — This is invalid and returns a list like:  
```json
["Hello, world!", "message:"]
```

---

### 🔹 Step 6: Run the App

```bash
fastapi dev main.py
```

---

### 🌐 Access the App

- Main Route: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## ❓ What is `uv`?

`uv` is a modern project management tool for Python that:

- Manages virtual environments
- Installs and pins dependencies
- Runs development tools like `fastapi dev`

Official site: [https://astral.sh/uv](https://astral.sh/uv)

---

## ✅ Final Thoughts

FastAPI is an excellent framework for modern Python web development. It's fast, easy to use, and ideal for both beginners and professionals. With tools like `uv`, starting a project becomes quick and smooth.

Happy coding! 🎉