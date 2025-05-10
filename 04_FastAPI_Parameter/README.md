# FastAPI Parameters Validation Example 🚀

This project demonstrates how to use **Path Parameters**, **Query Parameters**, and **Request Body Validation** in a FastAPI application.

## 📌 Features

- ✅ Path Parameter validation using `Path()`
- 🔍 Query Parameter validation using `Query()`
- 📦 Request Body parsing using `Body()` and Pydantic models
- 📜 Auto-generated interactive documentation via Swagger UI (`/docs`)
- 🧪 Clean and testable code structure

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/)
- Python 3.10+

## 📂 Project Setup

```bash
# Step 1: Initialize project and navigate
uv init fastdca_p1
cd fastdca_p1

# Step 2: Create and activate virtual environment
uv venv
source .venv/bin/activate

# Step 3: Install FastAPI
uv add "fastapi[standard]"

# Step 4: Save code as main.py and run server
fastapi dev main.py
```

Visit:
- `http://localhost:8000/docs` — Swagger UI
- `http://localhost:8000/redoc` — ReDoc UI

## 📄 API Endpoints

### GET `/items/{item_id}`

Retrieve an item using its ID with validation.

**Path Parameter:**
- `item_id` (int): Required, must be ≥ 1

**Example Response:**
```json
{
  "item_id": 1
}
```

### GET `/items/`

Retrieve items with optional filters.

**Query Parameters:**
- `q` (str, optional): Search string (min 3, max 50 characters)
- `skip` (int): Default 0, must be ≥ 0
- `limit` (int): Default 10, must be ≤ 100

**Example Response:**
```json
{
  "q": "search",
  "skip": 0,
  "limit": 10
}
```

### PUT `/items/validated/{item_id}`

Update an item with path, query, and body parameters.

**Path Parameter:**
- `item_id` (int): Required, must be ≥ 1

**Query Parameter:**
- `q` (str, optional): Search string (min 3 characters)

**Request Body:**
```json
{
  "name": "Laptop",
  "description": "Gaming laptop",
  "price": 1299.99
}
```

**Example Response:**
```json
{
  "item_id": 2,
  "q": "offer",
  "item": {
    "name": "Laptop",
    "description": "Gaming laptop",
    "price": 1299.99
  }
}
```

## ✅ Validation Summary

- `Path()`:
  - Use `ge`, `le`, `title`, `description` for constraints
- `Query()`:
  - Add `min_length`, `max_length`, default values, and type checks
- `Body()`:
  - Uses Pydantic models for structured validation
- Automatically returns `422 Unprocessable Entity` on invalid input

## 📚 Learning Goals

- Understand parameter validation in FastAPI
- Combine path, query, and body parameters in one endpoint
- Create self-validating and self-documenting APIs

## 📧 Contact

For questions, improvements, or contributions:
- Star the repo ⭐
- Open issues 🐞
- Submit pull requests 🔁

## 📝 License

Licensed under the MIT License.
Feel free to use, modify, and share.
